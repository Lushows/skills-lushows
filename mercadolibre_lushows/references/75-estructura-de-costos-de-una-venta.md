# Estructura de costos de una venta

La plata no se va en un solo lugar: se va en cuatro. El vendedor que resta solo "la comisión" cree
que gana 20% y en realidad gana 4%, o pierde. Este módulo arma la cascada completa, en orden, con
los números oficiales de Mercado Libre Colombia que sí existen.

## Los cuatro lugares donde se pierde plata

| # | Concepto | Quién lo cobra | Estado del dato |
|---|---|---|---|
| 1 | Cargo por venta (comisión) | Mercado Libre | **8% a 22%** (oficial ML Colombia, verificado sep-2026). El detalle por categoría, tras login (`76`) |
| 2 | Costo de envío | Mercado Libre / transportadora | **Tablas oficiales completas** por peso y rango de precio (`78`) |
| 3 | IVA | La DIAN, no ML | Tarifa legal (`81`) |
| 4 | Costos propios (producto, empaque, mano de obra) | Tú | Los tienes en casa |

**En Colombia NO existe el "cargo fijo por venta de bajo valor".** Esa es la trampa argentina del
bloque y tiene módulo propio: `77`. Lo que sí existe es un **precio mínimo de publicación de
$2.900** (oficial ML Colombia, verificado sep-2026).

## La cascada, en el orden correcto

```
precio publicado (con IVA)
  – IVA (no es tuyo, es de la DIAN)
  = base sin IVA
      – cargo por venta 8%-22% (se cobra sobre el precio CON IVA)
      – costo de envío, ya neto del descuento por reputación
      – empaque y costos propios
      – costo del producto
  = utilidad
```

Tres detalles cambian el resultado y casi nadie los tiene en cuenta:

1. **El cargo por venta se calcula sobre el precio CON IVA.** Si publicas a $119.000 y tu categoría
   cobra 14%, no son 14% de $100.000 ($14.000): son 14% de $119.000 ($16.660). Ver `81`.
2. **El costo de envío aplica a toda venta con Mercado Envíos.** La página oficial es literal:
   *"El costo de los Envíos aplica a todas las ventas, incluso si el comprador paga el envío"*
   (oficial ML Colombia, verificado sep-2026). No des por sentado que si el comprador paga, tu
   línea de envío es cero: míralo en el desglose de una venta real.
3. **El IVA sale primero.** Si eres responsable, esa plata nunca fue tuya.

**Vender no es cobrar: entre el precio publicado y tu bolsillo hay cuatro descuentos, y solo uno
de ellos te lo recuerdan.**

## El umbral de $60.000 parte la cascada en dos

Este es el número que organiza todo el bloque (oficial ML Colombia, verificado sep-2026):

| | Producto nuevo bajo $60.000 | Producto nuevo desde $60.000 |
|---|---|---|
| Envío gratis | Opcional, **el costo corre por tu cuenta** | Obligatorio, con descuentos por reputación |
| Envío de 1 kg, reputación verde | $4.300 | **$8.200** |
| Efecto | Costo bajo, sin la etiqueta verde | Costo casi el doble, con exposición |

Cruzar $60.000 **casi duplica** tu costo de envío. Ese salto es el cálculo real detrás de
"¿le subo el precio o no?". Ver `79`.

## Ejemplo de la cascada completa

Producto de 1 kg que te cuesta $42.000, publicado a $89.900, responsable de IVA, reputación verde,
empaque $900. Cargo por venta **14,5% — ejemplo dentro del rango oficial 8%-22%, verifica el tuyo**
(`76`). Envío de tabla oficial: 0,5-1 kg, producto sobre $60.000, verde → **$8.200**.

| Línea | Valor |
|---|---|
| Precio publicado | $89.900 |
| – IVA 19% | –$14.354 |
| = Base sin IVA | $75.546 |
| – Cargo por venta 14,5% sobre $89.900 | –$13.036 |
| – Envío (tabla oficial, 1 kg, verde) | –$8.200 |
| – Empaque | –$900 |
| – Costo del producto | –$42.000 |
| **= Utilidad** | **$11.410** |
| Margen sobre base sin IVA | 15,1% |

No lo hagas de cabeza. Córrelo:

```
python scripts/margen_ml.py margen --precio 89900 --costo 42000 --comision 14.5 \
    --envio 8200 --otros 900 --iva 19
```

Ver `82` para la documentación completa de la calculadora.

## La reputación es una línea de costo, no un adorno

El descuento en envíos depende del color del termómetro (oficial ML Colombia, verificado sep-2026):

| Reputación | Descuento en envíos (nuevos desde $60.000) | Envío de 1 kg |
|---|---|---|
| MercadoLíder, verde, **o sin reputación** | 50% | $8.200 |
| Amarilla | 40% | $9.840 aprox. |
| **Naranja o roja** | **Ninguno** | **$16.400** |
| Con Envíos Full | 50% | $8.200 |

Que un vendedor **sin reputación** tenga el mismo 50% que un verde es clave: el castigo no es no
tenerla, **es perderla**. Perder el verde cuesta $8.200 por venta en un producto de 1 kg. Eso ya no
es un tema de orgullo, es una línea del P&G. Ver bloque `125`-`144`.

## Lo que NO entra en esta cascada (y sí en tu P&G)

La cascada es **por unidad vendida**. Hay costos que no dependen de la venta individual:

| Costo | Naturaleza | Dónde se mide |
|---|---|---|
| Mercado Ads | Por clic, no por venta | ACOS, ver `150` |
| Stock antiguo en Full | Cargo mensual por unidad, **exponencial** desde el 4º mes | `100`-`124` |
| "Mi Página" | $44.990 COP/mes | Fijo mensual |
| Devoluciones | Probabilístico | `95` |
| Reclamos y mediaciones | Probabilístico + daño reputacional que encarece el envío | `96` |

## El único dato que sigue tras login

> ⚠️ **Parcialmente verificable (sep-2026).** El rango **8%-22%** es oficial y público, pero
> **el porcentaje exacto de tu categoría solo se ve logueado**, en `/landing/costos-de-venta` o en
> el simulador de costos. La API `GET /sites/MCO/listing_prices` **ya no es pública**: responde
> `403 PA_UNAUTHORIZED_RESULT_FROM_POLICIES` y exige token.

Por eso `margen_ml.py` recibe la comisión como parámetro obligatorio (`82`).

## El error clásico

Calcular el margen con el precio de compra y el de venta, y creer que el resto son "detalles". Los
detalles son entre 20 y 35 puntos del precio. El segundo error, más sutil: calcular bien la primera
vez y no volver a calcular cuando el precio cruza $60.000 o cuando el termómetro cambia de color.

## Lista de chequeo antes de publicar un precio

```
□ Tengo el % real de mi categoría, leído logueado en el simulador, con fecha
□ Sé si mi producto es Supermercado (paga otros costos, oficial)
□ Mi precio es igual o superior a $2.900 (mínimo oficial de publicación)
□ Busqué mi costo de envío en la tabla oficial: peso × rango de precio × mi reputación
□ Usé el peso MAYOR entre real y volumétrico (así lo cobra ML, oficial)
□ Sé si soy responsable de IVA y con qué tarifa
□ Sumé empaque, etiqueta y el tiempo de alistar
□ Corrí margen_ml.py y el veredicto no dice "pierdes plata"
□ El margen resultante deja espacio para un ACOS por debajo de él (ver 150)
```

## Relacionados

`76` el cargo por venta 8%-22% · `77` el mínimo de $2.900 y la trampa del cargo fijo · `78` el
envío que pagas tú · `79` el umbral de los $60.000 · `81` IVA y el precio que publicas · `82` la
calculadora de margen · `83` precio mínimo viable · `95` costo oculto de la devolución · `97`
margen por SKU · `99` revisión de precios mensual · `150` ACOS sano
