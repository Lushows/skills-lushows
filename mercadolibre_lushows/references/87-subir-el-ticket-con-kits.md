# Subir el ticket con kits

La salida al problema de `86`, y la que recomienda la propia ayuda oficial de Mercado Libre:
*"Puedes vender productos de menor valor **ofreciendo packs o combos**"* (oficial ML Colombia,
verificado sep-2026). Un kit bien armado cruza el umbral de $60.000, reparte un solo envío entre
varias unidades y te saca de la comparación directa de precio.

## Los cuatro efectos de un kit

| Efecto | Por qué pasa |
|---|---|
| **Un solo envío para varias unidades** | El costo de envío se calcula por unidad vendida; un kit es una unidad |
| **Cruza el umbral de $60.000** | Con la etiqueta de envío gratis y su exposición (`79`) |
| **Diluye el peso de los costos fijos** | El mismo alistamiento y empaque repartido entre 3 productos |
| **Rompe la comparación de precio** | Nadie tiene tu combinación exacta: sales del commodity (`89`) |

El primero es el más subestimado. Si vendes 3 unidades sueltas en 3 pedidos, pagas 3 envíos. Si
vendes un kit de 3, pagas uno.

**Un kit no es un descuento: es un envío repartido entre tres.**

## La aritmética del envío repartido

Producto de 350 g que vendes a $22.000. Reputación verde, tabla oficial (`78`):

| Formato | Precio | Peso | Envío oficial | Envío por unidad |
|---|---|---|---|---|
| 1 unidad suelta | $22.000 | 0,35 kg | $2.700 (col. $15.000-$29.999) | **$2.700** |
| Kit x3 | $63.000 | 1,05 kg | $8.500 (col. >$60.000, 1-2 kg) | **$2.833** |
| Kit x4 | $84.000 | 1,4 kg | $8.500 | **$2.125** |
| Kit x6 | $125.000 | 2,1 kg | $8.600 (2-3 kg) | **$1.433** |

Fíjate en el kit x3: **no mejora nada**. Cruzó el umbral, el envío saltó a $8.500, y el costo por
unidad quedó igual o peor. Es la zona muerta del `79` disfrazada de kit.

El kit x4 sí funciona, y el x6 reduce el envío por unidad casi a la mitad. **El kit tiene que
cruzar el umbral con holgura, no rozarlo.**

## La regla del kit que sí sirve

```
precio del kit ≥ $60.000 + (salto de envío de su peso) + margen de seguridad
```

Con el salto de $3.900-$4.000 típico de los pesos livianos (`79`), eso significa apuntar a
**$70.000 o más**. Debajo de $65.000 el kit no está pagando su propio escalón.

Segunda regla, sobre el peso: **vigila que el kit no salte de rango de peso**. Pasar de 2-3 kg
($8.600) a 3-4 kg ($10.100) cuesta $1.500; pasar de 5-7 kg ($10.500) a 7-10 kg ($15.200) cuesta
$4.700. Ese salto puede borrar el beneficio de agregar una unidad más.

| Rango de peso | Envío (>$60.000, verde) | Salto al siguiente |
|---|---|---|
| 1 a 2 kg | $8.500 | +$100 |
| 2 a 3 kg | $8.600 | **+$1.500** |
| 3 a 4 kg | $10.100 | +$100 |
| 4 a 5 kg | $10.200 | +$300 |
| 5 a 7 kg | $10.500 | **+$4.700** |
| 7 a 10 kg | $15.200 | **+$10.000** |

Arma tus kits **justo por debajo** de esos saltos: 2,9 kg es mucho mejor negocio que 3,1 kg, y
6,9 kg es muchísimo mejor que 7,1 kg.

## Los cinco tipos de kit

| Tipo | Ejemplo | Cuándo usarlo |
|---|---|---|
| **Por cantidad** | "Pack x6" de un consumible | Producto que se repone: filtros, cápsulas, repuestos |
| **Producto + complemento** | Cafetera + kilo de café | Sube el ticket y el valor percibido a la vez |
| **Set de uso** | Set de 5 utensilios de cocina | Cuando el comprador iba a comprar varios igual |
| **Producto + garantía/servicio** | Herramienta + estuche + garantía extendida | Categorías donde la certeza vale |
| **Surtido** | Caja con 4 sabores | Cuando el comprador no sabe cuál elegir |

El de cantidad es el más fácil y el que más margen recupera. El de complemento es el que mejor
defiende el precio, porque nadie puede compararlo uno a uno (`89`).

## Cómo armarlo bien en la publicación

```
□ El kit es UN ítem, con su propio SKU, no una variante del producto suelto
□ El título nombra el producto, la marca y la cantidad — sin "OFERTA" ni símbolos (ver 27)
□ La foto principal muestra el kit completo, fondo blanco, sin texto superpuesto
□ La descripción lista qué incluye, unidad por unidad
□ El precio del kit cruza $60.000 con holgura, no lo roza
□ El peso empacado del kit queda justo DEBAJO de un salto de rango
□ Corrí margen_ml.py con el peso y el precio del kit, no con los del producto suelto
□ Mantengo también el producto suelto publicado: sirve de ancla de precio (ver 88)
```

Ese último punto importa: el suelto a $22.000 hace que el kit x4 a $84.000 se lea como un buen
trato aunque no tenga descuento real.

## El descuento del kit: cuánto dar

La tentación es dar 15-20% por comprar el pack. Antes de darlo, calcula lo que ya ganaste:

En el ejemplo de arriba, el kit x4 ahorra $575 de envío por unidad ($2.700 → $2.125), o sea $2.300
en el pedido. Ese es tu presupuesto de descuento sin perder margen. Darle al comprador $2.000 de
rebaja sobre $88.000 (2,3%) ya es gratis para ti.

Corre los dos escenarios:

```
# Kit x4 sin descuento
python scripts/margen_ml.py margen --precio 88000 --costo 40000 --comision 15 \
    --envio 8500 --otros 1200 --iva 19

# Kit x4 con 10% de descuento
python scripts/margen_ml.py margen --precio 79200 --costo 40000 --comision 15 \
    --envio 8500 --otros 1200 --iva 19
```

Cargo **15% — ejemplo dentro del rango oficial 8%-22%, verifica el tuyo** (`76`).

## El carrito: el kit que arma el comprador

> *"Si vendes varios productos que juntos sumen **$60.000**, tu comprador tendrá envío gratis."*
> (oficial ML Colombia, verificado sep-2026)

Además, los productos en **Full** permiten agrupar artículos de **distintos vendedores** en un
carrito para alcanzar el mínimo. Traducción: aunque no armes kits, tener catálogo complementario y
estar en Full hace que el comprador arme el kit por ti. Ver `48` y el bloque `100`-`124`.

## El error clásico

Armar el kit x3 que queda en $63.000 y celebrar que "ya tiene envío gratis". Ese kit cruzó el
umbral, se comió el salto de $3.900 y no mejoró el margen por unidad. Es el mismo error del `79`,
solo que ahora con tres productos dentro.

El segundo: armar kits con productos que no se venden. Un kit no resucita inventario muerto, solo
lo esconde — y si está en Full, sigue pagando cargo mensual por unidad.

## Relacionados

`75` estructura de costos · `78` el envío que pagas tú · `79` el umbral de los $60.000 · `82` la
calculadora de margen · `85` el ticket que aguanta ML · `86` por qué los productos baratos pierden
· `88` precio psicológico · `89` la guerra de precios · `48` variaciones y productos
complementarios · `98` qué hacer con el SKU que no deja · `100` envíos y Full
