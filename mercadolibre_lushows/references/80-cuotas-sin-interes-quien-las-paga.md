# Cuotas sin interés: quién las paga

"Sin interés" para el comprador quiere decir "con interés" para alguien, y ese alguien eres tú.
En Colombia el costo es exacto y oficial: **ofrecer cuotas extra cuesta 3 puntos porcentuales más**
de cargo por venta. Este módulo trae la tabla, la nomenclatura correcta y el cálculo de si valen la
pena.

## La nomenclatura correcta (esto cambió)

El sitio colombiano **ya no habla de "Clásica" y "Premium"**. Hoy la ayuda de Mercado Libre
Colombia usa:

| Nombre actual en Colombia | Qué es |
|---|---|
| **Gratuita** | Sin costo, exposición baja, **no ofrece cuotas con 0% interés** |
| **Publicación con cuotas con 0% interés** | La estándar de pago |
| **Cuotas extra** | Más cuotas, +3 puntos de cargo |

"Clásica / Premium" es el nombre viejo, y sigue vigente en otros países. Si una fuente te habla de
Premium en Colombia, esa fuente está desactualizada o es de otro site. Ver `42` y `43`.

## La tabla oficial

> *"Cuando concretes la venta, pagarás **entre 8% y 22%** según la categoría de tu producto y la
> cantidad de cuotas que elijas ofrecer."* (oficial ML Colombia, verificado sep-2026)

| Precio del producto | Cuotas con 0% interés | Cargo por venta |
|---|---|---|
| Menos de $499.999 | Hasta 3 cuotas | **8% a 19%** |
| Menos de $499.999 | Cuotas extra – hasta 6 | **11% a 22%** |
| $500.000 a $1.499.999 | Hasta 6 cuotas | **8% a 19%** |
| $500.000 a $1.499.999 | Cuotas extra – hasta 9 | **11% a 22%** |
| Más de $1.500.000 | Hasta 12 cuotas | **8% a 19%** |

**Ofrecer cuotas extra cuesta exactamente 3 puntos porcentuales más.** No es una estimación: es
una resta limpia entre las dos filas de cada rango.

Y fíjate en el diseño: **cuanto más caro el producto, más cuotas obtienes sin pagar el recargo**.
Sobre $1.500.000 ya tienes 12 cuotas dentro del 8%-19%, y no existe opción de cuotas extra. Mercado
Libre ya asumió que el ticket alto se financia.

**Los 3 puntos no compran cuotas: compran las cuotas número 4, 5 y 6. Las tres primeras ya venían
incluidas.**

## La publicación Gratuita, y por qué casi nunca sirve

Oficial ML Colombia, verificado sep-2026:

> Duran **60 días**, tienen **exposición baja** en el listado y **no ofrecen cuotas con 0% interés**.

| Límite | Valor |
|---|---|
| Ventas gratis de **usados** | Hasta **20 en un año** |
| Ventas gratis de **nuevos** | Hasta **5 en un año** |
| Publicaciones gratuitas simultáneas | Máximo **10** |
| Stock por publicación gratuita | **1 unidad** |
| MercadoLíder o usuario profesional de Mercado Pago | **No puede vender de forma gratuita** |

Además, las ventas con publicación Gratuita **no cuentan** para MercadoLíder. Es para liquidar
cosas de la casa, no para un negocio.

## El cálculo de si las cuotas extra valen la pena

La pregunta no es "¿me cuesta 3 puntos?", es "¿esos 3 puntos traen más de 3 puntos de ventas?".

Sea `m` tu margen actual y `d` = 3 puntos. El aumento mínimo de unidades para empatar es:

```
aumento mínimo de unidades (%) = d / (m − d) × 100
```

| Margen actual | Aumento de unidades necesario para empatar |
|---|---|
| 40% | 8,1% |
| 30% | 11,1% |
| 25% | 13,6% |
| 20% | 17,6% |
| 15% | 25,0% |
| 12% | 33,3% |
| 10% | 42,9% |
| 6% | 100% |

Con 3 puntos el empate llega mucho antes que con los 4 del viejo esquema Clásica→Premium. Verifica
cualquier fila con `Matematicas_lushows` si vas a decidir sobre ella.

## El veredicto

| Situación | Qué hacer |
|---|---|
| Producto sobre $1.500.000 | **No hay decisión**: ya tienes 12 cuotas en el rango base |
| Ticket entre $200.000 y $1.499.999 | **Cuotas extra.** En Colombia el ticket medio-alto se financia |
| Categoría con catálogo activo | **Cuotas extra.** Es una de las variables que deciden el ganador (`63`) |
| Margen sobre 25% | **Cuotas extra.** Empatas con 14% más de unidades |
| Margen 15%-25% | Mídelo: 30 días en cada modalidad y compara utilidad total |
| Margen bajo 12% | **Sin cuotas extra.** No te queda espacio ni para pautar (`150`) |
| Producto de $18.000, compra impulsiva | **Sin cuotas extra.** Nadie financia $18.000 a 6 cuotas |
| Vas a entrar a Hot Sale | Cuotas extra. El evento se comunica con cuotas |

Ese último punto tiene fecha: **Hot Sale Colombia, segunda edición 19-23 de octubre de 2026**. La
primera edición (16-20 de marzo) se promocionó con hasta 12 cuotas sin interés y +40,4 millones de
búsquedas en 5 días. Ver `91`.

Si el margen te obliga a quedarte sin cuotas en una categoría que las exige, el problema no es la
modalidad: es el producto o el costo. Ver `84` y `98`.

## Cómo medirlo con la calculadora

Corre el mismo producto dos veces, cambiando solo el cargo. Números **de ejemplo dentro del rango
oficial 8%-22%, verifica el tuyo** (`76`):

```
# Sin cuotas extra, cargo de ejemplo 15%
python scripts/margen_ml.py margen --precio 249000 --costo 140000 --comision 15 \
    --envio 8500 --iva 19

# Con cuotas extra: exactamente 3 puntos más, 18%
python scripts/margen_ml.py margen --precio 249000 --costo 140000 --comision 18 \
    --envio 8500 --iva 19
```

La diferencia de utilidad entre los dos informes, dividida por la utilidad del primero, es lo que
tienes que recuperar en volumen.

## Cómo hacer la prueba bien

```
□ Confirmé en el simulador logueado el % exacto de mi categoría, con y sin cuotas extra
□ La diferencia debe ser 3 puntos: si no lo es, mi dato está mal
□ Calculé el aumento de unidades necesario con d/(m−d)
□ Corrí 30 días en una modalidad, con todo lo demás igual
□ Cambié y corrí 30 días en la otra
□ Comparé UNIDADES y UTILIDAD TOTAL, no solo la tasa de conversión
□ No hice la prueba durante Hot Sale: ese mes no es comparable
```

## El error clásico

Activar cuotas extra en todo el catálogo porque "vende más", y pagar 3 puntos adicionales también
en los productos de $15.000 donde ningún comprador financia. El inverso también existe: quedarse
sin cuotas en una categoría de catálogo y no entender por qué la ficha comparativa siempre pone a
otro arriba (`63`).

## Relacionados

`76` el cargo por venta 8%-22% · `82` la calculadora de margen · `63` ganar el catálogo · `84` el
producto que no sirve para ML · `85` el ticket que aguanta ML · `91` descuentos y campañas · `98`
qué hacer con el SKU que no deja · `150` ACOS sano · `42` y `43` tipos de publicación
