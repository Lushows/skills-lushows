# Cuánto se gana de verdad

El margen en Mercado Libre es estructuralmente menor que en tienda propia, y aun así puede convenir.
Aquí están los números reales de Colombia — comisión oficial, tablas de envío oficiales — metidos en
ejemplos completos, para que dejes de estimar de cabeza.

## Los costos que sí están verificados

| Concepto | Cifra | Origen |
|---|---|---|
| Crear una publicación | **$0** | oficial ML Colombia, verificado sep-2026 |
| Comisión por venta | **8% a 22%** según categoría y cuotas | oficial, sep-2026 |
| Ofrecer cuotas extra | **+3 puntos porcentuales** | oficial, sep-2026 |
| Precio mínimo de publicación | **$2.900** | oficial, sep-2026 |
| Cargo fijo por venta de bajo valor | **No existe en Colombia** | oficial, sep-2026 |
| Umbral de envío gratis | **$60.000** | oficial, sep-2026 |
| Descuento de envío por reputación | 50% verde/MercadoLíder/**sin reputación** · 40% amarilla · 0% naranja o roja | oficial, sep-2026 |
| Tope de envío en productos baratos | Los de menos de $15.000 pagan **máximo la mitad del precio** | oficial, sep-2026 |
| Peso que se cobra | El mayor entre el físico y el volumétrico, **por unidad** | oficial, sep-2026 |
| El costo de envío | **Aplica a todas las ventas, incluso si el comprador paga el envío** | oficial, sep-2026 |

> ⚠️ **Sin verificar sin login (sep-2026):** la comisión **exacta de tu categoría**. Solo es público
> el rango 8%-22%. Léela en `mercadolibre.com.co/landing/costos-de-venta` o en el simulador de
> costos, estando logueado. La API `listing_prices` ya responde 403 y exige token. Ver `76`.

Los productos de la sección **Supermercado** pagan otros costos (oficial, sep-2026).

## Ejemplo completo A — un producto de $65.000

Supuestos: costo del producto $25.000, peso 1 kg, envío gratis, IVA 19%, comisión **15%** (supuesto
del punto medio del rango oficial — cámbialo por el tuyo), reputación **verde**.

| Línea | Valor |
|---|---|
| Precio publicado | $65.000 |
| − IVA (no es tuyo, es de la DIAN) | −$10.378 |
| − Comisión 15% (se cobra sobre el precio con IVA) | −$9.750 |
| − Envío (1 kg, producto >$60.000, verde) | −$8.200 |
| − Costo del producto | −$25.000 |
| **= Utilidad** | **$11.672 → 18,0% del precio** |

Ese 18% es antes de tu empaque, tu tiempo, tu devolución ocasional y cualquier pauta. Y con comisión
del 22% en vez del 15%, la utilidad cae a **$7.122 (11,0%)**. El rango 8%-22% no es un detalle: es
la diferencia entre un negocio y un pasatiempo.

## Ejemplo B — el mismo producto con el termómetro en naranja

Nada cambia salvo el color. Envío de 1 kg sobre $60.000: pasa de $8.200 a **$16.400**.

| | Verde | Naranja / roja |
|---|---|---|
| Utilidad por venta | **$11.672** | **$3.472** |
| % del precio | 18,0% | 5,3% |

**Perder el verde te borra el 70% de la utilidad, venta por venta.** Esa es la razón económica por
la que `04` frena todo hasta arreglar la reputación, y por la que en naranja o rojo no se optimiza:
se rescata (`128`, `144`).

Y el dato que sorprende: **un vendedor sin reputación todavía paga la misma tarifa que un verde**
(50% de descuento, oficial sep-2026). El castigo no es arrancar sin reputación — es perderla.

## Ejemplo C — el salto de los $60.000 (el que casi nadie ve)

Mismo producto, mismo costo de $25.000, 1 kg, verde, comisión 15%, envío gratis en los dos casos.
Lo único que cambia es si publicas a $59.900 o a $65.000.

| Línea | A $59.900 | A $65.000 | Diferencia |
|---|---|---|---|
| Precio | $59.900 | $65.000 | +$5.100 |
| IVA | −$9.564 | −$10.378 | +$814 |
| Comisión 15% | −$8.985 | −$9.750 | +$765 |
| Envío (1 kg) | −$4.300 | **−$8.200** | **+$3.900** |
| Costo | −$25.000 | −$25.000 | — |
| **Utilidad** | **$12.051** | **$11.672** | **−$379** |

Subiste el precio $5.100 y **ganaste $379 menos**. Porque cruzar el umbral de $60.000 casi duplica
el costo de envío ($4.300 → $8.200) y encima pagas más IVA y más comisión.

**Alrededor de $60.000 hay una zona muerta: subir el precio puede bajarte la utilidad.** Si vas a
cruzar ese umbral, crúzalo con decisión — no con $5.000 — o quédate debajo. La tabla completa de
envíos por peso y rango de precio está en `78`; el umbral, en `79`.

## Ejemplo D — por qué los productos baratos pierden

Producto de $10.000, costo $4.000, 1 kg, envío gratis, verde. Envío de tabla: $2.700.

| Comisión | Utilidad | % del precio |
|---|---|---|
| 15% | **$203** | 2,0% |
| 22% | **−$497** | **pierdes plata** |

Con un solo reclamo, una devolución o un empaque de $500, el negocio ya es negativo. Por eso la
regla operativa no es "bajar costos": es **subir el ticket** con kits y combos (`87`), que además es
lo que la propia ayuda oficial sugiere para productos por debajo del mínimo de $2.900. Desarrollo en
`85` y `86`.

## Por qué el margen aquí es menor que en tienda propia

| Costo | Tienda propia | Mercado Libre |
|---|---|---|
| Tráfico | CAC pagado por adelantado | $0 orgánico |
| Comisión por venta | $0 | **8%-22%** |
| Envío | Tú decides si lo subsidias | Aplica **aunque el comprador lo pague** |
| Devoluciones | Tu política | La de ML, más generosa que la tuya (`137`, `138`) |
| Recompra | Tuya (correo, WhatsApp) | De ML |

Son dos estructuras distintas, no una mejor que otra. En tienda propia pagas **antes** de vender y
te quedas con el cliente; en ML pagas **después** de vender y el cliente es de ML. El error es traer
el precio de un canal al otro sin rehacer el número (`08`, `170`).

## Lo que ML te da a cambio

- Demanda ya presente: ~8 millones de usuarios únicos y +80 millones de visitas mensuales en
  Colombia (oficial de la compañía, sep-2026).
- Cero costo fijo de arranque y cero CAC en orgánico.
- Pasarela, antifraude, logística y garantía resueltos.
- Un descuento del 50% en envíos desde el día uno, aunque no tengas historial.

Si tu producto se busca por nombre y aguanta la comisión, **ese tráfico gratis vale más que los
puntos de margen que pierdes**. Si no aguanta, ningún truco de ficha lo arregla (`84`).

## Cuántos meses toma

> ⚠️ **Sin verificar (sep-2026):** no existe dato público de cuánto tarda en promedio un vendedor
> colombiano en vivir de Mercado Libre. Desconfía de cualquier cifra de "ingresos promedio del
> vendedor": no se publica.

Lo que sí son pisos duros, oficiales:

| Hito | Requisito | Piso temporal |
|---|---|---|
| Tener reputación | **10 primeras ventas** | Depende de ti |
| Que el pasado caduque | 60 ventas → evaluación a 60 días (antes, 365) | Depende de ti |
| Entrar a Full | Reputación activa (10 ventas) y disponibilidad de espacio | — |
| **MercadoLíder** | 120 ventas en 60 días + $10.000.000 + verde | **más de 4 meses registrado** |

Haz tú la aritmética: MercadoLíder son **2 ventas diarias sostenidas** durante dos meses, con un
ticket promedio de ~$83.000 si vendes exactamente 120. Con ticket menor, necesitas más ventas. Y las
ventas con **publicación Gratuita no cuentan** (oficial, sep-2026). Ver `06` y `129`.

## Checklist antes de decir "esto es rentable"

```
□ Leí la comisión REAL de mi categoría en el simulador logueado, no un rango       (76)
□ Corrí scripts/margen_ml.py con esa comisión, no la estimé de cabeza              (82)
□ Resté el IVA: el precio publicado lo incluye y no es mío                         (81)
□ Busqué mi peso y mi rango de precio en la tabla oficial de envíos                (78)
□ Verifiqué si estoy encima o debajo de los $60.000 y qué pasa si cruzo            (79)
□ Calculé el mismo producto con termómetro naranja: ese es mi riesgo real          (125)
□ Sumé empaque, y una devolución cada N ventas                                     (95, 110)
□ Si voy a pautar, mi ACOS objetivo es MENOR que este margen                       (150)
```

## El error clásico

Mirar el depósito de Mercado Pago y creer que eso es la utilidad. Entra el dinero, la cuenta crece,
el negocio "funciona" — y tres meses después el inventario no cuadra porque cada venta perdía plata.
Mercado Libre no te avisa cuando vendes por debajo del costo: **el único que puede avisarte es el
cálculo, hecho antes de publicar.**

## Relacionados

`02` la trampa de los datos y el caso resuelto · `04` diagnóstico inicial ·
`06` ciclo de vida del vendedor nuevo · `08` ML vs otros canales · `75` estructura de costos de una
venta · `76` las comisiones y cómo verificarlas · `77` el precio mínimo de $2.900 · `78` el envío
que pagas tú · `79` el umbral de los $60.000 · `81` IVA y el precio que publicas ·
`82` la calculadora de margen · `83` el precio mínimo viable · `84` el producto que no sirve para
ML · `85` el ticket que aguanta ML · `86` por qué los productos baratos pierden · `87` kits ·
`95` el costo oculto de la devolución · `125` el termómetro · `129` MercadoLíder ·
`150` el ACOS sano según tu margen · `170` vender en ML y en tu tienda a la vez
