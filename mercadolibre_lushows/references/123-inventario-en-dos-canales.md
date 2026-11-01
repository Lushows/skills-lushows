# Inventario en dos canales

Vender el mismo stock en Mercado Libre y en otro canal —tu web, WhatsApp, tienda física, otro
marketplace— es normal y es rentable. También es la causa más común de la falla más cara del
termómetro: **vender lo que ya no tienes y terminar cancelando.**

## Por qué la sobreventa es tan cara

Cuando vendes algo que ya se fue por el otro canal, solo tienes tres salidas y las tres pesan:

| Salida | Variable del termómetro | Techo para seguir verde |
|---|---|---|
| Cancelas tú | **Canceladas por ti** | 2,5% a 60 días · 4% a 365 días · 1,5% ML |
| Despachas tarde mientras repones | **Envíos incorrectos** | 12% a 60 d · 15,5% a 365 d |
| Mandas algo distinto | **Reclamo de calidad** | 3,5% de ventas con reclamos |

(Oficial ML Colombia, verificado sep-2026.)

La primera es la peor: el techo de canceladas es el más estrecho de los tres, y además **más del
2,5% de ventas canceladas puede llevar a la suspensión de la cuenta para vender** (oficial).

Y hay un cuarto costo: perder el verde te quita el 50% de descuento en envíos. Un producto de más
de $60.000 y 1 kg pasa de **$8.200 a $16.400** por venta (oficial). **Una sobreventa mal resuelta
puede duplicarte el flete de todo el mes siguiente.**

## El colchón de seguridad

La mitigación estándar, porque la API **no tiene reserva de stock entre canales ni bloqueo
atómico**:

```
STOCK PUBLICADO EN ML = stock real − colchón

colchón = ventas del otro canal en el tiempo que tardas en sincronizar + 1
```

| Situación | Colchón sugerido |
|---|---|
| Sincronizas en tiempo real por webhooks | 1 unidad |
| Sincronizas cada hora | 1 a 2 unidades |
| Sincronizas manual, una vez al día | 2 a 3 unidades, o más si el otro canal es fuerte |
| SKU de altísima rotación | Sube el colchón, no lo bajes |

**El colchón no es desperdicio: es el seguro más barato contra el 2,5%.** Una unidad que no
publicas cuesta una venta; una cancelación cuesta un porcentaje de todas.

## La sincronización, en orden de calidad

| Método | Latencia | Riesgo |
|---|---|---|
| Webhooks de ML + actualización inmediata del otro canal | Segundos | Bajo |
| Consulta periódica (polling) cada 15-60 min | Minutos | Medio |
| Integrador o ERP que maneje ambos canales | Depende | Medio |
| Planilla y buena memoria | Horas o días | **Alto** |

Los webhooks son la vía recomendada oficialmente ("preferir webhooks sobre polling", verificado).
Topics relevantes: `orders_v2`, `items`, `stock_fulfillment`, `stock_locations`. Requisito duro:
**HTTP 200 dentro de 500 ms**, o ML desactiva la suscripción de tu app (verificado). Detalle en
`190` y `196`.

## Los detalles técnicos que rompen la sincronización

| Detalle | Qué pasa |
|---|---|
| `available_quantity: 0` | El ítem pasa a `paused` con sub-estado `out_of_stock` (verificado) |
| Stock multi-origen (User Products) | `PUT /items` con `available_quantity` **se ignora** |
| Repricer activo en el ítem | Tu `PUT` de precio se puede pisar en la próxima corrida |
| IDs de usuario | Desde dic-2024 exceden Int32: guárdalos en Int64 o truena |
| Webhooks duplicados | Deduplica por `_id` o por `resource` + timestamp |

Con multi-bodega hay que usar `PUT /user-products/$USER_PRODUCT_ID/stock/type/$SELLER_WAREHOUSE`
(verificado). Ver `184`.

## El caso Full: el stock deja de ser tuyo

Este es el conflicto estructural. El inventario que está en la bodega de ML **no sirve para tu
otro canal**. No puedes sacar dos unidades para una venta por WhatsApp.

| Estrategia | Cómo funciona |
|---|---|
| **Partir el stock** | Una parte a Full para ML, otra en tu bodega para el otro canal |
| **Full solo para SKUs exclusivos de ML** | Los productos multicanal nunca van a Full |
| **Todo en tu bodega** | Renuncias a Full, ganas flexibilidad (`105`) |

La segunda suele ser la más limpia: **decide por SKU si es "de ML" o "multicanal", y no mezcles.**
Mezclar es lo que genera la llamada de "necesito una unidad y está en Funza".

Y cuidado con partir el stock sin plan de rotación: lo que mandas a Full y no se vende empieza a
pagar cargo mensual por unidad desde el mes 4 — $690 pequeño, $3.600 grande, y a los 6 meses
$6.500 y $64.100 (oficial). Ver `108`.

## La rutina de control

```
□ Conteo físico semanal de los SKUs de mayor rotación, no mensual
□ Comparar stock real vs stock publicado en ML vs stock publicado en el otro canal
□ Revisar el colchón: ¿se sobrevendió algo este mes? Sube el colchón de ese SKU
□ Revisar los SKUs que quedaron en cero: ¿se repusieron o siguen pausados?
□ En Full: revisar antigüedad del inventario y decidir antes del día 90 (`108`)
```

El cuarto punto atrapa un costo silencioso: un ítem que quedó en `paused` por stock cero y nadie
repuso sale de la puja de catálogo y, al volver, tiene que reconstruir señales. Si tenía pauta,
reinicia el aprendizaje.

## Cuándo NO conviene el multicanal

| Señal | Lectura |
|---|---|
| Sobreventas repetidas y cancelaciones cerca del 2,5% | Reduce a un canal hasta estabilizar |
| El otro canal vende 5% de lo que vende ML | No vale el riesgo: cierra o separa stock |
| No tienes forma de sincronizar ni manual | Un canal, hasta que la tengas |
| El producto es de stock unitario o pieza única | Nunca lo publiques en dos lados |

## El error clásico

Publicar en ML el stock completo "para no perder ventas" y confiar en que va a alcanzar. Funciona
diez veces y falla la once, justo con el producto que ya se vendió en la tienda física. Esa once
cuesta una cancelación, y la cancelación cuesta el 2,5% más caro del marketplace.

**Publica menos de lo que tienes. Siempre.**

## Relacionados

`103` Full · `105` cuándo conviene Full · `106` ingresar inventario · `108` inventario viejo ·
`113` la demora y su costo · `114` el flujo diario · `119` entrega fallida · `124` auditoría
mensual · `126` las tres métricas · `140` el quiebre de stock · `184` stock multi-bodega · `189`
webhooks · `196` la sobreventa multicanal · `100` tarifas oficiales de envío
