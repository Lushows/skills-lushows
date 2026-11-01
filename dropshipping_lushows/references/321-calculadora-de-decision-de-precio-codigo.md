# Calculadora de decisión de precio (código)

## Qué hace

Recibe **costo puesto en bodega, flete al cliente, comisión, CAC y varios precios candidatos**, y
devuelve para cada uno: **margen, techo de CAC, holgura, ROAS de equilibrio, múltiplo, utilidad** y
—lo importante— **la conversión mínima que ese precio necesita para ganarle al precio actual**.

`228` decide si el producto se lanza; esto decide **a cuánto**. Guárdalo como `precio.py` y corre
`python precio.py`.

```python
# precio.py — decisión de precio por candidato (dropshipping, Q4-2026)
from dataclasses import dataclass
from decimal import Decimal as D, ROUND_HALF_UP

def money(x) -> D:
    return D(str(x)).quantize(D("0.01"), rounding=ROUND_HALF_UP)

def ratio(x) -> D:
    return D(str(x)).quantize(D("0.001"), rounding=ROUND_HALF_UP)

def pct(x) -> D:
    return (D(str(x)) * 100).quantize(D("0.01"), rounding=ROUND_HALF_UP)

@dataclass
class Oferta:
    nombre: str
    moneda: str
    tipo_cambio: D        # unidades de moneda local por 1 USD (1 si trabajas en USD)
    costo_bodega: D       # USD: producto + flete intl + arancel + empaque (ver 28)
    flete_envio: D        # USD: envío al cliente (última milla)
    comision_pct: D       # fracción sobre el ticket (pasarela + plataforma)
    cac: D                # USD observado. Si no lo tienes, estímalo con 228
    cvr_actual: D         # conversión del precio ACTUAL, en fracción
    precio_actual: D      # en moneda local
    multiplo_minimo: D    # veto duro del país/escenario (México Q4-2026: 2.70)

def evaluar(o: Oferta, precio_local: D) -> dict:
    ticket = money(D(str(precio_local)) / o.tipo_cambio)
    comision = money(ticket * o.comision_pct)
    margen = money(ticket - o.costo_bodega - o.flete_envio - comision)
    techo_cac = margen                       # todo el margen podría irse en adquisición
    holgura = ratio(techo_cac / o.cac) if o.cac > 0 else D("0")
    roas_eq = ratio(ticket / margen) if margen > 0 else D("0")
    multiplo = ratio(ticket / o.costo_bodega) if o.costo_bodega > 0 else D("0")
    return {"precio_local": D(str(precio_local)), "ticket": ticket, "comision": comision,
            "margen": margen, "techo_cac": techo_cac, "holgura": holgura,
            "roas_eq": roas_eq, "multiplo": multiplo, "utilidad": money(margen - o.cac)}

def veredicto(r: dict, o: Oferta) -> str:
    if r["margen"] <= 0:
        return "MUERTO (margen negativo)"
    if r["multiplo"] < o.multiplo_minimo:
        return f"VETO (multiplo < {o.multiplo_minimo}x)"
    if r["holgura"] < D("2.0"):
        return "RIESGO (holgura < 2,0x)"
    return "VIABLE"

def comparar(o: Oferta, candidatos: list) -> None:
    base = evaluar(o, o.precio_actual)
    print(f"\n{o.nombre} — precio actual {o.precio_actual} {o.moneda} "
          f"(USD {base['ticket']}) | CVR actual {pct(o.cvr_actual)}% | CAC USD {o.cac}\n")
    enc = (f"{'Precio':>9} {'Ticket$':>8} {'Margen':>8} {'TechoCAC':>9} {'Holgura':>8} "
           f"{'ROASeq':>7} {'Mult':>6} {'Util':>7} {'CVRmin':>8} {'CaidaMax':>9}  Veredicto")
    print(enc); print("-" * len(enc))
    for p in candidatos:
        r = evaluar(o, p)
        if r["margen"] > 0:
            cvr_min = o.cvr_actual * base["margen"] / r["margen"]
            caida = D("1") - (base["margen"] / r["margen"])
        else:
            cvr_min, caida = D("0"), D("0")
        marca = " *" if D(str(p)) == o.precio_actual else "  "
        print(f"{str(r['precio_local']):>7}{marca} {r['ticket']:>8} {r['margen']:>8} "
              f"{r['techo_cac']:>9} {str(r['holgura'])+'x':>8} {r['roas_eq']:>7} "
              f"{str(r['multiplo'])+'x':>6} {r['utilidad']:>7} "
              f"{str(pct(cvr_min))+'%':>8} {str(pct(caida))+'%':>9}  {veredicto(r, o)}")
    print("\n* = precio actual. CVRmin = conversion minima para igualar el margen por visitante.")
    print("CaidaMax = conversion que puedes perder y seguir empatado (negativa = ese precio exige")
    print("VENDER MAS para empatar). Verificar significancia en Matematicas_lushows.\n")

if __name__ == "__main__":
    mx = Oferta(
        nombre="Bundle Mexico dic-2026", moneda="MXN", tipo_cambio=D("18.30"),
        costo_bodega=D("16.38"),      # 30% del PVP de 999 — SUPUESTO A VERIFICAR
        flete_envio=D("8.74"),
        comision_pct=D("0.055"),
        cac=D("10.54"),
        cvr_actual=D("0.020"),
        precio_actual=D("999"),
        multiplo_minimo=D("2.70"),    # Mexico Q4-2026, ganador real (ver 216)
    )
    comparar(mx, [D("799"), D("899"), D("999"), D("1099"), D("1199"), D("1299"), D("1599")])
```

## Salida real

```
Bundle Mexico dic-2026 — precio actual 999 MXN (USD 54.59) | CVR actual 2.00% | CAC USD 10.54

   Precio  Ticket$   Margen  TechoCAC  Holgura  ROASeq   Mult    Util   CVRmin  CaidaMax  Veredicto
---------------------------------------------------------------------------------------------------
    799      43.66    16.14     16.14   1.531x   2.705 2.665x    5.60    3.28%   -64.00%  VETO
    899      49.13    21.31     21.31   2.022x   2.305 2.999x   10.77    2.48%   -24.21%  VIABLE
    999 *    54.59    26.47     26.47   2.511x   2.062 3.333x   15.93    2.00%     0.00%  VIABLE
   1099      60.05    31.63     31.63   3.001x   1.899 3.666x   21.09    1.67%    16.31%  VIABLE
   1199      65.52    36.80     36.80   3.491x   1.780 4.000x   26.26    1.44%    28.07%  VIABLE
   1299      70.98    41.96     41.96   3.981x   1.692 4.333x   31.42    1.26%    36.92%  VIABLE
   1599      87.38    57.45     57.45   5.451x   1.521 5.335x   46.91    0.92%    53.93%  VIABLE
```

## Cómo se lee

| Columna | Significado | Decisión |
|---|---|---|
| Margen | ticket − bodega − flete − comisión | antes de publicidad |
| TechoCAC | máximo que puedes pagar por cliente | ver `11` |
| Holgura | techo ÷ CAC | < 2,0x = riesgo, < 1,5x = no |
| ROASeq | ROAS de equilibrio | ver `226` |
| Mult | ticket ÷ costo bodega | < 2,70x en México = **veto** |
| **CVRmin** | conversión que ese precio necesita para empatar | la columna que decide |
| **CaidaMax** | conversión que puedes darte el lujo de perder | negativa = tienes que vender más |

Las dos últimas son el aporte real. Ejemplo: a **1.099 puedes perder 16,31% de la conversión y
seguir igual**; a **899 necesitas vender 24,21% más solo para empatar**. Por eso subir casi siempre
es la apuesta con mejor relación riesgo-beneficio en dropshipping (`319`).

Y a 799 el modelo dispara **VETO**: 2,665x está por debajo del mínimo mexicano de 2,70x. No hay nada
que probar ahí. Ver `216`.

## Cómo usarlo con `318`

```
1. Van Westendorp (317) → rango
2. Corre esta calculadora sobre el rango → descarta los VETO y los RIESGO
3. De los VIABLE, quédate con 2 y mira su CVRmin
4. Si la diferencia de CVRmin entre los dos es < 15% relativo,
   NO tienes tráfico para distinguirlos: quédate con el más alto y sigue
5. Si es > 25%, vale un test secuencial de 7+7 días (318)
```

El paso 4 es el que ahorra dinero: **si el efecto que buscas es más chico que tu ruido, la prueba no
existe**, y elegir el precio alto es la opción con mejor valor esperado.

## Advertencias del modelo

| Advertencia | Detalle |
|---|---|
| El costo **no escala** con el precio | `costo_bodega` es fijo en USD. El "30% del PVP" solo sirvió para derivar 16,38 a partir de 999. Es un **supuesto a verificar** con tu proveedor real |
| El bundle cuesta más | si el precio alto trae más unidades, sube `costo_bodega` o el múltiplo es mentira. La economía verificada del bundle a 1.099 da techo 30,73 (no 31,63) justo por eso |
| El CAC no es constante | al subir el precio la conversión baja y el CAC sube. Este modelo asume CAC fijo: es optimista. Reevalúa con el CAC observado tras cada bloque |
| Faltan devoluciones y contracargos | en prepago pesan poco, en COD lo son todo. Descuéntalos del margen |
| El tipo de cambio y el MSI | 18,30 MXN/USD es referencia, verificar; la comisión de meses sin intereses va sumada a `comision_pct` para el Buen Fin (`238`) |
| No calcula significancia | esa columna no existe a propósito: rutea a `Matematicas_lushows`, que también verifica cualquier número de esta tabla. IVA y facturación, `contador_lushows` |

## Relacionados
`11` · `28` · `216` · `217` · `218` · `220` · `226` · `228` · `231` · `238` · `316` · `317` · `318` · `319` · `320`
