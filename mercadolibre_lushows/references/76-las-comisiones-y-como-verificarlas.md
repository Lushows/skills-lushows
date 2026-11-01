# Las comisiones y cómo verificarlas

Mercado Libre Colombia sí publica el rango: **entre 8% y 22%** del precio, según la categoría y la
cantidad de cuotas que ofrezcas. Lo que no publica abiertamente es el número exacto de TU
categoría. Este módulo trae la tabla oficial, la regla de los 3 puntos, y cómo conseguir tu dato
real sin caer en las cifras argentinas que circulan.

## El dato oficial

> *"Crear una publicación no tiene costo. Cuando concretes la venta, pagarás **entre 8% y 22%**
> según la categoría de tu producto y la cantidad de cuotas que elijas ofrecer."*
> (oficial ML Colombia, verificado sep-2026)

| Precio del producto | Cuotas con 0% interés | Cargo por venta |
|---|---|---|
| Menos de $499.999 | Hasta 3 cuotas | **8% a 19%** |
| Menos de $499.999 | Cuotas extra – hasta 6 | **11% a 22%** |
| $500.000 a $1.499.999 | Hasta 6 cuotas | **8% a 19%** |
| $500.000 a $1.499.999 | Cuotas extra – hasta 9 | **11% a 22%** |
| Más de $1.500.000 | Hasta 12 cuotas | **8% a 19%** |

Todo oficial ML Colombia, verificado sep-2026.

Lee la tabla despacio, porque dice tres cosas:

1. **El rango base es 8%-19%.** Dónde caes dentro de él lo decide tu categoría.
2. **Ofrecer cuotas extra cuesta exactamente 3 puntos porcentuales más.** 8-19% pasa a 11-22%. Es
   una resta limpia, no una estimación. Ver `80`.
3. **Cuantas más cuotas permite tu rango de precio, más caro es el producto.** Sobre $1.500.000 ya
   tienes 12 cuotas sin pagar el recargo: no hay opción de "cuotas extra" en ese rango.

Dos notas oficiales más:

- *"El precio de tu producto debe ser **igual o superior a $2.900**."* Ver `77`.
- *"Los productos de la sección **Supermercado** pagan otros costos."* Si vendes ahí, esta tabla
  no es la tuya.

**El rango 8%-22% es público; tu número exacto vive detrás de tu login. Todo lo demás que
encuentres en internet es de otro país.**

## Cómo funciona el mecanismo

El cargo depende de tres variables:

| Variable | Qué cambia |
|---|---|
| **País** (site) | MCO ≠ MLA ≠ MLM. Números totalmente distintos |
| **Categoría** | Decide dónde caes dentro del 8%-19% |
| **Cuotas que ofreces** | Cuotas extra = +3 puntos exactos |

Y sobre eso: **se cobra sobre el precio publicado con IVA**, no sobre la base (`81`), y solo cuando
vendes. Publicar no cuesta.

## Los tres métodos para conseguir TU número

### 1. El simulador de costos, logueado (el único definitivo)

El detalle por categoría está en `/landing/costos-de-venta` y en el simulador de costos, **tras
login**. Es la única fuente que combina tu cuenta, tu categoría y tu configuración de cuotas.

```
□ Entra logueado a mercadolibre.com.co
□ Busca el simulador de costos de venta (el buscador interno ayuda:
    mercadolibre.com.co/ayuda/search?q=costos)
□ Escoge la categoría EXACTA: la hoja final, no la categoría padre
□ Pon un precio real de los que vas a publicar
□ Anota el porcentaje Y el monto en pesos
□ Repite con y sin cuotas extra: la diferencia debe ser 3 puntos
□ Anota la fecha. Esto cambia y tu hoja no se entera sola (ver 99)
```

### 2. Al crear la publicación (el más honesto)

Al elegir el tipo de publicación, ML te muestra el costo de cada opción **para ese producto, en esa
categoría, a ese precio**. Es el número que de verdad te van a cobrar. Captura la pantalla.

### 3. El desglose de una venta real (el irrefutable)

Si ya vendiste, el detalle de la venta muestra exactamente qué te descontaron. Nada le gana. Úsalo
para auditar lo que creías que ibas a pagar.

### Lo que YA NO sirve: la API abierta

> ⚠️ **Cambió en 2026.** `GET https://api.mercadolibre.com/sites/MCO/listing_prices?price=50000`
> **ya no es pública**: responde `403 PA_UNAUTHORIZED_RESULT_FROM_POLICIES` y exige token OAuth.
> Si tienes app autenticada la puedes seguir usando con token (ver bloque `175`-`199`); si no, tu
> vía es el simulador logueado.

Otra trampa operativa: **las URLs viejas del centro de ayuda no dan 404, redirigen a una página
equivocada** (`/ayuda/1064`, sobre hackeo de dispositivos). Slugs muertos conocidos:
`costos-de-vender_1265`, `tipos-de-publicacion_1285`, `reputacion-vendedor_1622`. Para encontrar un
artículo, usa el buscador interno: `mercadolibre.com.co/ayuda/search?q=`

## La trampa argentina, explícita

Circula masivamente esto: *"desde el 1-sep-2026, los ítems bajo $33.000 pagan un cargo fijo de
$1.330 / $2.740 / $3.320 según rango"*. **Es Argentina, en pesos argentinos.** Fuentes: Página/12,
iProfesional, iProUp. Los buscadores lo devuelven mezclado cuando preguntas por Colombia, porque el
signo `$` es el mismo. **En Colombia no hay cargo fijo por venta de bajo valor** (`77`).

Cómo detectar una cifra contaminada antes de usarla:

```
□ ¿La fuente dice explícitamente "Colombia" o "MCO"? Si no, sospecha
□ ¿El monto tiene sentido en pesos colombianos?
□ ¿Cita una URL de mercadolibre.com.co, o de .com.ar / .com.mx?
□ ¿Habla de "Clásica y Premium"? Esa nomenclatura ya no es la colombiana (ver 80)
□ ¿Menciona un cargo fijo en COP? En Colombia no existe. Es Argentina
□ Ante la duda: simulador logueado. Siempre gana el panel
```

## Cómo usarlo en la calculadora

`margen_ml.py` recibe el porcentaje en `--comision`. Mientras no tengas el tuyo, corre los
extremos del rango oficial y mira si el producto aguanta el peor caso:

```
# Mejor caso del rango oficial
python scripts/margen_ml.py margen --precio 89900 --costo 42000 --comision 8 --envio 8200 --iva 19

# Peor caso sin cuotas extra
python scripts/margen_ml.py margen --precio 89900 --costo 42000 --comision 19 --envio 8200 --iva 19

# Peor caso con cuotas extra
python scripts/margen_ml.py margen --precio 89900 --costo 42000 --comision 22 --envio 8200 --iva 19
```

Si el producto sobrevive al 22%, sobrevive a cualquier categoría. Si solo sobrevive al 8%, estás
apostando a caer en la categoría más barata del marketplace. Ver `82` y `84`.

## El error clásico

Calcular con "la comisión promedio de Mercado Libre" (ese número no existe: el rango oficial es de
14 puntos de ancho) y descubrir al tercer mes que tu categoría es de las caras. El segundo:
activar cuotas extra sin recalcular, y pagar 3 puntos adicionales en **todo** el catálogo,
incluidos los productos de $15.000 donde nadie financia (`80`).

## Relacionados

`75` estructura de costos · `77` el mínimo de $2.900 y la trampa del cargo fijo · `78` el envío que
pagas tú · `80` cuotas: quién las paga · `81` IVA y el precio que publicas · `82` la calculadora de
margen · `83` precio mínimo viable · `86` por qué los productos baratos pierden · `97` margen por
SKU · `99` revisión mensual
