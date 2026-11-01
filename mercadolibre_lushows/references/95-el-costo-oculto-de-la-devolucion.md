# El costo oculto de la devolución

Una devolución no cuesta "el producto": cuesta el producto, los dos envíos, el tiempo de gestión y
la venta que ya no vas a hacer con esa unidad. En un negocio de margen 15%, **una devolución se
come el margen de seis o siete ventas buenas**. Este módulo hace la cuenta y trae los plazos
oficiales.

## Los plazos oficiales

| Tipo de producto | Plazo de devolución |
|---|---|
| **Nuevos** | **30 días corridos** |
| **Usados** | **14 días corridos** |
| **Alimentos y bebidas** (personas y mascotas) | **6 días corridos** |

Oficial ML Colombia, confianza ALTA.

Y la cobertura de Compra Protegida, que es distinta:

| Situación | Cobertura |
|---|---|
| El producto no llegó | Hasta **21 días** desde la compra (o desde que termina la fabricación) |
| Arrepentimiento o problema con el producto | Hasta **30 días** desde que lo recibió |
| Qué reembolsa | Valor del producto **+ gastos de envío** si fue con Mercado Envíos |
| Qué NO reembolsa | Garantías o seguros adicionales |
| Procesamiento del reembolso | ~5 días hábiles tras llegar el paquete a instalaciones de ML |

Aparte y por encima de todo esto está la **Ley 1480 de 2011**, que da **5 días hábiles de
retracto** en compras online (`92`).

## El conflicto activo: ¿quién paga la devolución por arrepentimiento?

> ⚠️ **Conflicto sin resolver (sep-2026).** La página oficial vigente de Mercado Libre Colombia
> dice que el comprador *"puede devolver gratis **sin importar el motivo**"*. Pero prensa del
> **28-mar-2026** afirma que ML impondría un **cargo obligatorio por devolución de arrepentimiento
> en Colombia**. Las dos cosas no pueden ser ciertas a la vez.
> **Verifícalo en vivo en tu panel**, en el detalle de una devolución real, antes de construir tu
> política de precios sobre ello.

Referencia de otro país, que **no aplica a Colombia**: México ya eliminó las devoluciones gratis
por arrepentimiento en electrónica, celulares y cómputo, con un cargo de ~150-300 MXN. Es el camino
que la región parece estar tomando, pero mientras no lo veas en tu panel colombiano, **calcula como
si la devolución la pagaras tú**. Es el supuesto conservador y el que no te sorprende.

## Cuántas ventas se come una devolución

La fórmula:

```
ventas necesarias para compensar = costo total de la devolución ÷ utilidad por venta
```

Producto de 1 kg a $89.900, costo $42.000, cargo 15% (**ejemplo dentro del rango oficial 8%-22%**,
`76`), envío $8.200, IVA 19%. Utilidad por venta: unos **$11.500**.

Costo de una devolución en el escenario conservador:

| Concepto | Valor |
|---|---|
| Envío de ida (ya pagado) | $8.200 |
| Envío de retorno | $8.200 |
| Producto que vuelve dañado, abierto o incompleto | $0 a $42.000 |
| Tiempo de gestión (revisar, reacondicionar, republicar) | $5.000 estimado |
| **Total si el producto se recupera intacto** | **$21.400** |
| **Total si el producto se pierde** | **$63.400** |

| Escenario | Ventas que se come |
|---|---|
| Producto recuperado intacto | **1,9 ventas** |
| Producto recuperado pero no revendible como nuevo | ~3,5 ventas |
| Producto perdido o destruido | **5,5 ventas** |

Y ese cálculo es con margen 12,8%. Con margen 8%, el producto perdido se come **más de 9 ventas**.

**Una devolución no te quita una venta: te quita entre dos y nueve, según tu margen.**

## Cómo meterla en el precio

La forma correcta es cargar la tasa esperada de devolución al costo, no descubrirla al cierre de
mes:

```
costo ajustado = costo + (tasa de devolución × costo total de una devolución)
```

Con 5% de devoluciones y $21.400 por devolución: `$42.000 + (0,05 × $21.400) = $43.070`. Con 15%
de devoluciones: `$42.000 + $3.210 = $45.210`.

```
# Sin ajustar por devoluciones
python scripts/margen_ml.py margen --precio 89900 --costo 42000 --comision 15 \
    --envio 8200 --iva 19

# Ajustado por 15% de devoluciones
python scripts/margen_ml.py margen --precio 89900 --costo 45210 --comision 15 \
    --envio 8200 --iva 19
```

Corre los dos. La diferencia de veredicto es lo que te está costando no medir las devoluciones.

## Tasas esperadas por tipo de producto

| Tipo de producto | Tasa típica esperada | Qué la causa |
|---|---|---|
| Consumibles, repuestos con referencia clara | Baja | Poca ambigüedad |
| Hogar, herramientas | Media-baja | Expectativa de tamaño |
| Electrónica | Media | Compatibilidad, defectos |
| Moda con tallas | **Alta** | La talla es el motivo #1 de devolución |
| Productos con compatibilidad (repuestos, accesorios) | **Alta** | "No me sirvió para mi modelo" |

No hay cifras oficiales de ML Colombia por categoría. **Mide la tuya**: divide devoluciones entre
ventas de los últimos 90 días, por SKU. Ese es el único número que sirve.

## Las cinco formas de bajar la tasa

Ordenadas por efecto:

| # | Acción | Por qué funciona |
|---|---|---|
| 1 | **Atributos y ficha completos** | La mitad de las devoluciones son expectativa mal fijada (`25`-`54`) |
| 2 | **Fotos que muestren escala y detalle real** | Lo que se ve es lo que se espera |
| 3 | **Tabla de tallas o de compatibilidad en la descripción** | Ataca los dos motivos más frecuentes |
| 4 | **Video de hasta 60 segundos** (gratis, oficial) | Muestra el producto en uso |
| 5 | **Empaque que proteja de verdad** | La rotura genera reclamo NO excluible (`96`) |

## La devolución NO es una cancelación

Distinción oficial que importa mucho para la reputación:

> Venta cancelada = *"el comprador recibe su dinero de vuelta **antes** de que hayas entregado el
> producto"*. **Las devoluciones NO son cancelaciones.**

Y las cancelaciones tienen umbral duro: no cancelar más del **2,5%** a 60 días para mantener el
verde; superar el **2,5%** de ventas canceladas puede llevar a **suspensión de la cuenta**.

Además, **los reclamos por arrepentimiento del comprador no cuentan** para la reputación (oficial).
Una devolución por arrepentimiento te cuesta plata, pero no te cuesta el termómetro — y el
termómetro es el que decide si tu envío cuesta $8.200 o $16.400 (`78`).

## Lista de chequeo

```
□ Mido mi tasa de devolución por SKU, no en promedio
□ Metí el costo esperado de devolución dentro del --costo en margen_ml.py
□ Verifiqué en el panel quién paga hoy la devolución por arrepentimiento en Colombia
□ Los SKUs con tasa sobre 15% tienen ficha reforzada o están en revisión (ver 98)
□ Mis productos de moda tienen tabla de tallas
□ Mis repuestos tienen lista de compatibilidad explícita
□ Reviso el estado del producto devuelto antes de darlo por revendible
□ Sé que una devolución no es una cancelación, y no las mezclo en mis números
```

## El error clásico

Calcular el margen con el costo del producto "limpio" y tratar las devoluciones como un imprevisto.
No son imprevistos: son una tasa estadística de tu catálogo y hay que presupuestarlas como se
presupuesta el envío.

## Relacionados

`75` estructura de costos · `78` el envío que pagas tú · `82` la calculadora de margen · `83`
precio mínimo viable · `84` el producto que no sirve para ML · `92` el precio tachado y la SIC ·
`96` el costo oculto del reclamo · `97` margen por SKU · `98` qué hacer con el SKU que no deja ·
`125`-`144` reputación y posventa
