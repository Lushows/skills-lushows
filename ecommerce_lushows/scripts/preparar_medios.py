#!/usr/bin/env python3
"""
preparar_medios.py — deja las fotos y videos listos para una página de producto.

Subcomandos:
  recortar-fondo  <entrada> <salida.png> [--umbral 236]
      Quita fondo blanco/gris claro → PNG transparente con borde suave (para heros oscuros).
      Recorta al contenido. Sobre fondos claros basta mix-blend-mode:multiply.

  recortar  <entrada> <salida> x y ancho alto
      Recorta una región (quitar textos en inglés de fotos de fábrica, etc.).

  web  <entrada|carpeta> <carpeta_salida> [--anchos 480,960,1600] [--calidad 82]
      Genera WebP en varios anchos (para srcset) y reporta peso. Nunca sube de tamaño el original.

  portada  <video.mp4> <salida.jpg> [--segundo 1.0]
      Extrae un cuadro como poster (requiere ffmpeg en PATH).

  video-web  <video> <salida.mp4> [--alto 720]
      Recomprime para autoplay en la web: H.264, sin audio, faststart, ~5 MB.

  hoja  <carpeta> <salida.jpg>
      Hoja de contacto para revisar todos los medios de un vistazo.

Requiere Pillow. ffmpeg solo para portada/video-web. Todos los procesos tienen timeout.
"""
import argparse
import shutil
import subprocess
import sys
from pathlib import Path

from PIL import Image

EXT_IMG = {".jpg", ".jpeg", ".png", ".webp"}


def recortar_fondo(a):
    im = Image.open(a.entrada).convert("RGBA")
    px = im.load()
    w, h = im.size
    u = a.umbral
    for y in range(h):
        for x in range(w):
            r, g, b, al = px[x, y]
            brillo = (r + g + b) / 3
            sat = max(r, g, b) - min(r, g, b)
            if brillo > u and sat < 16:
                px[x, y] = (r, g, b, 0)
            elif brillo > u - 31 and sat < 26:  # borde suave
                px[x, y] = (r, g, b, max(0, round(255 - (brillo - (u - 31)) * (255 / 31))))
    bbox = im.getbbox()
    if bbox:
        im = im.crop(bbox)
    im.save(a.salida)
    print(f"ok {a.salida} {im.size}  — revisa el borde: si el producto es blanco, sube --umbral o recorta a mano")


def recortar(a):
    im = Image.open(a.entrada)
    im.crop((a.x, a.y, a.x + a.ancho, a.y + a.alto)).save(a.salida, quality=88)
    print(f"ok {a.salida}")


def web(a):
    src = Path(a.entrada)
    archivos = [p for p in (src.iterdir() if src.is_dir() else [src]) if p.suffix.lower() in EXT_IMG]
    out = Path(a.carpeta_salida)
    out.mkdir(parents=True, exist_ok=True)
    anchos = [int(x) for x in a.anchos.split(",")]
    for p in archivos:
        im = Image.open(p)
        modo = "RGBA" if im.mode in ("RGBA", "LA", "P") else "RGB"
        im = im.convert(modo)
        for w in anchos:
            if w > im.width:
                continue
            h = round(im.height * w / im.width)
            dst = out / f"{p.stem}-{w}.webp"
            im.resize((w, h), Image.LANCZOS).save(dst, "WEBP", quality=a.calidad, method=6)
            print(f"{dst.name:40} {w}x{h}  {dst.stat().st_size/1024:6.0f} KB")
        dst = out / f"{p.stem}.webp"
        im.save(dst, "WEBP", quality=a.calidad, method=6)
        print(f"{dst.name:40} {im.width}x{im.height}  {dst.stat().st_size/1024:6.0f} KB  (original)")


def ffmpeg(args, timeout=180):
    if not shutil.which("ffmpeg"):
        sys.exit("ffmpeg no está en el PATH")
    r = subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-nostdin", *args], timeout=timeout)
    if r.returncode:
        sys.exit(f"ffmpeg falló ({r.returncode})")


def portada(a):
    ffmpeg(["-ss", str(a.segundo), "-i", a.video, "-frames:v", "1", "-q:v", "3", a.salida])
    print(f"ok {a.salida}")


def video_web(a):
    ffmpeg(["-i", a.video, "-an", "-vf", f"scale=-2:{a.alto}", "-c:v", "libx264", "-preset", "slow",
            "-crf", "28", "-pix_fmt", "yuv420p", "-movflags", "+faststart", a.salida], timeout=600)
    kb = Path(a.salida).stat().st_size / 1024
    aviso = "  ⚠ pesa más de 5 MB: subir --crf o recortar duración" if kb > 5120 else ""
    print(f"ok {a.salida} {kb:.0f} KB{aviso}")


def hoja(a):
    archivos = sorted(p for p in Path(a.carpeta).iterdir() if p.suffix.lower() in EXT_IMG)
    if not archivos:
        sys.exit("sin imágenes")
    lado, cols = 300, 4
    filas = (len(archivos) + cols - 1) // cols
    lienzo = Image.new("RGB", (cols * lado, filas * lado), (40, 40, 48))
    for i, p in enumerate(archivos):
        im = Image.open(p).convert("RGBA")
        im.thumbnail((lado - 10, lado - 10))
        fondo = Image.new("RGBA", im.size, (40, 40, 48, 255))
        fondo.alpha_composite(im)
        lienzo.paste(fondo.convert("RGB"), ((i % cols) * lado + 5, (i // cols) * lado + 5))
    lienzo.save(a.salida, quality=85)
    print(f"ok {a.salida} ({len(archivos)} imágenes)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("recortar-fondo"); s.add_argument("entrada"); s.add_argument("salida"); s.add_argument("--umbral", type=int, default=236); s.set_defaults(f=recortar_fondo)
    s = sub.add_parser("recortar"); s.add_argument("entrada"); s.add_argument("salida")
    for k in ("x", "y", "ancho", "alto"):
        s.add_argument(k, type=int)
    s.set_defaults(f=recortar)
    s = sub.add_parser("web"); s.add_argument("entrada"); s.add_argument("carpeta_salida"); s.add_argument("--anchos", default="480,960,1600"); s.add_argument("--calidad", type=int, default=82); s.set_defaults(f=web)
    s = sub.add_parser("portada"); s.add_argument("video"); s.add_argument("salida"); s.add_argument("--segundo", type=float, default=1.0); s.set_defaults(f=portada)
    s = sub.add_parser("video-web"); s.add_argument("video"); s.add_argument("salida"); s.add_argument("--alto", type=int, default=720); s.set_defaults(f=video_web)
    s = sub.add_parser("hoja"); s.add_argument("carpeta"); s.add_argument("salida"); s.set_defaults(f=hoja)
    a = ap.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
