# El umbral del envío gratis

**$60.000** (oficial ML Colombia, verificado sep-2026). Es el número que parte tu catálogo en dos
mundos: debajo el envío es barato y opcional, encima es obligatorio y **casi el doble de caro**.
Entender ese salto es la decisión de precio con más impacto del marketplace colombiano.

## La regla oficial

> *"En publicaciones de productos nuevos **desde $60.000** ofrecerás importantes descuentos o
> envíos gratis […] y tú tendrás descuentos en los costos según tu reputación."*
> *"En publicaciones de productos **menores a $60.000** podrás ofrecer envíos gratis de manera
> opcional y **el costo correrá por tu cuenta**."*
> *"Si vendes varios productos que juntos sumen **$60.000**, tu comprador tendrá envío gratis."*
> (oficial ML Colombia, verificado sep-2026)

Nota: la cifra de **$90.000** que circula en algunas fuentes **es incorrecta para Colombia**. El
umbral oficial publicado es $60.000.

## El salto, con números reales

Costo de envío para reputación verde (tabla oficial, ver `78`):

| Peso | $30.000–$59.999 | Más de $60.000 | Salto |
|---|---|---|---|
| Hasta 0,3 kg | $4.100 | $8.000 | **+$3.900** |
| 0,5 a 1 kg | $4.300 | $8.200 | **+$3.900** |
| 1 a 2 kg | $4.500 | $8.500 | **+$4.000** |
| 3 a 4 kg | $4.700 | $10.100 | **+$5.400** |
| 7 a 10 kg | $5.000 | $15.200 | **+$10.200** |
| 10 a 20 kg | $5.100 | $25.200 | **+$20.100** |
| 20 a 30 kg | $5.200 | $41.400 | **+$36.200** |

Léelo: cruzar $60.000 **casi duplica** el envío en productos livianos y lo **multiplica por cinco o
más** en los pesados. En un producto de 20 kg, subir el precio de $59.900 a $60.500 te cuesta
$36.200 de envío adicional por venta.

**El umbral de $60.000 no es una línea: es un escalón. Y el escalón crece con el peso.**

## La zona muerta

Justo encima de $60.000 ganas menos que justo debajo. La zona muerta va de $60.000 hasta
**$60.000 + el salto de envío de tu peso**.

Producto de 1 kg, reputación verde, costo $25.000, cargo por venta **14,5% — ejemplo dentro del
rango oficial 8%-22%, verifica el tuyo** (`76`), sin IVA para simplificar la lectura:

| Precio | Envío que asumes | Cargo 14,5% | Te queda antes del costo |
|---|---|---|---|
| $55.000 | $4.300 | $7.975 | $42.725 |
| $59.900 | $4.300 | $8.686 | $46.914 |
| **$61.000** | **$8.200** | $8.845 | **$43.955** |
| $64.000 | $8.200 | $9.280 | $46.520 |
| $65.000 | $8.200 | $9.425 | $47.375 |
| $75.000 | $8.200 | $10.875 | $55.925 |

A $61.000 ganas **menos** que a $59.900. Sales de la zona muerta alrededor de $64.500. Con un
producto de 10 kg, la zona muerta llega hasta cerca de **$70.500**, y con uno de 20 kg hasta más de
**$96.000**.

> **Publica justo debajo de $60.000, o publica bastante por encima. Nunca apenas encima.**

"Bastante por encima" tiene definición exacta:

```
salida de la zona muerta ≈ $60.000 + (salto de envío ÷ (1 − cargo por venta))
```

Con salto de $3.900 y cargo 14,5%: $60.000 + $4.561 = **$64.561**. Verifica cualquier caso concreto
con `Matematicas_lushows` si vas a mover precios en serio.

## Las tres zonas

| Zona | Rango | Qué haces ahí |
|---|---|---|
| **Debajo** | < $60.000 | Envío barato y opcional. Vale la pena si tu producto es de compra rápida y no dependes del filtro de envío gratis |
| **Muerta** | $60.000 hasta la salida calculada arriba | El peor lugar del catálogo. Se sale subiendo, no bajando |
| **Encima** | > salida | Tienes la etiqueta, entras al filtro, y el precio ya pagó el envío |

La salida de la zona muerta casi nunca es bajar el precio: es **subir el ticket con un kit** (`87`)
hasta aterrizar cómodo en la tercera zona.

## El carrito: el umbral se alcanza entre varios

> *"Si vendes varios productos que juntos sumen **$60.000**, tu comprador tendrá envío gratis."*

Esto es enorme para el producto barato. No tienes que subir el precio de un SKU a $60.000: basta
con que el comprador se lleve tres. De ahí salen dos jugadas:

1. **Kits propios** que suman $60.000 en un solo ítem (`87`).
2. **Full**, porque los productos en Full permiten agrupar artículos de **distintos vendedores**
   en un carrito para alcanzar el mínimo. Tu producto barato puede viajar de polizón en el carrito
   de otro y alcanzar el umbral sin que tú subas nada. Ver bloque `100`-`124`.

## El peso decide si cruzar conviene

| Peso del producto | Salto al cruzar $60.000 | Veredicto |
|---|---|---|
| Menos de 2 kg | ~$3.900-$4.000 | Cruza sin miedo si el precio lo aguanta |
| 3 a 5 kg | ~$5.400 | Cruza, pero aterriza sobre $66.000 |
| 7 a 10 kg | ~$10.200 | Cruza solo si el precio va bien por encima de $71.000 |
| 10 a 20 kg | ~$20.100 | Piénsalo dos veces. Considera quedarte debajo |
| Más de 20 kg | $36.200 y subiendo | Este producto probablemente no es para ML (`84`) |

## Cómo verificarlo con la calculadora

```
# Debajo del umbral, 1 kg, verde
python scripts/margen_ml.py margen --precio 59900 --costo 25000 --comision 14.5 \
    --envio 4300 --iva 19

# Zona muerta
python scripts/margen_ml.py margen --precio 61000 --costo 25000 --comision 14.5 \
    --envio 8200 --iva 19

# Cómodamente encima
python scripts/margen_ml.py margen --precio 79900 --costo 25000 --comision 14.5 \
    --envio 8200 --iva 19
```

Los tres veredictos en pantalla, uno debajo del otro, convencen más que cualquier tabla.

## Lista de chequeo

```
□ Sé el peso (mayor entre real y volumétrico) de cada SKU
□ Busqué el salto de envío de ese peso en la tabla oficial (ver 78)
□ Calculé dónde termina la zona muerta para ese producto
□ Ningún SKU mío está entre $60.000 y la salida de su zona muerta
□ Los que estaban, los subí con kit o los bajé por debajo de $60.000
□ Revisé si mis productos baratos ganan estando en Full por el carrito agrupado
□ Mi reputación está verde: si no, el salto es del doble (ver 78)
```

## El error clásico

Poner el precio en $60.900 "para que salga con envío gratis y se venda más". Ese vendedor acaba de
regalar $3.900 por unidad —o $36.200 si el producto pesa 20 kg— a cambio de una etiqueta, y gana
menos que si hubiera publicado a $59.900. Es el error más común del bloque porque se comete con la
mejor intención.

## Relacionados

`75` estructura de costos · `76` el cargo por venta 8%-22% · `77` el mínimo de $2.900 · `78` el
envío que pagas tú, con tablas · `82` la calculadora de margen · `85` el ticket que aguanta ML ·
`86` por qué los productos baratos pierden · `87` subir el ticket con kits · `88` precio
psicológico · `100` envíos y Full
