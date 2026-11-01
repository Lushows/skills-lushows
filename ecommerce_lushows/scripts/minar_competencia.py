#!/usr/bin/env python3
"""
minar_competencia.py — extrae de tiendas competidoras que venden el MISMO producto:
producto, precios, oferta, apps, RESEÑAS de clientes y VIDEOS, para ANÁLISIS INTERNO.

Uso:
    python minar_competencia.py urls.txt <carpeta_salida> [--max-resenas 300] [--bajar-videos] [--max-mb 60]

urls.txt: una URL de producto por línea (Shopify rinde más; otras plataformas dan lo que se pueda).

Salida (<carpeta>/):
  <tienda>/radiografia.json     producto, precio, tachado, apps, oferta Kaching, videos
  <tienda>/resenas.json         reseñas normalizadas {estrellas, titulo, texto, autor, fecha, fuente, fotos}
  <tienda>/videos/*.mp4         (con --bajar-videos) para analizar_video.py
  resenas_todas.csv             corpus unificado para analizar_resenas.py
  resumen.md                    tabla comparativa de competidores

⚠ USO INTERNO. Las reseñas y videos de otras tiendas son de sus clientes y de sus dueños:
se ANALIZAN para sacar dolores, objeciones, ángulos y guiones. No se publican como propios
(PROFECO art. 32 / SIC Ley 1480 / derechos de autor). En páginas de PRUEBA se marcan con
data-origen="competencia" y revisar_pdp.py bloquea la publicación. Ver references/12.
"""
import argparse
import csv
import html as htmlmod
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/130 Safari/537.36"


def get(url, as_json=False, timeout=30, binario=False):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "es-MX,es;q=0.9,en;q=0.8"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        data = r.read()
    if binario:
        return data
    txt = data.decode("utf-8", "replace")
    return json.loads(txt) if as_json else txt


def limpio(t):
    t = re.sub(r"<(script|style)[\s\S]*?</\1>", " ", t or "")
    t = re.sub(r"<br\s*/?>", "\n", t)
    t = htmlmod.unescape(re.sub(r"<[^>]+>", " ", t))
    return re.sub(r"[ \t]+", " ", re.sub(r"\n\s*\n+", "\n", t)).strip()


def slug(url):
    host = urllib.parse.urlparse(url).netloc.replace("www.", "")
    return re.sub(r"[^a-z0-9]+", "-", host.lower()).strip("-")[:40]


# ------------------------------------------------------------------ producto
def producto_shopify(url):
    base = url.split("?")[0].rstrip("/")
    try:
        p = get(base + ".json", as_json=True)["product"]
    except Exception as e:
        return None, str(e)
    return {
        "id": p.get("id"), "handle": p.get("handle"), "titulo": p.get("title"), "vendor": p.get("vendor"),
        "creado": p.get("created_at"), "publicado": p.get("published_at"),
        "variantes": [{"nombre": v.get("title"), "precio": v.get("price"), "tachado": v.get("compare_at_price")} for v in p.get("variants", [])],
        "fotos": [i["src"] for i in p.get("images", [])],
        "descripcion": limpio(p.get("body_html"))[:6000],
    }, None


def jsonld(html):
    """Producto y reseñas desde schema.org (sirve en casi cualquier plataforma)."""
    out = {"producto": None, "resenas": [], "rating": None}
    for bloque in re.findall(r'<script[^>]+application/ld\+json[^>]*>([\s\S]*?)</script>', html, re.I):
        try:
            data = json.loads(bloque.strip())
        except Exception:
            continue
        for d in (data if isinstance(data, list) else data.get("@graph", [data]) if isinstance(data, dict) else []):
            if not isinstance(d, dict) or "Product" not in str(d.get("@type")):
                continue
            ofertas = d.get("offers") or {}
            if isinstance(ofertas, list):
                ofertas = ofertas[0] if ofertas else {}
            out["producto"] = {"titulo": d.get("name"), "precio": ofertas.get("price"), "moneda": ofertas.get("priceCurrency"), "descripcion": limpio(str(d.get("description", "")))[:3000]}
            ag = d.get("aggregateRating") or {}
            if ag:
                out["rating"] = {"valor": ag.get("ratingValue"), "conteo": ag.get("reviewCount") or ag.get("ratingCount")}
            for r in d.get("review") or []:
                if isinstance(r, dict):
                    out["resenas"].append({
                        "estrellas": _num((r.get("reviewRating") or {}).get("ratingValue")),
                        "titulo": r.get("name") or "", "texto": limpio(r.get("reviewBody") or ""),
                        "autor": (r.get("author") or {}).get("name") if isinstance(r.get("author"), dict) else r.get("author"),
                        "fecha": r.get("datePublished"), "fuente": "json-ld", "fotos": []})
    return out


def _num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


# ------------------------------------------------------------------ reseñas por app
def resenas_loox(html, pid, maximo):
    m = re.search(r"loox\.io\\?/widget\\?/([A-Za-z0-9_-]+)\\?/", html)
    if not (m and pid):
        return []
    out, pagina = [], 1
    while len(out) < maximo and pagina <= 20:
        try:
            w = get(f"https://loox.io/widget/{m.group(1)}/reviews/{pid}?limit=20&page={pagina}")
        except Exception:
            break
        bloques = re.findall(r'<div[^>]+class="[^"]*grid-item[^"]*"[\s\S]*?(?=<div[^>]+class="[^"]*grid-item|\Z)', w)
        nuevos = 0
        for b in bloques:
            texto = re.search(r'class="[^"]*(?:pre-wrap|main-text)[^"]*"[^>]*>([\s\S]*?)</', b)
            calif = re.search(r"Rating icons:\s*(\d)\s*/\s*5", b)  # etiqueta accesible por reseña
            estrellas = int(calif.group(1)) if calif else (len(re.findall(r"loox-icon[^>]*star(?!-empty)", b)) or None)
            autor = re.search(r'class="[^"]*title[^"]*"[^>]*>([\s\S]*?)</', b)
            fotos = re.findall(r'(https://images\.loox\.io/[^"\')\s]+)', b)
            if texto:
                out.append({"estrellas": estrellas, "titulo": "", "texto": limpio(texto.group(1)), "autor": limpio(autor.group(1)) if autor else "", "fecha": None, "fuente": "loox", "fotos": fotos[:4]})
                nuevos += 1
        if not nuevos:
            break
        pagina += 1
    return out


def resenas_judgeme(html, url, pid, maximo):
    shop = re.search(r'Shopify\.shop\s*=\s*"([^"]+)"', html)
    if not (shop and pid and "judge" in html.lower()):
        return []
    out, pagina = [], 1
    while len(out) < maximo and pagina <= 20:
        q = urllib.parse.urlencode({"url": shop.group(1), "shop_domain": shop.group(1), "platform": "shopify", "page": pagina, "per_page": 20, "product_id": pid})
        try:
            data = get(f"https://judge.me/reviews/reviews_for_widget?{q}", as_json=True)
        except Exception:
            break
        h = data.get("html", "") if isinstance(data, dict) else ""
        revs = re.findall(r'<div class=[\'"]jdgm-rev [\s\S]*?(?=<div class=[\'"]jdgm-rev |\Z)', h)
        if not revs:
            break
        for r in revs:
            est = re.search(r"data-score=['\"](\d)", r)
            titulo = re.search(r"jdgm-rev__title['\"][^>]*>([\s\S]*?)</", r)
            cuerpo = re.search(r"jdgm-rev__body['\"][^>]*>([\s\S]*?)</div>", r)
            autor = re.search(r"jdgm-rev__author['\"][^>]*>([\s\S]*?)</", r)
            fecha = re.search(r"data-content=['\"]([^'\"]+)['\"][^>]*jdgm-rev__timestamp|jdgm-rev__timestamp[^>]*data-content=['\"]([^'\"]+)", r)
            fotos = re.findall(r"(https://[^'\"\s]+judge[^'\"\s]+\.(?:jpe?g|png|webp))", r)
            out.append({"estrellas": _num(est.group(1)) if est else None, "titulo": limpio(titulo.group(1)) if titulo else "",
                        "texto": limpio(cuerpo.group(1)) if cuerpo else "", "autor": limpio(autor.group(1)) if autor else "",
                        "fecha": (fecha.group(1) or fecha.group(2)) if fecha else None, "fuente": "judge.me", "fotos": fotos[:4]})
        pagina += 1
    return out


def resenas_yotpo(html, pid, maximo):
    key = re.search(r"staticw2\.yotpo\.com/([A-Za-z0-9]{20,})/widget\.js", html) or re.search(r'data-appkey="([A-Za-z0-9]{20,})"', html)
    if not (key and pid):
        return []
    out, pagina = [], 1
    while len(out) < maximo and pagina <= 10:
        try:
            data = get(f"https://api-cdn.yotpo.com/v1/widget/{key.group(1)}/products/{pid}/reviews.json?per_page=50&page={pagina}", as_json=True)
        except Exception:
            break
        revs = (((data or {}).get("response") or {}).get("reviews")) or []
        if not revs:
            break
        for r in revs:
            out.append({"estrellas": _num(r.get("score")), "titulo": r.get("title") or "", "texto": limpio(r.get("content")),
                        "autor": (r.get("user") or {}).get("display_name"), "fecha": r.get("created_at"), "fuente": "yotpo",
                        "fotos": [i.get("original_url") for i in (r.get("images_data") or []) if i.get("original_url")][:4]})
        pagina += 1
    return out


def resenas_okendo(html, pid, maximo):
    sub = re.search(r'okendo[^"]*?(?:subscriberId|subscriber-id)["\s:=]+["\']?([0-9a-f-]{36})', html, re.I)
    if not (sub and pid):
        return []
    out, url = [], f"https://api.okendo.io/v1/stores/{sub.group(1)}/products/shopify-{pid}/reviews?limit=25"
    while url and len(out) < maximo:
        try:
            data = get(url, as_json=True)
        except Exception:
            break
        for r in data.get("reviews", []):
            out.append({"estrellas": _num(r.get("rating")), "titulo": r.get("title") or "", "texto": limpio(r.get("body")),
                        "autor": (r.get("reviewer") or {}).get("displayName"), "fecha": r.get("dateCreated"), "fuente": "okendo",
                        "fotos": [m.get("fullSizeUrl") for m in (r.get("media") or []) if m.get("fullSizeUrl")][:4]})
        nxt = data.get("nextUrl")
        url = ("https://api.okendo.io/v1" + nxt) if nxt else None
    return out


def resenas_en_pagina(html):
    """Último recurso: bloques de reseña escritos en el propio HTML (temas con testimonios)."""
    out = []
    for b in re.findall(r'<(?:div|article|li)[^>]+class="[^"]*(?:review|testimonial|resena)[^"]*"[^>]*>([\s\S]{40,1500}?)</(?:div|article|li)>', html, re.I)[:40]:
        t = limpio(b)
        if 40 < len(t) < 1200:
            out.append({"estrellas": None, "titulo": "", "texto": t, "autor": "", "fecha": None, "fuente": "html-tema (puede ser texto de plantilla)", "fotos": []})
    return out


# ------------------------------------------------------------------ videos
def videos(html):
    mp4 = sorted(set(u if u.startswith("http") else "https:" + u for u in re.findall(r'(?:https?:)?//[^"\'\s)]+\.mp4[^"\'\s)]*', html)))
    yt = sorted(set(re.findall(r"(?:youtube\.com/(?:embed/|watch\?v=|shorts/)|youtu\.be/)([\w-]{11})", html)))
    vimeo = sorted(set(re.findall(r"player\.vimeo\.com/video/(\d+)", html)))
    tiktok = sorted(set(re.findall(r"tiktok\.com/@[\w.]+/video/\d+", html)))
    # quedarse con la mejor calidad por video de Shopify (mismo id, distinta resolución)
    mejor = {}
    for u in mp4:
        vid = re.search(r"/videos/c/vp/([0-9a-f]+)/", u)
        k = vid.group(1) if vid else u
        res = int((re.search(r"(\d{3,4})p", u) or [0, 0])[1])
        if k not in mejor or res > mejor[k][0]:
            mejor[k] = (res, u)
    return {"mp4": [v[1] for v in mejor.values()], "youtube": yt, "vimeo": vimeo, "tiktok": tiktok}


# ------------------------------------------------------------------ principal
def minar(url, carpeta, maximo, bajar, max_mb):
    nombre = slug(url)
    dst = Path(carpeta) / nombre
    dst.mkdir(parents=True, exist_ok=True)
    print(f"\n== {nombre}  {url}")
    try:
        html = get(url)
    except Exception as e:
        print(f"   ✗ no carga: {e}")
        return None
    prod, err = producto_shopify(url)
    ld = jsonld(html)
    pid = (prod or {}).get("id")
    moneda = re.search(r'Shopify\.currency\s*=\s*\{"active":"([A-Z]{3})"', html)

    resenas = []
    for fn in (lambda: resenas_loox(html, pid, maximo), lambda: resenas_judgeme(html, url, pid, maximo),
               lambda: resenas_yotpo(html, pid, maximo), lambda: resenas_okendo(html, pid, maximo)):
        try:
            resenas += fn()
        except Exception as e:
            print(f"   ⚠ reseñas: {e}")
    resenas += ld["resenas"]
    if not resenas:
        resenas = resenas_en_pagina(html)
    vistos, unicas = set(), []
    for r in resenas:
        k = (r.get("texto") or "")[:120]
        if k and k not in vistos:
            vistos.add(k)
            unicas.append(r)

    vids = videos(html)
    rad = {
        "url": url, "tienda": nombre, "moneda": moneda.group(1) if moneda else (ld["producto"] or {}).get("moneda"),
        "producto": prod or ld["producto"], "error_json": err, "rating_jsonld": ld["rating"],
        "tema": (re.search(r'"schema_name":"([^"]+)"', html) or [None, None])[1],
        "apps": sorted({a for a in ["kaching", "loox", "judge", "yotpo", "okendo", "stamped", "klaviyo", "gempages", "pagefly", "releasit", "easysell", "vitals", "countdown", "timer"] if a in html.lower()}),
        "videos": vids, "resenas_extraidas": len(unicas),
        "fuentes_resenas": sorted({r["fuente"] for r in unicas}),
    }
    (dst / "radiografia.json").write_text(json.dumps(rad, ensure_ascii=False, indent=2), encoding="utf-8")
    (dst / "resenas.json").write_text(json.dumps(unicas, ensure_ascii=False, indent=2), encoding="utf-8")
    (dst / "pagina.html").write_text(html, encoding="utf-8")

    if bajar and vids["mp4"]:
        vdir = dst / "videos"
        vdir.mkdir(exist_ok=True)
        for i, u in enumerate(vids["mp4"][:12], 1):
            try:
                req = urllib.request.Request(u, headers={"User-Agent": UA, "Range": f"bytes=0-{max_mb * 1024 * 1024}"})
                with urllib.request.urlopen(req, timeout=90) as r:
                    (vdir / f"video{i:02d}.mp4").write_bytes(r.read())
            except Exception as e:
                print(f"   ⚠ video {i}: {e}")

    precio = None
    if prod and prod.get("variantes"):
        precio = f"{prod['variantes'][0]['precio']} (tachado {prod['variantes'][0]['tachado']})"
    elif ld["producto"]:
        precio = ld["producto"].get("precio")
    print(f"   precio {precio} {rad['moneda'] or ''} · reseñas {len(unicas)} {rad['fuentes_resenas']} · videos mp4 {len(vids['mp4'])} yt {len(vids['youtube'])}")
    return rad, unicas, precio


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("urls")
    ap.add_argument("carpeta")
    ap.add_argument("--max-resenas", type=int, default=300)
    ap.add_argument("--bajar-videos", action="store_true")
    ap.add_argument("--max-mb", type=int, default=60)
    a = ap.parse_args()

    urls = [l.strip() for l in Path(a.urls).read_text(encoding="utf-8").splitlines() if l.strip() and not l.startswith("#")]
    Path(a.carpeta).mkdir(parents=True, exist_ok=True)
    filas, corpus = [], []
    for u in urls:
        r = minar(u, a.carpeta, a.max_resenas, a.bajar_videos, a.max_mb)
        if not r:
            filas.append(f"| {slug(u)} | no cargó | | | | |")
            continue
        rad, resenas, precio = r
        est = [x["estrellas"] for x in resenas if x.get("estrellas")]
        prom = f"{sum(est)/len(est):.1f}" if est else "—"
        filas.append(f"| {rad['tienda']} | {precio} {rad['moneda'] or ''} | {len(resenas)} ({prom}★) | {len(rad['videos']['mp4'])} mp4 · {len(rad['videos']['youtube'])} yt | {', '.join(rad['apps'])} | {rad['tema'] or ''} |")
        for x in resenas:
            corpus.append({"tienda": rad["tienda"], **{k: x.get(k) for k in ("estrellas", "titulo", "texto", "autor", "fecha", "fuente")}, "fotos": " ".join(x.get("fotos") or [])})

    with open(Path(a.carpeta) / "resenas_todas.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=["tienda", "estrellas", "titulo", "texto", "autor", "fecha", "fuente", "fotos"])
        w.writeheader()
        w.writerows(corpus)
    resumen = ["# Competencia — resumen (USO INTERNO)", "", "| Tienda | Precio | Reseñas | Videos | Apps | Tema |", "|---|---|---|---|---|---|", *filas, "",
               f"Corpus: {len(corpus)} reseñas → `resenas_todas.csv` → `python analizar_resenas.py resenas_todas.csv`"]
    (Path(a.carpeta) / "resumen.md").write_text("\n".join(resumen), encoding="utf-8")
    print("\n" + "\n".join(resumen))


if __name__ == "__main__":
    main()
