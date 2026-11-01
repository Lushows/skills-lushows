# Condición del producto

Nuevo, usado o reacondicionado. Es un campo de características, **no va en el título** —lo dice ML
Colombia con esas palabras— y define cosas duras: cuántos días tiene el comprador para devolver,
qué filtros te alcanzan y si puedes publicar gratis.

## La regla del título

> "Si tu producto es nuevo, usado o reacondicionado, **no lo incluyas en el título**"
> (oficial ML Colombia, verificado sep-2026).

La condición se declara en el campo correspondiente de la ficha y ML la muestra donde debe
mostrarse. Ponerla en el título es gastar caracteres y romper una regla (`29`).

## Las tres condiciones

| Condición | Qué significa | Valor en la API |
|---|---|---|
| Nuevo | Sin uso, sin abrir, en su empaque original | `"condition": "new"` |
| Usado | Ya tuvo uso, aunque sea poco | `"condition": "used"` |
| Reacondicionado | Se usó, se reparó o revisó y se dejó funcional | `"condition": "refurbished"` |

## La consecuencia grande: los plazos de devolución

| Condición | Plazo de devolución |
|---|---|
| **Nuevos** | **30 días corridos** |
| **Usados** | **14 días corridos** |
| Alimentos y bebidas (personas y mascotas) | **6 días corridos** |

(Confianza ALTA.) Son días **corridos**, no hábiles: cuentan sábados, domingos y festivos.

Ese plazo se suma a la Compra Protegida, que cubre "no llegó" hasta **21 días** desde la compra y
"arrepentimiento o problema" hasta **30 días** desde que el comprador lo recibió (ALTA, ver `138`).

**Declarar "nuevo" un producto usado te duplica la ventana de devolución y te deja expuesto a un
reclamo de "producto distinto al anunciado", que no es excluible de tu reputación** (ALTA, `136`).

## La otra consecuencia: publicar gratis

Los límites de la publicación Gratuita dependen de la condición (oficial ML Colombia, verificado
sep-2026):

| Condición | Ventas gratis permitidas |
|---|---|
| Usados | Hasta **20 ventas en un año** |
| Nuevos | Hasta **5 ventas en un año** |

Es coherente con para qué existe la Gratuita: sacar cosas de tu casa, no montar un negocio (`42`).

## Cómo se decide bien

| Caso | Condición correcta |
|---|---|
| Producto sellado, del proveedor | Nuevo |
| Producto de exhibición, sin uso pero abierto | Usado, y dilo en la descripción |
| Devolución de un cliente, sin uso, empaque abierto | Usado |
| Equipo revisado y reparado por técnico | Reacondicionado |
| Producto nuevo con la caja golpeada | Nuevo, y muestra la caja en foto (`36`) |
| Producto nuevo de un lote viejo | Nuevo, y declara la fecha si aplica |

Regla honesta: **si tienes que pensar mucho si es nuevo, no es nuevo.**

## Vender usado o reacondicionado sin generar reclamos

Estos productos venden bien si la expectativa está calibrada. La forma de calibrarla:

```
□ Declara la condición correcta en el campo, no en el título
□ Describe el estado con detalle en la descripción: qué funciona, qué está marcado
□ Fotografía los defectos, no los escondas: una foto por defecto (`36`)
□ Di qué NO incluye (caja original, cargador, manual) (`33`)
□ Si es reacondicionado, di quién lo revisó y qué se cambió
□ Declara la garantía real, aunque sea corta (`50`)
```

Mostrar el rayón vende. Esconderlo genera una devolución, un reclamo de calidad —que **sí** cuenta
para el termómetro (ALTA, `125`)— y una opinión mala.

## Cambiar la condición después

Cambiar de "nuevo" a "usado" en una publicación con ventas es una señal rara y cambia el marco
legal de lo ya vendido. Veredicto: **para un producto de otra condición, publicación aparte** (`41`).

## Lo legal

La condición del producto no suspende la garantía legal ni el derecho de retracto del Estatuto del
Consumidor: **Ley 1480 de 2011, 5 días hábiles de retracto en compras online** (ALTA, ver `22`).
Vender usado no te exime; cambia el alcance de lo que se espera del producto.

Para el tratamiento contable y tributario de la venta de usados, rutea a `contador_lushows`.

## El error clásico

Marcar "nuevo" porque "prácticamente está nuevo". El comprador recibe algo abierto, reclama
"producto distinto al anunciado", y ese reclamo no se puede excluir de tu reputación. Perder el
verde no es simbólico: con reputación naranja o roja pierdes el 50% de descuento en envíos y un
paquete de 1 kg de un producto de más de $60.000 te pasa de **$8.200 a $16.400** (oficial ML
Colombia, verificado sep-2026; ver `126`). **Mentir en la condición cuesta $8.200 por envío,
además de la venta.**

## Chequeo

```
□ La condición está en el campo, no en el título
□ Corresponde a la verdad, sin interpretaciones generosas
□ Si es usado o reacondicionado, la descripción detalla el estado
□ Hay foto de cada defecto relevante
□ Está declarado qué no incluye
□ La garantía declarada es la que realmente puedo cumplir (`50`)
□ Sé qué plazo de devolución me aplica: 30 / 14 / 6 días corridos
```

## Relacionados

`29` prohibiciones del título · `33` la descripción · `36` la secuencia de fotos · `41` estructura ·
`42` publicación gratuita · `50` garantía · `22` Estatuto del Consumidor · `23` garantía legal · `125` reputación ·
`126` qué cuesta perder el verde · `136` reclamos no excluibles · `138` devoluciones ·
tributario → `contador_lushows`
