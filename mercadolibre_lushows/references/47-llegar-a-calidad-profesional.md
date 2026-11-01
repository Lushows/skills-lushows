# Llegar a calidad Profesional

El indicador y sus límites están en `46`. Aquí está lo accionable: los **cuatro objetivos** que hay
que cumplir para que una publicación llegue al nivel Profesional, y el orden en que conviene
atacarlos.

## Los cuatro objetivos

| # | Objetivo | Confianza |
|---|---|---|
| 1 | **Atributos completos y verificados** | MEDIA |
| 2 | **Estar en catálogo** si la categoría lo exige | MEDIA |
| 3 | **Usar variaciones** en vez de publicaciones separadas | MEDIA |
| 4 | **Tener el precio más competitivo** | MEDIA |

> ⚠️ **Sin verificar para Colombia (sep-2026).** Los cortes numéricos entre básica, estándar y
> profesional no se publican, ni el peso de cada objetivo en el puntaje. Trabaja los cuatro
> objetivos; no persigas un número que nadie publicó.

## Objetivo 1: atributos completos

El más barato y el que más mueve. Es trabajo de escritorio, no cuesta plata y no depende de nadie.

```
□ GET /categories/$CATEGORY_ID/attributes para tener la lista completa (`31`)
□ Todos los tags.required llenos
□ Todos los tags.catalog_required llenos (`32`)
□ Abrí "Ver más características" en el formulario y llené lo que aplica
□ Valores elegidos de la lista, no escritos a mano
□ Peso y dimensiones reales, medidos
□ Ningún dato inventado: vacío es mejor que falso (`136`)
```

## Objetivo 2: catálogo, si la categoría lo exige

En categorías estandarizadas ML crea una ficha única compartida y elige un ganador que aparece como
"la mejor oferta"; el resto va a "Otras opciones de compra" (MEDIA, `62`).

| Tu caso | Qué hacer |
|---|---|
| Tu categoría tiene catálogo y tú no estás | Entra: te falta el objetivo 2 (`62`) |
| Tu categoría tiene catálogo y ya estás | Cumplido. Ahora pelea por ganar (`63`) |
| Tu categoría no tiene catálogo | No aplica; no pierdas tiempo buscándolo |

> ⚠️ **Sin verificar para Colombia (sep-2026).** Qué categorías tienen catálogo habilitado en `MCO`
> en 2026 **no está confirmado**. Compruébalo en tu categoría desde el panel.

Advertencia antes de entrar: si la publicación compite en catálogo, **ya no podrás editar el
título** (oficial ML Colombia, verificado sep-2026; ver `28`). Deja el título como lo quieres para
siempre antes de dar el paso.

## Objetivo 3: variaciones en vez de publicaciones sueltas

Si vendes el mismo producto en colores o tallas separado en varias publicaciones, unifícalo (`40`).
El procedimiento de migración sin perder historial está en `41`.

```
□ Identifiqué todas mis publicaciones del mismo producto
□ Elegí la que tiene más ventas y opiniones como la que se queda
□ Le agregué las variantes
□ Le quité el color del título (`28` `29`)
□ Cada variante tiene su foto propia
□ Pausé las demás gradualmente, no de golpe
```

## Objetivo 4: el precio más competitivo

El único de los cuatro que cuesta plata, y el único que puede ser una mala idea.

| Situación | Veredicto |
|---|---|
| Estás caro por descuido o por no haber recalculado | Corrígelo |
| Estás caro porque tu costo es más alto | No bajes: mejora los otros tres objetivos |
| Bajar te deja bajo el margen mínimo | No bajes. Nunca |
| Estás cerca del líder y te falta poco | Evalúa con el número en la mano (`82`) |

Antes de mover un precio, calcula: `python scripts/margen_ml.py margen --precio X --costo Y
--comision Z --iva 19`. Si el cálculo tiene que ser exacto, rutea a `Matematicas_lushows`.

Recuerda que la comisión en Colombia va de **8% a 22%** según categoría y cuotas, y que activar
cuotas extra suma exactamente **3 puntos porcentuales** (oficial ML Colombia, verificado sep-2026;
ver `42` `43`). Un precio "competitivo" con cuotas extra puede dejarte en rojo.

**Profesional con margen negativo es un adorno caro.**

## El orden correcto de ataque

| Orden | Objetivo | Por qué en ese lugar |
|---|---|---|
| 1 | Atributos | Gratis, rápido, efecto inmediato |
| 2 | Variaciones | Gratis, concentra historial |
| 3 | Catálogo | Requiere datos y es irreversible en el título |
| 4 | Precio | Cuesta plata: último, y con la calculadora abierta |

## Cómo hacerlo a escala

Si tienes decenas de publicaciones, el editor masivo del panel es donde se corrigen atributos en
bloque (oficial ML Colombia, verificado sep-2026). Si tienes cientos, se automatiza leyendo los
atributos faltantes con la API y corrigiendo con `PUT /items/$ITEM_ID` (`182`).

```
□ Semana 1: atributos de los 20 productos que más venden
□ Semana 2: unificar variaciones
□ Semana 3: revisar catálogo donde aplique
□ Semana 4: revisar precios con la calculadora, uno por uno
□ Mes 2: repetir sobre el resto del catálogo
```

## El error clásico

Empezar por el precio porque es el botón más fácil de mover. Bajas $5.000, subes el indicador, y
descubres a fin de mes que vendiste más y ganaste menos. Los tres primeros objetivos son gratis y
ninguno toca tu utilidad. **Baja el precio solo cuando ya hiciste todo lo que era gratis.**

## Relacionados

`46` el indicador de calidad · `31` atributos · `32` obligatorios vs opcionales · `40` variaciones ·
`41` estructura · `28` el título y el catálogo · `42` `43` cuotas y comisión · `62` `63` catálogo ·
`82` margen real · `182` mantener fichas por API · `54` auditoría en 15 minutos
