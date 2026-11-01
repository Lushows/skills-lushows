# El precio mínimo viable

Es el piso: el precio por debajo del cual la venta no tiene sentido. No es "el precio al que no
pierdo" —ese es el punto de equilibrio y es un mal objetivo—. Es el precio al que ganas el margen
que el negocio necesita para sobrevivir a devoluciones, publicidad y meses malos.

## Tres pisos distintos, no uno

| Piso | Definición | Para qué sirve |
|---|---|---|
| **Punto de equilibrio** | Utilidad = 0 | Saber dónde está el abismo. No publicar ahí |
| **Piso operativo** | Margen que cubre devoluciones y reclamos | El mínimo defendible (`95`, `96`) |
| **Piso estratégico** | Margen que además deja espacio para pautar | El que usas si quieres crecer (`150`) |

Y en Colombia hay un cuarto, legal y absoluto: **$2.900**, el precio mínimo de publicación (oficial
ML Colombia, verificado sep-2026). Por debajo de eso no puedes publicar, punto (`77`).

**El precio mínimo no es donde dejas de perder: es donde el negocio aguanta un mes malo.**

## Cómo calcularlo

```
python scripts/margen_ml.py minimo --costo 42000 --margen-objetivo 25 --comision 14.5 \
    --envio 10100 --iva 19 --otros 900
```

Cargo **14,5% — ejemplo dentro del rango oficial 8%-22%, verifica el tuyo** (`76`). Envío de tabla
oficial (3-4 kg, producto sobre $60.000, reputación verde) = $10.100 (`78`).

Lo que hay detrás, por si quieres entenderlo en vez de confiar:

```
base × (1 − cargo_efectivo − margen) = costo + envío + otros
precio = base × (1 + IVA)
```

Con el cargo cobrado sobre el precio con IVA (el caso normal), el cargo efectivo sobre la base es
`cargo × (1 + IVA)` — ver `81`. Si cargo + margen objetivo suman 100% o más, el script lanza un
error en vez de devolverte un absurdo.

## El problema circular del envío

Aquí hay una trampa que ningún script resuelve solo: **el costo de envío depende del precio**, y el
precio mínimo depende del envío. Si calculas el mínimo con el envío de la columna
"$30.000-$59.999" y el resultado te da $64.000, tu cálculo está mal: a ese precio el envío es el de
la columna "más de $60.000", casi el doble (`79`).

Cómo se resuelve, a mano y en dos pasadas:

```
□ Pasada 1: calcula el mínimo con el envío de la columna donde CREES que va a caer
□ Mira el resultado. ¿Cayó en esa columna?
□ Si cayó en otra columna, repite con el envío de la columna correcta
□ Repite hasta que el precio resultante y la columna de envío coincidan
□ Si nunca converge, es que tu producto vive en la zona muerta: usa un kit (ver 87)
```

Casi siempre converge en dos pasadas. Cuando no converge, el producto te está diciendo algo.

## Qué margen objetivo pedirle

| Situación | `--margen-objetivo` |
|---|---|
| Solo quieres saber el abismo | 0 |
| Producto sin devoluciones, sin pauta, vendes por volumen | 12-15 |
| Caso general: quieres poder pautar algún día | 25 |
| Categoría con devoluciones frecuentes (moda, electrónica) | 30-35 |
| Producto único, marca propia, sin competencia directa | 35+ |

La ancla dura viene de `150`: el ACOS objetivo debe ser **menor que el margen neto**. La estrategia
de Rentabilidad de Mercado Ads arranca en un ACOS de **5%-15%** (oficial ML Colombia, verificado
sep-2026). Con margen 12% no te queda espacio: pautas y destruyes rentabilidad aunque las métricas
se vean bien.

## Los tres pisos de un mismo producto

Mismo costo de $42.000, mismo envío, cargo de ejemplo 14,5%:

```
python scripts/margen_ml.py minimo --costo 42000 --margen-objetivo 0  --comision 14.5 --envio 10100 --iva 19
python scripts/margen_ml.py minimo --costo 42000 --margen-objetivo 15 --comision 14.5 --envio 10100 --iva 19
python scripts/margen_ml.py minimo --costo 42000 --margen-objetivo 30 --comision 14.5 --envio 10100 --iva 19
```

Tres precios. El primero es el abismo, el tercero es con el que de verdad puedes operar. La
distancia entre ellos es la conversación real del negocio: si el mercado solo aguanta el primero,
no tienes un problema de precio.

## Qué hacer si el mínimo te deja por encima del líder

Este es el momento de la verdad y pasa seguido. Calculas el mínimo, miras la ficha del líder (`70`)
y él está $18.000 más barato que tu piso.

Cinco salidas, en el orden en que hay que intentarlas:

| # | Salida | Cuándo funciona | Módulo |
|---|---|---|---|
| 1 | **Bajar el costo** | Proveedor nuevo, volumen, importar directo. La única que no toca al cliente | `dropshipping_lushows` |
| 2 | **Bajar el envío** | Empaque más pequeño (ojo al peso volumétrico), o **recuperar el verde**: pasar de naranja a verde te ahorra la mitad del envío | `78` |
| 3 | **Volverlo kit** | Sube el ticket y el margen absoluto, y te saca de la comparación directa | `87` |
| 4 | **Diferenciarte para no competir en precio** | Fotos, video, garantía, ficha completa. El comprador paga más por certeza | `25`-`54` |
| 5 | **Matar el SKU** | Cuando las cuatro anteriores ya se intentaron | `98` |

La salida 2 merece un número: en un producto de 1 kg sobre $60.000, pasar de reputación naranja a
verde baja el envío de **$16.400 a $8.200** (oficial ML Colombia, verificado sep-2026). Son $8.200
de margen por venta que no dependen de negociar con nadie.

Lo que **no** es una salida: bajar el precio por debajo de tu mínimo "para entrar y después subir".
Entras a una guerra que no puedes ganar (`89`), el algoritmo te fija una posición basada en un
precio insostenible, y al subir pierdes la posición habiendo quemado el margen del arranque.

Única excepción defendible: un lote pequeño y acotado, con fecha de fin, para conseguir las
primeras opiniones. Con presupuesto cerrado y contado como costo de adquisición, no como venta.

## Cuando el líder está por debajo de tu costo

Significa una de tres cosas:

1. Él compra mucho más barato que tú (volumen, importación directa, fabricante).
2. Está vendiendo a pérdida para ganar posición, y no va a durar.
3. Ese producto es un commodity puro donde el margen vive en la escala.

En los casos 1 y 3, **ese producto no es para ti** (`84`). En el 2, puedes esperar — pero espera
sin inventario parado, y menos en Full, donde el stock viejo cobra cargo mensual por unidad.

## Lista de chequeo

```
□ Calculé los tres pisos: equilibrio, operativo y estratégico
□ Usé el cargo REAL de mi categoría, del simulador logueado, con fecha (ver 76)
□ El envío que usé corresponde a la columna de precio donde cayó el resultado (dos pasadas)
□ Verifiqué mi color de reputación antes de elegir la tabla de envío (ver 78)
□ Ningún precio mío queda por debajo de $2.900
□ Mi margen objetivo es mayor que el ACOS al que pienso pautar (ver 150)
□ Comparé el mínimo con el precio del líder real, mirando su ficha
□ Si quedé arriba, recorrí las salidas 1 a 4 antes de pensar en bajar el precio
□ Anoté el precio mínimo por SKU en una hoja, con fecha (ver 97 y 99)
```

## El error clásico

Calcular el mínimo una vez, al lanzar, y no volver a calcularlo. El costo del proveedor sube, el
precio cruza los $60.000 y el envío se duplica, o el termómetro pasa a amarillo y el descuento baja
de 50% a 40%. El precio que era tu piso hace seis meses hoy está por debajo del abismo. Ver `99`.

## Relacionados

`75` estructura de costos · `76` el cargo por venta 8%-22% · `78` el envío que pagas tú · `79` el
umbral de los $60.000 · `82` la calculadora de margen · `84` el producto que no sirve para ML ·
`87` subir el ticket con kits · `89` la guerra de precios · `97` margen por SKU · `98` qué hacer
con el SKU que no deja · `99` revisión mensual · `150` ACOS sano · `70` el líder de la categoría
