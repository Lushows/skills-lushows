# LTV real por cohorte (código)

> Todo este bloque se resume en tres preguntas: **cuánto vale un cliente de verdad, cuánto puedo
> pagar por conseguirlo y en cuántos meses recupero esa plata.** Este script las responde con
> `Decimal` (nunca `float` para dinero). Antes de mover presupuesto con el resultado, rutea a
> `Matematicas_lushows`.

| Función | Devuelve |
|---|---|
| `supervivientes` | serie de retención mes a mes a partir de un churn |
| `ltv_compra_unica` | margen acumulado y múltiplo por número de compras (`300`) |
| `ltv_suscripcion` | margen acumulado, LTV neto de CAC, vida media y retención final |
| `techo_cac` | cuánto puedes pagar por cliente según la retención observada (`11`) |
| `payback_meses` | mes en que el margen acumulado cubre el CAC |
| `impacto_dunning` | suscriptores y dinero que recupera el dunning (`304`) |

## El script

```python
from decimal import Decimal, ROUND_HALF_UP, getcontext

getcontext().prec = 28
D = Decimal
CENT = D("0.01")

def money(x):
    """Redondeo comercial a centavo."""
    return D(x).quantize(CENT, rounding=ROUND_HALF_UP)

def supervivientes(churn_mensual, meses):
    """serie[0]=1 (todos); serie[k]=fracción viva en el mes k."""
    vivos, serie = D(1), [D(1)]
    for _ in range(meses):
        vivos = vivos * (D(1) - churn_mensual)
        serie.append(vivos)
    return serie

def vida_media(churn_mensual):
    """Meses esperados de vida = 1 / churn."""
    if churn_mensual <= 0:
        raise ValueError("churn debe ser > 0")
    return D(1) / churn_mensual

def ltv_compra_unica(margen_unitario, cac, compras):
    """Sin suscripción: el CAC se paga una vez, el margen vuelve en cada compra."""
    bruto = margen_unitario * D(compras)
    neto, base = bruto - cac, margen_unitario - cac
    return {"compras": compras, "margen_bruto": money(bruto), "ltv_neto": money(neto),
            "multiplo_vs_1": (neto / base).quantize(CENT) if base > 0 else None}

def ltv_suscripcion(margen_mensual, churn_mensual, meses, cac):
    """Cobros en los meses 0..meses-1, ponderados por la retención de cada mes."""
    serie = supervivientes(churn_mensual, meses)
    cobros = sum(serie[:meses], D(0))
    bruto = margen_mensual * cobros
    return {"meses": meses, "cobros_equivalentes": cobros.quantize(CENT),
            "margen_bruto": money(bruto), "ltv_neto": money(bruto - cac),
            "vida_media_meses": vida_media(churn_mensual).quantize(D("0.1")),
            "retencion_final_pct": (serie[meses] * D(100)).quantize(D("0.1"))}

def techo_cac(margen_unitario, compras_promedio, margen_objetivo_pct=D(0)):
    """Máximo pagable por cliente. margen_objetivo_pct reserva utilidad (ej. D('0.20'))."""
    return money(margen_unitario * compras_promedio * (D(1) - margen_objetivo_pct))

def payback_meses(cac, margen_mensual, churn_mensual, tope=36):
    """Primer mes en que el margen acumulado cubre el CAC; None si no ocurre."""
    serie, acum = supervivientes(churn_mensual, tope), D(0)
    for k in range(tope):
        acum += margen_mensual * serie[k]
        if acum >= cac:
            return k + 1
    return None

def impacto_dunning(n_subs, churn_total, churn_involuntario, recuperacion, meses, margen):
    """Cuánto vale recuperar una fracción del churn por fallo de pago."""
    mejorado = churn_total - (churn_involuntario * recuperacion)
    base = D(n_subs) * supervivientes(churn_total, meses)[meses]
    mejor = D(n_subs) * supervivientes(mejorado, meses)[meses]
    delta = mejor - base
    return {"churn_original_pct": (churn_total * D(100)).quantize(CENT),
            "churn_con_dunning_pct": (mejorado * D(100)).quantize(D("0.001")),
            "vivos_sin_dunning": base.quantize(D("0.1")),
            "vivos_con_dunning": mejor.quantize(D("0.1")),
            "suscriptores_extra": delta.quantize(D("0.1")),
            "margen_extra_mensual": money(delta * margen)}

if __name__ == "__main__":
    MARGEN, CAC = D("26.47"), D("10.54")  # proyecto MX: margen sin adquisición y CAC Meta medido
    print("== Margen acumulado por número de compras ==")
    for n in (1, 2, 3, 6, 12):
        r = ltv_compra_unica(MARGEN, CAC, n)
        print(f"{n:>2} compras | neto {r['ltv_neto']:>7} USD | {r['multiplo_vs_1']}x")
    print("\n== Techo de CAC según recompra ==")
    for etiqueta, compras in (("sin recompra", D("1.0")), ("20% vuelve", D("1.2")),
                              ("40% a 3 compras", D("1.8"))):
        print(f"{etiqueta:<18} -> {techo_cac(MARGEN, compras)} USD")
    print("\n== Dunning: 100 suscriptores, 12 meses (red Recurly jul-2026) ==")
    for k, v in impacto_dunning(100, D("0.0360"), D("0.0125"), D("0.5"), 12, MARGEN).items():
        print(f"{k:<24} {v}")
    print("\n== Suscripción a 12 meses, churn 7% ==")
    for k, v in ltv_suscripcion(MARGEN, D("0.07"), 12, CAC).items():
        print(f"{k:<22} {v}")
    print("payback (meses):", payback_meses(CAC, MARGEN, D("0.07")))
```

## Salida de referencia (ejecutada, no estimada)

| Compras | LTV neto USD | Múltiplo | | Techo de CAC | USD |
|---|---|---|---|---|---|
| 1 | 15,93 | 1,00x | | Sin recompra | 26,47 |
| 2 | 42,40 | 2,66x | | 20% vuelve una vez | 31,76 |
| 3 | 68,87 | 4,32x | | **40% a 3 compras** | **47,65** |
| 6 | 148,28 | 9,31x | | | |
| 12 | 307,10 | 19,28x | | | |

| Dunning: 100 suscriptores a 12 meses | |
|---|---|
| Vivos sin dunning (churn 3,60%) | **64,4** |
| Vivos recuperando la mitad del involuntario (churn 2,975%) | **69,6** |
| Suscriptores extra | **+5,2** |
| Margen extra al mes | **USD 137,47** |

Las tablas de `300` y `304` muestran 47,64 y ~137 porque redondean antes de multiplicar; el script
multiplica el delta sin redondear. Es diferencia de centavos: **nunca dejes una decisión colgando de
un centavo.**

## Cómo usarlo con TUS datos

| Entrada | De dónde sale |
|---|---|
| `MARGEN` | ticket − producto − envío − pasarela (`223`) |
| `CAC` | gasto de pauta ÷ clientes nuevos, **por canal** (`224`) |
| `compras_promedio` | pedidos ÷ clientes únicos, **por cohorte** (`302`) |
| `churn_mensual` | cancelaciones ÷ suscriptores activos al inicio del mes |
| `churn_involuntario` | fallos de cobro no recuperados ÷ activos (`304`) |
| `recuperacion` | tasa real de tu dunning; 0,30-0,60 es el rango observado (`304`) |

## Advertencias

| Trampa | Por qué importa |
|---|---|
| `compras_promedio` de la tienda entera | mezcla cohortes y siempre engaña (`302`) |
| Proyectar 12 meses con 2 meses de datos | la curva se aplana, no sigue recta (`301`) |
| Usar el techo de CAC antes de medir la retención | es exactamente el error que advierte `230` |
| Meter `float` en dinero | por eso todo el script es `Decimal` |
| Olvidar devoluciones y contracargos | réstalos del margen **antes** de entrar al script |
| Leer `payback = 1` como que todo va bien | con margen 26,47 y CAC 10,54 el payback siempre es 1; el riesgo no está ahí, está en si la segunda compra existe (`305`) |

## Relacionados
`11` · `223` · `224` · `230` · `300` · `301` · `302` · `303` · `304` · `305` · `308`
