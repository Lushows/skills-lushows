#!/usr/bin/env python3
"""
espiar_tienda.py — radiografía de una página de producto de referencia (Shopify primero).

Uso:
    python espiar_tienda.py "https://tienda.com/products/handle" [carpeta_salida]

Qué saca (sin navegador, solo HTTP):
  1. Producto desde <url>.json: título, variantes, precio, precio tachado, fotos, descripción,
     fecha de creación/publicación (¿test de ayer o ganador de meses?).
  2. Tema de Shopify y apps de conversión detectadas en el HTML (bundles, reseñas, urgencia,
     constructores de página, email/SMS, pagos).
  3. Configuración de Kaching Bundles si existe (niveles, descuentos, preselección, regalos).
  4. Conteo REAL de reseñas en Loox / Judge.me cuando se puede leer el widget.
  5. Videos alojados (mp4/m3u8) y variables de color del tema.

Salida: <carpeta>/radiografia.json + imprime un resumen. Lo que NO puede ver (orden visual de
secciones, animaciones, carrito) se completa con Playwright a 390x844 (ver references/01).

Solo lee páginas públicas. No reutilices textos, fotos, videos ni reseñas ajenas: se estudia la
estructura, no se copia el contenido.
"""
import json
import re
import sys
import urllib.request
from pathlib import Path

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/130 Safari/537.36"

APPS = {
    "bundles": ["kaching", "bundler", "fast bundle", "wide bundles", "zipify", "rebuy", "releasit", "easysell", "vitals"],
    "resenas": ["loox", "judge.me", "judgeme", "yotpo", "okendo", "stamped", "ali-reviews", "alireviews", "trustoo", "ryviu", "rivyo", "reviews.io"],
    "urgencia": ["countdown", "timer", "hurrify", "scarcity", "stock-counter", "sales-pop", "fomo"],
    "constructor": ["gempages", "pagefly", "shogun", "replo", "zipify-pages"],
    "email_sms": ["klaviyo", "omnisend", "postscript", "attentive", "privy"],
    "upsell_post": ["reconvert", "aftersell", "carthook", "upcart", "monster cart"],
    "pagos_latam": ["mercadopago", "conekta", "openpay", "kueski", "aplazo", "oxxo", "addi", "sistecredito", "wompi"],
    "cod": ["cod form", "releasit", "easysell", "codform", "dropi"],
}


def get(url, as_json=False):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "es-MX,es;q=0.9"})
    with urllib.request.urlopen(req, timeout=30) as r:
        body = r.read().decode("utf-8", "replace")
    return json.loads(body) if as_json else body


def texto_plano(html):
    html = re.sub(r"<(script|style)[\s\S]*?</\1>", " ", html)
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html)).strip()


def producto(url):
    base = url.split("?")[0].rstrip("/")
    try:
        p = get(base + ".json", as_json=True)["product"]
    except Exception as e:  # tienda no Shopify o JSON cerrado
        return {"error": f"sin {base}.json ({e})"}
    return {
        "id": p.get("id"),
        "titulo": p.get("title"),
        "marca_vendor": p.get("vendor"),
        "creado": p.get("created_at"),
        "publicado": p.get("published_at"),
        "variantes": [
            {"nombre": v.get("title"), "precio": v.get("price"), "tachado": v.get("compare_at_price"), "sku": v.get("sku")}
            for v in p.get("variants", [])
        ],
        "opciones": [{o["name"]: o["values"]} for o in p.get("options", [])],
        "fotos": [i["src"] for i in p.get("images", [])],
        "descripcion": texto_plano(p.get("body_html") or "")[:4000],
    }


def apps_detectadas(html):
    low = html.lower()
    out = {}
    for grupo, claves in APPS.items():
        # límite de palabra: evita falsos positivos ("addi" dentro de "additional")
        hits = {k: n for k in claves if (n := len(re.findall(r"(?<![a-z])" + re.escape(k) + r"(?![a-z])", low)))}
        if hits:
            out[grupo] = hits
    return out


def kaching(html):
    """Busca el JSON de configuración de Kaching Bundles embebido en la página."""
    m = re.search(r'\{"blockTitle"[\s\S]*?"otherProductHandles":\[[^\]]*\]\}', html)
    if not m:
        return None
    try:
        cfg = json.loads(m.group(0))
    except json.JSONDecodeError:
        return {"crudo": m.group(0)[:500]}
    gifts = (cfg.get("progressiveGifts") or {}).get("gifts") or []
    return {
        "titulo_bloque": cfg.get("blockTitle"),
        "preseleccionado": cfg.get("preselectedDealBarId"),
        "niveles": [
            {
                "id": d.get("id"),
                "titulo": d.get("title"),
                "cantidad": d.get("quantity"),
                "tipo_descuento": d.get("discountType"),
                "valor": d.get("discountValue"),
                "insignia": d.get("badgeText"),
            }
            for d in cfg.get("dealBars", [])
        ],
        "regalos_progresivos": {
            "titulo": (cfg.get("progressiveGifts") or {}).get("title"),
            "regalos": [{"titulo": g.get("title"), "desbloquea_en_nivel": g.get("unlockAtBar")} for g in gifts],
        },
    }


def resenas_reales(html, product_id):
    out = {}
    # el id de tienda aparece como loox.io/widget/<id>/ y a veces con barras escapadas (loox.io\/widget\/<id>\/)
    m = re.search(r"loox\.io\\?/widget\\?/([A-Za-z0-9_-]+)\\?/", html)
    if m and product_id:
        try:
            w = texto_plano(get(f"https://loox.io/widget/{m.group(1)}/reviews/{product_id}?limit=50"))
            conteo = re.search(r"\((\d+)\)", w)
            out["loox"] = {"texto_widget": w[:300], "primer_conteo": conteo.group(1) if conteo else None}
        except Exception as e:
            out["loox"] = {"error": str(e)}
    rating_escrito = re.findall(r"(\d[.,]\d)\s*/\s*5[^<]{0,60}", texto_plano(html))
    if rating_escrito:
        out["rating_escrito_en_la_pagina"] = rating_escrito[:5]
    return out


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    url = sys.argv[1]
    carpeta = Path(sys.argv[2] if len(sys.argv) > 2 else "radiografia")
    carpeta.mkdir(parents=True, exist_ok=True)

    html = get(url)
    (carpeta / "pagina.html").write_text(html, encoding="utf-8")
    prod = producto(url)
    pid = prod.get("id")

    tema = re.search(r"Shopify\.theme\s*=\s*(\{[^}]*\})", html)
    radiografia = {
        "url": url,
        "producto": prod,
        "tema_shopify": json.loads(tema.group(1)) if tema else None,
        "apps": apps_detectadas(html),
        "kaching": kaching(html),
        "resenas": resenas_reales(html, pid),
        "videos": sorted(set(re.findall(r"(?:https?:)?//[^\"' )]+\.(?:mp4|m3u8)", html)))[:20],
        "youtube": sorted(set(re.findall(r"youtube\.com/(?:embed/|watch\?v=)[\w-]+", html)))[:10],
        "colores_tema": sorted(set(re.findall(r"--color-[a-z-]+:\s*[^;\"]+", html)))[:30],
    }
    (carpeta / "radiografia.json").write_text(json.dumps(radiografia, ensure_ascii=False, indent=2), encoding="utf-8")

    p = radiografia["producto"]
    print(f"\n== {p.get('titulo')}  (creado {p.get('creado')}, publicado {p.get('publicado')})")
    for v in p.get("variantes", []):
        print(f"   {v['nombre']}: ${v['precio']}  tachado ${v['tachado']}")
    print("== tema:", (radiografia["tema_shopify"] or {}).get("schema_name"))
    print("== apps:", json.dumps(radiografia["apps"], ensure_ascii=False))
    if radiografia["kaching"]:
        k = radiografia["kaching"]
        print("== bundles:", [(n["titulo"], n["cantidad"], n["tipo_descuento"], n["valor"]) for n in k["niveles"]])
        print("   regalos:", k["regalos_progresivos"])
    r = radiografia["resenas"]
    print("== reseñas:", json.dumps(r, ensure_ascii=False)[:400])
    if (r.get("loox") or {}).get("primer_conteo") == "0" and r.get("rating_escrito_en_la_pagina"):
        print("   ⚠ ALERTA: la página muestra calificación escrita pero el widget tiene 0 reseñas reales. No copiar.")
    if radiografia["kaching"] and re.search(r"solo quedan|quedan \d+", str(radiografia["kaching"]), re.I):
        print("   ⚠ ALERTA: escasez escrita a mano en los bundles (verificar si es real antes de imitar).")
    print(f"== videos: {len(radiografia['videos'])}  ->  {carpeta / 'radiografia.json'}")


if __name__ == "__main__":
    main()
