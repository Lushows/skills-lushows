# Cuánto stock declarar

El stock no es solo un número de inventario: es una señal que el algoritmo lee y un riesgo operativo
que puede costarte la cuenta. Declarar de menos te frena; declarar de más te lleva a cancelar
ventas, y cancelar es lo único con un umbral oficial de suspensión.

## El stock como señal

| Situación | Cómo la lee ML |
|---|---|
| Stock alto y sostenido | Vendedor con respaldo; buena señal para catálogo (`63`) |
| Stock de 1 unidad | Señal débil; además es el límite de la Gratuita (`42`) |
| Stock cero | Sale de la competencia y de la puja de catálogo (MEDIA, `61`) |
| Reposición tras agotarse | "Revive como más nueva o menos confiable": hay que reconstruir señales (MEDIA, `61`) |

Técnicamente, `available_quantity: 0` pasa el ítem a `paused` con sub-estado `out_of_stock` (ALTA).
No es una pausa inocente: es salirse de la carrera y volver a empezar.

## El colchón de seguridad

Si vendes el mismo inventario en varios canales (tu tienda, WhatsApp, un local físico, otro
marketplace), **no declares en ML todo lo que tienes**. La API de Mercado Libre no tiene reserva de
stock entre canales ni bloqueo atómico (MEDIA-BAJA, análisis; ver `196`): dos ventas simultáneas en
canales distintos pueden dejarte sin producto.

| Situación | Colchón sugerido |
|---|---|
| Vendes solo en ML | Ninguno necesario |
| ML + un canal más, rotación lenta | Resta 1 unidad |
| ML + varios canales, rotación alta | Resta 2-3, o sincroniza por webhooks (`196`) |
| Producto con un solo ejemplar | Publícalo en un canal a la vez |

## Por qué el colchón: el único umbral oficial de suspensión

> **Más del 2,5% de ventas canceladas puede dejar tu cuenta suspendida para vender** (ALTA).

Y para ser verde, la regla publicada es no cancelar más del **2,5%** medido a 60 días (o 4% a 365
días; 1,5% si eres MercadoLíder) (oficial ML Colombia, verificado sep-2026; ver `126`).

Lo que agrava el caso: cancelar por falta de stock es **culpa tuya** y el reclamo por falta de stock
**no es excluible** (ALTA, `136`). No hay forma de limpiarlo.

**Vender una unidad que no tienes es la forma más cara de vender.** Pierdes la venta, la comisión no
te la devuelven en tiempo, la cancelación cuenta y, si te pasas del 2,5%, dejas de vender del todo.

## Cuánto es "suficiente"

No hay un número oficial. La forma práctica de decidirlo:

```
□ Mira cuántas unidades vendiste de ese producto en los últimos 30 días
□ Multiplícalo por el tiempo de reposición de tu proveedor, en meses
□ Súmale un 20% de seguridad
□ Ese es el stock que deberías tener; declara eso menos el colchón multicanal
```

Ejemplo del método: si vendes 20 al mes y tu proveedor demora 15 días, necesitas ~10 en tránsito
más lo que ya tienes. Si el cálculo tiene que ser exacto, rutea a `Matematicas_lushows`.

## Stock en Full: cuidado con el otro lado

En Full el exceso de stock sí cuesta plata. Hay un **cargo mensual por unidad** por inventario
antiguo, que empieza a los **4 meses** (a los **2 meses** en Supermercado) y crece de forma brutal
(oficial ML Colombia, verificado sep-2026):

| Tamaño | 4 a 6 meses | 6 a 12 meses | Más de 12 meses |
|---|---|---|---|
| Pequeño | $690 | $6.500 | $13.100 |
| Mediano | $1.100 | $16.200 | $29.200 |
| Grande | $3.600 | $64.100 | $110.000 |
| Extragrande | $9.600 | $117.700 | $149.900 |

Un producto grande olvidado un año en Full cuesta **$110.000 por unidad**. Detalle completo en
`108`. **En bodega propia sobrar es incómodo; en Full sobrar es carísimo.**

## Stock por variante

En publicaciones con variaciones (`40`), el stock es por variante. Una variante en cero visible
manda al comprador a otro lado sin comprar nada. Si no vas a reponerla pronto, quítala en vez de
dejarla agotada.

## Actualizar por API

```
PUT https://api.mercadolibre.com/items/$ITEM_ID
{"available_quantity": 30}
```

(ALTA.) Si usas stock multi-origen ("User Products"), ese `PUT` **se ignora o da error**: hay que
usar `PUT /user-products/$USER_PRODUCT_ID/stock/type/$SELLER_WAREHOUSE` (ALTA). Ver `196`.

## El error clásico

Publicar con stock 1 "por si acaso" y no subirlo nunca. Bajas la señal frente al algoritmo, no
puedes ganar catálogo, y cada venta te deja en cero con la publicación pausada. **El stock en 1 no
es prudencia: es apagar la publicación después de cada venta.**

El error opuesto, igual de caro: cargar 500 unidades en Full de un producto que rota 4 al mes.

## Chequeo

```
□ El stock declarado existe físicamente
□ Descontado el colchón si vendo en más de un canal
□ Ninguna variante visible en cero (`40`)
□ Ninguna publicación activa con stock 1 salvo que sea Gratuita
□ En Full: nada que vaya a pasar de 4 meses sin rotar (`108`)
□ Mi tasa de canceladas está muy por debajo del 2,5% (`126`)
□ Tengo alerta cuando el stock baja del punto de reposición
```

## Relacionados

`40` variaciones · `41` estructura · `42` la Gratuita · `61` stock cero y ranking · `63` ganar el
catálogo · `108` cargos por inventario antiguo en Full · `126` reputación y umbrales ·
`136` reclamos no excluibles · `196` stock por API y sobreventa · cálculos → `Matematicas_lushows`
