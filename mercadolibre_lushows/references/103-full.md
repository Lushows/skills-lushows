# Full: tu inventario en la bodega de Mercado Libre

Full es el fulfillment de ML: le mandas producto por adelantado, ellos lo guardan, y cuando
alguien compra, ellos empacan y despachan. Los beneficios oficiales son **50% de descuento en los
costos de envío gratis desde $60.000** y **entrega al día siguiente** (oficial ML Colombia,
verificado sep-2026). El costo es control, almacenamiento y un cargo por stock antiguo que es
brutal.

## Los requisitos oficiales

> "Tener reputación como vendedor. Se activa al completar tus **primeras 10 ventas**."
> "Vender productos **aptos para Full** y dentro de las **dimensiones permitidas**."
> "La activación de Full para nuevos vendedores está sujeta a la **disponibilidad de espacio** en
> nuestros centros de distribución."
> "El **traslado corre por tu cuenta**."
> (oficial ML Colombia, verificado sep-2026)

Dos consecuencias que la gente no ve:

1. **Puedes cumplir todo y aun así no entrar**, porque no hay espacio. No es un error tuyo.
2. **El flete hasta la bodega lo pagas tú**, en cada reposición. Ese costo va dentro del costo por
unidad, no aparte. Ver `106`.

## Qué resuelve

| Beneficio | Estado |
|---|---|
| 50% de descuento en envío gratis desde $60.000 | Oficial ML Colombia, verificado sep-2026 |
| Entrega al día siguiente | Oficial ML Colombia, verificado sep-2026 |
| Mejor posición: la logística es pilar del ranking | Verificado como pilar, sin peso publicado |
| Peso en el desempate del catálogo | Verificado (`63`) |
| **Agrupación de carrito entre vendedores distintos** | Verificado |
| Tú dejas de empacar y despachar | Consecuencia directa |

La quinta fila es la subestimada. Los productos Full permiten agrupar artículos de **distintos
vendedores** en un carrito para alcanzar el mínimo de envío gratis. Tu producto de $18.000 puede
viajar gratis porque otra persona completó $60.000 comprándole a alguien más. Fuera de Full,
dependes de que el comprador arme carrito contigo solo. Para tickets bajos, eso solo puede
justificar Full.

## Dónde está la bodega

> El centro de fulfillment de Full en Colombia estaría en **Funza, Cundinamarca**.
> ⚠️ **Una sola fuente, sin confirmación oficial (sep-2026).** Confírmalo al generar tu primer
> envío a bodega: la dirección de destino real aparece ahí.

Si es cierto, tiene una consecuencia planeable: como el traslado es por tu cuenta, **el costo de
entrar a Full depende de qué tan lejos estés de la Sabana de Bogotá.** Un vendedor en Bogotá paga
flete urbano; uno en Pasto paga flete nacional en cada reposición.

## Qué te cuesta

**1. Control.** El inventario sale de tu mano. No puedes sacar dos unidades para una venta por
WhatsApp ni revisar si llegó fallado. Si vendes en dos canales, ese stock no te sirve para el otro
(`123`).

**2. Almacenamiento.** Corre todos los días. Ver `107`.

**3. Stock antiguo.** Este es el que mata. Cargo **mensual por unidad**, desde los **4 meses** (o
**2 meses** en Supermercado), oficial ML Colombia, verificado sep-2026:

| Tamaño | 4 a 6 meses | 6 a 12 meses | Más de 12 meses |
|---|---|---|---|
| Pequeño | $690 | $6.500 | $13.100 |
| Mediano | $1.100 | $16.200 | $29.200 |
| Grande | $3.600 | $64.100 | $110.000 |
| Extragrande | $9.600 | $117.700 | $149.900 |

**Un producto grande olvidado un año en Full cuesta $110.000 por unidad.** No es una multa
proporcional: es exponencial. Detalle, tabla de Supermercado y plan de salida en `108`.

## Qué cambia en tu reputación

Full mueve el riesgo, no lo elimina.

| Riesgo | Sin Full | Con Full |
|---|---|---|
| Despacho con demora | Tuyo, todos los días | De ML, una vez el stock está adentro |
| Producto incompleto o defectuoso | Tuyo | **Sigue siendo tuyo**: tú mandaste eso a bodega |
| Quedarte sin stock | Tuyo, repones en horas | **Peor**: reponer toma días |
| Error en el ingreso a bodega | No existe | Riesgo nuevo, ver `106` |

Los únicos reclamos que cuentan contra tu reputación son los de **producto incompleto/faltante** y
de **calidad** (oficial). Full no te protege de ninguno de los dos: si mandaste un lote
defectuoso, los reclamos llegan en serie y ya no puedes revisar unidad por unidad.

## El riesgo del quiebre de stock

- Con `available_quantity: 0` el ítem pasa a `paused` con sub-estado `out_of_stock` (verificado).
- Sale de la competencia y de la puja de catálogo.
- Al reponer, revive con menos señales y debe reconstruirlas.
- Si tenías pauta, reinicia el aprendizaje y encarece la pauta futura.

Con inventario propio repones en horas. Con Full repones en días: preparar, trasladar (pagando
tú), que reciban, que ingresen. **Full convierte un error de planeación en una semana sin
publicación.**

## La pregunta correcta antes de entrar

```
□ ¿Cuántas unidades de ESTE SKU vendo al mes, con datos reales?
□ ¿Cuántos días va a estar cada unidad parada? (si pasa de 120, mira la tabla de arriba)
□ ¿Cuánto me cuesta el traslado hasta la bodega, y cada cuánto tendría que hacerlo?
□ ¿Ya tengo las 10 ventas que activan la reputación, que es requisito?
□ ¿Mi producto está dentro de las dimensiones permitidas?
□ ¿Tengo capital para tener inventario inmovilizado?
□ ¿Qué pasa con mi otro canal si el stock está allá? (`123`)
```

Tabla de decisión completa en `105`.

## Comprar espacio

> Existe un cargo por unidad para comprar espacio adicional en Full, pero ML dice que
> "la tarifa por unidad puede variar según la demanda".
> ⚠️ **Sin cifra publicada (sep-2026).** Consúltala en el panel de Full en el momento en que la
> necesites; no la planees con un número de blog.

## El error clásico

Mandar el catálogo entero en el primer envío, incluyendo los productos que "van a despegar". Los
que no despegan llegan a los 6 meses y pasan de $690 a **$6.500 por unidad** si son pequeños, o de
$3.600 a **$64.100** si son grandes. Esa factura se come la ganancia de los que sí vendieron.

**Full se prueba con dos o tres SKUs de rotación comprobada, nunca con todo el inventario.**

## Relacionados

`100` tarifas oficiales de envío · `101` modalidades · `102` Flex · `104` colecta y puntos · `105`
cuándo conviene Full y cuándo no · `106` ingresar inventario · `107` costo de almacenamiento ·
`108` inventario viejo · `116` productos grandes · `123` inventario en dos canales · `124`
auditoría mensual · `63` ganar el catálogo · `75` el cálculo del margen · `126` las tres métricas
