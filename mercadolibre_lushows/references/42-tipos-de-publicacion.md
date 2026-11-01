# Tipos de publicación

En Colombia, Mercado Libre ya **no habla de "Clásica" y "Premium"**. Hoy el sitio colombiano
organiza las publicaciones por otra cosa: si son **Gratuitas**, y cuántas **cuotas con 0% interés**
ofreces. Esa segunda decisión es la que mueve tu comisión.

## Primero, la nomenclatura

| Nombre | Estado en Colombia |
|---|---|
| Gratuita | **Vigente**, con reglas publicadas |
| Publicación con cuotas con 0% interés | **Vigente**: es la opción de pago normal |
| Cuotas extra | **Vigente**: más cuotas, más comisión |
| "Clásica" / "Premium" | **Nombre viejo.** Sigue vigente en otros países de la región |

Si lees un blog que habla de Clásica y Premium, o es antiguo o es de Argentina o México. Traduce:
"Clásica" ≈ publicación con las cuotas base; "Premium" ≈ publicación con cuotas extra.

## Lo que cuesta vender

> "Crear una publicación no tiene costo. Cuando concretes la venta, pagarás **entre 8% y 22%**
> según la categoría de tu producto y la cantidad de cuotas que elijas ofrecer"
> (oficial ML Colombia, verificado sep-2026).

| Precio del producto | Cuotas con 0% interés | Cargo por venta |
|---|---|---|
| Menos de $499.999 | Hasta 3 cuotas | **8% a 19%** |
| Menos de $499.999 | Cuotas extra – hasta 6 | **11% a 22%** |
| $500.000 a $1.499.999 | Hasta 6 cuotas | **8% a 19%** |
| $500.000 a $1.499.999 | Cuotas extra – hasta 9 | **11% a 22%** |
| Más de $1.500.000 | Hasta 12 cuotas | **8% a 19%** |

(oficial ML Colombia, verificado sep-2026.)

**Ofrecer cuotas extra cuesta exactamente 3 puntos porcentuales más.** Ese es el dato duro, y
reemplaza al viejo "Premium cuesta unos 4 puntos más que Clásica".

Dos reglas más de la misma página:

> "El precio de tu producto debe ser **igual o superior a $2.900**. Esto te permitirá cubrir las
> tarifas de venta. Puedes vender productos de menor valor ofreciendo packs o combos."

> "Los productos de la sección **Supermercado** pagan otros costos."

## La publicación Gratuita: reglas oficiales

| Regla | Valor |
|---|---|
| Duración | **60 días** |
| Exposición | **Baja** en el listado |
| Cuotas con 0% interés | **No ofrece** |
| Usados | Gratis hasta **20 ventas en un año** |
| Nuevos | Gratis hasta **5 ventas en un año** |
| Publicaciones simultáneas | Máximo **10** |
| Stock por publicación | Máximo **1 unidad** |
| Quién NO puede usarla | **MercadoLíder o usuario profesional de Mercado Pago** |

(oficial ML Colombia, verificado sep-2026.)

Y un detalle que casi nadie conecta: para calificar a MercadoLíder, "**no se tienen en cuenta las
ventas con publicación Gratuita**" (oficial ML Colombia, verificado sep-2026; ver `129`). O sea,
vender gratis no te construye carrera.

## Qué te da cada camino

| | Gratuita | Con cuotas 0% (base) | Con cuotas extra |
|---|---|---|---|
| Costo por venta | $0 | 8%-19% | 11%-22% |
| Duración | 60 días | Indefinida | Indefinida |
| Exposición | Baja | Normal | Normal |
| Cuotas sin interés para el comprador | No | Sí, hasta 3/6/12 según precio | Más cuotas |
| Stock permitido | 1 unidad | Libre | Libre |
| Suma para MercadoLíder | **No** | Sí | Sí |
| Límite anual de ventas | 5 nuevos / 20 usados | Ninguno | Ninguno |

## Para qué sirve de verdad la Gratuita

No es una versión económica del negocio: es una **rampa de prueba**.

| Uso legítimo | Comentario |
|---|---|
| Sacar cosas usadas de tu casa | Es su caso natural: 20 ventas al año |
| Probar si un producto tiene demanda | Con exposición baja, la prueba es conservadora |
| Llegar a las primeras ventas | Pero ojo: no suman para MercadoLíder |

| Uso equivocado | Por qué |
|---|---|
| Montar un catálogo de 10 productos gratis | Stock de 1 unidad y exposición baja: no es un negocio |
| Evitar la comisión | Se acaba a las 5 ventas de productos nuevos |
| Escalar | Si llegas a MercadoLíder, ML te la quita |

**La Gratuita no es barata: es limitada. Se acaba justo cuando empiezas a vender.**

## La decisión que sí importa

En la práctica, salvo que estés vendiendo usados de tu casa, el tipo de publicación se reduce a una
sola pregunta: **¿ofrezco cuotas extra y pago 3 puntos más?** Esa comparación, con el margen en la
mano, está en `43`.

## Lo que no es público

> ⚠️ **Sin verificar para Colombia (sep-2026).** La comisión exacta **por categoría** no es
> pública: solo el rango 8%-22%. El detalle está tras login en el simulador de costos del panel,
> y la API `GET /sites/MCO/listing_prices` **ya no responde sin token** (devuelve
> `403 PA_UNAUTHORIZED_RESULT_FROM_POLICIES`). Léela logueada antes de fijar cualquier precio.

## El error clásico

Elegir el tipo de publicación al final del formulario, con afán, sin haber calculado el margen. Tres
puntos porcentuales sobre un producto con 20% de margen bruto son el 15% de tu utilidad, venta tras
venta, para siempre. **El tipo de publicación no es una casilla: es una decisión de margen.**

## Relacionados

`43` cuál tipo te conviene · `41` estructura de publicaciones · `48` kits y combos · `63` ganar el
catálogo · `75` costos de vender · `76` leer tu comisión real · `77` el piso de $2.900 · `82`
margen real · `129` MercadoLíder · cálculos exactos → `Matematicas_lushows`
