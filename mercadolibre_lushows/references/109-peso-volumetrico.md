# Peso volumétrico

Te cobran el envío por lo que **ocupa** el paquete cuando eso es más que lo que pesa. ML lo dice
literalmente: **"Comparamos el peso físico con el volumétrico y usamos siempre el valor más
alto"**, y **"el costo se calcula por unidad"** (oficial ML Colombia, verificado sep-2026).

## La lógica

Un camión se llena por espacio antes que por peso. Por eso la logística cobra el mayor de dos
números:

```
PESO REAL         = lo que marca la balanza, en kg
PESO VOLUMÉTRICO  = (largo × ancho × alto en cm) ÷ DIVISOR

PESO FACTURABLE   = el MAYOR de los dos     ← confirmado oficialmente por ML Colombia
```

> ⚠️ **Sin verificar para Colombia (sep-2026).** Lo que ML **no** publica es el **divisor** que usa
> para convertir centímetros cúbicos a kilos. Los divisores que circulan (5000, 4000, 6000) son de
> transportadoras internacionales, no necesariamente el de Mercado Envíos MCO.
>
> Cómo deducirlo tú mismo, empíricamente:
> 1. Toma un envío real de un producto **grande y liviano** ya despachado.
> 2. `GET /shipments/$SHIPMENT_ID/costs` → mira qué rango de peso te cobraron.
> 3. Compara contra la tabla oficial de `100` y despeja el peso facturable que te aplicaron.
> 4. Con dos o tres casos, deduces el escalón real.
>
> La API `GET /sites/MCO/listing_prices` **ya no es pública**: hoy devuelve
> `403 PA_UNAUTHORIZED_RESULT_FROM_POLICIES` y exige token. El simulador logueado sí sirve.

## "Por unidad": la frase que cuesta plata

El costo se calcula **por unidad** (oficial). Si el comprador lleva tres unidades del mismo
producto, no pagas un envío: pagas el costo por cada unidad. Esto cambia dos decisiones:

| Decisión | Implicación |
|---|---|
| Publicar packs de 3 como un solo SKU | Un producto = un costo, en vez de tres |
| Precio por cantidad / combos | Revisa si te conviene armar el pack como ítem único |
| Cruzar los $60.000 con cantidad | Envío gratis para el comprador, pero pagas por unidad |

**Si vendes barato y por cantidad, armar el pack como un solo producto puede ser la decisión
logística más rentable del mes.**

## Dónde te muerde el volumen

| Producto | ¿Volumen o peso? | Riesgo |
|---|---|---|
| Ropa, cojines, peluches, edredones | Volumen | Alto |
| Vasos, cajas de regalo, organizadores | Volumen | Alto |
| Lámparas, decoración, cosas huecas | Volumen | Muy alto |
| Herramientas, repuestos, pesas | Peso real | Bajo |
| Libros, cosméticos, electrónica pequeña | Peso real | Bajo |
| Cualquier cosa con mucho relleno protector | Volumen | El relleno te lo cobran |

La última fila es la trampa de los frágiles: proteges bien, la caja crece, y la protección te
cuesta dos veces — el material y el flete. Ver `117`.

## Lo que se gana al bajar de escalón

Con la tabla oficial de `100` (verde, producto de más de $60.000), los saltos reales:

| Peso facturable | Costo | Salto contra el anterior |
|---|---|---|
| Hasta 0,3 kg | $8.000 | — |
| 0,5 a 1 kg | $8.200 | +$200 |
| 1 a 2 kg | $8.500 | +$300 |
| 3 a 4 kg | $10.100 | **+$1.500** |
| 7 a 10 kg | $15.200 | **+$4.700** |
| 10 a 20 kg | $25.200 | **+$10.000** |

Entre 2-3 kg y 3-4 kg hay un salto de $1.500 por venta. Con 200 ventas al mes son **$300.000
mensuales** que dependen de si tu caja factura 2,9 kg o 3,1 kg. Eso es lo que está en juego en
`110`.

En productos baratos el efecto es mucho menor: de 0,3 kg a 10-20 kg, en el rango de $0-$14.999,
vas de $2.500 a $3.400. **El volumen castiga sobre todo a los productos caros.**

## Cómo medir bien

Se mide **el paquete listo para despachar**, no el producto.

```
□ Mide con el producto YA empacado: caja cerrada, relleno adentro, cinta puesta
□ Mide el punto más ancho: si la caja se abomba, cuenta la parte abombada
□ Redondea hacia arriba al centímetro
□ Pesa en balanza digital, con el paquete final
□ Anota las tres medidas y el peso en tu ficha interna de cada SKU
□ Vuelve a medir si cambias de caja o de proveedor de empaque
□ Compara contra los escalones de tamaño de Full: 15×20×20 / 19×35×38 / 60×70×80 cm (`107`)
```

El penúltimo punto atrapa un error caro: cambias de caja porque estaba en oferta, la nueva es dos
centímetros más alta, y saltas de escalón en todas tus ventas del mes.

El último conecta dos costos: las mismas medidas deciden tu tarifa de envío **y** tu escalón de
cargo por stock antiguo en Full. Una caja que cruza de mediano a grande te sube el cargo de los
6-12 meses de $16.200 a **$64.100 por unidad** (oficial). Empacar apretado paga dos veces.

## Los atributos de la publicación

Los atributos de peso y dimensiones alimentan la cotización y los filtros. Mal declarados:

- Cotizas por debajo y la diferencia sale de tu bolsillo.
- O cotizas por encima, tu envío se ve más caro que el del competidor, y pierdes la venta.

Los atributos obligatorios dependen de la categoría; en la API traen `tags.required: true`
(verificado). Flujo: `GET /sites/MCO/domain_discovery/search?q=...` → `category_id` → `GET
/categories/$CATEGORY_ID/attributes`. Detalle en `182` y `180`.

## El error clásico

Cotizar el envío con el peso del producto en la mano, sin caja. El vendedor pesa el artículo, ve
600 gramos, y después el paquete real factura como 3 kilos. Con producto de más de $60.000 eso es
la diferencia entre $8.200 y $10.100 por venta.

**El envío no se cotiza sobre el producto: se cotiza sobre el paquete cerrado, con el mayor entre
peso y volumen.**

## Relacionados

`100` tarifas oficiales de envío · `110` empacar sin perder plata · `111` embalaje que evita
reclamos · `116` productos grandes · `117` frágiles · `107` costo de almacenamiento · `103` Full ·
`122` logística propia · `124` auditoría mensual · `182` descubrir atributos · `79` el umbral del
envío gratis · `75` el cálculo del margen
