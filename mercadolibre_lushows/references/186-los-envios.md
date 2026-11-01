# Los envíos

El envío es la parte del negocio donde más plata se escapa sin que te enteres, porque el costo
real no aparece en la publicación: aparece después, por venta. La API te lo da por número, y ese
número es lo que convierte tu margen estimado en margen real.

## Los dos endpoints

| Qué | Endpoint |
|---|---|
| Detalle del envío | `GET /shipments/$SHIPMENT_ID` |
| Costos del envío | `GET /shipments/$SHIPMENT_ID/costs` |

```
GET https://api.mercadolibre.com/shipments/987654321
Authorization: Bearer APP_USR-...
```

El `$SHIPMENT_ID` sale de la orden: campo `shipping.id` (`185`).

## Qué te da `/shipments/$SHIPMENT_ID`

| Campo | Para qué |
|---|---|
| `status` y `substatus` | En qué punto va el paquete |
| `logistic_type` | La modalidad: fulfillment, cross-docking, self-service, etc. |
| `receiver_address` | A dónde va — la dirección vive aquí, no en la orden |
| `tracking_number` | El número de guía |
| `date_created` / fechas de estado | Con qué demora despachaste |
| `shipping_items` | Qué va dentro, con dimensiones y peso declarados |

El `logistic_type` es el que te dice si esa venta salió por Full, por Flex o por Colecta, y por lo
tanto quién la manipuló y qué reglas de plazo aplican (`100`-`103`).

## Qué te da `/costs`

Este es el endpoint que importa para la plata. Desglosa quién paga qué:

| Concepto | Qué significa |
|---|---|
| Costo bruto del envío | Lo que vale mover ese paquete |
| Lo que pone el comprador | La porción que pagó él |
| Lo que pones tú | La porción que te descuentan a ti |
| Descuentos aplicados | El subsidio que asume Mercado Libre |

**Ese "lo que pones tú" es el número que casi nadie mira y el que decide si el producto deja
utilidad o no.**

## Las tres variables del costo (y por qué no hay tabla que te sirva)

El umbral y los descuentos sí son oficiales (ML Colombia, verificado sep-2026):

| Dato | Valor |
|---|---|
| Umbral de envío gratis | Productos nuevos **desde $60.000** |
| Por debajo de $60.000 | El envío gratis es opcional y **el costo corre por tu cuenta** |
| Carrito | Si varios productos suman **$60.000**, el comprador tiene envío gratis |
| Productos de menos de $15.000 | Pagan **como máximo la mitad del precio del producto** |
| Peso que se cobra | Se compara físico contra volumétrico y **se usa siempre el más alto** |
| Cómo se calcula | **Por unidad** |
| Y ojo | El costo **aplica a todas las ventas, incluso si el comprador paga el envío** |

Descuento por reputación, oficial:

| Reputación | Descuento en envíos |
|---|---|
| MercadoLíder, **verde**, o **sin reputación** | **50%** |
| **Amarilla** | **40%** |
| **Naranja o roja** | **Ninguno**: tarifa plena |
| Con Envíos Full | **50%** |

Ahora junta las tres: el costo de un envío depende del **peso**, del **rango de precio del
producto** y de **tu color de reputación** en ese momento. Son tres ejes que se mueven, y el
tercero se mueve solo, todos los días, sin que tú hagas nada (`127`).

**Por eso el costo real de una venta concreta no se puede deducir de una tabla estática: hay que
preguntárselo a la API, venta por venta.** Esa es la razón de existir de `/costs`.

Dos consecuencias que tu integración debería vigilar sola:

| Vigilancia | Por qué |
|---|---|
| Cruzar el umbral de $60.000 salta el costo | El mismo paquete cuesta mucho más del otro lado |
| Perder el verde te cambia todos los costos | Pasas de 50% de descuento a 0% de un día para otro |

Ese segundo punto es el argumento económico del bloque de reputación en un solo número: **el
termómetro no es orgullo, es el precio de cada envío que despachas** (`125`).

## Para qué sirve saber el costo real por API

| Uso | Qué desbloquea |
|---|---|
| Margen real por venta | Precio − comisión − **envío que asumiste** − costo (`124`) |
| Margen real por SKU | Un producto liviano y uno pesado no se comparan por precio |
| Decidir el precio | Si el envío te come 8 puntos, el precio tiene que subir o el producto sale |
| Decidir la pauta | El ACOS objetivo debe ser menor que el margen **neto** (`150`) |
| Detectar el producto que sangra | El que se vende mucho y no deja nada |

Sin `/costs`, todo eso es adivinanza. Con `/costs`, es una columna en tu base de datos.

## Qué automatizar

```
□ Al cerrar cada orden, guardar shipment_id, logistic_type y el costo que asumiste
□ Calcular y guardar el margen real de esa venta, no el estimado
□ Alarma si una venta lleva X horas sin pasar a despachado
□ Reporte mensual de costo de envio asumido por SKU
□ Marcar los SKU donde el envio se lleva mas de N puntos del precio
```

## Envíos incorrectos y el termómetro

Los **envíos incorrectos** —despachar con demora o desde el depósito equivocado— son una de las
tres variables base del termómetro de reputación (`126`), junto con reclamos y canceladas. Para
MercadoLíder el límite oficial es **menos del 10%** de envíos incorrectos (oficial ML Colombia,
verificado sep-2026).

Tu integración puede vigilarlo sola: comparar la fecha de la orden contra la fecha en que el envío
pasó a despachado y avisarte antes de que se venza. Es una alarma de cinco líneas que te protege
una métrica que cuesta meses recuperar.

## Lo que la API no te da

| No esperes | Por qué |
|---|---|
| Cambiar la modalidad de envío por API | Se define en la publicación y en la cuenta |
| Elegir transportadora | Lo decide Mercado Envíos |
| Tarifa exacta antes de vender | Depende de peso, rango de precio y tu reputación de ese día |
| Datos completos del comprador | Están restringidos; ver `185` |

## El error clásico

Clavar en el código una tarifa de envío fija, sacada de una tabla que alguien copió una vez. Esa
tabla asume un peso, un rango de precio y un color de reputación, y los tres cambian. El día que
tu termómetro pasa de verde a amarillo, cada envío te cuesta más y tu sistema sigue calculando
márgenes con el número viejo. **El único costo de envío verdadero es el que devuelve `/costs` para
esa venta.** Guárdalo por venta, no lo promedies antes de tenerlo.

## Relacionados

`100` cómo funciona Mercado Envíos · `102` Flex · `124` el costo real del envío ·
`125` el termómetro · `126` las tres métricas · `127` el periodo de evaluación · `150` ACOS sano ·
`180` los endpoints · `185` las órdenes · `199` arquitectura de referencia
