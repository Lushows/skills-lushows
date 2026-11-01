# Obligatorios vs opcionales

En la lista de atributos de una categoría hay tres grupos, no dos: los que te exigen para publicar,
los que te exigen para entrar a catálogo, y los que nadie te exige. **El tercer grupo es donde se
gana.**

## Los tres grupos

| Grupo | Marca en la API | Qué pasa si falta |
|---|---|---|
| Obligatorio para publicar | `tags.required: true` | No te deja publicar |
| Obligatorio para catálogo | `tags.catalog_required: true` | Publicas, pero no entras a catálogo (`62`) |
| Opcional | sin tag | Publicas igual, y quedas fuera de ese filtro |

(MEDIA-ALTA.)

Cómo leerlos:

```
GET https://api.mercadolibre.com/categories/$CATEGORY_ID/attributes
```

Busca en la respuesta los bloques `"tags"`. Si quieres verlo ordenado, pídele a Claude que te lo
convierta en tres listas.

## Por qué llenar TODOS

| Razón | Detalle |
|---|---|
| Filtros | Cada atributo vacío es un filtro donde no existes (`31`) |
| Indicador de calidad | "Atributos completos y verificados" es uno de los cuatro objetivos para llegar a Profesional (MEDIA, `47`) |
| Catálogo | Sin los `catalog_required` no puedes competir por la ficha compartida (`62`) |
| Buscador semántico | Es la materia prima que el modelo lee para entender tu producto (`30`) |
| Comparación | ML arma tablas comparativas con atributos; si los tuyos están vacíos, pierdes la comparación |
| Envíos | Peso y dimensiones mal puestos = cotización errada y pérdida en cada venta (`109`) |

**El mínimo obligatorio es el piso legal de la publicación, no la meta.**

## Cuánto cuesta realmente

| Tarea | Tiempo real |
|---|---|
| Llenar solo los obligatorios | 3-5 minutos |
| Llenar todos los atributos | 10-15 minutos la primera vez |
| Replicar a productos de la misma categoría | 2 minutos (copias la estructura) |

Diez minutos por SKU, una sola vez. Es el trabajo mejor pagado de todo el proceso.

## Excepciones: cuándo NO llenar un atributo

| Caso | Qué hacer |
|---|---|
| No conoces el dato con certeza | Déjalo vacío. Inventarlo es reclamo no excluible (`136`) |
| El atributo no aplica a tu producto | Déjalo vacío; no inventes un valor "neutro" |
| El valor real no está en la lista cerrada | Elige el más cercano honesto, o déjalo vacío |
| Es un dato que cambia por unidad (número de serie) | No va en atributos |

Vacío por no saber es correcto. Vacío por pereza es plata perdida.

## Cómo priorizar si tienes 200 SKUs y poco tiempo

```
□ 1. Los 20 productos que más venden: todos los atributos, sin excepción
□ 2. Todos los productos: BRAND, MODEL, GTIN, medidas y peso
□ 3. Categoría por categoría: el atributo que más se usa como filtro en esa rama
□ 4. El resto, por tandas, mientras no haya nada más urgente
```

Regla: antes de crear una publicación nueva, termina de llenar la que ya vende. Un SKU completo
rinde más que dos incompletos.

## Verificar qué te falta sin abrir el panel

Con el ítem ya publicado:

```
GET https://api.mercadolibre.com/items/$ITEM_ID
```

Compara el arreglo `attributes` que te devuelve con la lista completa de la categoría. Lo que está
en la categoría y no en tu ítem, es lo que te falta. Para muchos ítems, esto se automatiza (`182`).

## El error clásico

Creer que el formulario del panel muestra todos los atributos. El panel a veces agrupa los
opcionales bajo "Ver más características" o los deja al final de una pantalla larga, y la gente le
da publicar sin abrir esa sección. **Si no bajaste hasta el final del formulario, no llenaste la
ficha.**

## Chequeo

```
□ Corrí GET /categories/$ID/attributes y tengo la lista completa
□ Todos los tags.required están llenos
□ Todos los tags.catalog_required están llenos (si quiero catálogo)
□ Abrí "Ver más características" y llené lo que aplica
□ Ningún valor inventado
□ Marca escrita igual en todas mis publicaciones
□ Peso y dimensiones son los reales, medidos
□ El indicador de calidad subió después de guardar (`46`)
```

## Relacionados

`31` ficha técnica y atributos · `27` el predictor · `30` búsqueda semántica · `46` indicador de
calidad · `47` llegar a Profesional · `62` catálogo · `109` peso y dimensiones · `136` reclamos no
excluibles · `182` mantener fichas por API
