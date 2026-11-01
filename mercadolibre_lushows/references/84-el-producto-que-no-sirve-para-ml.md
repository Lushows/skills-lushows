# El producto que no sirve para ML

No todo producto que se vende bien en la calle sobrevive en Mercado Libre. La plataforma tiene una
estructura de costos que descarta categorías enteras, y ahora que las tablas de envío son oficiales
se puede decidir antes de comprar inventario, no después. Este módulo es un filtro de descarte.

## La regla de arranque

Con un cargo por venta oficial de **8% a 22%** (`76`), un envío que sobre $60.000 arranca en $8.000
y puede llegar a $83.400 en productos pesados (`78`), y un IVA que convierte tu cargo nominal en
uno efectivo de hasta 26,2% (`81`), la aritmética es implacable:

> **Si tu margen bruto sobre el costo no llega al 60%, en Mercado Libre no te queda nada.**

No es una opinión: corre `margen_ml.py` con un producto que compras a $60.000 y vendes a $90.000
(50% de markup) con envío de tabla y cargo del 16%, y mira el veredicto.

## Los siete criterios de descarte

| # | Criterio | Señal de alarma | Por qué mata |
|---|---|---|---|
| 1 | **Margen delgado** | Markup bajo 60% sobre costo | El cargo + envío + IVA se lo comen entero |
| 2 | **Muy pesado** | Más de 10 kg | Sobre $60.000 el envío pasa de $15.200 y sube rápido (`78`) |
| 3 | **Muy voluminoso** | Peso volumétrico > peso real | Pagas por transportar aire, y ML usa el mayor de los dos (oficial) |
| 4 | **Muy barato** | Bajo $15.000 | El envío puede llegar al 50% del precio (oficial). Y bajo $2.900 ni se publica (`77`) |
| 5 | **Frágil** | Vidrio, cerámica, electrónica delicada | Rotura = reclamo NO excluible = reputación = envío al doble |
| 6 | **Alta tasa de devolución** | Tallas, colores, compatibilidades | 30 días de devolución en productos nuevos (oficial). Ver `95` |
| 7 | **Commodity puro** | Idéntico al de otros 40 vendedores | Solo compites por precio y el margen tiende a cero (`89`) |

## Tabla de descarte, con números

Pasa tu producto por estas filas antes de comprar inventario:

| Pregunta | Corte de descarte | Si falla |
|---|---|---|
| ¿Markup sobre costo? | **< 60%** | Descarta o renegocia costo |
| ¿Peso (mayor entre real y volumétrico)? | **> 10 kg** y precio > $60.000 | Descarta salvo ticket muy alto |
| ¿Precio de venta? | **< $15.000** | Solo como kit (`87`) |
| ¿Precio de venta? | **< $2.900** | Imposible: no se puede publicar |
| ¿Se rompe si la caja cae 1 metro? | Sí | Descarta o reempaca antes de decidir |
| ¿Tasa de devolución esperada? | **> 10%** | Recalcula con `95` antes de seguir |
| ¿Cuántos vendedores idénticos hay? | **> 20 con el mismo producto** | Necesitas diferenciación real o descarta |
| ¿El líder vende por debajo de tu costo? | Sí | Descarta: no es tu mercado (`83`) |

Tres fallas o más: no lo compres. Una sola de las filas de "imposible" (precio bajo $2.900, líder
bajo tu costo): tampoco.

**Mercado Libre no castiga los productos malos: castiga los productos pesados, baratos y comunes.
Son cosas distintas.**

## El caso del producto pesado, con números oficiales

Un producto de 15 kg vendido a $120.000, reputación verde: el envío de tabla es **$25.200**
(columna "más de $60.000", fila 10-20 kg). Eso es el **21% del precio**, antes del cargo por venta.

Sumado a un cargo del 15% y al IVA, ese producto necesita un markup superior al 120% para dejar
algo. Casi ningún producto pesado lo tiene.

Salidas reales para producto pesado:

| Salida | Cómo |
|---|---|
| Subir mucho el ticket | A $400.000 el envío de $25.200 pesa 6%, no 21% |
| Reducir peso volumétrico | Empaque ajustado, desarmar, enviar plano |
| Vender bajo $60.000 | En esa columna el envío de 15 kg es $5.100, no $25.200 (pero sin etiqueta) |
| Retiro en persona / Flex | Si tu operación local lo permite |
| No venderlo en ML | La respuesta correcta más veces de las que quisieras |

Mira esa tercera fila con cuidado, porque es contraintuitiva y es real: **el mismo paquete de 15 kg
cuesta $5.100 si el producto vale $50.000 y $25.200 si vale $61.000**. Para productos pesados,
quedarse debajo del umbral puede ser la decisión rentable (`79`).

## Lo que este módulo NO decide

Qué producto vender, cómo encontrarlo, de dónde traerlo, qué proveedor, qué país, qué tendencia.
Eso es `dropshipping_lushows`, que es la skill de selección de producto. Este módulo solo responde
una pregunta: **dado un producto, ¿aguanta la estructura de costos de Mercado Libre Colombia?**

Para la viabilidad del negocio completo (no del SKU), `economist_lushows`.

## El producto que SÍ sirve

El retrato hablado, para que sepas qué buscar:

```
□ Pesa menos de 2 kg empacado (real y volumétrico)
□ Se vende entre $60.000 y $400.000
□ Markup sobre costo por encima del 80%
□ No se rompe si la caja se cae
□ No tiene tallas ni compatibilidades que generen devoluciones
□ Tiene alguna diferencia defendible: marca, kit, garantía, presentación
□ Su categoría no es de las caras del rango 8%-22% (verifícalo logueado)
□ Rota: no se queda meses en bodega (crítico si usas Full, ver 100-124)
```

Ese perfil no es casualidad. Es exactamente el producto que la estructura de costos de la
plataforma premia.

## El error clásico

Comprar el inventario primero y calcular después. El vendedor trae 200 unidades de algo pesado y
barato, publica, vende 15, y descubre que cada venta le quitó plata. Para entonces el inventario ya
está comprado y la única salida es liquidarlo por debajo del costo.

El segundo error: descartar un producto por el margen calculado con el envío equivocado. Antes de
matar un SKU, verifica que usaste la columna correcta de la tabla oficial y el color correcto de
reputación (`78`).

## Lista de chequeo antes de comprar inventario

```
□ Pesé y medí una unidad EMPACADA
□ Busqué su costo de envío en la tabla oficial, en las dos columnas relevantes
□ Corrí margen_ml.py con el cargo en 8%, 14,5%, 19% y 22%
□ Sobrevive al 22%: si solo sobrevive al 8%, es una apuesta, no un plan
□ Miré cuántos vendedores idénticos hay y a qué precio está el líder
□ Estimé la tasa de devolución y la metí en el cálculo de 95
□ Si es pesado, comparé el escenario "bajo $60.000" contra "sobre $60.000"
□ Si falló 3 filas de la tabla de descarte, no lo compré
```

## Relacionados

`75` estructura de costos · `76` el cargo por venta 8%-22% · `77` el mínimo de $2.900 · `78` el
envío que pagas tú · `79` el umbral de los $60.000 · `82` la calculadora de margen · `83` precio
mínimo viable · `85` el ticket que aguanta ML · `86` por qué los productos baratos pierden · `87`
subir el ticket con kits · `89` la guerra de precios · `95` costo de la devolución · `98` qué hacer
con el SKU que no deja · `dropshipping_lushows` para elegir producto · `economist_lushows` para la
viabilidad del negocio
