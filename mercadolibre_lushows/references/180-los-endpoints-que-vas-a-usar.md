# Los endpoints que vas a usar

Toda la API vive en un solo host, `https://api.mercadolibre.com`, y el site de Colombia es `MCO`.
Este módulo es la tabla de referencia: cada endpoint escrito literalmente, para copiar sin
adivinar. Un endpoint mal escrito es peor que uno ausente, porque el error que devuelve confunde.

## Las dos constantes

| Constante | Valor | Nota |
|---|---|---|
| Host | `https://api.mercadolibre.com` | **Único para todos los países** |
| Site de Colombia | `MCO` | `MLA` AR · `MLM` MX · `MLC` CL · `MPE` PE · `MLB` BR |

El dominio `mercadolibre.com.co` es el portal de compra y la documentación: **la API nunca se
llama contra el dominio del país**. Si ves código que apunta a `api.mercadolibre.com.co`, está mal.

## Autenticación

Casi todo lo privado va con el token en la cabecera:

```
Authorization: Bearer APP_USR-...
```

## Cuenta y usuario

| Qué | Endpoint | Token |
|---|---|---|
| Usuario autenticado | `GET /users/me` | Sí |
| Detalle de un usuario | `GET /users/$USER_ID` | Según el dato |
| Reputación | `GET /users/$USER_ID` → objeto `seller_reputation` | Sí |

Dentro de `seller_reputation` te interesan `level_id` (el color del termómetro),
`power_seller_status` (nivel MercadoLíder), `transactions` y
`metrics.claims / delayed_handling_time / cancellations`. Qué significa cada métrica está en el
bloque de reputación: `125` a `128`.

## Catálogo y categorías

| Qué | Endpoint | Token |
|---|---|---|
| Predictor de categoría | `GET /sites/MCO/domain_discovery/search?q=$Q&limit=3` | No |
| Árbol de categorías del site | `GET /sites/MCO/categories` | No |
| Detalle de una categoría | `GET /categories/$CATEGORY_ID` | No |
| Atributos de la categoría | `GET /categories/$CATEGORY_ID/attributes` | No |

## Publicaciones

| Qué | Endpoint | Token |
|---|---|---|
| Crear publicación | `POST /items` | Sí (`write`) |
| Modificar publicación | `PUT /items/$ITEM_ID` | Sí (`write`) |
| Multi-bodega | `PUT /user-products/$USER_PRODUCT_ID/stock/type/$SELLER_WAREHOUSE` | Sí |

## Costos de publicación

```
GET /sites/MCO/listing_prices?price=50000
```

> 🔴 **Cambió: este endpoint ya NO es público (verificado 14-sep-2026).** Hoy responde **403** con
> el código `PA_UNAUTHORIZED_RESULT_FROM_POLICIES`: **exige token de autenticación**. Si tenías
> código o documentación que lo llamaba abierto, deja de funcionar. Sigue siendo la forma correcta
> de conocer la comisión real de tu categoría — solo que ahora autenticado.

## Órdenes y envíos

| Qué | Endpoint | Token |
|---|---|---|
| Buscar órdenes | `GET /orders/search?seller=$SELLER_ID` | Sí |
| Detalle de orden | `GET /orders/$ORDER_ID` | Sí |
| Detalle de envío | `GET /shipments/$SHIPMENT_ID` | Sí |
| Costos del envío | `GET /shipments/$SHIPMENT_ID/costs` | Sí |

## Preguntas y mensajes

| Qué | Endpoint | Token |
|---|---|---|
| Buscar preguntas de un ítem | `GET /questions/search?item_id=$ITEM_ID&api_version=4` | Sí |
| Responder una pregunta | `POST /answers` (body: `question_id`, `text`) | Sí (`write`) |
| Bloquear a un preguntador | `DELETE /users/$SELLER_ID/questions_blacklist/$USER_ID` | Sí (MEDIA) |
| Mensajes posventa | `GET /messages/packs/$PACK_ID/sellers/$SELLER_ID?tag=post_sale` | Sí |

El `api_version=4` en preguntas no es opcional en la práctica: sin él la forma de la respuesta es
la vieja y tu código se rompe cuando la mueven.

## Pruebas

| Qué | Endpoint |
|---|---|
| Crear usuario de test | `POST /users/test_user` con `{"site_id": "MCO"}` |

## Autenticación (OAuth)

| Qué | Endpoint |
|---|---|
| Canjear el código | `POST /oauth/token` con `grant_type=authorization_code` |
| Renovar | `POST /oauth/token` con `grant_type=refresh_token` |

## Los errores que vas a ver

| Código | Qué significa | Qué haces |
|---|---|---|
| `400` | Payload mal armado, o `invalid_grant` en tokens | Lee el cuerpo: trae `cause` (`179`) |
| `401` | Token vencido o ausente | Refresca y reintenta **una** vez (`178`) |
| `403` | Sin permiso, o el recurso dejó de ser público | Revisa scope; ver `listing_prices` |
| `404` | El recurso no existe o no es tuyo | ML devuelve 404 también por privacidad |
| `429` | Demasiadas peticiones, cuerpo vacío | Espera y reduce ritmo (`193`) |

## Dos hábitos que te ahorran horas

```
□ Pagina SIEMPRE con offset y limit: no asumas que vino todo
□ Registra en log la URL completa y el cuerpo del error, no solo el codigo
□ Verifica la FORMA de la respuesta, no solo que llego un 200 (`199`)
□ Guarda los IDs como texto o entero de 64 bits, nunca de 32 (`199`)
```

## El error clásico

Copiar un `category_id` o un ejemplo de la documentación de Argentina o México y usarlo en
Colombia. Los IDs son por site: un `MLA1234` no existe en `MCO`. **Todo ID que uses tiene que
haberlo devuelto la propia API contra `MCO`.**

## Relacionados

`178` tokens · `181` publicar un ítem · `182` atributos de categoría · `183` precio y stock ·
`185` órdenes · `186` envíos · `187` preguntas · `188` mensajes posventa · `193` límites de uso ·
`194` usuarios de prueba · `199` arquitectura de referencia
