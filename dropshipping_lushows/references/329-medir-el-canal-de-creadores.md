# Medir el canal de creadores (código)

Sin medición, este canal es superstición: "sentí que ese video movió". El script de abajo compara el **CAC real por creador** contra el CAC de tu pauta (USD 10,54) y te dice a quién recontratar, a quién pasar a afiliado y a quién no volver a escribirle.

## Las tres señales que se registran

| Señal | Qué captura | Fiabilidad |
|---|---|---|
| **Código de descuento** (`ANA10`) | Ventas donde el comprador usó el código | Alta pero **subestima**: mucha gente no lo usa |
| **Enlace único** (`?ref=ana`) | Clics y sesiones desde el post | Media: se pierde si el usuario cambia de dispositivo |
| **Encuesta post-compra** ("¿dónde nos conociste?") | Atribución declarada por el cliente | La más honesta para el efecto indirecto. Ver `311` |

## El problema de atribución, dicho claro

El comprador ve al creador en TikTok, **no hace clic**, busca la marca en Google o en Instagram al día siguiente y compra ahí. El código nunca se usa y el enlace nunca se toca. El crédito se lo lleva "búsqueda de marca" o "directo", y tú concluyes que el creador no sirvió. Tres causas: TikTok tiene mucha fricción para salir de la app, nadie compra un producto de MX$1.099 en caliente, y muchos ven en el celular y compran en la computadora.

**La solución práctica no es un modelo de atribución, es preguntarle al cliente.** La encuesta post-compra de `311` (un campo obligatorio en el checkout o un mensaje inmediato tras la compra) recupera la parte que el código no ve. El script trata esas respuestas como una fuente separada y calcula un **CAC ajustado**.

Regla de oro: **si el CAC por código ya le gana a la pauta, no necesitas ajustar nada — recontrata.** El ajuste solo sirve para rescatar a creadores que parecen malos y no lo son.

## El script

Guárdalo como `cac_creadores.py`. Edita el bloque `DATOS` con tu hoja de registro (`325`). Corre con `python cac_creadores.py`.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CAC real por creador vs CAC de pauta. Dinero siempre en Decimal."""

from decimal import Decimal as D, ROUND_HALF_UP

# ---------- PARAMETROS DEL NEGOCIO (editar) ----------
MARGEN_POR_VENTA = D("26.47")   # USD, margen antes de adquisicion
CAC_PAUTA        = D("10.54")   # USD, CAC de Meta como vara de comparacion
MXN_POR_USD      = D("18.30")   # verificar el tipo de cambio del dia

# ---------- DATOS (una fila por creador, de tu hoja de registro) ----------
# costo_mxn: lo que le pagaste (0 en seeding puro -> usa costo_producto_usd)
# v_codigo / v_enlace / v_encuesta: NUNCA cuentes un pedido en dos columnas
DATOS = [
    # nombre, costo_mxn, costo_producto_usd, v_codigo, v_enlace, v_encuesta
    ("@ana",    "500",  "0",     4, 1, 2),
    ("@luis",   "800",  "0",     1, 0, 0),
    ("@sofia",  "0",    "16.50", 3, 2, 1),
    ("@diego",  "3000", "0",     6, 1, 3),
    ("@karla",  "500",  "0",     0, 0, 1),
]

CENT = D("0.01")


def r(x):
    return x.quantize(CENT, rounding=ROUND_HALF_UP)


def analizar(fila):
    nombre, costo_mxn, costo_prod, v_cod, v_link, v_enc = fila
    costo = r(D(costo_mxn) / MXN_POR_USD + D(costo_prod))

    directas = v_cod + v_link          # lo que puedes probar
    totales = directas + v_enc         # lo que realmente paso, segun el cliente

    cac_directo = r(costo / D(directas)) if directas else None
    cac_ajustado = r(costo / D(totales)) if totales else None
    margen_total = r(D(totales) * MARGEN_POR_VENTA - costo)

    # ventas necesarias para empatar el costo
    empate = (costo / MARGEN_POR_VENTA).quantize(D("0.1"), rounding=ROUND_HALF_UP)

    if cac_directo is not None and cac_directo <= CAC_PAUTA:
        veredicto = "RECONTRATAR  (gana a la pauta con datos duros)"
    elif cac_ajustado is not None and cac_ajustado <= CAC_PAUTA:
        veredicto = "RECONTRATAR* (gana solo con la encuesta 311)"
    elif totales > 0 and margen_total > 0:
        veredicto = "AFILIADO     (vende, pero no al precio que pagaste)"
    else:
        veredicto = "NO REPETIR"

    return {
        "nombre": nombre, "costo": costo, "directas": directas,
        "totales": totales, "cac_directo": cac_directo,
        "cac_ajustado": cac_ajustado, "margen_total": margen_total,
        "empate": empate, "veredicto": veredicto,
    }


def main():
    filas = [analizar(f) for f in DATOS]

    print("\nCAC POR CREADOR vs CAC DE PAUTA (USD %s)\n" % CAC_PAUTA)
    enc = "%-9s %8s %6s %6s %9s %9s %9s %6s  %s"
    print(enc % ("creador", "costo", "vtaD", "vtaT", "CACdir", "CACajus",
                 "margenT", "empate", "veredicto"))
    print("-" * 112)
    for f in filas:
        print(enc % (
            f["nombre"], f["costo"], f["directas"], f["totales"],
            f["cac_directo"] if f["cac_directo"] is not None else "s/vta",
            f["cac_ajustado"] if f["cac_ajustado"] is not None else "s/vta",
            f["margen_total"], f["empate"], f["veredicto"]))

    costo_tot = sum((f["costo"] for f in filas), D("0"))
    v_dir = sum(f["directas"] for f in filas)
    v_tot = sum(f["totales"] for f in filas)
    print("\nCANAL COMPLETO")
    print("  invertido:        USD %s" % r(costo_tot))
    print("  ventas probadas:  %s" % v_dir)
    print("  ventas reales:    %s  (incluye encuesta 311)" % v_tot)
    print("  margen del canal: USD %s"
          % r(D(v_tot) * MARGEN_POR_VENTA - costo_tot))
    if v_dir:
        print("  CAC canal (dir):  USD %s" % r(costo_tot / D(v_dir)))
    if v_tot:
        cac_canal = r(costo_tot / D(v_tot))
        print("  CAC canal (ajus): USD %s   vs pauta USD %s" % (cac_canal, CAC_PAUTA))
        print("  veredicto canal:  %s" % (
            "el canal gana a la pauta" if cac_canal <= CAC_PAUTA
            else "la pauta sigue siendo mas barata"))

    rescatadas = v_tot - v_dir
    if v_dir:
        pct = r(D(rescatadas) * D("100") / D(v_dir))
        print("\n  La encuesta 311 rescato %s ventas que el codigo no vio (+%s%%)."
              % (rescatadas, pct))
        print("  Si ese numero es alto, NO estas midiendo bien: refuerza la encuesta.")


if __name__ == "__main__":
    main()
```

## Cómo leer la salida

| Veredicto | Qué haces |
|---|---|
| `RECONTRATAR` | Vuelve a comprarle, sube el presupuesto, pide derechos y **pauta su video** |
| `RECONTRATAR*` | Gana solo con la encuesta. Recontrata **y** arregla tus códigos y enlaces |
| `AFILIADO` | Vendió, pero no justificó el fijo. Pásalo a comisión (`327`) |
| `NO REPETIR` | Sin ventas. Guarda el contenido si tienes derechos y sigue |

## Umbrales de decisión

| Métrica | Umbral | Acción |
|---|---|---|
| CAC del creador | ≤ USD 10,54 | Gana a la pauta: escala ahí |
| CAC del creador | USD 10,54-26,47 | Rentable pero peor que la pauta: afiliado |
| CAC del creador | > USD 26,47 | Pierdes dinero por venta. Corta |
| Ventas de la encuesta / ventas del código | > 40% | **Tu medición está rota**, no el creador |
| 0 ventas con >2.000 vistas | — | Problema de oferta o de página, no del creador |

Esa penúltima fila es la más útil del módulo: **cuando la encuesta ve muchas más ventas que el código, el problema eres tú.** Arregla el código (que aparezca hablado en el video, escrito en pantalla y en la bio), no despidas al creador.

## Higiene de datos antes de correrlo

Resta devoluciones y contracargos de `v_codigo` (una venta devuelta no es una venta). Nunca cuentes un pedido en dos columnas: si tiene código, no lo metas también en enlace. Un código por creador, nunca compartido — un código que se filtra a sitios de cupones deja de medir. Corre el script a 7 y a 30 días del post, porque las ventas siguen llegando semanas después. Y anota el tipo de cambio usado: si cambia, tus comparaciones históricas se deforman.

**Lo que este script NO hace.** No mide efecto de marca a largo plazo, no compara contra el rendimiento del **mismo video pautado** (que suele ser mayor que el orgánico) y no proyecta LTV. Para pautar el contenido del creador, `tiktok_ads_lushows` y `facebook_ads_lushows`. Para verificar cualquier variante del cálculo, `Matematicas_lushows`. Para cómo encaja con las demás fuentes, `240`.

## Relacionados
`322` el canal en México · `323` nano vs micro · `324` tarifas y negociación · `325` encontrar y filtrar · `327` afiliados · `328` seeding · `311` encuesta post-compra · `240` de dónde viene el tráfico · `Matematicas_lushows` cálculos · `tiktok_ads_lushows` pautar el contenido del creador
