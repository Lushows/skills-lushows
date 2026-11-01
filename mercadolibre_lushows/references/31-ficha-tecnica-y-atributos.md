# Ficha técnica y atributos

Los atributos son los campos estructurados de tu publicación: marca, modelo, material, capacidad,
color, medidas. No son decoración. **Son lo que alimenta los filtros de la izquierda del buscador**,
y si no los llenas, desapareces cada vez que un comprador filtra.

## Qué son y de dónde salen

Los atributos dependen 100% de la categoría (MEDIA-ALTA). Los de "Licuadoras" no se parecen a los
de "Camisetas". Para saber cuáles te van a exigir, antes de publicar:

```
GET https://api.mercadolibre.com/categories/$CATEGORY_ID/attributes
```

(ALTA.) El `category_id` lo sacaste del predictor (`27`).

Cada atributo trae, entre otras cosas:

| Campo | Qué significa |
|---|---|
| `id` | El código interno: `BRAND`, `MODEL`, `COLOR`, `CAPACITY` |
| `name` | Cómo se llama en español en el formulario |
| `value_type` | `string`, `number_unit`, `list`, `boolean` |
| `values` | Si es lista, los valores permitidos |
| `tags.required` | Obligatorio para publicar (`32`) |
| `tags.catalog_required` | Obligatorio solo para entrar a catálogo (`32`) |

## Por qué los filtros lo son todo

El comprador que filtra ya decidió comprar. Está acotando. Es el tráfico de mayor intención de todo
el marketplace, y **sin el atributo lleno quedas fuera de ese filtro** (MEDIA).

| Comprador | Filtro que usa | Si no llenaste... |
|---|---|---|
| Busca licuadora para hielo | Potencia ≥ 600 W | El atributo Potencia → invisible |
| Busca camiseta talla L | Talla | El atributo Talla → invisible |
| Busca olla para inducción | Tipo de cocina compatible | Ese atributo → invisible |
| Busca repuesto de su modelo | Compatibilidad | Ese atributo → invisible |

No es que bajes de posición: es que **no estás en esa lista**. Es la diferencia entre el puesto 40
y el cero absoluto.

## Ficha incompleta = riesgo de pausa

Una ficha incompleta es causa citada de pausas, revisiones y bloqueos (MEDIA). El caso típico:
publicas con lo mínimo, vendes un poco, y un día aparece "Inactiva para revisar". Eso es temporal y
se reactiva al corregir (MEDIA, ver `73`), pero mientras tanto no vendes y rompes tu racha de
conversión.

## Cómo conseguir los datos que no tienes

| Dato que falta | Dónde sacarlo |
|---|---|
| Medidas y peso | Mídelo tú con balanza y metro. No lo inventes: el envío se cotiza con eso (`109`) |
| Material | Etiqueta del producto o ficha del proveedor |
| Modelo | Caja, manual o placa del producto |
| Potencia, voltaje | Placa del producto |
| Marca de un genérico | Usa el valor "Genérico" / "Sin marca" que ofrece la lista |
| Código EAN / GTIN | Caja del producto. Es clave para catálogo (`62`) |

**Un atributo inventado es peor que uno vacío**: un dato falso en la ficha es reclamo de "producto
distinto al anunciado", y ese tipo de reclamo **no es excluible** de tu reputación (ALTA, ver
`136`).

## Atributos que casi siempre pesan más

| Atributo | Por qué |
|---|---|
| `BRAND` (Marca) | Filtro de primera línea en casi toda categoría |
| `MODEL` (Modelo) | Permite entrar a catálogo y ser comparado (`62`) |
| `GTIN` / EAN | Identificación universal; catálogo lo pide |
| Color | Base de variaciones (`40`) |
| Medidas y peso | Cotización de envío y filtro de tamaño |
| Garantía | Filtro y confianza (`50`) |

## El flujo correcto

```
□ 1. Predictor → category_id (`27`)
□ 2. GET /categories/$ID/attributes → lista completa
□ 3. Separa: los que traen tags.required y el resto (`32`)
□ 4. Consigue los datos reales que te faltan ANTES de abrir el formulario
□ 5. Llena TODOS, no solo los obligatorios
□ 6. Revisa el indicador de calidad después de guardar (`46`)
```

## El error clásico

Llenar solo los campos que el formulario marca en rojo y darle publicar. El formulario te deja
publicar con el mínimo; el buscador no te deja aparecer con el mínimo. **Los obligatorios te dejan
publicar; los opcionales te dejan vender.**

## Errores concretos que cuestan filtros

| Error | Efecto |
|---|---|
| Poner el color en el título y no en el atributo | Fuera del filtro de color |
| Escribir "Genérica" a mano en vez de elegir de la lista | Valor no reconocido, no filtra |
| Medidas en unidades mezcladas (cm y pulgadas) | Datos incomparables |
| Dejar la garantía vacía | Fuera del filtro de garantía, menos confianza (`50`) |
| Marca escrita distinto en cada publicación ("JBL", "jbl", "J.B.L") | Tus propios ítems no se agrupan |

## Mantenimiento

Los atributos de una categoría cambian: ML agrega campos nuevos. Cada tanto vuelve a correr
`GET /categories/$ID/attributes` sobre tus categorías principales y compara con lo que tienes
lleno. Si manejas muchos SKUs, esto se automatiza (`182`).

## Relacionados

`27` el predictor · `32` obligatorios vs opcionales · `40` variaciones · `46` indicador de
calidad · `47` llegar a Profesional · `50` garantía · `62` catálogo · `73` pausas · `136` reclamos
no excluibles · `182` mantener fichas por API
