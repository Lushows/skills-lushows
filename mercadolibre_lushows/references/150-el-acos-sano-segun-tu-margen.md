# El ACOS sano según tu margen

No existe un ACOS bueno universal. El único número contra el que se compara el ACOS es **tu margen
neto**, y ese número es distinto para cada SKU tuyo. Este módulo convierte esa regla en una tabla
de decisión con cifras oficiales de Colombia.

## La regla, en una línea

**El ACOS objetivo debe ser MENOR que tu margen neto. Si es igual, trabajas gratis. Si es mayor,
pagas por vender.**

No es una recomendación de estilo, es aritmética: el ACOS es un costo más que sale de la misma
utilidad de la que ya salieron la comisión, el IVA y el envío.

## Por qué el margen es más chico de lo que crees

Dos cifras oficiales de Mercado Libre Colombia (verificado sep-2026) que la mayoría no mete en la
cuenta:

| Costo | Cifra oficial |
|---|---|
| **Cargo por venta** | **8% a 22%** del precio, según categoría y cuotas. Hasta 3 cuotas sin interés: 8%-19%. Con cuotas extra: 11%-22% |
| **Envío** (producto nuevo desde $60.000, 1 kg, reputación verde) | **$8.200** por unidad, ya con el 50% de descuento por reputación |

Ofrecer cuotas extra cuesta exactamente **3 puntos porcentuales** más de comisión. Esos 3 puntos
salen del mismo bolsillo del que saldría el ACOS.

## El cálculo correcto, paso a paso

Usa la fórmula de `75` y ejecútala, no la estimes:

```
python scripts/margen_ml.py margen --precio 80000 --costo 30000 --comision 14 --iva 19
```

Ejemplo trabajado, producto de **$80.000** (comisión 14%, dentro del rango oficial):

| Concepto | Valor |
|---|---|
| Precio publicado (con IVA) | $80.000 |
| − IVA 19% (19/119 del precio) | −$12.773 |
| − Cargo por venta 14% (sobre el precio con IVA) | −$11.200 |
| − Envío 1 kg, producto > $60.000, verde | −$8.200 |
| − Empaque | −$1.500 |
| − Costo del producto | −$30.000 |
| **= Utilidad antes de publicidad** | **$16.327** |
| **Margen neto sobre el precio** | **20,4%** |

Ese 20,4% es tu **techo absoluto de ACOS**. A 20,4% de ACOS ganas exactamente cero.

## La tabla de decisión: margen contra estrategia

Cruza tu margen neto (el de `82`, no el que crees tener) con las tres estrategias oficiales
(`148`):

| Margen neto | Rentabilidad 5-15% | Crecimiento 15-30% | Visibilidad >30% | Veredicto |
|---|---|---|---|---|
| **Menos de 10%** | ✗ ni el piso cabe | ✗ | ✗ | **No pautes.** Arregla precio o costo primero |
| **10% - 15%** | ⚠ solo el piso (5-8%) | ✗ | ✗ | Al límite. Probablemente no valga la pena |
| **15% - 20%** | ✓ | ✗ | ✗ | Rentabilidad y nada más |
| **20% - 30%** | ✓ cómodo | ⚠ solo el piso | ✗ | Rentabilidad; Crecimiento con pérdida controlada |
| **30% - 40%** | ✓ | ✓ | ⚠ con fecha de apagado | Puedes crecer de verdad |
| **Más de 40%** | ✓ | ✓ | ✓ táctico | El único caso donde Visibilidad no es locura |

**Con margen de 15% probablemente no debes pautar.** El piso de la estrategia más conservadora ya
se lleva un tercio de lo que ganas, y la primera devolución o el primer quiebre de stock te pone
en negativo.

## El ACOS objetivo que deberías fijarte

No apuntes a tu techo. Apunta a la mitad o dos tercios del techo, porque el ACOS del reporte no
incluye devoluciones, reclamos ni stock que se quedó sin vender:

| Margen neto (techo de ACOS) | ACOS objetivo sensato |
|---|---|
| 20% | 10% - 13% |
| 25% | 12% - 16% |
| 30% | 15% - 20% |
| 40% | 20% - 26% |
| 50% | 25% - 33% |

La regla rápida: **apunta a dos tercios de tu margen neto.** Ese tercio de colchón es lo que
absorbe las sorpresas.

## El mismo producto, tres comisiones distintas

El rango oficial 8%-22% no es un detalle: son 14 puntos de diferencia sobre el mismo precio. Sobre
el producto de $80.000 del ejemplo:

| Comisión | Utilidad antes de pauta | Margen neto | ACOS objetivo sensato |
|---|---|---|---|
| 8% (categoría barata, hasta 3 cuotas) | $21.127 | 26,4% | 13% - 17% |
| 14% (categoría media) | $16.327 | 20,4% | 10% - 13% |
| 22% (categoría cara + cuotas extra) | $9.927 | 12,4% | **no pautes** |

El mismo producto, el mismo precio: en una categoría se puede pautar y en otra no. Por eso no
existe un ACOS bueno universal, y por eso el ACOS se fija **por SKU**, no por cuenta.

> ⚠️ **Sin verificar para Colombia (sep-2026).** La **comisión exacta de tu categoría** no está
> publicada: solo el rango 8%-22%. Léela logueado en el simulador de costos del panel — la API
> `listing_prices` ya **no es pública** y responde 403. Ver `76`.

## El error clásico

Buscar en Google "cuál es un buen ACOS" y adoptar la primera cifra que aparezca. Esa cifra sale de
Amazon Estados Unidos o de un caso argentino, con comisiones y márgenes que no son los tuyos. Un
ACOS de 25% es excelente para quien tiene 50% de margen y es ruina para quien tiene 18%.
**El benchmark no está en internet: está en tu propia calculadora.**

## Checklist antes de fijar el ACOS objetivo

```
□ Ejecuté `scripts/margen_ml.py` para ESTE SKU, no para "mis productos en general"
□ Metí la comisión real leída en el panel logueado, no un promedio (`76`)
□ Metí el envío real de la tabla oficial según peso y rango de precio (`78`)
□ Verifiqué si ofrezco cuotas extra: son 3 puntos más de comisión
□ Mi ACOS objetivo es ~2/3 del margen neto, no el margen completo
□ Elegí la estrategia que contiene ese ACOS objetivo (`148`)
□ Si el margen neto es menor al 15%, decidí NO pautar este SKU (`164`)
```

## Relacionados

`145` qué es Mercado Ads · `146` Product Ads · `147` la subasta y el CPC ·
`148` las tres estrategias y su ACOS · `149` ACOS y TACOS ·
`154` el error de pautar sin margen · `156` optimizar semana a semana ·
`164` cuándo no es la respuesta · `75` estructura de costos · `76` las comisiones ·
`78` el envío que pagas tú · `80` cuotas sin interés · `81` IVA y el precio que publicas ·
`82` la calculadora de margen · `83` precio mínimo viable · `86` por qué los productos baratos
pierden · `97` margen por SKU
