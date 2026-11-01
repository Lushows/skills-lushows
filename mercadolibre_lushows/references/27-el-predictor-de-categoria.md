# El predictor de categoría

Mercado Libre tiene un modelo que, a partir del nombre de un producto, te dice en qué categoría y
en qué "dominio" va. Es la forma más rápida y menos opinada de resolver `26`. Funciona desde el
panel cuando publicas y también por API, gratis y sin autenticación.

## Por panel

Cuando creas una publicación, ML te pide el nombre del producto antes que nada y devuelve una o
varias categorías sugeridas. Eso es el predictor.

```
□ Escribe el nombre REAL del producto, como lo diría el comprador
□ No escribas todavía el título completo con especificaciones
□ Anota las 2-3 sugerencias, no aceptes la primera de una
□ Contrasta con la miga de pan de los líderes de esa búsqueda (`26`)
```

Si escribes "organizador" te va a sugerir cualquier cosa. Si escribes "organizador de cubiertos
para cajón de cocina", la sugerencia sirve.

## Por API

```
GET https://api.mercadolibre.com/sites/MCO/domain_discovery/search?q=parlante+bluetooth&limit=3
```

(ALTA — endpoint oficial, `MCO` es el site de Colombia.) No requiere token para consultar.

Parámetros:

| Parámetro | Qué es |
|---|---|
| `sites/MCO` | Colombia. Argentina `MLA`, México `MLM`, Chile `MLC`, Perú `MPE`, Brasil `MLB` |
| `q` | El nombre del producto, con `+` o `%20` en vez de espacios |
| `limit` | Cuántas sugerencias quieres (3 es suficiente) |

Respuesta (forma típica):

```json
[
  {
    "domain_id": "MCO-SPEAKERS",
    "domain_name": "Parlantes",
    "category_id": "MCO1000",
    "category_name": "Parlantes y Bocinas",
    "attributes": [{ "id": "BRAND", "value_name": "JBL" }]
  }
]
```

Lo que te importa de ahí:

| Campo | Para qué lo usas |
|---|---|
| `category_id` | Es lo que va en el ítem al publicar (`175` en adelante) |
| `domain_name` | Te confirma en palabras si el modelo te entendió |
| `attributes` | El predictor a veces ya te extrae marca o modelo del texto |

## El flujo completo, encadenado

Este es el orden que evita el 90% de los errores de ficha:

```
□ 1. GET /sites/MCO/domain_discovery/search?q=<producto>&limit=3   → category_id
□ 2. GET /categories/$CATEGORY_ID                                   → nombre, ruta, estado
□ 3. GET /categories/$CATEGORY_ID/attributes                        → qué te van a exigir (`31`)
□ 4. Simulador de costos del panel, logueado                        → cuánto te cuesta (`76`)
```

Con esos cuatro pasos sabes, antes de escribir una sola letra del título: dónde vas, qué datos
tienes que conseguir y cuánto te va a costar cada venta. **Ninguna decisión de publicación debería
tomarse antes de correr esas cuatro consultas.**

Ojo con el paso 4: la API `GET /sites/MCO/listing_prices` **ya no es pública**. Hoy responde
`403 PA_UNAUTHORIZED_RESULT_FROM_POLICIES` y exige token. La comisión se lee logueado en el
simulador de costos (`76`). Lo público es solo el rango **8%-22%** (oficial ML Colombia,
verificado sep-2026).

## Cómo probarlo sin saber programar

Pega la URL completa en el navegador. Devuelve texto JSON: feo, pero legible. Busca
`"category_name"` y `"category_id"` con Ctrl+F.

Si quieres verlo ordenado, pídele a Claude que lo consulte y te lo traduzca a una tabla.

## Cuándo el predictor se equivoca

| Caso | Por qué falla | Qué hacer |
|---|---|---|
| Producto de nicho sin nombre estándar | El modelo no tiene ejemplos | Busca en ML y copia la rama del líder |
| Kit o combo | Le das dos productos a la vez | Corre el predictor solo con el producto principal (`48`) |
| Servicio o digital | La lógica es otra | Ve directo a `49` |
| Nombre inventado de tu marca | No hay señal de producto | Escribe el genérico: "vela aromática", no "Velaluz Premium" |
| Repuesto compatible | Lo manda a la marca original | Fuerza la rama de repuestos y usa el atributo de compatibilidad |

## El error clásico

Correr el predictor con el título ya armado y lleno de especificaciones. El modelo se distrae con
"12 meses garantía envío inmediato" y te manda a cualquier lado. **Predice con el sustantivo,
publica con el título.**

El segundo error: confiar en un `category_id` copiado de otro país. Los IDs de `MLA` o `MLM` no
sirven en `MCO`, ni siquiera cuando la categoría se llama igual.

## Verificación rápida

```
□ El domain_name que devolvió describe mi producto en palabras
□ El category_id empieza por "MCO"
□ Los atributos obligatorios de esa categoría tienen sentido para mi producto
□ Al menos un competidor real que venda está en esa misma rama
□ Ya leí la comisión de esa categoría antes de decidir el precio
```

## Relacionados

`26` elegir categoría · `28` el título · `31` ficha técnica y atributos · `32` obligatorios vs
opcionales · `48` kits y combos · `49` servicios y digitales · `75` comisiones · `181` publicar
por API · `180` endpoints de referencia
