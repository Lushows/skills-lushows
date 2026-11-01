#!/usr/bin/env python3
"""
revisar_pdp.py — auditoría estática de una página de producto antes de entregarla.

Uso:
    python revisar_pdp.py landing.html

Revisa sin navegador (complementa la revisión visual con Playwright a 390px):
  · HONESTIDAD: frases de escasez/urgencia/reseñas típicas de plantilla que suelen ser falsas.
  · CONVERSIÓN (Baymard): envío/costo total, fecha de entrega, garantía con días, precio por unidad,
    histograma de reseñas, botón fijo, MSI/pagos, FAQ.
  · TÉCNICA: lang, viewport, title/description, LCP con fetchpriority y sin lazy, alt en imágenes,
    width/height o aspect-ratio, videos autoplay con muted+playsinline+poster, prefers-reduced-motion,
    innerHTML, Intl.NumberFormat, peso de imágenes locales.

Salida: lista ✓ / ⚠ / ✗ y un puntaje. ✗ = no se entrega así. ⚠ = justificar o arreglar.
"""
import re
import sys
from pathlib import Path

SOSPECHOSAS = [
    (r"solo quedan \d+", "escasez numérica escrita a mano"),
    (r"quedan \d+ (unidades|regalos|piezas)", "escasez numérica escrita a mano"),
    (r"\+\s?\d[\d.,]*\s*(clientes|compradores|personas) (felices|satisfechos)", "contador de clientes sin fuente"),
    (r"\b[45][.,]\d\s*/\s*5\b", "calificación escrita a mano (debe venir del widget de reseñas)"),
    (r"(personas|usuarios) (están )?viendo (esto|este producto)", "contador de visitantes (suele ser falso)"),
    (r"(alguien|\w+) de \w+ (acaba de )?compr(ó|o) hace \d+", "notificación de compra inventada"),
    (r"oferta termina en|termina hoy|últimas horas", "urgencia de reloj (solo si la fecha es real)"),
    (r"el mejor del mercado|n[úu]mero 1|#1 en", "superlativo sin prueba (publicidad engañosa)"),
    (r"certificad[oa] por|aprobad[oa] por|avalad[oa] por", "aval/certificación: requiere prueba documental"),
    (r"interpolad", "resolución interpolada: publicar solo la del sensor"),
]

CONVERSION = [
    (r"env[ií]o (gratis|incluido|\$)|costo de env[ií]o", "costo de envío visible en la página"),
    (r"llega (entre|el)|entrega (estimada|entre)|rec[ií]bel[oa]s?|data-entrega", "fecha de entrega (no solo 'x días')"),
    (r"\d+\s*d[ií]as (de garant[ií]a|para (probar|devolver))|garant[ií]a de \d+", "garantía con número de días"),
    (r"c/u|cada uno|por unidad|\$[\d,.]+ c/u", "precio por unidad en paquetes"),
    (r"histogram|rating-bars|distribuci[oó]n de (estrellas|calificaciones)|data-stars|data-barra", "histograma 5★→1★ de reseñas"),
    (r"sticky|position:\s*fixed", "botón de compra fijo en móvil"),
    (r"meses sin intereses|\bMSI\b|cuotas", "MSI / cuotas visibles"),
    (r"oxxo|spei|mercado ?pago|contraentrega|pse|nequi", "pagos locales visibles"),
    (r"<details|preguntas frecuentes|faq", "preguntas frecuentes"),
    (r"a escala|en la mano|tama[nñ]o real|medidas", "referencia de tamaño (foto a escala o medidas)"),
]


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    ruta = Path(sys.argv[1])
    html = ruta.read_text(encoding="utf-8")
    # sumar CSS y JS locales enlazados (la plantilla separa pdp.css / pdp.js)
    extra = ""
    for ref in re.findall(r'(?:href|src)="([^"#?:]+\.(?:css|js))"', html, flags=re.I):
        p = ruta.parent / ref
        if p.exists():
            extra += "\n" + p.read_text(encoding="utf-8", errors="replace")
    low = (html + extra).lower()
    visible = re.sub(r"<(script|style)[\s\S]*?</\1>|<!--[\s\S]*?-->", " ", html)
    texto = re.sub(r"<[^>]+>", " ", visible).lower()
    ok, warn, err = [], [], []

    # --- honestidad
    for patron, motivo in SOSPECHOSAS:
        for m in re.finditer(patron, texto):
            frag = texto[max(0, m.start() - 30): m.end() + 30].strip()
            (err if "escasez" in motivo or "contador" in motivo or "inventada" in motivo or "calificación" in motivo else warn).append(f"{motivo}: «…{frag}…»")

    # --- conversión
    for patron, que in CONVERSION:
        (ok if re.search(patron, low) else warn).append(("tiene " if re.search(patron, low) else "falta: ") + que)

    # --- técnica
    chk = lambda cond, bien, mal, grave=False: (ok.append(bien) if cond else (err if grave else warn).append(mal))
    chk(re.search(r'<html[^>]+lang=', low), "lang definido", "falta lang en <html>")
    chk("name=\"viewport\"" in low, "viewport móvil", "falta meta viewport", grave=True)
    chk(re.search(r"<title>[^<]{10,}", low), "title", "title ausente o muy corto")
    chk('name="description"' in low, "meta description", "falta meta description")

    imgs = re.findall(r"<img\b[^>]*>", visible, flags=re.I)
    if imgs:
        primera = imgs[0].lower()
        chk("fetchpriority" in primera and "loading=\"lazy\"" not in primera,
            "primera imagen (LCP) con fetchpriority y sin lazy",
            "primera imagen: agregar fetchpriority=\"high\" y quitar loading=lazy", grave=True)
        sin_alt = [i for i in imgs if not re.search(r'\balt=', i, re.I)]
        chk(not sin_alt, "todas las imágenes con alt", f"{len(sin_alt)} imágenes sin alt")
        lazy = sum(1 for i in imgs[1:] if 'loading="lazy"' in i.lower())
        chk(lazy >= max(0, len(imgs) - 4), "imágenes bajo el pliegue con lazy", f"solo {lazy}/{len(imgs)-1} imágenes secundarias con loading=lazy")

    for v in re.findall(r"<video\b[^>]*>", visible, flags=re.I):
        vl = v.lower()
        if "autoplay" in vl:
            chk("muted" in vl and "playsinline" in vl, "video autoplay con muted+playsinline",
                "video autoplay sin muted/playsinline (no arranca en iPhone)", grave=True)
            chk("poster=" in vl, "video con poster", "video sin poster")

    n_comp = len(re.findall(r'data-origen="competencia"', visible))
    chk(n_comp == 0, "sin contenido de competencia", f"{n_comp} bloques con contenido de competencia (MODO PRUEBA): reemplazar por propio antes de publicar", grave=True)
    chk("prefers-reduced-motion" in low, "respeta prefers-reduced-motion", "falta @media (prefers-reduced-motion)")
    chk(".innerhtml" not in low, "sin innerHTML", "usa innerHTML: cambiar por textContent/DOM", grave=True)
    if re.search(r"\$\s?\d", texto):
        chk("intl.numberformat" in low or "tolocalestring" in low, "precios formateados con Intl",
            "precios dinámicos sin Intl.NumberFormat/toLocaleString")

    pesadas = []
    for src in re.findall(r'src="([^"#?]+\.(?:jpe?g|png|webp|avif|gif|mp4))', html, flags=re.I):
        p = (ruta.parent / src)
        if p.exists() and p.stat().st_size > (5_000_000 if src.endswith(".mp4") else 400_000):
            pesadas.append(f"{src} {p.stat().st_size/1024:.0f} KB")
    chk(not pesadas, "medios locales con peso razonable", "medios pesados: " + ", ".join(sorted(set(pesadas))))

    # --- reporte
    for x in ok:
        print("✓", x)
    for x in warn:
        print("⚠", x)
    for x in err:
        print("✗", x)
    total = len(ok) + len(warn) + len(err)
    puntaje = round(100 * (len(ok) + 0.5 * len(warn)) / total) if total else 0
    print(f"\nPuntaje {puntaje}/100 · {len(ok)} ✓ · {len(warn)} ⚠ · {len(err)} ✗")
    sys.exit(1 if err else 0)


if __name__ == "__main__":
    main()
