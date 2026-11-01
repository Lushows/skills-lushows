# Product Ads

El producto principal de Mercado Ads y el único que necesitas al empezar: promocionas una
publicación tuya y pagas **solo cuando alguien hace clic** (oficial ML Colombia, verificado
sep-2026). Nunca pagas por que el anuncio se muestre.

## Lo esencial en una tabla

| Qué | Cómo funciona |
|---|---|
| Modelo de cobro | **CPC** — costo por clic. La impresión es gratis |
| Qué se anuncia | Una publicación tuya que ya existe y está activa |
| Creativo | No hay creativo que diseñar: el anuncio **es tu ficha** (foto, título, precio, envío) |
| Dónde se decide | Una subasta interna cada vez que alguien busca (`147`) |
| Cómo se controla el gasto | Presupuesto diario por campaña + la estrategia que elijas (`148`) |
| Métrica de gobierno | **ACOS** (`149`), leído contra tu margen (`150`) |
| Dónde se administra | Mi cuenta → Marketing → Publicidad (`155`) |

**No diseñas el anuncio: lo diseñaste cuando hiciste la ficha.** Esa es la implicación grande de
Product Ads y la razón por la que `164` existe.

## Dónde aparecen los anuncios

Los espacios varían por dispositivo y por categoría, pero el patrón es consistente:

| Ubicación | Qué tan valiosa | Nota |
|---|---|---|
| **Resultados de búsqueda** | La más valiosa | Intención máxima: la persona escribió lo que quiere |
| Primeras posiciones del listado | Muy alta | Suele ser el espacio más disputado de la categoría |
| **Ficha de otro producto** | Alta | Apareces dentro de la publicación de un competidor |
| Carruseles de recomendados | Media | "Quienes vieron esto también vieron" |
| Home y páginas de categoría | Media-baja | Más exploración que intención |
| Carrito y post-compra | Variable | Complemento y venta cruzada |

Aparecer en la ficha del competidor es el movimiento más agresivo y más rentable de Product Ads:
la persona ya decidió el producto, solo está mirando a quién comprárselo. Si tu precio y tu envío
son mejores (`68`, `67`), ese clic se convierte muy alto.

## Una publicación puede aparecer dos veces

En la misma página de resultados puedes salir como **anuncio pagado** y como **resultado
orgánico**. No es un error ni una trampa del sistema: es el comportamiento normal y es una de las
razones por las que la pauta ayuda al orgánico (`153`). También es la razón por la que el ACOS
solo no cuenta la historia completa: parte de las ventas atribuidas a la pauta habrían ocurrido
igual. Por eso se mira también el TACOS (`149`).

## Qué se puede promocionar y qué no

```
□ La publicación está ACTIVA (no pausada, no sin stock)
□ Tiene stock real, no un número inflado
□ El precio es el precio final que quieres sostener durante la prueba
□ La ficha está completa: atributos, fotos 1200 px, descripción (`40`, `42`)
□ No es un producto de categoría restringida o prohibida
□ Es un SKU con margen suficiente para absorber el ACOS objetivo (`150`)
```

Las publicaciones pausadas o sin stock dejan de recibir clics: no gastas, pero la campaña pierde
aprendizaje y el CPC futuro sobre esa publicación se encarece. **Quedarte sin stock con pauta
encendida es el desperdicio más caro de Mercado Ads.**

## Cómo se estructura una cuenta sin enredarse

Empieza simple. La sobre-segmentación es un problema de cuentas grandes, no de la tuya.

| Etapa | Estructura recomendada |
|---|---|
| Arranque (1-10 SKU) | **Una campaña**, estrategia Rentabilidad, tus 3-5 mejores SKU |
| Ya con datos (1 mes) | Separa en 2 campañas: los que ganan plata y los que estás probando |
| Catálogo grande | Una campaña por familia de producto o por rango de margen |
| Fecha caliente | Campaña aparte, presupuesto aparte, para poder apagarla entera (`162`) |

El criterio de separación correcto no es "por categoría": es **por margen**. Productos con margen
distinto necesitan ACOS objetivo distinto (`150`), y el ACOS se fija a nivel de campaña.

## Presupuesto: lo que sí se puede decir

Se define un presupuesto diario por campaña, y la estrategia elegida determina qué tan agresiva
es la puja dentro de ese tope (`148`).

> ⚠️ **Sin verificar para Colombia (sep-2026).** El **presupuesto mínimo diario en COP** no está
> publicado en ninguna fuente oficial consultable, y las cifras que circulan son de Argentina o
> México. Léelo en el panel al crear la campaña: Mi cuenta → Marketing → Publicidad → Crear
> campaña. El monto mínimo aparece ahí, en pesos colombianos, antes de confirmar.

Lo que sí puedes decidir con criterio propio: **empieza con un presupuesto que puedas perder
entero durante dos semanas sin que te duela.** Ese es el costo del aprendizaje, y ninguna cuenta
lo salta.

## El error clásico

Promocionar todo el catálogo "para ver qué pega". El presupuesto se reparte entre decenas de
publicaciones, ninguna junta suficientes clics para que el sistema aprenda, y a los 15 días no
tienes ni ventas ni datos. Elige pocos SKU, con margen y con ficha buena, y déjalos correr.
**Pauta concentrada gana; pauta repartida solo gasta.**

## Checklist de la primera campaña

```
□ Ejecuté `python scripts/margen_ml.py margen ...` para cada SKU que voy a pautar (`82`)
□ Elegí máximo 3-5 SKU, los de mejor margen y mejor ficha
□ Elegí estrategia Rentabilidad para arrancar (`148`)
□ Leí el presupuesto mínimo diario directamente en el panel
□ Anoté la fecha de encendido: no juzgo resultados antes de 14 días (`151`)
□ Verifiqué stock para todo el periodo de prueba
□ No voy a cambiar precio ni ficha durante la prueba
```

## Relacionados

`145` qué es Mercado Ads · `147` la subasta y el CPC · `148` las tres estrategias ·
`149` ACOS y TACOS · `150` el ACOS sano según tu margen · `151` la ventana de atribución ·
`152` pautar una publicación nueva · `153` el efecto sobre lo orgánico · `155` leer los reportes ·
`156` optimizar semana a semana · `164` cuándo no es la respuesta · `40` atributos · `42` fotos ·
`48` indicador de calidad · `61` stock cero · `67` envío y posición · `68` precio como factor ·
`82` la calculadora de margen
