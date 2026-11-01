# Por qué los productos baratos pierden

No es una impresión ni mala suerte: es aritmética. Sobre un producto barato, el envío pesa
proporcionalmente muchísimo más, y Mercado Libre Colombia lo admite por escrito al fijar un tope de
"máximo la mitad del precio del producto". Este módulo hace las cuentas con el script y los números
oficiales.

## El mecanismo, en una frase

El cargo por venta es **proporcional** (8%-22%, siempre el mismo porcentaje), pero el envío es
**casi plano**: cuesta más o menos lo mismo mandar algo de $8.000 que algo de $50.000. Un costo
plano sobre un precio pequeño es una tajada enorme.

Envío de 1 kg, reputación verde, tabla oficial (verificado sep-2026): **$2.700** si el producto
vale menos de $15.000, **$4.300** si vale entre $30.000 y $59.999. El precio se multiplicó por
cinco; el envío subió 59%.

| Precio | Envío 1 kg (oficial) | Envío como % del precio |
|---|---|---|
| $5.000 | $2.500 (tope del 50%) | **50,0%** |
| $8.000 | $2.700 | **33,8%** |
| $12.000 | $2.700 | **22,5%** |
| $20.000 | $2.800 | 14,0% |
| $35.000 | $4.300 | 12,3% |
| $59.900 | $4.300 | 7,2% |
| $90.000 | $8.200 | 9,1% |
| $200.000 | $8.200 | 4,1% |

**El envío no es caro: es plano. Y un costo plano es un impuesto a los productos baratos.**

## El tope del 50%, leído al derecho

> *"Los productos de **menos de $15.000** pagan como máximo **la mitad del precio del producto**"*
> (oficial ML Colombia, verificado sep-2026).

Mercado Libre puso ese techo porque sin él, un producto de $4.000 pagaría $2.700 de envío — el 68%.
Pero fíjate en lo que el techo admite: la plataforma considera **normal** que un producto barato
pague **hasta la mitad de su precio en envío**. Eso no es una protección, es una advertencia.

## Las cuentas con el script

Mismo margen bruto (markup 100%: compras a X, vendes a 2X), reputación verde, IVA 19%, cargo
**15% — ejemplo dentro del rango oficial 8%-22%, verifica el tuyo** (`76`), producto de 1 kg.

```
# Barato: costo $5.000, precio $10.000
python scripts/margen_ml.py margen --precio 10000 --costo 5000 --comision 15 \
    --envio 2700 --iva 19

# Medio: costo $25.000, precio $50.000
python scripts/margen_ml.py margen --precio 50000 --costo 25000 --comision 15 \
    --envio 4300 --iva 19

# Alto: costo $100.000, precio $200.000
python scripts/margen_ml.py margen --precio 200000 --costo 100000 --comision 15 \
    --envio 8200 --iva 19
```

Resultado, con el **mismo markup del 100%** en los tres casos:

| Precio | Base sin IVA | Cargo 15% | Envío | Costo | Utilidad | Margen |
|---|---|---|---|---|---|---|
| $10.000 | $8.403 | $1.500 | $2.700 | $5.000 | **–$797** | **negativo** |
| $50.000 | $42.017 | $7.500 | $4.300 | $25.000 | $5.217 | 12,4% |
| $200.000 | $168.067 | $30.000 | $8.200 | $100.000 | $29.867 | 17,8% |

Léelo despacio: **el mismo negocio, con el mismo markup, pierde plata a $10.000 y deja 17,8% a
$200.000**. Duplicar el precio de compra no te salva; lo que te salva es el tamaño del ticket.

Verifica estos números tú mismo corriendo los comandos. No los memorices: el cargo real de tu
categoría cambia el resultado.

## El markup que necesitas según el ticket

Cuánto tienes que montarle al costo para llegar a un margen del 20%, con cargo 15%, 1 kg, verde,
IVA 19%:

| Precio de venta | Envío | Markup necesario aprox. |
|---|---|---|
| $10.000 | $2.700 | **imposible** (ni al 300%) |
| $15.000 | $2.800 | ~290% |
| $30.000 | $4.300 | ~145% |
| $59.900 | $4.300 | ~105% |
| $90.000 | $8.200 | ~105% |
| $200.000 | $8.200 | ~90% |
| $400.000 | $8.200 | ~85% |

Calcúlalo tú con `margen_ml.py minimo --margen-objetivo 20` y despeja hacia atrás. Si vas a tomar
una decisión grande con esta tabla, pásala por `Matematicas_lushows`.

La lectura: **por debajo de $15.000 necesitas markups que ningún proveedor real te permite**. Por
eso los productos baratos pierden.

## Las tres razones, ordenadas por peso

| # | Razón | Tamaño del daño |
|---|---|---|
| 1 | **El envío es plano** | El grande: hasta 50% del precio |
| 2 | **El IVA no escala en tu favor** | Convierte tu cargo nominal en uno efectivo 19% mayor (`81`) |
| 3 | **El piso de $2.900** | Corta por abajo; no hay negocio de $1.500 en ML |

Nota lo que **no** está en la lista: el cargo por venta. El porcentaje es el mismo en un producto
de $8.000 que en uno de $800.000; no es él quien castiga al barato. Culpar a la comisión es
diagnosticar mal y arreglar lo que no está roto.

## Las salidas

| Salida | Qué hace | Módulo |
|---|---|---|
| **Kit** | Sube el ticket sumando unidades o complementos | `87` |
| **Pack por cantidad** | "x12" en consumibles | `87` |
| **Carrito con Full** | Tu producto barato suma $60.000 con otros vendedores | `100` |
| **Subir el valor percibido** | Marca, empaque, garantía | `directorcreativo_lushows` |
| **Vender fuera de ML** | El barato de compra recurrente a veces vive mejor en otro canal | `dropshipping_lushows` |
| **Matarlo** | Cuando nada funciona | `98` |

La primera es la buena y la ayuda oficial de ML la recomienda expresamente: *"Puedes vender
productos de menor valor ofreciendo packs o combos."*

## Lista de chequeo

```
□ Calculé el envío como % del precio para cada SKU barato mío
□ Ningún SKU tiene el envío por encima del 20% del precio
□ Corrí margen_ml.py con el envío de la columna correcta, no con un promedio
□ Verifiqué el markup necesario para 20% de margen a ese ticket
□ Si el markup necesario supera el 150%, el SKU va a kit o se muere
□ Revisé si estando en Full mis baratos entran a carritos ajenos
```

## El error clásico

Explicar las pérdidas con "es que la comisión de Mercado Libre es muy alta". No es la comisión: es
el envío plano sobre un ticket pequeño. El vendedor que cree que el problema es el porcentaje
negocia categorías o se va de la plataforma, cuando la solución estaba en subir el ticket un
escalón.

## Relacionados

`75` estructura de costos · `76` el cargo por venta 8%-22% · `77` el mínimo de $2.900 · `78` el
envío que pagas tú · `79` el umbral de los $60.000 · `82` la calculadora de margen · `84` el
producto que no sirve para ML · `85` el ticket que aguanta ML · `87` subir el ticket con kits ·
`98` qué hacer con el SKU que no deja · `Matematicas_lushows` para verificar
