# La revisión de precios mensual

Un precio calculado bien hoy está mal dentro de tres meses: cambia el costo del proveedor, cambia
tu color de reputación, el producto cruza los $60.000, ML ajusta el cargo de tu categoría. Este
módulo es la rutina que evita descubrirlo en el cierre del año.

## La rutina, por frecuencia

| Frecuencia | Qué revisas | Cuánto toma |
|---|---|---|
| **Semanal** | Color del termómetro · precio de los 5 SKUs top · stock de los 10 top | 15 minutos |
| **Mensual** | La tabla completa de margen por SKU (`97`) | 2 horas |
| **Trimestral** | Cargo por venta de tus categorías · tabla de envíos · costos de proveedor | 3 horas |
| **Anual** | Qué categorías vale la pena seguir trabajando; qué SKUs matar en bloque | Medio día |

Lo semanal es lo que evita los desastres; lo mensual es lo que hace crecer el margen.

## La revisión semanal (15 minutos)

```
□ Mi termómetro sigue verde
□ Mis tres porcentajes están bajo 3,5% reclamos / 12% envíos incorrectos / 2,5% canceladas
□ Ningún SKU top cruzó $60.000 en ninguna dirección
□ Ningún precio cambió sin que yo lo tocara (repricer o integración, ver 90)
□ Los 10 SKUs más vendidos tienen stock
□ Ningún mensaje lleva más de 24 horas hábiles sin responder (ver 96)
```

La primera casilla es la más rentable de las seis: perder el verde duplica el costo de envío de
**todo** el catálogo (`78`).

## La revisión mensual (2 horas)

```
□ Actualizo la tabla de margen por SKU con costos, pesos y envíos reales (ver 97)
□ Ordeno por utilidad total mensual ASCENDENTE
□ Los 5 peores entran al proceso de 98
□ Reviso qué SKUs quedaron en la zona muerta ($60.000 a ~$66.000) y los muevo (ver 79)
□ Reviso qué SKUs tienen el envío sobre el 15% del precio y los mando a kit (ver 87)
□ Comparo mi precio con el del líder en mis 10 SKUs principales (ver 70)
□ Actualizo la tasa de devolución por SKU de los últimos 90 días (ver 95)
□ Verifico que ningún margen esté por debajo del ACOS al que estoy pautando (ver 150)
□ Reviso el inventario en Full: nada acercándose a los 4 meses (2 en Supermercado)
```

## La revisión trimestral (3 horas)

Aquí se revisan los **parámetros**, no los precios:

```
□ Entro logueado al simulador y reviso el cargo por venta de cada categoría mía
□ Anoto la fecha: sin fecha, un dato de comisión no sirve (ver 76)
□ Verifico que el rango siga siendo 8%-22% y que mi número no se haya movido
□ Reviso la tabla oficial de envíos por si cambió (ver 78)
□ Confirmo que el umbral de envío gratis sigue en $60.000
□ Confirmo que el precio mínimo de publicación sigue en $2.900
□ Pido precios actualizados a mis proveedores
□ Recalculo TODOS los precios mínimos viables con los parámetros nuevos (ver 83)
□ Corro `python scripts/margen_ml.py test` para verificar la calculadora
```

Ese último paso parece trivial y no lo es: si alguien tocó el script, las seis pruebas te lo dicen
en dos segundos (`82`).

## Los siete disparadores de revisión de emergencia

No esperes al mes. Recalcula **hoy** si pasa cualquiera de estos:

| Disparador | Qué recalculas | Por qué |
|---|---|---|
| **Tu termómetro cambió de color** | **Todo el catálogo** | El descuento de envío pasó de 50% a 40% o a 0% (`78`) |
| **Un SKU cruzó $60.000** | Ese SKU | El envío cambió de columna: puede duplicarse (`79`) |
| **Subió el costo de un proveedor** | Los SKUs de ese proveedor | Obvio y aun así se olvida |
| **Activaste o desactivaste cuotas extra** | Todo | Son exactamente 3 puntos (`80`) |
| **Vas a entrar a una campaña** | Los SKUs involucrados, ANTES de aceptar | Hot Sale: 19-23 de octubre de 2026 (`91`) |
| **Cambiaste de empaque o el producto cambió de peso** | Ese SKU | Puede saltar de rango de peso (`87`) |
| **Un competidor grande bajó el precio** | Ese SKU, sin reaccionar en caliente | Ver `89` antes de mover nada |

El primero es el que más gente pasa por alto. **Un cambio de color no afecta a un producto: afecta
a todos**, porque cambia el precio de cada envío que despachas.

**El precio no se fija una vez: se administra. Lo que no se revisa, se erosiona.**

## La hoja mínima que debes tener

Si no vas a montar nada sofisticado, ten al menos esto, con fecha en cada celda de parámetro:

| Columna | Se actualiza |
|---|---|
| SKU y nombre | Nunca |
| Categoría | Nunca |
| **Cargo por venta % + fecha del dato** | Trimestral |
| Precio publicado | Cuando lo mueves |
| **Peso empacado** | Cuando cambia el empaque |
| **Columna de envío + color de reputación** | Cuando cambie cualquiera de los dos |
| Envío en pesos | Con lo anterior |
| Costo del producto + fecha | Trimestral |
| Tasa de devolución (90 días) | Mensual |
| Margen % y utilidad/unidad | Mensual |
| Unidades/mes y utilidad total | Mensual |

Las columnas con fecha son las que evitan la pregunta "¿de cuándo es este número?", que es la
pregunta que hunde estas hojas.

## Qué NO hacer en la revisión

| Tentación | Por qué no |
|---|---|
| Mover todos los precios el mismo día | Cambios bruscos pueden dejar publicaciones "inactivas para revisar" |
| Reaccionar al precio del competidor en caliente | Así se entra a una guerra (`89`) |
| Actualizar precios por API sin apagar el repricer | Se pisan y el precio real es una lotería (`90`) |
| Usar un envío promedio en vez del de tabla | Es el error que arruina toda la hoja (`78`) |
| Confiar en un cargo por venta sin fecha | El rango es 8%-22%: 14 puntos de error posible (`76`) |

## El error clásico

Hacer la revisión una vez, con entusiasmo, en una hoja preciosa, y no volver a abrirla. A los seis
meses la hoja existe, nadie confía en ella, y las decisiones se toman de memoria. Una hoja fea que
se actualiza cada mes vale infinitamente más que una perfecta y vieja.

El segundo: revisar precios y no revisar el termómetro. El precio lo controlas tú; el descuento de
envío lo controla tu reputación, y vale más que cualquier ajuste de precio que vayas a hacer.

## Relacionados

`75` estructura de costos · `76` el cargo por venta 8%-22% · `78` el envío que pagas tú · `79` el
umbral de los $60.000 · `80` cuotas sin interés · `82` la calculadora de margen · `83` precio
mínimo viable · `87` subir el ticket con kits · `89` la guerra de precios · `90` el repricer · `91`
descuentos y campañas · `95` costo de la devolución · `96` costo del reclamo · `97` margen por SKU
· `98` qué hacer con el SKU que no deja · `150` ACOS sano
