# Topics y payload

Un topic es el tipo de evento al que te suscribes; el payload es lo que Mercado Libre te manda
cuando ocurre. Lo más importante de este módulo cabe en una línea: **el payload no trae el dato,
trae la dirección donde está el dato.**

## La lista de topics

| Topic | Qué avisa |
|---|---|
| `orders_v2` | Ventas. **Reemplaza al `orders` v1: usa siempre este** |
| `questions` | Preguntas nuevas en tus publicaciones |
| `items` | Cambios en tus publicaciones |
| `messages` | Mensajes de posventa |
| `shipments` | Cambios de estado de un envío |
| `payments` | Movimientos de pago |
| `orders_feedback` | Calificaciones |
| `claims` | Reclamos |
| `quotations` | Cotizaciones |
| `invoices` | Facturas |
| `items_prices` | Cambios de precio en tus ítems |
| `item_competition` | Competencia sobre tus ítems |
| `catalog_suggestions` | Sugerencias de catálogo |
| `stock_fulfillment` | Stock en Full |
| `stock_locations` | Stock por ubicación |

(oficial ML, verificado sep-2026)

`orders` v1 sigue apareciendo en tutoriales viejos. **Si tu código dice `orders` a secas, está
desactualizado: es `orders_v2`.**

## El payload

Lo que llega a tu `callback_url` es un POST con un JSON de esta forma:

```json
{
  "_id": "a1b2c3d4-0000-1111-2222-333344445555",
  "resource": "/orders/2000009876543210",
  "user_id": 123456789,
  "topic": "orders_v2",
  "application_id": 1234567890123456,
  "attempts": 1,
  "sent": "2026-09-14T15:04:05.000Z",
  "received": "2026-09-14T15:04:05.100Z"
}
```

## Campo por campo

| Campo | Qué es | Para qué lo usas |
|---|---|---|
| `_id` | Identificador único de **la notificación** | Deduplicar (`192`) |
| `resource` | La **ruta** del recurso que cambió | Hacerle el `GET` |
| `user_id` | De qué cuenta es | Elegir el token correcto si manejas varias |
| `topic` | Qué tipo de evento | Enrutar al worker que corresponde |
| `application_id` | Tu app | Verificar que es para ti |
| `attempts` | Número de intento | Si es > 1, ya fallaste antes: alarma |
| `sent` | Cuándo lo mandó ML | Medir tu latencia real |
| `received` | Cuándo lo recibió el sistema | Comparar con `sent` |

## LO IMPORTANTE: el payload solo trae la referencia

En el ejemplo de arriba no hay precio, no hay comprador, no hay producto. Solo
`"/orders/2000009876543210"`. Para saber qué pasó, tienes que llamar:

```
GET https://api.mercadolibre.com/orders/2000009876543210
Authorization: Bearer APP_USR-...
```

El `resource` viene como **ruta relativa**: le antepones el host `https://api.mercadolibre.com`.

Esto tiene tres consecuencias de diseño:

| Consecuencia | Detalle |
|---|---|
| Necesitas token válido al procesar | Si venció, el aviso llega y no puedes leerlo (`178`) |
| El `GET` va **después** de responder 200 | Nunca antes: no cabe en 500 ms (`191`) |
| Lees el estado actual, no el del evento | Con dos avisos seguidos, el 2º ya trae el final |

Esa última es una ventaja escondida: **como siempre relees el estado actual, procesar un aviso
viejo no te deja datos viejos.** Reduce mucho el daño de los duplicados.

Y es también tu defensa de seguridad: como el contenido real lo traes tú desde la API con tu
token, una notificación inventada por un tercero no puede meterte datos falsos.

## Qué `resource` trae cada topic

| Topic | Forma del `resource` | Qué haces |
|---|---|---|
| `orders_v2` | `/orders/$ORDER_ID` | `GET` la orden (`185`) |
| `questions` | `/questions/$QUESTION_ID` | `GET` la pregunta (`187`) |
| `items` | `/items/$ITEM_ID` | `GET` el ítem |
| `shipments` | `/shipments/$SHIPMENT_ID` | `GET` el envío y sus costos (`186`) |
| `messages` | Referencia al mensaje o al pack | Leer el hilo (`188`) |

## El patrón de procesamiento

```
1. Llega el POST
2. Validas minimo: tiene _id, resource, topic y application_id es el tuyo
3. Encolas {_id, resource, topic, user_id}
4. RESPONDES 200                                <- antes de los 500 ms (`191`)
5. Un worker aparte:
     5a. Verifica que el _id no se haya procesado ya (`192`)
     5b. GET https://api.mercadolibre.com + resource
     5c. Valida la FORMA de la respuesta, no solo que sea 200 (`199`)
     5d. Procesa
     5e. Marca el _id como procesado
```

## Qué guardar de cada aviso

```
□ _id y resource, para deduplicar
□ topic y user_id, para enrutar
□ attempts y sent, para medir salud
□ El resultado: procesado, fallido o ignorado
□ Todo esto ANTES de procesar, no despues
```

## El error clásico

Confiar en el contenido del payload. Como el JSON trae campos de aspecto informativo (`sent`,
`user_id`), hay quien construye lógica sobre ellos e incluso quien asume que en algún topic vendrá
el dato completo. No viene, en ninguno. **El aviso dice "mira ahí", nunca dice "esto pasó".**

El segundo error: suscribirse a `orders` en vez de `orders_v2` copiando un tutorial de hace tres
años, y no entender por qué la forma del aviso no cuadra con nada.

## Relacionados

`178` tokens · `185` las órdenes · `186` los envíos · `187` las preguntas ·
`188` mensajes de posventa · `189` webhooks: configuración · `191` responder en 500 ms ·
`192` duplicados y reintentos · `199` arquitectura de referencia
