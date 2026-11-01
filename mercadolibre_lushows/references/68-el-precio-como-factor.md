# El precio como factor

El precio no solo decide cuánto ganas: decide **si te ven**. Es uno de los cinco pilares del
ranking y una de las ocho variables del catálogo. Por eso existe una tensión permanente entre el
precio que te posiciona y el precio que te deja margen, y ese pulso se resuelve con números, no
con corazonadas. El otro lado del pulso está en `83`.

## Qué mira el algoritmo

| Lo que el algoritmo compara | Lo que tú crees que compara |
|---|---|
| Tu **precio final** contra el de la misma categoría | Tu precio de lista |
| El total que paga el comprador, con envío | El número grande de la publicación |
| Tu competitividad relativa, no tu número absoluto | "Si es barato, subo" |

El precio final incluye el envío. Un producto de $45.000 con envío de $12.000 compite contra uno
de $55.000 con envío gratis y **pierde**, aunque el número grande sea menor. Por eso `86` y `67`
son parte de esta conversación.

**Bajar el precio es la palanca más rápida de todas y la única que tu competidor puede copiar en
treinta segundos.**

## Dónde pesa

| Lugar | Cómo |
|---|---|
| Ranking de búsqueda | "Precio / competitividad" es uno de los cinco pilares (`57`) |
| Catálogo | "Precio final" es la primera variable de las ocho (`63`) |
| Conversión | El precio es la razón número uno de abandono; y la conversión es la señal más pesada (`58`) |
| Indicador de calidad | "Tener el precio más competitivo" es uno de los objetivos para llegar a "Profesional" (`48`) |
| Filtros del comprador | Los rangos de precio del buscador te dejan dentro o fuera |

Fíjate en el cuarto: el propio indicador de calidad de la publicación premia el precio
competitivo. Es el reconocimiento más explícito que ML hace de que el precio es señal, no solo
número.

## La tensión con el margen

```
precio publicado (con IVA)
  – IVA (no es tuyo, es de la DIAN)
  = base sin IVA
      – comisión de la categoría, 8%-22% (se cobra sobre el precio CON IVA)
      – envío que asumes tú, neto del descuento por reputación
      – empaque y costos propios
      – costo del producto
  = utilidad
```

Cada peso que bajas para posicionarte sale de la última línea. Y la comisión se calcula sobre el
precio **con IVA**, así que bajar el precio baja la comisión en términos absolutos pero no cambia
el porcentaje que te cobran.

Corre siempre el número antes de mover el precio:
`python scripts/margen_ml.py margen --precio X --costo Y --comision Z --iva 19`

Si el cálculo tiene que ser exacto para una decisión grande, rutea a `Matematicas_lushows`. Si el
tema es IVA, retenciones o facturación, rutea a `contador_lushows`.

## La comisión: el rango oficial

"Crear una publicación no tiene costo. Cuando concretes la venta, pagarás **entre 8% y 22%** según
la categoría de tu producto y la cantidad de cuotas que elijas ofrecer" (oficial ML Colombia,
verificado sep-2026).

| Precio del producto | Cuotas con 0% interés | Cargo por venta |
|---|---|---|
| Menos de $499.999 | Hasta 3 cuotas | **8% a 19%** |
| Menos de $499.999 | Cuotas extra – hasta 6 | **11% a 22%** |
| $500.000 a $1.499.999 | Hasta 6 cuotas | **8% a 19%** |
| $500.000 a $1.499.999 | Cuotas extra – hasta 9 | **11% a 22%** |
| Más de $1.500.000 | Hasta 12 cuotas | **8% a 19%** |

**Ofrecer cuotas extra cuesta exactamente 3 puntos porcentuales.** No es una estimación: es la
diferencia entre las dos filas de cada rango. Antes de activarlas, calcula si esos 3 puntos te los
devuelve la conversión que ganas. En catálogo suelen devolverse; en publicación propia, depende.

Los productos de la sección **Supermercado** pagan otros costos (oficial ML Colombia, verificado
sep-2026).

> ⚠️ **Sin verificar para Colombia (sep-2026).** La comisión **exacta de tu categoría** dentro del
> 8%-22% no es pública: el detalle vive detrás del login, en `/landing/costos-de-venta` y en el
> simulador de costos. Y la API **ya no sirve**: `GET /sites/MCO/listing_prices` hoy responde
> `403 PA_UNAUTHORIZED_RESULT_FROM_POLICIES` y exige token. Léela logueado y mete ese número en la
> calculadora; nunca uses el promedio del rango.

## El precio mínimo: $2.900 (y la trampa argentina, resuelta)

En Colombia **no existe un cargo fijo por venta de bajo valor**. Lo que existe es un piso:

> "El precio de tu producto debe ser **igual o superior a $2.900**. Esto te permitirá cubrir las
> tarifas de venta. Puedes vender productos de menor valor ofreciendo packs o combos."
> (oficial ML Colombia, verificado sep-2026)

Esto cierra la trampa número uno del ecosistema. Circula masivamente —y los buscadores lo devuelven
al preguntar por Colombia— que "los ítems bajo $33.000 pagan un cargo fijo de $1.330 / $2.740 /
$3.320 según rango". **Eso es Argentina, en pesos argentinos.** No aplica aquí, y la página oficial
colombiana no menciona ningún cargo fijo en COP.

El mecanismo colombiano para productos baratos es doble y hay que conocerlo:

| Mecanismo | Regla |
|---|---|
| Piso de publicación | $2.900. Debajo de eso, arma packs o combos (`89`) |
| Tope de envío en productos baratos | "Los productos de menos de **$15.000** pagan como máximo **la mitad del precio** del producto" |

El segundo es un alivio real: en un producto de $12.000, el envío que asumes no puede pasar de
$6.000 por más que pese.

## Cuándo sí bajar el precio

| Situación | Veredicto |
|---|---|
| Peleas catálogo y ya ganaste en Full, reputación y cuotas | **Sí**, es la última carta y toca jugarla |
| Tienes costo real más bajo que el competidor | **Sí**, es tu ventaja estructural |
| Tu conversión es buena pero no te ven | **No**: el problema es exposición, no precio |
| Te ven mucho y no vendes | Revisa foto y entrega primero; el precio es el tercer sospechoso |
| Vas a quedar con menos de tu piso de margen | **No.** Ver `64`: cambia de producto |
| Estás en las primeras 72 horas | **Define el precio correcto de entrada** y no lo muevas (`59`) |
| Es Hot Sale (19-23 oct 2026) | Sí, con descuento planeado y stock, no reactivo (`163`) |

## Cuándo subir el precio

Se habla poco de esto y es igual de importante:

```
□ Cuando se te va a acabar el stock y repones en días: frena la venta sin caer a cero (`61`)
□ Cuando tu conversión es altísima: estás dejando plata en la mesa
□ Cuando el líder del catálogo subió y quedaste con margen para acompañar
□ Cuando el costo del proveedor subió y ya no cubres
```

Cuidado con el cómo: un **cambio brusco de precio** es una causa citada de que la publicación
quede "inactiva para revisar" (ver `73`). Sube en escalones, no de un salto.

## El escalón de los $60.000

Hay un punto del precio que no es gradual: **$60.000**. Desde ahí ML te pide ofrecer envío gratis o
con descuento, y tu costo de envío casi se duplica. Con reputación verde y 1 kg, el envío pasa de
**$4.300** (producto de $30.000-$59.999) a **$8.200** (producto desde $60.000) — oficial ML
Colombia, verificado sep-2026.

| Precio del producto | Envío de 1 kg que asumes (verde) | Lectura |
|---|---|---|
| $55.000 | $4.300 | Zona barata del envío |
| $62.000 | $8.200 | Subiste $7.000 de precio y $3.900 de costo |

Subir de $55.000 a $62.000 te deja **$3.100 netos**, no $7.000. Y bajar de $61.000 a $59.000 puede
dejarte **más** utilidad que antes. Corre los dos escenarios completos antes de mover un precio
cerca del umbral: la tabla de costos por peso y rango está en `86`.

**Cerca de los $60.000 el precio deja de ser una recta: hay un escalón, y el que no lo ve pierde
plata subiendo.**

## Lo que la SIC vigila en Colombia

La Superintendencia de Industria y Comercio vigila los "descuentos falsos": el precio final debe
corresponder al promocional, sin costos ocultos (confianza media, sep-2026). Inflar el precio de
lista para mostrar un descuento grande no es solo mala práctica comercial: es riesgo regulatorio.
Ver `18`.

## Checklist antes de mover un precio

```
□ Saqué la comisión real del simulador logueado, no del promedio del rango 8%-22%
□ Si cruzo los $60.000, comparé el costo de envío de los dos lados del umbral (`67`)
□ Calculé el margen con la calculadora, incluyendo IVA, envío y empaque
□ Comparé mi PRECIO FINAL (con envío) contra el del competidor, no el de lista
□ Verifiqué si el competidor tiene Full o cuotas que expliquen su posición
□ Definí mi piso de margen y el nuevo precio queda por encima
□ No estoy dentro de las primeras 72 horas de la publicación
□ El cambio es gradual, no un salto que pueda pausar la publicación
□ Si es promoción, el precio tachado es un precio que realmente cobré
```

## El error clásico

Bajar el precio como primera reacción a "no vendo". Nueve de cada diez veces el problema era la
foto 1, el tiempo de entrega o la reputación — cosas que no cuestan margen — y el vendedor regaló
tres puntos de utilidad para descubrir que seguía sin vender. **El precio es el último ajuste, no
el primero.**

## Relacionados

`18` SIC y precios · `48` indicador de calidad · `57` factores del ranking ·
`58` la conversión manda · `59` primeras 72 horas · `61` stock cero ·
`63` cómo se gana el catálogo · `64` cuándo no competir en catálogo · `67` envío y posición ·
`70` espiar al líder · `73` pausas e infracciones · `78` Clásica vs Premium ·
`80` comisión real · `83` precio con margen · `86` envío gratis · `163` Hot Sale
