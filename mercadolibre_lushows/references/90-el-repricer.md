# El repricer

Mercado Libre ofrece ajustar tu precio automáticamente para mantenerte competitivo. Es cómodo, a
veces funciona, y tiene dos riesgos concretos: te mete en una guerra de precios sin que la
declares (`89`) y **pisa los cambios que hagas por API**. Este módulo dice cuándo conviene y cómo
ponerle correa.

## Qué hace

Un ajuste automático que baja (y en algunos casos sube) el precio de tu publicación según lo que
hacen los competidores en la misma ficha o categoría. Trabaja 24/7, reacciona en minutos y no
consulta tu costo.

Esa última frase es la importante: **el repricer conoce el mercado, no conoce tu margen**. Sabe a
cuánto vende el otro; no sabe a cuánto compraste tú, cuánto pesa tu producto ni en qué columna de
envío caes.

**El repricer no defiende tu margen: defiende tu posición. Son objetivos distintos y a veces
opuestos.**

## El riesgo verificado: pisa tus cambios por API

Dato confirmado: **antes de modificar `price` con `PUT /items/$ITEM_ID`, revisa si el ítem tiene
ajuste automático de precio activo — el `PUT` puede quedar pisado en la siguiente corrida del
repricer.**

Esto rompe integraciones enteras en silencio. Tu sistema escribe el precio correcto, la API
responde 200, y 40 minutos después el precio es otro. Nadie falla, nadie avisa, y tú vendes al
precio que decidió el repricer.

```
□ Antes de escribir precios por API, lista qué ítems tienen el ajuste automático activo
□ Decide por SKU: o lo maneja el repricer, o lo maneja tu sistema. NUNCA los dos
□ Si tu sistema manda, apaga el repricer en ese ítem
□ Si el repricer manda, quita ese ítem de tu rutina de escritura de precios
□ Monitorea: compara el precio que escribiste contra el precio real 2 horas después
□ Suscríbete al topic `items_prices` por webhook para enterarte de los cambios que no hiciste tú
```

Detalle completo de la mecánica de API en `183` y en el bloque `175`-`199`.

## Cuándo conviene

| Situación | ¿Repricer? | Por qué |
|---|---|---|
| Commodity con muchos competidores y margen holgado | **Sí** | La posición vale más que los pesos de diferencia |
| Compites por el catálogo en una categoría muy activa | **Sí, con piso duro** | El precio final pondera para ganar la oferta (`63`) |
| Producto único, kit o marca propia | **No** | No hay contra quién repreciar; solo te vas a bajar solo |
| Margen por debajo del 15% | **No** | No hay espacio para que un algoritmo lo recorte |
| Catálogo grande, sin tiempo de revisar precios | Sí, pero con pisos por SKU | Es el caso de uso legítimo |
| Tienes integración que escribe precios | **No, o apaga la integración** | Se pisan entre sí |

## El piso: la única configuración que importa

Si lo activas, dale un suelo. Y el suelo correcto no es "el costo": es **tu precio mínimo viable**
del `83`, calculado con el margen objetivo que tu negocio necesita.

```
□ Corre margen_ml.py minimo con tu margen objetivo real para ese SKU
□ Ese precio, no el punto de equilibrio, es el piso del repricer
□ Recalcula el piso cuando cambie el costo, el peso o tu reputación
□ Ojo con el umbral: si el piso está justo debajo de $60.000, no dejes que el
  repricer lo cruce hacia arriba ni hacia abajo sin recalcular el envío (ver 79)
```

Ese último punto es específico de Colombia y el repricer no lo entiende: **cruzar $60.000 casi
duplica tu costo de envío** (`78`, `79`). Un repricer que sube tu precio de $59.900 a $61.500 para
igualar a un competidor te acaba de costar $3.900 por venta sin avisarte.

## Qué vigilar cada semana

| Señal | Qué significa |
|---|---|
| Precio actual por debajo del piso que configuraste | El piso no está donde crees. Revísalo |
| Precio cruzó $60.000 en cualquier dirección | Recalcula el margen: el envío cambió de columna |
| Unidades arriba y utilidad abajo | Estás en una guerra que no declaraste (`89`) |
| El precio cambió y tú no lo tocaste ni el repricer tampoco | Hay una integración escribiendo. Encuéntrala |
| La publicación quedó "inactiva para revisar" | Cambio brusco de precio. Se reactiva al corregir |

## La alternativa: reprecio manual con disciplina

Para catálogos de menos de ~50 SKUs, un repaso quincenal con una hoja bien hecha gana al repricer:
tú sí conoces tu costo, tu peso y tu columna de envío. La rutina está en `99`.

Para catálogos grandes, la salida intermedia es un repricer **propio** por API con tu piso
calculado por SKU, en vez del automático de la plataforma. Ojo: si escribes precios por API tienes
que apagar el ajuste automático de ML en esos ítems o se pisan. Ver `183`.

## El error clásico

Activarlo "para no quedarme atrás", no configurar piso, y descubrir seis semanas después que el
catálogo vende al costo. El repricer hizo exactamente lo que le pidieron: mantener la posición. Lo
que nadie le pidió fue ganar plata.

El segundo, más silencioso: tener integración por API escribiendo precios **y** el repricer activo
en los mismos ítems. Los dos funcionan, ninguno falla, y el precio real es una lotería que se
resuelve cada corrida.

## Lista de chequeo

```
□ Sé exactamente en qué ítems está activo el ajuste automático
□ Ningún ítem tiene repricer Y escritura de precios por API al mismo tiempo
□ Cada ítem con repricer tiene un piso = su precio mínimo viable (ver 83)
□ Los pisos se recalcularon después del último cambio de costo o de reputación
□ Ningún piso deja que el precio cruce $60.000 sin recalcular el envío
□ Reviso semanalmente precio real vs. piso configurado
□ Tengo webhook en `items_prices` para enterarme de cambios que no hice
```

## Relacionados

`78` el envío que pagas tú · `79` el umbral de los $60.000 · `83` precio mínimo viable · `88`
precio psicológico · `89` la guerra de precios · `91` descuentos y campañas · `99` revisión de
precios mensual · `63` ganar el catálogo · `183` actualizar precio y stock por API · `175`-`199`
API y automatización
