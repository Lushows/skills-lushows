#!/usr/bin/env python3
"""
analizar_resenas.py — voz del cliente a partir de reseñas de la competencia (o propias).

Uso:
    python analizar_resenas.py resenas_todas.csv [salida.md] [--temas temas.json]

Entrada: CSV con columnas tienda, estrellas, titulo, texto (lo genera minar_competencia.py;
también sirve un CSV exportado de Judge.me/Loox o reseñas copiadas de Amazon/Mercado Libre).

Qué produce (voz_del_cliente.md + .json):
  1. Distribución de estrellas total y por tienda.
  2. Temas: cuántas veces aparece cada tema en reseñas BUENAS (4-5★ = qué enamora) y MALAS
     (1-3★ = qué duele / qué objetar), con 3 citas literales por lado.
  3. Frases literales candidatas a titular ("por fin", "ya no", "me encanta", "vale la pena"…).
  4. Frases de decepción ("dejó de", "no sirve", "no llegó"…) → FAQ y "¿es para ti?".
  5. Bigramas y trigramas más repetidos en buenas y en malas.

El reporte es materia prima: Claude lo lee y lo convierte en titulares, beneficios, objeciones,
FAQ y guiones de video (references/06 y 12). Las citas son de clientes de OTRAS tiendas:
se usan para entender y redactar, nunca se publican como reseñas propias.
"""
import argparse
import csv
import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

TEMAS = {
    "calidad_materiales": ["calidad", "material", "plastico", "plástico", "resistente", "fragil", "frágil", "barato", "cheap", "quality", "sturdy", "flimsy", "acabado", "se rompio", "se rompió", "broke"],
    "bateria_carga": ["bateria", "batería", "carga", "cargar", "battery", "charge", "dura poco", "duracion", "duración", "se descarga"],
    "funciona_efectividad": ["funciona", "no funciona", "sirve", "no sirve", "works", "doesn't work", "does not work", "efectivo", "resultado", "results", "effective"],
    "facilidad_uso": ["facil", "fácil", "sencillo", "intuitivo", "complicado", "dificil", "difícil", "easy", "simple", "confusing", "instrucciones", "manual"],
    "app_conexion": ["app", "aplicacion", "aplicación", "bluetooth", "wifi", "conecta", "conexion", "conexión", "sincroniza", "pair", "connect", "sync"],
    "imagen_video_camara": ["camara", "cámara", "video", "foto", "imagen", "resolucion", "resolución", "nitido", "nítido", "borroso", "camera", "picture", "footage", "blurry"],
    "sonido_audio": ["sonido", "audio", "volumen", "bocina", "microfono", "micrófono", "se escucha", "sound", "speaker", "volume", "mic"],
    "comodidad_ajuste": ["comodo", "cómodo", "incomodo", "incómodo", "ligero", "pesado", "talla", "tamaño", "ajusta", "queda", "comfortable", "fit", "size", "heavy", "light"],
    "diseno_estetica": ["diseño", "bonito", "bonita", "elegante", "estilo", "se ve", "color", "look", "stylish", "beautiful", "design"],
    "precio_valor": ["precio", "caro", "barato", "vale la pena", "valor", "costo", "price", "worth", "value", "expensive", "money"],
    "envio_tiempo": ["envio", "envío", "llego", "llegó", "tardo", "tardó", "rapido", "rápido", "entrega", "paqueteria", "paquetería", "shipping", "arrived", "delivery", "late"],
    "empaque_estado": ["empaque", "caja", "llego roto", "llegó roto", "dañado", "golpeado", "packaging", "box", "damaged"],
    "atencion_servicio": ["atencion", "atención", "servicio", "respondieron", "soporte", "devolucion", "devolución", "reembolso", "garantia", "garantía", "customer service", "refund", "support", "return"],
    "regalo": ["regalo", "regale", "regalé", "cumpleaños", "navidad", "gift", "present", "birthday"],
    "olor_sabor_textura": ["olor", "sabor", "textura", "huele", "sabe", "smell", "taste", "texture"],
    "durabilidad": ["duro", "dejo de", "dejó de", "a los dias", "a los días", "semana", "mes", "stopped", "after a week", "lasted", "durable"],
}

TITULAR = [r"por fin", r"ya no (tengo|tienes|me)", r"ahora puedo", r"me encant", r"vale (mucho )?la pena", r"lo (mejor|recomiendo)", r"super (bien|recomendad)",
           r"justo lo que", r"mejor de lo que", r"no puedo vivir sin", r"lo uso (todos los días|diario)", r"love (it|these|this)", r"game ?changer", r"worth (it|every)",
           r"exactly what", r"better than expected", r"highly recommend"]
DECEPCION = [r"dej[oó] de", r"no sirve", r"no funciona", r"no lleg", r"se rompi", r"no es como", r"no se parece", r"p[eé]sim", r"no lo recomiendo", r"devolv",
             r"se calient", r"no carga", r"no (se )?oscurec", r"muy (grande|voluminos|pesad)", r"se escucha mal", r"no (me )?(contestan|responden)",
             r"stopped working", r"doesn'?t work", r"broke", r"waste of money", r"not as described", r"returned", r"disappoint",
             r"won'?t charge", r"(very|gets?) hot", r"bulky", r"choppy", r"not the quality", r"is bad", r"too (loud|big|heavy)", r"can'?t be turned",
             r"doesn'?t really (seem to )?work", r"no (delivery|answer)", r"wrong", r"don'?t have it", r"dies (very )?fast", r"takes forever"]

STOP = set("""de la que el en y a los se del las un por con no una su para es al lo como más mas pero sus le ya o fue este ha si sí porque esta
entre cuando muy sin sobre también me hasta hay donde quien desde todo nos durante todos uno les ni contra otros ese eso ante ellos e esto mí antes
algunos qué unos yo otro otras otra él tanto esa estos mucho quienes nada muchos cual poco ella estar estas algunas algo nosotros mi mis tú te ti tu tus
the and to a of it is i for in this that was my with they but are on have be not so as very you them just these one all at had would get
producto lentes gafas""".split())


def norm(t):
    t = unicodedata.normalize("NFKD", (t or "").lower())
    return "".join(c for c in t if not unicodedata.combining(c))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv")
    ap.add_argument("salida", nargs="?", default="voz_del_cliente.md")
    ap.add_argument("--temas", help="JSON {tema: [palabras]} para agregar/reemplazar temas del vertical")
    ap.add_argument("--excluir-sospechosas", action="store_true", help="sacar del análisis las tiendas con riesgo ALTO de reseñas falsas/IA")
    a = ap.parse_args()

    temas = dict(TEMAS)
    if a.temas:
        temas.update(json.loads(Path(a.temas).read_text(encoding="utf-8")))

    filas = list(csv.DictReader(open(a.csv, encoding="utf-8-sig")))
    filas = [f for f in filas if (f.get("texto") or "").strip()]
    if not filas:
        sys.exit("CSV sin reseñas con texto")

    def est(f):
        try:
            return float(f.get("estrellas") or 0)
        except ValueError:
            return 0.0

    dist = Counter(int(est(f)) for f in filas if est(f))
    por_tienda = defaultdict(list)
    for f in filas:
        por_tienda[f.get("tienda", "?")].append(est(f))

    # ---- autenticidad por tienda (reseñas importadas, generadas con IA o de plantilla contaminan el análisis)
    MARCAS_IA = ["chatgpt said", "as an ai", "here's a review", "here is a review", "certainly!", "as a language model", "[product name]", "{{"]
    autent = {}
    for t, lista in defaultdict(list, {k: [f for f in filas if f.get("tienda", "?") == k] for k in por_tienda}).items():
        n = len(lista)
        e = [est(f) for f in lista if est(f)]
        pct5 = 100 * sum(1 for x in e if x >= 5) / len(e) if e else 0
        pct_bajas = 100 * sum(1 for x in e if x <= 3) / len(e) if e else 0
        aperturas = Counter(" ".join(re.findall(r"[a-záéíóúñü']+", norm(f["texto"]))[:4]) for f in lista if len(f["texto"]) > 20)
        top_ap, top_n = (aperturas.most_common(1) or [("", 0)])[0]
        cuerpos = Counter(norm(f["texto"])[:70] for f in lista)
        dup = sum(v - 1 for v in cuerpos.values() if v > 1)
        ia = sum(1 for f in lista if any(m in norm(f["texto"]) for m in MARCAS_IA))
        # ráfaga: muchas reseñas en la misma hora (cargas masivas / importadas)
        horas = Counter((f.get("fecha") or "")[:13] for f in lista if f.get("fecha"))
        rafaga_h, rafaga_n = (horas.most_common(1) or [("", 0)])[0]
        # autores con sufijo aleatorio pegado al nombre (Elijahntgw, Chloevnpd) o nombres de pila repetidos con inicial
        raros = sum(1 for f in lista if re.fullmatch(r"[A-Z][a-z]{3,}[b-df-hj-np-tv-z]{4}", (f.get("autor") or "").strip()))
        pilas = Counter((f.get("autor") or "").split(" ")[0] for f in lista if re.fullmatch(r"\S+ [A-Z]\.", (f.get("autor") or "").strip()))
        pila_top, pila_n = (pilas.most_common(1) or [("", 0)])[0]
        senales = []
        if rafaga_n >= 5:
            senales.append(f"{rafaga_n} reseñas en la misma hora ({rafaga_h})")
        if raros >= 3:
            senales.append(f"{raros} autores con letras al azar al final del nombre")
        if pila_n >= 5 and n >= 20:
            senales.append(f"nombre «{pila_top} X.» repetido ×{pila_n}")
        if n >= 30 and pct5 >= 90 and pct_bajas < 3:
            senales.append(f"{pct5:.0f}% 5★ y {pct_bajas:.0f}% ≤3★ (distribución irreal)")
        if n >= 20 and top_n / n >= .06 and top_n >= 3:
            senales.append(f"apertura repetida «{top_ap}…» ×{top_n}")
        if dup:
            senales.append(f"{dup} textos duplicados")
        if ia:
            senales.append(f"{ia} con marcas de texto de IA")
        riesgo = "ALTO" if len(senales) >= 2 or ia else "medio" if senales else "bajo"
        # marcar reseñas individuales sospechosas (una tienda puede mezclar un lote falso con reseñas reales)
        for f in lista:
            autor = (f.get("autor") or "").strip()
            motivos = []
            if rafaga_n >= 5 and (f.get("fecha") or "")[:13] == rafaga_h:
                motivos.append("ráfaga")
            if re.fullmatch(r"[A-Z][a-z]{3,}[b-df-hj-np-tv-z]{4}", autor):
                motivos.append("autor aleatorio")
            if pila_n >= 5 and autor.startswith(pila_top + " ") and re.fullmatch(r"\S+ [A-Z]\.", autor):
                motivos.append("nombre en serie")
            if top_n >= 3 and n >= 20 and " ".join(re.findall(r"[a-záéíóúñü']+", norm(f["texto"]))[:4]) == top_ap:
                motivos.append("apertura de plantilla")
            if cuerpos[norm(f["texto"])[:70]] > 1:
                motivos.append("duplicada")
            if any(m in norm(f["texto"]) for m in MARCAS_IA):
                motivos.append("texto de IA")
            f["_sospecha"] = motivos
        limpias = [f for f in lista if not f["_sospecha"]]
        e2 = [est(f) for f in limpias if est(f)]
        irreal = len(limpias) >= 30 and e2 and sum(1 for x in e2 if x >= 5) / len(e2) >= .9 and sum(1 for x in e2 if x <= 3) / len(e2) < .03
        autent[t] = {"n": n, "pct5": round(pct5), "pct_bajas": round(pct_bajas), "senales": senales, "riesgo": riesgo,
                     "sospechosas": n - len(limpias), "creibles": 0 if irreal else len(limpias), "tienda_descartada": bool(irreal)}
    if a.excluir_sospechosas:
        descartadas = {t for t, v in autent.items() if v["tienda_descartada"]}
        filas = [f for f in filas if not f.get("_sospecha") and f.get("tienda", "?") not in descartadas]
        if not filas:
            sys.exit("no quedaron reseñas creíbles")
        dist = Counter(int(est(f)) for f in filas if est(f))

    buenas = [f for f in filas if est(f) >= 4]
    malas = [f for f in filas if 0 < est(f) <= 3]
    sin_est = [f for f in filas if not est(f)]

    tema_res = {}
    for tema, claves in temas.items():
        # palabras largas por raíz (cómodo → cómodas), cortas exactas (app, mes)
        pats = [re.compile(r"(?<!\w)" + (re.escape(norm(k)[:-1]) if len(k) > 5 and " " not in k else re.escape(norm(k)) + r"(?!\w)")) for k in claves]
        def hits(lista):
            return [f for f in lista if any(p.search(norm(f["titulo"] + " " + f["texto"])) for p in pats)]
        hb, hm = hits(buenas), hits(malas)
        tema_res[tema] = {"buenas": len(hb), "malas": len(hm),
                          "citas_buenas": [f["texto"][:220] for f in hb[:3]], "citas_malas": [f["texto"][:220] for f in hm[:3]]}

    def frases(lista, patrones):
        out = []
        for f in lista:
            for oracion in re.split(r"(?<=[.!?¡¿\n])\s+", f["texto"]):
                if any(re.search(p, norm(oracion)) for p in patrones) and 12 < len(oracion) < 220:
                    out.append((oracion.strip(), f.get("tienda"), f.get("estrellas")))
        return out

    tit = frases(buenas + sin_est, TITULAR)
    dec = frases(malas + sin_est, DECEPCION)

    def ngramas(lista, n):
        c = Counter()
        for f in lista:
            w = [x for x in re.findall(r"[a-záéíóúñü']+", (f["titulo"] + " " + f["texto"]).lower()) if x not in STOP and len(x) > 2]
            c.update(" ".join(w[i:i + n]) for i in range(len(w) - n + 1))
        return [(k, v) for k, v in c.most_common(15) if v > 1]

    total = len(filas)
    prom = sum(est(f) for f in filas if est(f)) / max(1, sum(1 for f in filas if est(f)))
    L = [f"# Voz del cliente — {total} reseñas (USO INTERNO: análisis, no publicar)", "",
         f"Promedio {prom:.2f}★ · buenas (4-5★) {len(buenas)} · malas (1-3★) {len(malas)} · sin estrellas {len(sin_est)}", "",
         "## Distribución", "", "| ★ | reseñas | % |", "|---|---|---|"]
    for s in (5, 4, 3, 2, 1):
        L.append(f"| {s} | {dist.get(s, 0)} | {100 * dist.get(s, 0) / max(1, sum(dist.values())):.0f}% |")
    L += ["", "| Tienda | reseñas | promedio |", "|---|---|---|"]
    for t, v in sorted(por_tienda.items(), key=lambda x: -len(x[1])):
        e = [x for x in v if x]
        L.append(f"| {t} | {len(v)} | {sum(e)/len(e):.2f}★ |" if e else f"| {t} | {len(v)} | — |")

    L += ["", "## Autenticidad por tienda (¿son reseñas reales?)", "", "| Tienda | reseñas | % 5★ | % ≤3★ | riesgo | sospechosas | creíbles | señales |", "|---|---|---|---|---|---|---|---|"]
    for t, v in sorted(autent.items(), key=lambda x: -x[1]["n"]):
        cre = "0 (tienda descartada: lo que queda sigue siendo irreal)" if v["tienda_descartada"] else v["creibles"]
        L.append(f"| {t} | {v['n']} | {v['pct5']}% | {v['pct_bajas']}% | {v['riesgo']} | {v['sospechosas']} | {cre} | {'; '.join(v['senales']) or '—'} |")
    L += ["", ("Reseñas sospechosas **excluidas una por una** del análisis de abajo (ráfaga, autor aleatorio, nombre en serie, apertura de plantilla, duplicada, texto de IA)."
               if a.excluir_sospechosas else "Repetir con `--excluir-sospechosas` para analizar solo las creíbles.")]
    L += ["", "## Temas (qué enamora vs qué duele)", "", "| Tema | en buenas | en malas | lectura |", "|---|---|---|---|"]
    for tema, r in sorted(tema_res.items(), key=lambda x: -(x[1]["buenas"] + x[1]["malas"])):
        if not (r["buenas"] or r["malas"]):
            continue
        lectura = "OBJECIÓN a resolver en la página" if r["malas"] > r["buenas"] else "BENEFICIO para titular" if r["buenas"] >= 2 * max(1, r["malas"]) else "mixto: prometer con matiz"
        L.append(f"| {tema} | {r['buenas']} | {r['malas']} | {lectura} |")
    for tema, r in sorted(tema_res.items(), key=lambda x: -(x[1]["buenas"] + x[1]["malas"]))[:8]:
        if not (r["citas_buenas"] or r["citas_malas"]):
            continue
        L += ["", f"### {tema}"]
        L += [f"- ✚ «{c}»" for c in r["citas_buenas"]]
        L += [f"- ✖ «{c}»" for c in r["citas_malas"]]

    L += ["", "## Frases candidatas a titular (literal, adaptar al español del país)", ""]
    L += [f"- «{o}» — {t} {e or ''}★" for o, t, e in tit[:25]] or ["- (ninguna)"]
    L += ["", "## Decepciones → FAQ / ¿es para ti? / letra clara", ""]
    L += [f"- «{o}» — {t} {e or ''}★" for o, t, e in dec[:25]] or ["- (ninguna)"]
    L += ["", "## Palabras que más se repiten", "", "**Buenas:** " + ", ".join(f"{k} ({v})" for k, v in ngramas(buenas, 2)),
          "", "**Malas:** " + ", ".join(f"{k} ({v})" for k, v in ngramas(malas, 2)), "",
          "**Frases de 3 palabras (todas):** " + ", ".join(f"{k} ({v})" for k, v in ngramas(filas, 3))]
    L += ["", "## Siguiente paso", "", "Convertir en: 3 titulares · 6 beneficios con prueba · 8 objeciones → FAQ · tabla ¿es para ti? · 5 guiones de video (references/06, 12)."]

    Path(a.salida).write_text("\n".join(L), encoding="utf-8")
    Path(a.salida).with_suffix(".json").write_text(json.dumps({"total": total, "promedio": prom, "distribucion": dist, "temas": tema_res,
        "titulares": tit[:50], "decepciones": dec[:50]}, ensure_ascii=False, indent=2), encoding="utf-8")
    print("\n".join(L[:40]))
    print(f"\n→ {a.salida}")


if __name__ == "__main__":
    main()
