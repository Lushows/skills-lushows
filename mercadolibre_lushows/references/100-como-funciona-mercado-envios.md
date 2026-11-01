# Cómo funciona Mercado Envíos

Mercado Envíos es la capa logística del marketplace: ML negocia con las transportadoras, genera la
etiqueta, rastrea y responde ante el comprador. No es opcional en la práctica, y su costo **aplica
a todas tus ventas, incluso si el comprador paga el envío** (oficial ML Colombia, verificado
sep-2026).

## La frase oficial que casi nadie lee

> "El costo de los Envíos aplica a todas las ventas, incluso si el comprador paga el envío."
> (oficial ML Colombia, verificado sep-2026)

Es decir: el envío **siempre** te cuesta algo. Lo que cambia con el umbral de $60.000 es cuánto de
ese costo te descuenta ML y cuánto sale de tu liquidación.

## Las reglas del umbral de $60.000 (oficiales)

| Situación | Qué pasa |
|---|---|
| Producto **nuevo desde $60.000** | Ofreces envío gratis, y tú tienes descuento por reputación |
| Producto **menor a $60.000** | El envío gratis es opcional y **el costo corre por tu cuenta** |
| Carrito que **sume $60.000** entre varios productos | El comprador tiene envío gratis |
| Producto de **menos de $15.000** | Pagas máximo **la mitad del precio del producto** |

(Todo oficial ML Colombia, verificado sep-2026.)

La tercera fila es la palanca de los tickets bajos: **dos productos tuyos de $32.000 le dan envío
gratis al comprador y te reparten un solo costo de envío entre dos ventas.** Por eso el combo es
una decisión logística además de comercial.

## El descuento por reputación (oficial)

| Reputación | Descuento en el costo de envío |
|---|---|
| MercadoLíder, **verde**, o **sin reputación** | **50%** |
| Amarilla | **40%** |
| Naranja o roja | **Ninguno** — tarifa plena |
| Con Envíos Full | **50%** |

(Oficial ML Colombia, verificado sep-2026.)

Lee bien la primera fila. **Un vendedor sin reputación tiene el mismo 50% que un verde.** El
castigo no es no tener reputación: es perderla. Tu peor momento económico no es el día uno, es el
día en que caes a naranja.

## La tabla oficial de costos — verde / MercadoLíder / sin reputación

Productos nuevos, con Full, Colecta, Agencias o Correo. El precio es el del producto. (Oficial ML
Colombia, verificado sep-2026.)

| Peso | $0–$14.999 | $15.000–$29.999 | $30.000–$59.999 | Más de $60.000 |
|---|---|---|---|---|
| Hasta 0,3 kg | $2.500 | $2.600 | $4.100 | $8.000 |
| 0,3 a 0,5 kg | $2.600 | $2.700 | $4.200 | $8.100 |
| 0,5 a 1 kg | $2.700 | $2.800 | $4.300 | $8.200 |
| 1 a 2 kg | $2.800 | $2.900 | $4.500 | $8.500 |
| 2 a 3 kg | $2.900 | $3.000 | $4.600 | $8.600 |
| 3 a 4 kg | $3.000 | $3.200 | $4.700 | $10.100 |
| 4 a 5 kg | $3.100 | $3.300 | $4.800 | $10.200 |
| 5 a 7 kg | $3.200 | $3.400 | $4.900 | $10.500 |
| 7 a 10 kg | $3.300 | $3.500 | $5.000 | $15.200 |
| 10 a 20 kg | $3.400 | $3.600 | $5.100 | $25.200 |
| 20 a 30 kg | $3.500 | $3.700 | $5.200 | $41.400 |
| 30 a 40 kg | $3.600 | $3.800 | $5.300 | $49.000 |
| 40 a 50 kg | $3.700 | $3.900 | $5.400 | $66.700 |
| 50 a 60 kg | $3.800 | $4.000 | $5.500 | $69.400 |
| 60 a 70 kg | $3.900 | $4.100 | $5.600 | $71.500 |
| 70 a 80 kg | $4.000 | $4.200 | $5.700 | $72.400 |
| 80 a 90 kg | $4.100 | $4.300 | $5.800 | $75.100 |
| 90 a 100 kg | $4.200 | $4.400 | $5.900 | $77.800 |
| 100 a 120 kg | $4.300 | $4.500 | $6.000 | $83.400 |
| 120 a 140 kg | $4.400 | $4.600 | $6.100 | $89.700 |
| 140 a 160 kg | $4.500 | $4.700 | $6.200 | $94.600 |
| 160 a 180 kg | $4.600 | $4.800 | $6.300 | $97.700 |
| 180 a 200 kg | $4.700 | $4.900 | $6.400 | $105.300 |
| 200 a 230 kg | $4.800 | $5.000 | $6.500 | $114.300 |
| 230 a 260 kg | $4.900 | $5.100 | $6.600 | $124.000 |
| 260 a 290 kg | $5.000 | $5.200 | $6.700 | $130.800 |
| 290 a 320 kg | $5.100 | $5.300 | $6.800 | $134.800 |
| 320 a 350 kg | $5.200 | $5.400 | $6.900 | $145.700 |
| 350 a 380 kg | $5.300 | $5.500 | $7.000 | $168.200 |
| Más de 381 kg | $5.400 | $5.600 | $7.100 | $181.300 |

## El salto que decide tu precio

Mira la fila de 0,5 a 1 kg. Ese mismo paquete cuesta **$4.300** si el producto vale
$30.000-$59.999 y **$8.200** si vale más de $60.000. **Cruzar el umbral de $60.000 casi duplica tu
costo de envío.**

| Precio que pones | Envío (1 kg, verde) | Lo que tienes que ganar de más |
|---|---|---|
| $59.900 | $4.300 | — |
| $60.100 | $8.200 | $3.900 solo para quedar igual |

Antes de subir un precio de $58.000 a $62.000, ese es el número que hay que mirar. El análisis
completo de precio y margen está en `79` y `75`.

## Qué resuelve, más allá del costo

| Beneficio | Por qué importa |
|---|---|
| Etiqueta y guía generadas por ML | No cotizas ni negocias con transportadora |
| Promesa de entrega visible | El comprador ve una fecha, no un rango vago |
| Cobertura de Compra Protegida | Si no llega, ML responde (`118`) |
| Señal para el ranking | La logística es pilar del posicionamiento (`55`) |
| Peso en el desempate de catálogo | Full/Flex es variable del ganador (`63`) |

## Dónde ver tus números reales

> ⚠️ **Corrección importante (sep-2026).** La API `GET /sites/MCO/listing_prices` **ya no es
> pública**: hoy responde `403 PA_UNAUTHORIZED_RESULT_FROM_POLICIES` y exige token. Si un módulo
> viejo o un blog te la presenta como consulta abierta, está desactualizado.
>
> Además, las URLs viejas del centro de ayuda **no dan 404: redirigen a una página equivocada**.
> Para encontrar un artículo usa el buscador interno: `mercadolibre.com.co/ayuda/search?q=`

```
□ GET /shipments/$SHIPMENT_ID          → estado, modalidad, promesa (con token)
□ GET /shipments/$SHIPMENT_ID/costs    → cuánto pagó el comprador y cuánto asumiste tú
□ Panel → Ventas → Envíos              → lo mismo en pantalla
□ Simulador de costos, logueado        → antes de publicar
```

## El error clásico

Poner el precio sin mirar la tabla. El vendedor calcula margen con "el envío como unos $5.000", y
resulta que su producto de $70.000 y 8 kg paga **$15.200**. Tres veces su estimación, en cada
venta. **El envío no se estima: se busca en la tabla, por peso facturable y por rango de precio.**

## Relacionados

`101` modalidades · `102` Flex · `103` Full · `104` colecta y puntos · `109` peso volumétrico ·
`112` el tiempo que prometes · `116` productos grandes · `118` el paquete perdido · `122`
logística propia · `124` auditoría mensual · `55` algoritmo · `63` ganar el catálogo · `75` el
cálculo del margen · `79` el umbral del envío gratis · `126` las tres métricas
