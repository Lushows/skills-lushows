# Tendencias de Mercado Libre

Mercado Libre publica los términos más buscados de su propio sitio. Es gratis, viene de dentro del
marketplace donde la gente compra, y casi nadie lo usa. La mayoría de vendedores decide qué
publicar mirando TikTok, y luego se pregunta por qué nadie lo busca en ML.

> ⚠️ **Sin verificar para Colombia (sep-2026).** La URL exacta de la herramienta, su cobertura en
> MCO y su frecuencia de actualización **no se pudieron confirmar**: las páginas
> `mercadolibre.com.co/ayuda/*` y `vendedores.mercadolibre.com.co` devuelven **403** a acceso
> automatizado. Búscala estando logueado, desde el panel de vendedor, en la sección de
> tendencias / términos más buscados. Si no aparece en tu cuenta, usa los métodos alternativos de
> más abajo.

## Por qué vale más que cualquier keyword tool

| Fuente | Qué mide | Problema |
|---|---|---|
| Google Trends / Keyword Planner | Búsquedas en Google | Gente informándose, no comprando |
| TikTok / redes | Qué se ve | Cero señal de intención de compra |
| Blogs de "productos ganadores" | Lo que ya se saturó | Llegas tarde por definición |
| **Tendencias de ML** | Qué se busca **dentro del marketplace** | Ninguno: es la intención real |

Alguien que escribe un término en el buscador de Mercado Libre ya decidió que va a comprar. Está
eligiendo a quién. Esa es la diferencia con todo lo demás.

**En Google la gente pregunta; en Mercado Libre la gente compra. No optimices con datos de quien
pregunta.**

## Para qué sirve exactamente

| Uso | Cómo |
|---|---|
| Elegir la palabra del título | Usa el término tal como lo escribe el comprador, no la jerga del proveedor |
| Detectar estacionalidad | Qué sube en octubre, qué muere en febrero |
| Ver demanda insatisfecha | Términos con búsquedas altas y pocos resultados |
| Confirmar un producto antes de comprarlo | Si nadie lo busca en ML, no lo vas a vender en ML |
| Preparar temporada alta | Hot Sale, navidad, regreso a clases |
| Encontrar sinónimos reales | "chaqueta" vs "windbreaker" vs "rompevientos" |

El cuarto es el más rentable y el que más plata ahorra: **antes de importar cien unidades,
verifica que el término exista.**

## El método

```
□ Entra logueado al panel de vendedor y ubica la sección de tendencias
□ Filtra por tu categoría, no mires solo el listado general
□ Anota los 20 términos más buscados de tu categoría
□ Para cada término que te sirva, búscalo en ML en incógnito y anota:
    - cuántos resultados hay (competencia)
    - si los primeros tienen Full (barrera logística)
    - el rango de precios de los 5 primeros
□ Tu oportunidad = búsquedas altas + pocos resultados + sin Full dominante
□ Repite mensualmente y guarda el histórico: la tendencia es la serie, no la foto
```

La relación búsquedas/resultados es el filtro que separa un término útil de uno imposible. Un
término con muchísimas búsquedas y 40.000 publicaciones no es una oportunidad: es una pared.

## Métodos alternativos si la herramienta no te aparece

Sin la herramienta oficial todavía puedes leer la demanda:

```
□ AUTOCOMPLETADO: escribe tu término en el buscador de ML y mira las sugerencias.
  Están ordenadas por lo que la gente realmente busca
□ FILTROS: los filtros de la izquierda te dicen qué atributos importan en la categoría
□ CANTIDAD DE RESULTADOS: "1.243 resultados" es tu medida de competencia
□ "MÁS VENDIDOS": la sección de más vendidos por categoría muestra qué se mueve
□ PREGUNTAS de los líderes: el vocabulario real de tus clientes (`70`)
□ API: GET /sites/MCO/search?q=TERMINO devuelve el total de resultados en `paging.total`
□ PREDICTOR: GET /sites/MCO/domain_discovery/search?q=TERMINO&limit=3 te dice a qué
  categoría asocia ML ese término — útil para saber si estás publicando donde debes
```

El truco del autocompletado es el más subestimado: es literalmente la lista de intenciones más
frecuentes, gratis, sin login y actualizada.

## Estacionalidad de Colombia

Lo que sí está verificado y hay que tener en el calendario:

| Fecha | Qué es | Confianza |
|---|---|---|
| **16-20 marzo 2026** | Primera edición de Hot Sale Colombia: +40,4 millones de búsquedas en 5 días, descuentos hasta 65%, hasta 12 cuotas sin interés, 80+ empresas | MEDIA-ALTA |
| **19-23 octubre 2026** | Segunda edición de Hot Sale Colombia | MEDIA-ALTA |

Ese "+40,4 millones de búsquedas en 5 días" es la dimensión del evento. Preparar la ficha y el
stock con anticipación para esa ventana vale más que tres meses de optimización en temporada
normal. Ver `163`.

> ⚠️ **Sin verificar para Colombia (sep-2026).** No hay datos oficiales de estacionalidad por
> categoría en MCO (qué sube en qué mes). Constrúyela tú con el histórico de tus propias ventas y
> con mediciones mensuales de la herramienta de tendencias.

## Contexto de mercado que conviene tener en la cabeza

| Dato | Valor |
|---|---|
| Usuarios de ML en Colombia | ~8 millones de usuarios únicos |
| Visitas mensuales | +80 millones |
| Vendedores activos | +98.000 |
| Categoría líder del e-commerce CO | Tecnología, 19,9% de participación |
| Hogar/decoración | 1,5% — la logística de muebles grandes lo frena |
| Moda | La mayor tasa de recompra del país |
| Inversión de ML en Colombia 2026 | US$600 millones, a tecnología y logística |

La fila de moda es la más accionable: **la mayor tasa de recompra del país**. Si vendes algo
recomprable, el valor del cliente no está en la primera venta.

## Lo que la herramienta NO te dice

- No te dice si el término es **rentable**. Búsquedas altas con margen de 4% es un mal negocio.
  Corre el número en `83`.
- No te dice quién está ganando ese término. Para eso, `70`.
- No te dice si puedes competir en logística. Para eso, `67`.
- No reemplaza la decisión de qué producto vender: eso es `dropshipping_lushows`.

## El error clásico

Encontrar un término con muchas búsquedas y publicar de inmediato. Búsquedas altas suelen
significar competencia alta, líderes con Full, márgenes exprimidos y catálogo cerrado. El término
que te sirve no es el más buscado: es el que tiene **demanda suficiente y competencia que puedes
batir**. Mide las dos cosas antes de comprar inventario.

## Relacionados

`31` título · `40` atributos · `41` criterios de categoría · `55` cómo funciona el buscador ·
`56` buscador con IA · `62` qué es el catálogo · `67` envío y posición · `68` precio como factor ·
`69` medir tu posición real · `70` espiar al líder · `83` precio con margen ·
`163` Hot Sale · `dropshipping_lushows` qué producto vender
