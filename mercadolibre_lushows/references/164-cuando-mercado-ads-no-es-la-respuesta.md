# Cuándo Mercado Ads no es la respuesta

Los casos en que pautar es tirar la plata. Este módulo existe porque la pregunta que llega casi
siempre es "¿cómo pauto?" cuando la pregunta correcta es "¿debería?". Casi nunca la respuesta es
la pauta primero.

## La idea central

**Mercado Ads es un multiplicador, no un arreglo.** Multiplica lo que ya tienes: si tu publicación
convierte y deja plata, la pauta te da más de eso. Si no convierte o no deja plata, la pauta te da
más de nada, más rápido y más caro.

## Los seis casos en que NO se pauta

| # | Caso | Qué arreglar primero |
|---|---|---|
| 1 | **Margen delgado** (neto bajo 15%) | Precio, costo o producto (`83`, `154`) |
| 2 | **Ficha mala** | Atributos, fotos, título (`40`, `42`, `28`, `48`) |
| 3 | **Reputación naranja o roja** | Reclamos, cancelaciones, despachos (`125`) |
| 4 | **Stock inestable** | Abastecimiento, no publicidad (`61`) |
| 5 | **Producto que no sirve para ML** | El producto, no el canal (`04`) |
| 6 | **No sabes tu margen** | Corre la calculadora hoy (`82`) |

### 1. Margen delgado

Con margen neto bajo 15%, ni el piso de la estrategia Rentabilidad (5%) sobrevive a la primera
devolución. Y ojo: el margen que creías tener suele ser bruto. Con la comisión oficial de
Colombia en **8%-22%** más el envío, un "15% de margen" calculado como precio menos costo
normalmente ya es negativo (`154`). **No pautes lo que no sabes si gana.**

### 2. Ficha mala

El anuncio de Product Ads **es tu ficha** (`146`). Pautar una ficha incompleta hace dos daños a la
vez: pagas clics que no convierten, y le enseñas al algoritmo que tu publicación recibe visitas y
no vende — la etiqueta más cara de quitar (`59`, `153`).

Señal inequívoca en el reporte: **clics sin ventas.** Eso no se arregla con presupuesto.

### 3. Reputación naranja o roja

Aquí el argumento es numérico, no moral. La reputación decide tu descuento de envío (oficial ML
Colombia, verificado sep-2026):

| Reputación | Descuento en envíos | Paquete de 1 kg, producto > $60.000 |
|---|---|---|
| Verde, MercadoLíder, o **sin reputación aún** | **50%** | **$8.200** |
| Amarilla | 40% | $9.600 |
| **Naranja o roja** | **Ninguno** | **$16.400** |

**Perder el verde te duplica el costo de envío: $8.200 más por cada venta.** Sobre 100 ventas al
mes son $820.000 que recuperas arreglando reputación, sin gastar un peso en pauta. Ninguna campaña
te devuelve eso. Y encima, la penalización de ranking por reputación caída no se compensa con
gasto publicitario (`66`).

Dato que conviene leer dos veces: un vendedor **sin reputación todavía** tiene el mismo 50% que un
verde. **El castigo no es no tenerla: es perderla.**

### 4. Stock inestable

Quedarte sin stock con la pauta encendida apaga los anuncios, corta la curva de aprendizaje y
encarece la pauta futura sobre esa publicación (`61`, `147`). Si tu abastecimiento es impredecible,
la pauta amplifica el problema: generas demanda que no puedes cumplir, y las cancelaciones golpean
la reputación — que es el caso 3.

### 5. Producto que no sirve para Mercado Libre

Hay productos que no funcionan en el canal, y ninguna campaña lo cambia:

| Producto | Por qué no |
|---|---|
| Muy barato, sin volumen | El precio mínimo de publicación es $2.900 y el envío se come todo (`86`) |
| Muy pesado o voluminoso | El envío mata el margen; el volumétrico manda (`109`) |
| Frágil o perecedero sin logística | Reclamos y devoluciones destruyen la reputación |
| Genérico idéntico a 200 vendedores | Pelea de precio pura: gana el que tiene más espalda (`63`) |
| Requiere explicación o asesoría larga | El canal es de decisión rápida; esa venta es de `ventas_lushows` |
| Categoría restringida o prohibida | Riesgo de pausa o suspensión (`73`) |

Si el problema es el producto, el tema no es Mercado Ads: es `dropshipping_lushows` (qué vender) o
`economist_lushows` (si el negocio cierra).

### 6. No sabes tu margen

No es un caso menor: es el más frecuente. Pautar sin el número es apostar. Corre esto antes de
abrir el panel de publicidad:

```
python scripts/margen_ml.py margen --precio 80000 --costo 30000 --comision 14 --iva 19
```

## El test de cinco preguntas

Respóndelas antes de crear cualquier campaña. Un solo "no" detiene todo:

```
□ ¿Sé el margen neto EXACTO de este SKU, calculado, no estimado?      (`82`)
□ ¿Ese margen neto supera el 15%?                                      (`150`)
□ ¿Mi reputación está en verde o verde claro?                          (`125`)
□ ¿La ficha está en calidad "Profesional" con fotos de 1200 px?        (`48`)
□ ¿Tengo stock verificado para 30 días?                                (`61`)
```

Cinco síes: pauta con `146` y `148`. Un no: arregla eso, es más rentable que cualquier campaña.

## El orden de retorno, de mayor a menor

Casi siempre hay algo gratis que rinde más que la pauta:

| Acción | Costo | Retorno típico |
|---|---|---|
| Arreglar la reputación a verde | $0 | Hasta $8.200 por envío + posición |
| Llenar los atributos obligatorios | $0 | Entras en los filtros de búsqueda (`40`) |
| Cambiar la foto principal a blanco puro 1200 px | Bajo | Sube el CTR en el listado (`42`) |
| Quitar cuotas extra que no necesitas | $0 | **3 puntos** de comisión recuperados (`80`) |
| Revisar el peso y el empaque | Bajo | Baja el costo de envío por unidad (`109`) |
| Subir el precio donde el mercado lo aguanta | $0 | Margen directo (`83`) |
| **Mercado Ads** | **Alto** | **Solo si todo lo anterior ya está hecho** |

## El error clásico

Pautar para tapar un problema. El vendedor ve que no vende, concluye que le faltan visitas y
compra visitas. Pero rara vez faltan visitas: falta conversión. Comprar visitas para una
publicación que no convierte es la forma más cara posible de confirmar el diagnóstico.
**Antes de preguntarte cuánto invertir en Mercado Ads, pregúntate por qué quien ya te visita no te
compra.**

## Relacionados

`145` qué es Mercado Ads · `146` Product Ads · `148` las tres estrategias ·
`150` el ACOS sano según tu margen · `151` la ventana de atribución ·
`153` el efecto sobre lo orgánico · `154` el error de pautar sin margen ·
`155` leer los reportes · `156` optimizar semana a semana · `163` tráfico externo ·
`04` diagnóstico inicial · `28` el título · `40` atributos · `42` fotos ·
`48` indicador de calidad · `59` las primeras 72 horas · `61` stock cero ·
`63` ganar el catálogo · `66` reputación como filtro · `73` pausas · `80` cuotas sin interés ·
`82` la calculadora de margen · `83` precio mínimo viable · `86` por qué los productos baratos
pierden · `109` peso volumétrico · `125` reputación
