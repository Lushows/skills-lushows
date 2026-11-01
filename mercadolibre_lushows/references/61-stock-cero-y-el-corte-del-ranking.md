# Stock cero y el corte del ranking

Quedarte sin stock no es una pausa: es un corte. La publicación sale de la competencia y de la
puja de catálogo, y al reponer "revive como más nueva o menos confiable" y tiene que reconstruir
señales. El daño no es el día que no vendiste; es el mes que tardas en volver a donde estabas.

## Qué pasa exactamente cuando llegas a cero

| Momento | Qué ocurre |
|---|---|
| `available_quantity` llega a 0 | El ítem pasa a `paused` con sub-estado `out_of_stock` (API, verificado sep-2026) |
| De inmediato | Deja de aparecer en resultados de búsqueda |
| De inmediato | Sale de la puja de catálogo: si venías ganando, pierdes el primer lugar (`63`) |
| Mientras dure | Tus competidores absorben tus visitas y tus ventas |
| Mientras dure | Si tenías Mercado Ads, el aprendizaje de la campaña se reinicia (`154`) |
| Al reponer | Vuelve, pero con las señales debilitadas: hay que reconstruir |

**Un día sin stock cuesta más que una semana de descuento: el descuento te quita margen, el cero
te quita posición.**

## Por qué duele tanto

El ranking premia la conversión acumulada y la continuidad. Mientras estuviste en cero:

1. No recibiste visitas → no acumulaste ventas → tu señal de conversión se congeló y envejeció.
2. El comprador que buscaba tu producto compró otro. Ese cliente ya no vuelve a buscar.
3. En catálogo, tu competidor ganó la posición principal y ahora tiene que perderla para que tú
   la recuperes (ver `63`).
4. Si pautabas, el quiebre de stock reinicia el aprendizaje y encarece la pauta futura sobre esa
   publicación (confianza media-baja, sep-2026).

> ⚠️ **Sin verificar para Colombia (sep-2026).** No hay una cifra oficial de cuántos días tarda
> una publicación en recuperar posición tras un quiebre de stock. Lo verificado es el mecanismo,
> no el plazo. Mídelo en tu propia cuenta.

## El colchón de seguridad

Nunca dejes que el número visible llegue a cero. Define un piso y trátalo como si fuera cero.

| Rotación de la publicación | Piso recomendado |
|---|---|
| Vendes menos de 1/semana | 2 unidades |
| Vendes 1-5/semana | Cubre 2 semanas de venta promedio |
| Vendes más de 5/semana | Cubre el tiempo de reposición completo + 1 semana |
| Vendes en Full | Cubre el tiempo de envío al centro de fulfillment + recepción |

Con Full el riesgo es mayor porque no puedes despachar tú si se acaba: el inventario está en Funza
(confianza media-baja, una sola fuente) y reponerlo toma días. Ver `107`.

## Checklist anti-quiebre

```
□ Define el punto de reorden por publicación, no para todo el catálogo
□ Configura alerta cuando el stock baje del piso, no cuando llegue a cero
□ Revisa el stock de las publicaciones que ganan catálogo TODOS los días
□ Si vendes en varios canales, usa colchón: resta 1-2 unidades del disponible real
□ Antes de una fecha alta (Hot Sale 19-23 oct 2026), duplica el piso
□ Nunca dejes 1 unidad como "vitrina": frena al que quiere dos
□ Si el proveedor falla, sube el precio antes que caer a cero (ver abajo)
```

## Qué hacer si sabes que te vas a quedar sin stock

Tienes tres salidas y una es mala.

| Salida | Cuándo usarla | Efecto |
|---|---|---|
| **Subir el precio** | Se te acaba mañana y repones en días | Frenas la venta sin perder la publicación. La conversión baja un poco |
| **Ampliar el tiempo de manejo** | Repones en pocos días y puedes cumplir | Sigues vendiendo; ojo, despachar tarde sí pesa en reputación (`126`) |
| **Dejarla caer a cero** | Solo si la discontinuaste | Corte total |

La peor jugada es **seguir vendiendo lo que no tienes**. Cancelar la venta es peor que todo lo
anterior junto: cancelar por falta de stock es un reclamo **no excluible** (oficial ML, verificado
sep-2026), y más del **2,5% de ventas canceladas puede llevar a suspensión de la cuenta para
vender** (oficial ML Colombia, verificado sep-2026). Ver `133`.

## Multicanal: el escenario de la sobreventa

Si vendes lo mismo en ML y en otro canal, la API **no tiene reserva de stock cross-canal ni
locking atómico** (análisis, no texto oficial). Dos compradores pueden tomar la última unidad al
mismo tiempo. Mitigación estándar:

```
□ Colchón de seguridad: publica 1-2 unidades menos del stock real
□ Webhooks (topic orders_v2) en vez de polling, para reaccionar en segundos (`185`)
□ Descuenta el stock al confirmar la orden, no al despachar
□ Si usas multi-bodega, PUT /items con available_quantity se ignora:
  usa PUT /user-products/$USER_PRODUCT_ID/stock/type/$SELLER_WAREHOUSE
```

## Cómo volver bien después de un cero

```
□ Repón con cantidad suficiente para no repetirlo en 30 días
□ NO cambies precio ni título el mismo día que repones: deja que estabilice
□ Revisa si perdiste el catálogo y ataca las variables de `63`
□ Si tenías campaña de Ads, reactívala con presupuesto bajo y súbelo gradual
□ Trata la reactivación como un mini-lanzamiento: protocolo de 3 días de `59`
□ Si a las 3 semanas no recupera, corre el diagnóstico de `72`
```

## El error clásico

Manejar el stock por intuición y darse cuenta del cero cuando ML manda el aviso de publicación
pausada. Para entonces ya perdiste el catálogo, el competidor entró, y el aprendizaje de la
campaña se reinició. El stock no es tema de bodega: **es una variable de posicionamiento.**

## Relacionados

`44` variaciones · `57` factores del ranking · `58` la conversión manda ·
`59` primeras 72 horas · `60` relanzar una publicación quemada · `62` qué es el catálogo ·
`63` ganar el catálogo · `72` por qué cayó mi publicación · `103` Full · `107` inventario en Full ·
`126` envíos incorrectos · `133` cancelaciones · `154` quiebre de stock y pauta ·
`185` webhooks · `191` stock por API
