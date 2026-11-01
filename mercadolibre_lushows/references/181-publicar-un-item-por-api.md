# Publicar un ítem por API

`POST /items` crea una publicación. El JSON no es largo, pero cada campo decide algo que después
cuesta cambiar: la categoría fija los atributos obligatorios y el `listing_type_id` fija la
comisión. Este módulo desarma el payload campo por campo.

## El JSON mínimo

```json
{
  "title": "Nombre del producto",
  "category_id": "MCO1234",
  "price": 10000,
  "currency_id": "COP",
  "available_quantity": 50,
  "buying_mode": "buy_it_now",
  "listing_type_id": "gold_special",
  "condition": "new",
  "pictures": [{ "source": "https://misitio.com/imagen1.jpg" }],
  "attributes": [{ "id": "BRAND", "value_name": "Marca genérica" }]
}
```

```
POST https://api.mercadolibre.com/items
Authorization: Bearer APP_USR-...
Content-Type: application/json
```

## Campo por campo

| Campo | Qué es | Trampa |
|---|---|---|
| `title` | El título. Límite **60 caracteres** | Sin símbolos, sin promesas, sin contacto (`29`) |
| `category_id` | Categoría, empieza por `MCO` | Sale del predictor (`27`, `182`), no la inventes |
| `price` | Precio **con IVA**, número sin separadores | Mínimo **$2.900**; nunca `"10.000"` |
| `currency_id` | `COP` para Colombia | Un `ARS` copiado de un ejemplo rompe la publicación |
| `available_quantity` | Unidades disponibles | `0` la pasa a pausada (`183`) |
| `buying_mode` | `buy_it_now` (compra inmediata) | Es lo normal hoy |
| `listing_type_id` | El tipo de publicación | Define tu comisión y si hay cuotas |
| `condition` | `new`, `used` o `not_specified` | Usado tiene reglas propias de devolución (`137`) |
| `pictures` | Lista de objetos con `source` | URLs públicas, ML las descarga |
| `attributes` | Lista de `{id, value_name}` | Los obligatorios se descubren con `182` |

## `listing_type_id`: el nombre técnico no es el nombre comercial

Aquí hay un desfase que tienes que tener presente al integrar: **la API sigue usando los valores
técnicos viejos, mientras la interfaz que ve el vendedor en Colombia usa nombres nuevos.**

| Valor de la API | Nombre viejo | Cómo se llama hoy en Colombia |
|---|---|---|
| `gold_special` | Clásica | Publicación con **cuotas con 0% interés** |
| `gold_pro` | Premium | Publicación con **cuotas extra** |
| `free` | Gratuita | **Gratuita** |

Colombia ya no dice "Clásica" ni "Premium" (esos nombres siguen vigentes en otros países). Si tu
panel propio muestra "Premium" y el vendedor busca esa palabra en Mercado Libre, no la encuentra.
**Manda el valor técnico a la API; muestra el nombre comercial al humano.**

## Lo que cuesta cada opción

Crear la publicación no cuesta nada; el cargo llega al concretar la venta:

> "Cuando concretes la venta, pagarás **entre 8% y 22%** según la categoría de tu producto y la
> cantidad de cuotas que elijas ofrecer." (oficial ML Colombia, verificado sep-2026)

| Precio del producto | Cuotas con 0% interés | Cargo por venta |
|---|---|---|
| Menos de $499.999 | Hasta 3 | **8% a 19%** |
| Menos de $499.999 | Cuotas extra, hasta 6 | **11% a 22%** |
| $500.000 a $1.499.999 | Hasta 6 | **8% a 19%** |
| $500.000 a $1.499.999 | Cuotas extra, hasta 9 | **11% a 22%** |
| Más de $1.500.000 | Hasta 12 | **8% a 19%** |

**Ofrecer cuotas extra cuesta exactamente 3 puntos porcentuales más.** Ese es el número que decide
si mandas `gold_special` o `gold_pro`, y se decide por producto, no de una vez para todo.

La comisión exacta de **tu** categoría dentro de ese 8%-22% no es pública: se lee logueada en el
simulador de costos, o por API con `GET /sites/MCO/listing_prices?price=50000` — **ese endpoint ya
exige token desde 2026** (`180`, `193`).

Nota: los productos de la sección **Supermercado** pagan otros costos.

## El precio mínimo: $2.900

> "El precio de tu producto debe ser **igual o superior a $2.900**." (oficial ML Colombia,
> verificado sep-2026)

Para quien integra esto es una regla de validación, no un consejo: **si tu `POST /items` manda un
`price` menor a $2.900, Mercado Libre lo rechaza.** Valídalo en tu código antes de llamar, o vas a
depurar un error de publicación que en realidad es de negocio.

Si vendes cosas más baratas que eso, la salida oficial es armar packs o combos (`48`).

Y recuerda: los usuarios de prueba **no pueden publicar en `gold` ni `gold_premium`** (`194`).

## Las fotos

`pictures` acepta URLs públicas que ML descarga y rehospeda. Reglas que aplican igual que por
panel:

```
□ La primera foto es la principal: fondo blanco puro, solo el producto
□ 1200x1200 px estandar; el zoom se habilita desde 1200 px de lado
□ JPG / JPEG / PNG, hasta 10 MB
□ La URL debe ser accesible sin login: si tu servidor la protege, ML no la baja
```

El detalle fotográfico completo está en el bloque `36`-`41`. Aquí solo el mecanismo.

## Descripción, aparte

La descripción **no va dentro del `POST /items`** en el flujo moderno: se manda como recurso
propio del ítem una vez creado. Si tu librería la acepta embebida, verifica en la respuesta que
efectivamente quedó guardada, no asumas.

## Variaciones

Si vendes tallas o colores, van como **variaciones de un mismo ítem**, no como publicaciones
separadas. Cada variación lleva sus propias combinaciones de atributos, su stock y sus fotos. Es
además uno de los objetivos del indicador de calidad "Profesional": usar variaciones en vez de
publicaciones sueltas (`43`).

## La secuencia correcta

```
□ 1. GET /sites/MCO/domain_discovery/search?q=<producto>&limit=3   -> category_id
□ 2. GET /categories/$CATEGORY_ID/attributes                        -> obligatorios (`182`)
□ 3. Arma attributes[] con TODOS los de tags.required
□ 4. Valida que el precio sea >= 2900 y sube las fotos a una URL publica
□ 5. POST /items
□ 6. Lee el ITEM_ID de la respuesta y guardalo en tu base
□ 7. Carga la descripcion
□ 8. Abre la publicacion en el navegador y mirala con ojos de comprador
```

## Leer la respuesta

Un `POST /items` exitoso devuelve el ítem completo, incluido el `id` (`MCO123456789`). Guárdalo:
es la llave de todas las operaciones posteriores.

Si falla, el cuerpo del error trae un arreglo `cause` con el campo culpable. **Ese arreglo es la
única información útil: no lo descartes en tu log.** Los errores más frecuentes:

| Mensaje típico | Causa |
|---|---|
| Falta un atributo requerido | No corriste `182` |
| Categoría inválida o de otro site | Copiaste un ID de `MLA` o `MLM` |
| Precio inválido | Lo mandaste como texto, con separadores, o por debajo de $2.900 |
| Imagen no descargable | La URL pide login o dio timeout |

## El error clásico

Publicar por API a las carreras para "probar que funciona" y dejar la ficha incompleta. El
algoritmo evalúa la publicación en sus **primeras 48-72 horas** y la etiqueta de baja conversión
que le cuelga después cuesta muchísimo quitar (`56`). **Por API es tan caro publicar mal como por
panel: la velocidad no te exime de la ficha completa.**

Si solo quieres probar el mecanismo, hazlo con un usuario de test (`194`) y el título
"Item de Prueba - Por favor, NO OFERTAR", no con tu cuenta real.

## Relacionados

`27` el predictor de categoría · `29` lo prohibido en el título · `43` indicador de calidad ·
`48` kits y combos · `56` la ventana de 48-72 horas · `76` la comisión de tu categoría ·
`180` los endpoints · `182` atributos de categoría · `183` precio y stock ·
`193` límites de uso · `194` usuarios de prueba
