# Stock multi-bodega

Cuando tu cuenta maneja stock en varios orígenes (tu bodega y Full, o dos bodegas propias), el
modelo de datos cambia: el stock deja de vivir en el ítem y pasa a vivir en el "User Product". Si
no te enteras, tus actualizaciones de stock fallan en silencio o con un error que no explica nada.

## Qué es un "User Product"

Es una capa intermedia entre tu producto y sus publicaciones. Un mismo User Product puede
alimentar varias publicaciones y tener stock repartido en varios depósitos.

```
        PRODUCTO (user_product_id)
              |
    +---------+----------+
    |                    |
  stock en              stock en
  tu bodega             Full
    |                    |
    +---------+----------+
              |
      PUBLICACIONES (item_id)
```

En el modelo viejo, el stock era un número dentro del ítem. En el nuevo, el ítem solo **refleja**
la suma de los orígenes. Por eso escribir en el ítem deja de tener sentido.

## La regla

> Con stock multi-origen ("User Products"), el `PUT /items` con `available_quantity`
> **se ignora o da error**. (oficial ML, verificado sep-2026)

Que se ignore es peor que que falle: tu integración reporta éxito, tú crees que actualizaste y el
stock real nunca se movió. **Un `200` no es prueba de que el stock cambió.**

## El endpoint correcto

```
PUT https://api.mercadolibre.com/user-products/$USER_PRODUCT_ID/stock/type/$SELLER_WAREHOUSE
Authorization: Bearer APP_USR-...
Content-Type: application/json
```

Las dos piezas de la URL:

| Pieza | Qué es |
|---|---|
| `$USER_PRODUCT_ID` | El identificador del producto, no el del ítem |
| `$SELLER_WAREHOUSE` | El tipo de origen: el depósito del vendedor |

El cuerpo lleva la cantidad para ese origen. Cada origen se actualiza por separado: **no existe
una llamada que reparta el stock entre bodegas por ti.**

## Cómo saber en qué modelo estás

```
□ 1. GET /items/$ITEM_ID y busca si trae un user_product_id asociado
□ 2. Si lo trae -> estas en multi-origen: usa el endpoint de user-products
□ 3. Si no lo trae -> PUT /items con available_quantity sirve (`183`)
□ 4. Ante la duda: haz un cambio de prueba de 1 unidad y VERIFICA leyendo de vuelta
□ 5. Nunca asumas por el tipo de cuenta: verifica por item
```

El paso 5 importa porque la migración no siempre es de golpe: puedes tener ítems viejos en el
modelo clásico e ítems nuevos en multi-origen conviviendo en la misma cuenta.

## Full cambia quién manda

Si parte de tu inventario está en Full, ese stock **no lo controlas tú**: lo controla el
inventario físico que Mercado Libre tiene en su centro de fulfillment. Tu integración puede leerlo
pero no inventarlo.

| Origen | ¿Quién fija el número? | Qué puede hacer tu bot |
|---|---|---|
| Tu bodega | Tú | Escribir la cantidad |
| Full | El inventario real en el centro de ML | Leer, y disparar reabastecimiento |

El centro de fulfillment de Full en Colombia es **Funza, Cundinamarca** (confianza MEDIA-BAJA, una
sola fuente). Los costos de almacenamiento y el cargo por inventario viejo no están verificados
para Colombia: ver `110` y siguientes, y no uses las cifras mexicanas que circulan.

## Qué se rompe al migrar

Si tu integración nació en el modelo viejo y la cuenta pasa a multi-origen, esto deja de funcionar
sin aviso:

| Lo que hacías | Qué pasa ahora |
|---|---|
| `PUT /items` con `available_quantity` | Se ignora o falla |
| Leer el stock desde el campo del ítem | Te da la suma, no el detalle por bodega |
| Restar 1 al stock del ítem tras cada venta | No sabes de qué bodega salió |
| Un solo "número de stock" en tu sistema | Necesitas uno por origen |

La consecuencia de fondo: **tu base de datos también tiene que aprender el concepto de bodega.**
Si tu tabla de inventario tiene una sola columna de cantidad, ya no alcanza.

## Lista de chequeo de migración

```
□ Mapeo item_id -> user_product_id guardado en mi base
□ Lista de mis origenes de stock, con su identificador
□ Mi tabla de inventario tiene cantidad POR ORIGEN
□ Tras cada escritura, leo de vuelta y comparo (no confio en el 200)
□ El stock de Full lo trato como solo lectura
□ Colchon de seguridad configurado por origen (`196`)
```

## El error clásico

Descubrir el multi-origen cuando ya vendiste lo que no tenías. El síntoma es exactamente este: las
actualizaciones "funcionan" durante semanas —devuelven 200— pero el stock en la publicación nunca
cambia, hasta que llega una venta de algo agotado. Y una cancelación tuya golpea el termómetro y
te acerca al **2,5%** que puede suspender la cuenta (oficial ML Colombia, verificado sep-2026).

**Verifica leyendo de vuelta desde el primer día. El costo de esa lectura extra es ridículo
comparado con una cancelación.**

## Relacionados

`110` Full y almacenamiento · `139` cancelaciones y riesgo de cuenta · `180` los endpoints ·
`183` actualizar precio y stock · `185` las órdenes · `196` la sobreventa multicanal ·
`199` arquitectura de referencia
