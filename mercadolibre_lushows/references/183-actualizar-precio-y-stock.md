# Actualizar precio y stock

Es la automatización que más plata salva y la que más rápido se paga. Un solo endpoint hace las
dos cosas, pero cada una tiene una trampa propia: el stock en cero pausa la publicación y el
precio puede ser pisado por el ajuste automático.

## El endpoint

```
PUT https://api.mercadolibre.com/items/$ITEM_ID
Authorization: Bearer APP_USR-...
Content-Type: application/json
```

Cuerpo:

```json
{ "available_quantity": 30, "price": 12000 }
```

Puedes mandar los dos campos o solo uno. Lo que no mandas, no se toca.

## La regla del stock en cero

> `available_quantity: 0` pasa el ítem a **`paused`** con sub-estado **`out_of_stock`**
> (oficial ML, verificado sep-2026).

No es un error: es el comportamiento esperado. Pero tiene consecuencias que la gente descubre
tarde:

| Consecuencia | Detalle |
|---|---|
| Sale de la competencia | Deja de mostrarse y sale de la puja de catálogo (`63`) |
| Pierde señales | Al reponer, "revive como más nueva o menos confiable" y debe reconstruirlas |
| Encarece tu pauta | Reinicia el aprendizaje del algoritmo sobre esa publicación (`153`) |

Por eso el veredicto: **antes de dejar un ítem en 0, pregúntate si no es mejor dejar 1 unidad y
alargar el tiempo de despacho.** Quedarte sin stock no es gratis aunque no vendas nada esos días.

Para reactivar, mandas cantidad mayor que cero; si el ítem quedó pausado a mano, puede que
necesites mandar también `"status": "active"`.

## La advertencia del repricer

Si el ítem tiene **ajuste automático de precio** activo (el repricer de Mercado Libre), tu `PUT`
puede quedar pisado en la próxima corrida del ajuste. No falla, no avisa: simplemente el precio
vuelve a moverse y tú crees que tu integración no funcionó.

```
□ Antes de tocar price por API, revisa si el item tiene ajuste automatico activo
□ Si lo tiene: decide quien manda, tu codigo o el repricer. Nunca los dos
□ Si tu codigo manda, apaga el ajuste automatico para ese item
□ Si manda el repricer, tu codigo solo lee el precio, no lo escribe
```

**Dos sistemas fijando el mismo precio no es redundancia, es una guerra que pierdes tú.**

## Multi-bodega: cuando el `PUT` deja de servir

Si tu cuenta usa stock multi-origen ("User Products"), el `PUT /items` con `available_quantity`
**se ignora o da error**. Ese caso tiene su propio endpoint y su propio módulo: `184`.

Cómo saber en cuál estás: si tu ítem tiene un `user_product_id` asociado, estás en multi-origen.

## Ritmo y volumen

| Situación | Ritmo recomendado |
|---|---|
| Vendes solo en ML | Reaccionar al webhook de orden basta (`190`) |
| Vendes también fuera de ML | Empuja el cambio apenas ocurre, no cada hora (`196`) |
| Cargue masivo inicial | Distribuye las llamadas en el tiempo, no en ráfaga (`193`) |

Nunca hagas un barrido completo de todos tus ítems cada pocos minutos: es la forma más rápida de
comerte el presupuesto de peticiones y ganarte un `429` (`193`). Actualiza **lo que cambió**.

## Frenos obligatorios

Un bug en un bucle de precios puede publicar tu catálogo entero a $1. Pon los frenos antes:

```
□ Tope de variacion: rechaza cualquier cambio mayor a X% respecto al precio actual
□ Piso absoluto por SKU: por debajo del costo, no se publica jamas
□ Tope de items tocados por corrida: si supera N, frena y avisa
□ Log de todo cambio: item, precio viejo, precio nuevo, quien lo pidio
□ Modo simulacion: poder correr todo sin escribir, y leer el reporte
```

El piso por SKU se calcula con el método del bloque de margen (`75`-`99`), y el cálculo exacto se
ejecuta, no se estima: `Matematicas_lushows`.

## Verificar que quedó

Un `200` no siempre significa lo que crees. Después de un `PUT` crítico, lee el ítem y compara:

```
GET https://api.mercadolibre.com/items/$ITEM_ID
```

Y revisa `price`, `available_quantity`, `status` y `sub_status`. Esto es especialmente importante
con el repricer activo y en multi-bodega.

## El error clásico

Sincronizar el stock en un solo sentido: descontar en ML cuando vendes por fuera, pero no
descontar en tu sistema cuando vendes en ML. Terminas con un inventario que solo sabe la mitad de
la verdad y vendes dos veces la misma unidad. La sobreventa acaba en cancelación, y las
cancelaciones por encima del **2,5%** pueden suspender la cuenta (oficial ML Colombia, verificado
sep-2026). Ver `196`.

El segundo error: subir el precio y bajar el stock en dos llamadas separadas con minutos de
diferencia. En ese hueco alguien compra al precio viejo con el stock nuevo. Manda ambos campos en
el mismo `PUT`.

## Relacionados

`63` ganar el catálogo · `75` comisiones y margen · `153` quiebre de stock y pauta ·
`180` los endpoints · `184` stock multi-bodega · `185` las órdenes · `190` topics y payload ·
`193` límites de uso · `196` la sobreventa multicanal
