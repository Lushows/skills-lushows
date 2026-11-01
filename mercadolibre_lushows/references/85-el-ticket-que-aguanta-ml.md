# El ticket que aguanta ML

Hay un piso de ticket por debajo del cual el marketplace no deja nada, y no es una opinión: sale de
los tres números oficiales del bloque. El precio mínimo de publicación, el escalón de envío de los
$60.000 y el cargo de 8%-22% dibujan juntos una curva que dice exactamente en qué rango de precio
vale la pena estar.

## Los tres números que dibujan el piso

| Número | Valor | Fuente |
|---|---|---|
| Precio mínimo de publicación | **$2.900** | oficial ML Colombia, verificado sep-2026 |
| Tope de envío en productos baratos | **50% del precio** si vale menos de $15.000 | oficial, verificado sep-2026 |
| Umbral de envío gratis | **$60.000** | oficial, verificado sep-2026 |
| Cargo por venta | **8% a 22%** | oficial, verificado sep-2026 |

## La curva del peso de los costos

Producto de 1 kg, reputación verde, cargo de ejemplo 15% (**dentro del rango oficial 8%-22%,
verifica el tuyo** — `76`), envío de tabla oficial, sin IVA para leer la mecánica limpia:

| Precio | Envío (tabla oficial) | Cargo 15% | Costos ML totales | % del precio |
|---|---|---|---|---|
| $5.000 | $2.500 (tope: máx. $2.500) | $750 | $3.250 | **65,0%** |
| $10.000 | $2.700 | $1.500 | $4.200 | **42,0%** |
| $15.000 | $2.800 | $2.250 | $5.050 | 33,7% |
| $25.000 | $2.800 | $3.750 | $6.550 | 26,2% |
| $40.000 | $4.300 | $6.000 | $10.300 | 25,8% |
| $59.900 | $4.300 | $8.985 | $13.285 | 22,2% |
| $61.000 | $8.200 | $9.150 | $17.350 | **28,4%** |
| $90.000 | $8.200 | $13.500 | $21.700 | 24,1% |
| $150.000 | $8.200 | $22.500 | $30.700 | 20,5% |
| $300.000 | $8.200 | $45.000 | $53.200 | 17,7% |
| $600.000 | $8.200 | $90.000 | $98.200 | 16,4% |

Lee la última columna. Dice tres cosas:

1. **Bajo $15.000 los costos se llevan del 34% al 65% del precio.** Ahí no hay negocio salvo con
   markups extremos.
2. **Hay un mínimo local en $59.900** (22,2%): el mejor punto del catálogo barato, justo antes del
   escalón.
3. **Cruzar $60.000 devuelve el peso a 28,4%** y la curva tarda hasta ~$150.000 en volver a bajar
   de 21%. Esa es la zona muerta del `79`, vista desde otro ángulo.

**El ticket ideal en Mercado Libre Colombia no es "lo más alto posible": es $59.900, o de $90.000
para arriba. El medio es tierra de nadie.**

## Los cuatro rangos de ticket

| Rango | Peso de los costos ML | Veredicto |
|---|---|---|
| **$2.900 – $14.999** | 34%-65% | Solo como kit (`87`) o como complemento de carrito |
| **$15.000 – $59.999** | 22%-34% | Viable si el markup es alto. El punto óptimo es rozar $59.900 |
| **$60.000 – $89.999** | 24%-29% | **La zona muerta.** Sal de ella subiendo (`79`) |
| **$90.000 en adelante** | Bajo 25% y cayendo | El terreno bueno, si el peso acompaña |

Ojo con la última fila: **si el producto pesa**, la curva no baja igual. Con 15 kg, el envío sobre
$60.000 es $25.200 y el peso de los costos a $150.000 es 36%, no 20%. El ticket alto solo salva a
los productos livianos (`84`).

## El ticket y el cargo fijo que no existe

Conviene decirlo aquí porque es donde más se confunde: en Colombia **no hay cargo fijo por venta de
bajo valor**. El producto barato no paga un peaje en pesos; paga un **envío desproporcionado**
(hasta el 50% de su precio) y el piso de publicación de $2.900. El efecto en la cuenta es parecido,
la mecánica es distinta, y confundirlas te hace corregir el problema equivocado. Ver `77`.

## Cómo encontrar tu propio piso

```
□ Pesa el producto empacado y toma el mayor entre real y volumétrico
□ Arma la tabla de arriba con TU peso y TU cargo real (del simulador logueado)
□ Marca la columna "% del precio" en cada rango
□ Tu piso de ticket es donde esa columna baja de 25%
□ Verifica que a ese precio tu margen siga por encima del ACOS al que quieres pautar (150)
□ Si el piso te queda por encima de lo que el mercado paga, arma un kit (87)
```

Automatízalo con el script barriendo precios:

```
for p in 15000 25000 40000 59900 61000 90000 150000; do
  echo "--- $p ---"
  python scripts/margen_ml.py margen --precio $p --costo 20000 --comision 15 \
      --envio 8200 --iva 19 | grep -E "GANAS|PIERDES|Margen sobre"
done
```

Ajusta `--envio` según la columna que corresponda a cada precio: por debajo de $60.000 usa el valor
de la columna correcta de la tabla oficial (`78`). Ese detalle cambia el resultado y es el error
más común al hacer este barrido.

## Qué hacer si tu producto vive debajo del piso

| Salida | Cómo se ve | Módulo |
|---|---|---|
| Kit o combo | 3 unidades en un solo ítem que pasa de $60.000 | `87` |
| Pack de presentación | Producto + accesorio + estuche | `87` |
| Vender por cantidad | "Pack x12" en consumibles | `87` |
| Aprovechar el carrito | Estar en Full para sumar $60.000 con otros vendedores | `100` |
| Subir el valor percibido | Marca, empaque, garantía extendida | `directorcreativo_lushows` |
| Matarlo | Cuando nada de lo anterior funciona | `98` |

La propia ayuda oficial de Mercado Libre lo sugiere: *"Puedes vender productos de menor valor
ofreciendo packs o combos"* (oficial ML Colombia, verificado sep-2026). Cuando la plataforma te da
la salida por escrito, tómala.

## El error clásico

Traer un catálogo de productos de $8.000 a $20.000 porque "rotan rápido y son baratos de comprar",
y descubrir que entre envío y cargo se va la mitad del precio. Rotan, sí — rotan hacia afuera de tu
bolsillo. El segundo error: subir el ticket poniendo el precio en $61.000 sin entender el escalón
del envío, y empeorar el margen creyendo que lo mejoraste (`79`).

## Relacionados

`75` estructura de costos · `76` el cargo por venta 8%-22% · `77` el mínimo de $2.900 · `78` el
envío que pagas tú · `79` el umbral de los $60.000 · `82` la calculadora de margen · `84` el
producto que no sirve para ML · `86` por qué los productos baratos pierden · `87` subir el ticket
con kits · `88` precio psicológico · `98` qué hacer con el SKU que no deja · `150` ACOS sano
