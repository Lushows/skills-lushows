# ML vs tienda propia vs Amazon vs TikTok Shop

Cuatro canales que cobran de formas distintas y dan cosas distintas. No compiten por lo mismo: uno
te da tráfico, otro te da el cliente, otro te da descubrimiento. Aquí va la comparación honesta para
Colombia, con lo que no se pudo verificar marcado como tal.

## La tabla de decisión

| | **Mercado Libre** | **Tienda propia** | **Amazon Colombia** | **TikTok Shop** |
|---|---|---|---|---|
| ¿De dónde sale el tráfico? | Ya está adentro | Lo compras tú | Ya está adentro | Descubrimiento en el feed |
| Costo variable principal | Comisión **8%-22%** + envío | Pauta (CAC) | Comisión por venta | Comisión + creadores |
| Costo fijo de arranque | ~$0 | Plataforma + dominio + pauta | ~$0 | ~$0 |
| ¿De quién es el cliente? | **De ML** | **Tuyo** | Del marketplace | De TikTok |
| Velocidad de arranque | Días | Semanas | — (ver abajo) | Días si ya tienes contenido |
| Qué te compra la gente | Lo que ya venía buscando | Lo que le mostraste | Lo que ya venía buscando | Lo que no sabía que quería |
| Riesgo mortal | Suspensión de cuenta | Que se acabe la plata de pauta | Suspensión de cuenta | Depender del alcance orgánico |
| Control del precio final | Tuyo, pero comparado en público | Total | Tuyo, comparado en público | Tuyo |
| Dueño de las reglas | ML | Tú | Amazon | TikTok |

## Mercado Libre: el tráfico gratis que se paga al final

Lo que compras con la comisión es **demanda con intención de compra ya presente**: ~8 millones de
usuarios únicos y +80 millones de visitas mensuales en Colombia (oficial de la compañía, verificado
sep-2026). No pagas CAC por adelantado.

Lo que pagas: la comisión, el envío que asumas, y la propiedad del cliente.

| Costo real en Colombia | Cifra oficial (verificado sep-2026) |
|---|---|
| Crear la publicación | $0 |
| Comisión por venta | **8% a 22%** según categoría y cuotas |
| Ofrecer cuotas extra | **+3 puntos porcentuales** |
| Precio mínimo de publicación | $2.900 |
| Envío | Aplica a todas las ventas, **incluso si el comprador lo paga** |

> ⚠️ **Sin verificar sin login (sep-2026):** el porcentaje **exacto** de tu categoría. Solo es
> público el rango 8%-22%; el detalle está tras login en
> `mercadolibre.com.co/landing/costos-de-venta` o en el simulador de costos. La API
> `listing_prices` **ya no es pública**: responde 403 y exige token. Y desconfía de los blogs que
> dicen "12-16% Clásica / 16-21% Premium": ni el rango ni los nombres corresponden a Colombia
> (`02`).

**Conviene cuando:** tu producto se busca por nombre, aguanta la comisión y puedes cumplir la
promesa logística. Detalle del cálculo en `82` y `84`.

## Tienda propia: dueño del cliente, dueño del costo

Aquí no hay comisión, pero hay CAC: cada visita se paga antes de saber si compra. La ventaja real no
es el margen bruto, es que **te quedas con el correo, el WhatsApp y el pixel** — o sea, con la
segunda venta y la tercera, que en ML no controlas.

| Ventaja | Costo |
|---|---|
| Cliente tuyo, recompra tuya | Tienes que aprender a comprar tráfico |
| Control total del precio y de la oferta | Sin tráfico, no existes |
| Bundles, upsells y checkout a tu gusto | Plataforma, dominio, pasarela, logística |

Todo lo de investigar producto, proveedores, tienda, oferta y contraentrega es de
**`dropshipping_lushows`** — no lo desarrolles aquí. Cómo convivir con ambos canales a la vez está
en `170`.

## Amazon en Colombia: existe, pero no como canal de venta local

Lo verificado (sep-2026):

- **Amazon Prime lanzó en Colombia en mayo de 2025.**
- Amazon invirtió **US$25 millones en Rappi**, con opción a llegar al 12%.

> ⚠️ **Sin verificar (sep-2026):** si existe un marketplace de Amazon con vendedores **locales
> colombianos** (Seller Central con sitio .com.co, FBA local, tarifas en COP). Lo verificado es
> presencia de Prime y la inversión en Rappi, que no es lo mismo que poder vender ahí como pyme
> colombiana. Verifícalo en Amazon Seller Central antes de planear nada.

Veredicto: **hoy, para un vendedor colombiano que quiere facturar este mes, Amazon no es la
respuesta y Mercado Libre sí.** Lo que importa de Amazon no es su marketplace: es que su llegada, y
la inversión de US$600 millones que ML anunció en Colombia para 2026 (+27% vs 2025), suben la vara
logística para todos. Quien despache lento va a perder posición sin que nadie le avise.

## TikTok Shop: descubrimiento, no búsqueda

TikTok resuelve un problema que ML no resuelve: **vender lo que nadie está buscando**. En ML el
comprador escribe lo que quiere; en TikTok se lo muestras antes de que sepa que existe. Por eso son
complementarios y no sustitutos.

> ⚠️ **Sin verificar (sep-2026):** el estado de TikTok Shop en Colombia — si está abierto a
> vendedores locales, sus comisiones y sus requisitos. No hay dato en la investigación de esta
> skill. Confírmalo en el TikTok Shop Seller Center antes de montar operación.

Todo lo de campañas, creadores, contenido y compra de tráfico en TikTok es de
**`tiktok_ads_lushows`**. Lo que sí es de esta skill: **llevar ese tráfico externo hacia una
publicación de Mercado Libre** y si eso conviene o no (`163`).

## El competidor que nadie pone en la tabla: Shein y Temu

No son un canal para ti, son la presión de precio contra la que compites:

| Dato | Cifra | Confianza |
|---|---|---|
| Pedidos Shein + Temu en Colombia | **+700.000 al mes** (ago-2026) | fuente secundaria, sep-2026 |
| Paquetes entrados en 2025 | **77 millones** | fuente secundaria, sep-2026 |
| Contexto | Presión gremial para que la DIAN actúe | fuente secundaria, sep-2026 |

Qué significa operativamente: **el producto genérico chino barato ya está en Colombia sin tu
estructura de costos.** Competirle por precio en esa franja es perder, y los números lo confirman:
un producto de $10.000 con costo de $4.000 deja $203 de utilidad con comisión del 15% y **pierde
$497 con comisión del 22%** (cálculo con cifras oficiales, ver `09`). La salida es ticket más alto,
entrega inmediata, garantía real y kits (`85`, `86`, `87`). Y ojo con el riesgo regulatorio: si la
DIAN cambia el régimen de esos paquetes, la ventaja de precio de ellos se mueve — eso es de
`contador_lushows`, no de aquí.

## La regla de decisión

```
□ ¿El producto se busca por nombre?              SÍ → Mercado Libre
□ ¿Aguanta la comisión con margen?               NO → no lo lleves a ML aunque se busque   (84)
□ ¿Necesitas la recompra y el dato del cliente?  SÍ → tienda propia, además de ML          (170)
□ ¿Nadie lo busca porque no saben que existe?    SÍ → descubrimiento: TikTok / Meta
□ ¿Ticket bajo y competencia con Shein/Temu?     SÍ → replantea el producto, no el canal   (86)
□ ¿Quieres un solo canal para empezar?           → Mercado Libre: es el de menor costo fijo
```

## El error clásico

Tratar los canales como una competencia deportiva ("¿cuál es mejor?") en vez de como una secuencia
de caja. Para alguien que arranca en Colombia, la secuencia que menos capital quema es:

```
1. Mercado Libre  → valida que el producto se vende y a qué precio, sin pagar CAC
2. Tienda propia  → cuando ya sabes que vende, y quieres ser dueño de la recompra
3. Descubrimiento → cuando tienes contenido y margen para pagar alcance
```

**Empieza donde el tráfico ya está; compra tráfico cuando ya sepas que el producto convierte.** Al
revés — montar tienda y comprar pauta para validar — se paga la validación dos veces.

## Relacionados

`01` qué es ML y por qué no es una tienda · `02` los cuatro motores · `04` diagnóstico inicial ·
`09` cuánto se gana de verdad · `76` las comisiones y cómo verificarlas · `82` la calculadora de
margen · `84` el producto que no sirve para ML · `85` el ticket que aguanta ML ·
`86` por qué los productos baratos pierden · `87` subir el ticket con kits ·
`163` tráfico externo hacia tu publicación · `170` vender en ML y en tu tienda a la vez ·
`171` cuándo abrir otro país · skills: `dropshipping_lushows`, `tiktok_ads_lushows`,
`facebook_ads_lushows`, `contador_lushows`
