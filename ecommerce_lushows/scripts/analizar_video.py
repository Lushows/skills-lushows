#!/usr/bin/env python3
"""
analizar_video.py — desarma videos (de la competencia o propios) para entender por qué venden.

Uso:
    python analizar_video.py <video.mp4 | carpeta> <carpeta_salida> [--umbral 0.30] [--max-cuadros 16] [--transcribir]

Por cada video produce:
  <nombre>_hoja.jpg     hoja de contacto con los cuadros de cada cambio de escena y su segundo
                        → Claude la LEE (Read) y deduce: gancho de los primeros 2 s, tipo de video
                          (demo, POV, testimonio, unboxing, antes/después), ritmo, textos en pantalla, cierre.
  <nombre>_ficha.json   duración, resolución, orientación (9:16, 1:1, 16:9), fps, tiene audio,
                        cortes por minuto, segundos de cada corte, transcripción si se pidió.
  resumen_videos.md     tabla de todos los videos.

--transcribir usa Whisper vía Groq (GROQ_API_KEY) u OpenAI (OPENAI_API_KEY) si hay llave en el entorno.
Sin llave, se omite sin error.

Requiere ffmpeg/ffprobe y Pillow. USO INTERNO: los videos ajenos se analizan para escribir
guiones propios; no se republican (references/07 y 12).
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import urllib.request
import uuid
from pathlib import Path

from PIL import Image, ImageDraw

EXT = {".mp4", ".mov", ".webm", ".m4v"}


def run(cmd, timeout=300):
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, errors="replace")


def ficha(video):
    r = run(["ffprobe", "-v", "error", "-print_format", "json", "-show_streams", "-show_format", str(video)], 60)
    data = json.loads(r.stdout or "{}")
    v = next((s for s in data.get("streams", []) if s.get("codec_type") == "video"), {})
    a = any(s.get("codec_type") == "audio" for s in data.get("streams", []))
    w, h = int(v.get("width", 0)), int(v.get("height", 0))
    rot = str((v.get("tags") or {}).get("rotate", ""))
    if rot in ("90", "270"):
        w, h = h, w
    dur = float((data.get("format") or {}).get("duration") or 0)
    num, _, den = (v.get("avg_frame_rate") or "0/1").partition("/")
    fps = round(float(num) / float(den or 1), 1) if float(den or 1) else 0
    ratio = w / h if h else 0
    orient = "vertical 9:16" if 0.5 <= ratio <= 0.62 else "vertical 4:5" if 0.75 <= ratio <= 0.85 else "cuadrado 1:1" if 0.95 <= ratio <= 1.05 else "horizontal 16:9" if 1.7 <= ratio <= 1.8 else f"{w}x{h}"
    return {"duracion_s": round(dur, 1), "ancho": w, "alto": h, "orientacion": orient, "fps": fps, "audio": a,
            "peso_mb": round(int((data.get("format") or {}).get("size") or 0) / 1048576, 1)}


def cortes(video, umbral):
    # detectar escenas sobre cuadros reducidos: mismo resultado, varias veces más rápido en PCs lentas
    # si un archivo raro atasca la detección, no se cuelga todo: sin cortes → cuadros repartidos en el tiempo
    try:
        r = run(["ffmpeg", "-hide_banner", "-nostdin", "-i", str(video), "-an", "-filter:v", f"scale=160:-2,select='gt(scene,{umbral})',showinfo", "-f", "null", "-"], 120)
    except subprocess.TimeoutExpired:
        print(f"   ⚠ {Path(video).name}: detección de escenas lenta, uso cuadros repartidos")
        return []
    return [round(float(t), 2) for t in re.findall(r"pts_time:([\d.]+)", r.stderr)]


def hoja(video, tiempos, destino, max_cuadros, duracion=0):
    tmp = destino.parent / f"_tmp_{uuid.uuid4().hex[:6]}"
    tmp.mkdir()
    marcas = [0.3] + tiempos
    if len(marcas) < 6 and duracion > 1:  # pocos cortes (giro de producto, testimonio): repartir en el tiempo
        marcas = sorted(set(marcas + [round(duracion * k / 8, 2) for k in range(1, 8)]))
    if len(marcas) > max_cuadros:
        paso = len(marcas) / max_cuadros
        marcas = [marcas[int(i * paso)] for i in range(max_cuadros)]
    cuadros = []
    for i, t in enumerate(marcas):
        f = tmp / f"c{i:03d}.jpg"
        run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-nostdin", "-y", "-ss", str(t), "-i", str(video), "-frames:v", "1", "-vf", "scale=-2:360", str(f)], 60)
        if f.exists():
            cuadros.append((t, Image.open(f).convert("RGB")))
    if not cuadros:
        shutil.rmtree(tmp, ignore_errors=True)
        return 0
    cw = max(im.width for _, im in cuadros)
    cols = min(4 if cw < 300 else 3, len(cuadros))
    filas = (len(cuadros) + cols - 1) // cols
    lienzo = Image.new("RGB", (cols * (cw + 8) + 8, filas * (360 + 30) + 8), (24, 24, 28))
    d = ImageDraw.Draw(lienzo)
    for i, (t, im) in enumerate(cuadros):
        x, y = 8 + (i % cols) * (cw + 8), 8 + (i // cols) * (390)
        lienzo.paste(im, (x, y))
        d.rectangle([x, y + 360, x + 90, y + 384], fill=(0, 0, 0))
        d.text((x + 6, y + 365), f"{t:5.1f} s", fill=(255, 210, 90))
    lienzo.save(destino, quality=82)
    shutil.rmtree(tmp, ignore_errors=True)
    return len(cuadros)


def transcribir(video, carpeta):
    llave, url, modelo = None, None, None
    if os.environ.get("GROQ_API_KEY"):
        llave, url, modelo = os.environ["GROQ_API_KEY"], "https://api.groq.com/openai/v1/audio/transcriptions", "whisper-large-v3"
    elif os.environ.get("OPENAI_API_KEY"):
        llave, url, modelo = os.environ["OPENAI_API_KEY"], "https://api.openai.com/v1/audio/transcriptions", "whisper-1"
    if not llave:
        return None
    audio = carpeta / f"_{uuid.uuid4().hex[:6]}.mp3"
    run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-nostdin", "-y", "-i", str(video), "-vn", "-ac", "1", "-b:a", "48k", str(audio)], 180)
    if not audio.exists():
        return None
    borde = uuid.uuid4().hex
    cuerpo = b"".join([
        f"--{borde}\r\nContent-Disposition: form-data; name=\"model\"\r\n\r\n{modelo}\r\n".encode(),
        f"--{borde}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"a.mp3\"\r\nContent-Type: audio/mpeg\r\n\r\n".encode(),
        audio.read_bytes(), f"\r\n--{borde}--\r\n".encode()])
    req = urllib.request.Request(url, data=cuerpo, headers={"Authorization": f"Bearer {llave}", "Content-Type": f"multipart/form-data; boundary={borde}"})
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            return json.loads(r.read().decode()).get("text")
    except Exception as e:
        return f"(error transcribiendo: {e})"
    finally:
        audio.unlink(missing_ok=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("entrada")
    ap.add_argument("salida")
    ap.add_argument("--umbral", type=float, default=0.30)
    ap.add_argument("--max-cuadros", type=int, default=16)
    ap.add_argument("--transcribir", action="store_true")
    a = ap.parse_args()
    if not shutil.which("ffmpeg"):
        sys.exit("ffmpeg no está en el PATH")

    src = Path(a.entrada)
    videos = sorted(p for p in (src.rglob("*") if src.is_dir() else [src]) if p.suffix.lower() in EXT)
    out = Path(a.salida)
    out.mkdir(parents=True, exist_ok=True)
    filas = []
    for v in videos:
        # nombre único: carpetas distintas pueden tener video01.mp4 cada una
        rel = v.relative_to(src) if src.is_dir() else Path(v.name)
        partes = [x for x in rel.with_suffix("").parts if x != "videos"]
        nombre = "_".join(partes) if len(partes) > 1 else v.stem
        try:
            f = ficha(v)
            if not f["ancho"] or not f["duracion_s"]:
                print(f"⚠ {nombre}: no se pudo leer (archivo incompleto o inexistente), se omite")
                continue
            t = cortes(v, a.umbral)
            n = hoja(v, t, out / f"{nombre}_hoja.jpg", a.max_cuadros, f["duracion_s"])
        except subprocess.TimeoutExpired:
            print(f"⚠ {nombre}: tardó demasiado, se omite")
            continue
        f.update({"cortes_s": t, "cortes_por_min": round(len(t) / (f["duracion_s"] / 60), 1) if f["duracion_s"] else 0,
                  "primer_corte_s": t[0] if t else None, "cuadros_en_hoja": n})
        if a.transcribir and f["audio"]:
            f["transcripcion"] = transcribir(v, out)
        (out / f"{nombre}_ficha.json").write_text(json.dumps(f, ensure_ascii=False, indent=2), encoding="utf-8")
        filas.append(f"| {nombre} | {f['duracion_s']} s | {f['orientacion']} | {f['cortes_por_min']} | {f['primer_corte_s']} | {'sí' if f['audio'] else 'no'} | {f['peso_mb']} MB |")
        print(f"✓ {nombre}: {f['duracion_s']} s · {f['orientacion']} · {len(t)} cortes · hoja {n} cuadros")

    resumen = ["# Videos analizados (USO INTERNO)", "", "| Video | Duración | Formato | Cortes/min | 1er corte | Audio | Peso |", "|---|---|---|---|---|---|---|", *filas, "",
               "Leer cada `_hoja.jpg` y anotar: gancho (0-2 s), tipo de video, textos en pantalla, prueba que muestra, cierre/CTA. Luego escribir guiones PROPIOS (references/12)."]
    (out / "resumen_videos.md").write_text("\n".join(resumen), encoding="utf-8")
    print("\n".join(resumen))


if __name__ == "__main__":
    main()
