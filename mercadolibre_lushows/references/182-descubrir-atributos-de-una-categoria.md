# Descubrir atributos de una categoría

Los atributos obligatorios **dependen 100% de la categoría**: no hay una lista universal que
puedas memorizar. La API te los dice exactamente, y hacerlo bien es lo que separa una ficha que
aparece en los filtros de una que queda invisible aunque exista.

## El flujo correcto, en tres llamados

```
1. GET https://api.mercadolibre.com/sites/MCO/domain_discovery/search?q=$Q&limit=3
      -> te devuelve category_id

2. GET https://api.mercadolibre.com/categories/$CATEGORY_ID
      -> confirma nombre y ruta de la categoria

3. GET https://api.mercadolibre.com/categories/$CATEGORY_ID/attributes
      -> la lista completa de atributos con sus reglas

4. Armas attributes[] con TODOS los que traen tags.required: true
```

Los tres primeros son de lectura y no tocan nada. Córrelos siempre antes de publicar (`181`).

## Qué devuelve `/attributes`

Un arreglo. Cada elemento describe un atributo, en forma típica:

```json
{
  "id": "BRAND",
  "name": "Marca",
  "value_type": "string",
  "tags": { "required": true, "catalog_required": true },
  "values": [
    { "id": "9344", "name": "Samsung" },
    { "id": "206", "name": "LG" }
  ]
}
```

## Los campos que importan

| Campo | Para qué lo usas |
|---|---|
| `id` | Lo que va en tu `attributes[]`: `"id": "BRAND"` |
| `name` | El nombre humano, para tu propio panel |
| `value_type` | `string`, `number`, `number_unit`, `boolean`, `list` |
| `values` | La lista cerrada de valores válidos, si la hay |
| `tags` | Las reglas. Aquí está todo lo que decide |
| `allowed_units` | Unidades válidas cuando es `number_unit` (cm, g, ml) |

## Los dos `tags` que mandan

| Tag | Qué significa | Consecuencia de ignorarlo |
|---|---|---|
| `tags.required: true` | **Obligatorio para publicar** | El `POST /items` falla |
| `tags.catalog_required: true` | Solo para catálogo | Publicas, pero sin catálogo (`63`) |

Hay otros tags según la categoría (por ejemplo, atributos marcados como variación o como de solo
lectura). La regla práctica: **si no entiendes un tag, no pelees con ese atributo — llénalo con el
valor correcto y sigue.**

## Cómo se arma el `attributes[]`

Dos formas de mandar el valor, y elegir mal es el segundo error más común:

| Cuando el atributo... | Mandas | Ejemplo |
|---|---|---|
| Tiene `values` (lista cerrada) | `value_id` | `{"id":"BRAND","value_id":"9344"}` |
| Es texto libre | `value_name` | `{"id":"MODEL","value_name":"A54 5G"}` |
| Es `number_unit` | `value_name` con la unidad | `{"id":"WEIGHT","value_name":"500 g"}` |
| Es `boolean` | `value_id` del sí/no de la lista | Léelo de `values`, no mandes `true` |

Cuando existe `values` y tú mandas `value_name` con un texto que no coincide exactamente, ML puede
crear un valor "libre" que **no entra en los filtros de búsqueda**. Es la trampa silenciosa: la
publicación se crea, se ve bien, y desaparece cuando el comprador filtra por esa marca.

## Por qué esto decide tus ventas

Los atributos alimentan los filtros del buscador. Si el comprador filtra por "Marca: Samsung" y tu
atributo `BRAND` está vacío o con un valor libre, **no existes en ese resultado**. No es una
penalización del algoritmo, es exclusión aritmética.

Y hay más: los atributos completos y verificados son el primer objetivo del indicador de calidad
para llegar a "Profesional" (`43`), y la ficha incompleta es causa citada de pausas y revisiones.

## Lista de chequeo antes de publicar

```
□ Corri /categories/$ID/attributes contra la categoria REAL, no una parecida
□ Lleno TODOS los de tags.required
□ Lleno tambien los de tags.catalog_required si quiero catalogo
□ Para cada atributo con values, use value_id de la lista, no texto
□ Las unidades salen de allowed_units, no me las invente
□ Lleno tambien los opcionales que un comprador usaria para filtrar
```

Ese último punto no es opcional en la práctica. **Los obligatorios te dejan publicar; los
opcionales te dejan aparecer.**

## Cachear la respuesta

La lista de atributos de una categoría cambia poco. Si vas a publicar 300 productos, no llames 300
veces: guarda la respuesta por `category_id` con una vigencia razonable (un día está bien) y
refréscala cuando un `POST /items` falle por atributo faltante. Eso te ahorra buena parte del
presupuesto de peticiones (`193`).

## El error clásico

Usar una plantilla de atributos copiada de otra categoría o de otro país. Los `id` de atributo
suelen parecerse entre categorías, pero las listas de `values` no, y los IDs de valor son
distintos por site. **El único origen legítimo de un `value_id` es la respuesta de
`/categories/$CATEGORY_ID/attributes` contra `MCO`.**

El segundo error: llenar lo obligatorio y parar ahí. Es exactamente la ficha "Básica" y la ficha
básica no gana catálogo ni gana filtros.

## Relacionados

`27` el predictor de categoría · `31` ficha técnica y atributos · `32` obligatorios vs opcionales ·
`43` indicador de calidad · `63` ganar el catálogo · `180` los endpoints ·
`181` publicar un ítem por API · `193` límites de uso
