# Los sitios de LatAm y cuál elegir

Mercado Libre no es una plataforma: son varias plataformas que comparten el código y poco más. Cada
país es un **sitio** con su propio ID, sus tarifas, sus reglas y su catálogo. Confundirlos es el
origen de casi todos los datos falsos que circulan.

## Los seis sitios que te importan

| Sitio | País | Idioma | Moneda | Lo que cambia |
|---|---|---|---|---|
| `MCO` | Colombia | Español | COP | El default de esta skill |
| `MLA` | Argentina | Español | ARS | Genera la mayoría del contenido en español sobre ML |
| `MLM` | México | Español | MXN | El otro gran generador de contenido contaminante |
| `MLC` | Chile | Español | CLP | Mensajería migrando desde feb-2026 (`188`) |
| `MPE` | Perú | Español | PEN | — |
| `MLB` | Brasil | **Portugués** | BRL | Otro idioma: fichas, títulos y atención se rehacen |

Site IDs verificados sep-2026. El listado completo se consulta por API: `GET /sites`.

> ⚠️ **Sin verificar (sep-2026):** el tamaño relativo de cada sitio (usuarios, GMV, número de
> vendedores). Esta skill solo tiene cifras verificadas de **Colombia** (`01`). No cites rankings de
> "el país más grande de ML" — los que circulan no traen fuente. Si lo necesitas, pídelo en el
> reporte de resultados de MELI (empresa pública) o en el panel del sitio.

## Lo que NO es igual entre sitios

Esta es la lista que hay que tener en la cabeza antes de repetir cualquier dato:

| Cosa | ¿Igual entre países? |
|---|---|
| El host de la API (`api.mercadolibre.com`) | **Sí**, uno solo para todos. Cambia el `site_id` |
| Los porcentajes de comisión | **No.** Por país y por categoría. En Colombia el rango oficial es **8%-22%** (verificado sep-2026) |
| El cargo fijo por venta de bajo valor | **No**, y ni siquiera existe en todos: **en Colombia no hay**. Lo que hay es un precio mínimo de publicación de **$2.900** (oficial, sep-2026) |
| El umbral de envío gratis | **No.** En Colombia son **$60.000** (oficial, sep-2026) |
| Los requisitos de MercadoLíder | **No.** En Colombia: 120 ventas / $10M COP (oficial, sep-2026). Los blogs con 180 o 415 ventas hablan de otro país |
| Las tarifas de Full | **No**, y la de México circula disfrazada de colombiana |
| Qué categorías tienen catálogo habilitado | **No** |
| Las devoluciones gratis | **No.** México ya eliminó la devolución gratis por arrepentimiento en electrónica, celulares y cómputo, con cargo de ~150-300 MXN. **No aplica a Colombia** |
| Los productos permitidos y las categorías reguladas | **No.** Cambian con la ley de cada país |
| El calendario comercial | **No.** Hot Sale, Buen Fin y Black Friday no caen igual |
| La estructura del termómetro y las variables base | **Sí**, el modelo es el mismo. Los números no |
| Las reglas de la API, OAuth y webhooks | **Sí** |

**Una cifra sin sitio y sin fecha no es una cifra: es un rumor.** Esa es la regla que separa esta
skill de cualquier blog de marketplace (`02`).

## El caso que lo prueba: el cargo fijo argentino

Desde el 1-sep-2026 circula por todo Google que "los ítems bajo $33.000 pagan $1.330 / $2.740 /
$3.320 de cargo fijo". Es **MLA, en pesos argentinos**. Y al leer la página oficial colombiana con
navegador real quedó claro que **en Colombia ese cargo ni siquiera existe**: lo que hay es un precio
mínimo de publicación de $2.900 (oficial ML Colombia, verificado sep-2026). Quien calculó su margen
colombiano con la cifra argentina no se equivocó de monto: se equivocó de mecanismo completo. El
caso resuelto, con las tres capas de fuentes, está en `02`.

Otra trampa del mismo tipo, esta vez de vocabulario: los blogs siguen hablando de publicación
**"Clásica" y "Premium"**. El sitio colombiano ya no usa esos nombres — habla de **Gratuita**,
publicaciones **con cuotas con 0% interés** y **cuotas extra** (+3 puntos porcentuales). Los nombres
viejos siguen vigentes en otros sitios y en la API (`42`, `43`).

## Dificultad de entrada, honestamente

No hay una tabla verificada de dificultad por país. Lo que sí se puede decir con lo que hay:

| Factor | Cómo lo evalúas tú mismo, sitio por sitio |
|---|---|
| Idioma | Brasil exige rehacer todo en portugués, incluida la atención posventa |
| Fiscal | ¿Puedes facturar legalmente en ese país? Es la pregunta que casi siempre mata la idea |
| Logística | ¿Tienes inventario allá o vas a cruzar frontera en cada venta? |
| Devoluciones | Una devolución internacional puede costar más que el producto |
| Competencia local | Se mide entrando al buscador del sitio y mirando precios y reputaciones |

> ⚠️ **Sin verificar para Colombia (sep-2026):** los requisitos fiscales y societarios para que un
> vendedor colombiano opere como vendedor local en otro sitio. Eso no es marketplace, es tributario
> y societario → **rutea a `contador_lushows`** y, si es estructura de negocio, a
> `economist_lushows`.

## ¿Cuándo tiene sentido abrir otro país?

La respuesta corta es: **casi nunca al principio**. La señal no es el entusiasmo, es el techo.

```
□ Tu sitio actual está en verde y estable (nada de expandir con el termómetro golpeado)
□ Llevas al menos 3 meses con el margen ya calculado y positivo por SKU        (97)
□ Tocaste techo: tu categoría en MCO ya no crece aunque mejores ficha y precio
□ Tienes cómo facturar legalmente en el país nuevo                             (contador_lushows)
□ Tienes cómo entregar allá en un plazo competitivo, no "en 20 días"
□ Tienes quién responda preguntas en ese huso horario y en ese idioma
□ Puedes perder 3 meses de operación sin que se caiga el negocio principal
```

Si falla uno solo, no es momento. El desarrollo completo está en `171`; las dos vías reales
(Global Selling y vender desde Colombia hacia afuera) están en `120` y `121`.

## La alternativa que casi siempre gana

Antes de abrir un país nuevo, revisa si el crecimiento está más barato en casa:

| Palanca | Costo de intentarlo | Módulo |
|---|---|---|
| Subir la conversión de lo que ya tienes | Horas de trabajo, $0 | `54`, `58` |
| Ganar el catálogo en tu categoría | Precio y logística, no país nuevo | `63` |
| Entrar a Full y mejorar la promesa de entrega | Inventario inmovilizado | `103`, `105` |
| Subir el ticket con kits | Empaque | `87` |
| Mercado Ads con ACOS bajo el margen | Presupuesto controlado | `150` |
| Una fecha caliente bien preparada | Planeación | `161`, `162` |

Un país nuevo es empezar de cero: termómetro gris (**sin reputación hasta las primeras 10 ventas**),
sin opiniones, sin historial de conversión, y con periodo de evaluación de **365 días** hasta llegar
a 60 ventas (oficial ML Colombia, sep-2026 — verifica el equivalente en el sitio nuevo). Todo lo que
te costó construir aquí, otra vez.

## El error clásico

Abrir México "porque es más grande" con el inventario en Bogotá. El comprador mexicano ve una
promesa de entrega larga, no compra, la conversión se hunde en las primeras 72 horas (`59`), la
publicación queda etiquetada y el vendedor concluye que "México no funciona". México funcionaba: la
logística no.

El segundo error, más silencioso: **leer la ayuda de otro sitio porque la de Colombia está en 403**
y aplicar esa regla como si fuera local. Si tienes que hacerlo, dilo en voz alta y márcalo como
comparación, nunca como dato (`02`).

## Relacionados

`01` qué es ML y su tamaño en Colombia · `02` la trampa de los datos · `03` glosario ·
`04` diagnóstico inicial · `59` las primeras 72 horas · `97` margen por SKU ·
`120` Global Selling · `121` vender desde Colombia afuera · `129` MercadoLíder ·
`161` Hot Sale y el calendario comercial · `171` cuándo abrir otro país ·
`188` mensajes de posventa · `194` usuarios de prueba (se crean por sitio)
