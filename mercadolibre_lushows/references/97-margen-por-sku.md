# Margen por SKU

El margen promedio del catálogo es el número más peligroso de tu negocio: oculta que cinco SKUs
financian a quince. En Mercado Libre Colombia la dispersión es mayor que en cualquier otro canal,
porque el envío no escala con el precio y el cargo varía 14 puntos entre categorías. El margen se
calcula uno por uno o no se calcula.

## Por qué el promedio miente

Tres razones, todas específicas de este marketplace:

| Razón | Efecto |
|---|---|
| **El cargo por venta va de 8% a 22%** según categoría (oficial) | Dos SKUs con el mismo precio pueden tener 14 puntos de diferencia |
| **El envío no escala con el precio** | Un SKU de $18.000 paga proporcionalmente el triple que uno de $180.000 (`86`) |
| **El umbral de $60.000 parte el catálogo** | Dos SKUs de precio casi igual pueden tener envíos que difieren en el doble (`79`) |

Un catálogo con margen promedio del 18% puede estar compuesto por SKUs de 35% y SKUs de –4%. Vender
más del promedio no significa nada; vender más de los de –4% te quiebra.

**El promedio no es un margen: es la mezcla de tus aciertos con tus errores, presentada como si
fuera una sola cosa.**

## La tabla modelo

Una fila por SKU, actualizada al menos mensualmente (`99`):

| Campo | De dónde sale |
|---|---|
| SKU / `item_id` | Tu catálogo |
| Nombre corto | Tuyo |
| Categoría | La hoja final, no la padre |
| **Cargo por venta %** | Simulador logueado, con fecha (`76`) |
| Precio publicado | Tu publicación |
| **Peso empacado (mayor entre real y volumétrico)** | Báscula y cinta métrica |
| **Columna de precio del envío** | $0-14.999 / $15.000-29.999 / $30.000-59.999 / >$60.000 |
| **Envío (tabla oficial)** | Cruce peso × columna × tu color de reputación (`78`) |
| Costo del producto | Tu proveedor |
| Otros (empaque, alistamiento) | Tu operación |
| IVA % | Según el producto |
| **Tasa de devolución** | Devoluciones ÷ ventas, últimos 90 días (`95`) |
| **Utilidad por unidad** | `margen_ml.py` |
| **Margen %** | `margen_ml.py` |
| Unidades/mes | Tus reportes |
| **Utilidad total/mes** | Utilidad × unidades |
| Veredicto | Del script |

Las columnas en negrita son las que el 80% de los vendedores no tiene, y son exactamente las que
deciden.

## Ejemplo de la tabla, con datos oficiales de envío

Reputación verde, cargo **15% en todos — ejemplo dentro del rango oficial 8%-22%, verifica el
tuyo** (`76`), IVA 19%.

| SKU | Precio | Peso | Envío oficial | Costo | Utilidad | Margen | U/mes | Utilidad mes |
|---|---|---|---|---|---|---|---|---|
| A | $189.000 | 0,8 kg | $8.200 | $88.000 | $27.151 | 17,1% | 40 | **$1.086.040** |
| B | $74.900 | 1,5 kg | $8.500 | $34.000 | $13.720 | 21,8% | 65 | **$891.800** |
| C | $62.000 | 2,5 kg | $8.600 | $32.000 | $2.497 | 4,8% | 120 | $299.640 |
| D | $44.900 | 1 kg | $4.300 | $22.000 | $4.966 | 13,2% | 90 | $446.940 |
| E | $18.900 | 0,4 kg | $2.700 | $11.000 | –$1.320 | **–8,3%** | 210 | **–$277.200** |

Números ilustrativos: corre los tuyos con el script.

Lo que dice la tabla y no diría el promedio:

- **E es el más vendido y el que más plata pierde.** 210 unidades al mes destruyendo $277.200.
- **C está en la zona muerta**: a $62.000 paga el envío caro de la columna >$60.000 con un precio
  que apenas la cruzó. Bajarlo a $59.900 le subiría el margen (`79`).
- **A y B hacen el 70% de la utilidad** con el 25% de las unidades.
- El margen promedio simple de las cinco filas es 9,7%. Ese número no describe ningún SKU real.

## Cómo generarla sin sufrir

El script imprime utilidad y margen; con un bucle sacas el catálogo entero:

```
while IFS=, read -r sku precio costo comision envio otros; do
  echo "=== $sku ==="
  python scripts/margen_ml.py margen --precio "$precio" --costo "$costo" \
      --comision "$comision" --envio "$envio" --otros "$otros" --iva 19 \
      | grep -E "GANAS|PIERDES|Margen sobre|VEREDICTO"
done < catalogo.csv
```

`catalogo.csv` con una línea por SKU. La columna `envio` la llenas de la tabla oficial (`78`), no
de un promedio: es el error que arruina este ejercicio.

Para automatizarlo contra tu catálogo real por API, ver `183` y el bloque `175`-`199`.

## Las cuatro lecturas de la tabla

| Ordena por | Te muestra |
|---|---|
| **Utilidad total/mes, descendente** | Quién sostiene el negocio. Protégelos |
| **Utilidad total/mes, ascendente** | Quién lo sangra. Empieza por ahí (`98`) |
| **Margen %** | Quién aguanta publicidad (margen > ACOS, ver `150`) |
| **Envío como % del precio** | Quién está mal ubicado respecto al umbral (`79`) |

La cuarta es la que nadie mira y la que da las victorias rápidas: un SKU con el envío al 14% del
precio casi siempre se arregla moviendo el precio de lado del umbral.

## El SKU que vende mucho y no deja

Es el caso más frecuente y el más difícil de aceptar, porque es tu "producto estrella". Señales:

```
□ Está entre los 3 más vendidos por unidades
□ Está entre los 3 últimos por utilidad total
□ Su envío pesa más del 15% de su precio
□ Su margen está por debajo del 10%
□ Aumentaste ventas el último trimestre y la utilidad no subió
```

Tres marcadas: ese SKU está trabajando para Mercado Libre, no para ti. Ver `98`.

## Frecuencia y disparadores

| Momento | Qué recalculas |
|---|---|
| **Mensual** | Toda la tabla (`99`) |
| Cambió el costo del proveedor | Los SKUs de ese proveedor |
| Cambió tu color de reputación | **Todo el catálogo**: el envío cambió (`78`) |
| Un SKU cruzó $60.000 en cualquier dirección | Ese SKU: el envío cambió de columna |
| Entraste o saliste de una campaña | Los SKUs involucrados (`91`) |
| Activaste o desactivaste cuotas extra | Todo: son 3 puntos exactos (`80`) |

La tercera fila es la que se olvida y la que más duele: **pasar de verde a amarillo cambia el
margen de todos tus SKUs a la vez**, no de algunos.

## El error clásico

Mirar el reporte de ventas de Mercado Libre y ordenar por unidades. Ese ranking te muestra qué se
vende, no qué deja. El vendedor promociona su SKU más vendido, vende el doble, y gana menos.

El segundo: calcular la tabla una vez, sentirse organizado, y no volver a tocarla en seis meses
(`99`).

## Relacionados

`75` estructura de costos · `76` el cargo por venta 8%-22% · `78` el envío que pagas tú · `79` el
umbral de los $60.000 · `82` la calculadora de margen · `83` precio mínimo viable · `86` por qué
los productos baratos pierden · `95` costo de la devolución · `96` costo del reclamo · `98` qué
hacer con el SKU que no deja · `99` revisión mensual · `150` ACOS sano · `183` precio y stock por
API
