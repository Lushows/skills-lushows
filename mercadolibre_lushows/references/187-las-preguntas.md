# Las preguntas

Una pregunta sin responder es una venta que se va a la competencia. Por API puedes leerlas,
responderlas y bloquear a quien abusa. Es la automatización con mayor efecto por línea de código
después del stock, y la base del bot con IA de `195`.

## Los tres endpoints

| Qué | Endpoint |
|---|---|
| Buscar preguntas de un ítem | `GET /questions/search?item_id=$ITEM_ID&api_version=4` |
| Responder | `POST /answers` — body: `question_id`, `text` |
| Bloquear a un preguntador | `DELETE /users/$SELLER_ID/questions_blacklist/$USER_ID` |

## Leer preguntas

```
GET https://api.mercadolibre.com/questions/search?item_id=MCO123456789&api_version=4
Authorization: Bearer APP_USR-...
```

El `api_version=4` **no es decorativo**: define la forma de la respuesta. Sin él te sirven el
formato viejo y tu código se rompe el día que lo retiren.

Lo que te interesa de cada pregunta:

| Campo | Para qué |
|---|---|
| `id` | El `question_id` que necesitas para responder |
| `text` | Lo que preguntó |
| `status` | `UNANSWERED`, `ANSWERED`, `DELETED`, `BANNED` |
| `item_id` | De qué publicación es |
| `from.id` | Quién preguntó — lo necesitas para bloquear |
| `date_created` | Para medir tu tiempo de respuesta |
| `answer` | Si ya respondiste, viene aquí |

Filtra por `status=UNANSWERED` para trabajar solo lo pendiente.

## Responder

```
POST https://api.mercadolibre.com/answers
Authorization: Bearer APP_USR-...
Content-Type: application/json
```

```json
{
  "question_id": 12345678901,
  "text": "Sí, hay talla 42. Si compras antes de las 2 p.m., el envío sale hoy mismo."
}
```

Una pregunta se responde **una sola vez**: no hay edición. Si respondiste mal, lo único que queda
es aclararlo si el comprador vuelve a preguntar. Por eso todo bot necesita revisión antes de
enviar en los casos dudosos (`195`).

## Lo que la respuesta NO puede contener

Esto no es estilo, es regla de plataforma:

| Prohibido | Detalle |
|---|---|
| Teléfono, WhatsApp, correo, redes | En descripción, imágenes **y** en preguntas y respuestas |
| Invitar a comprar fuera de ML | Es sacar al comprador de la plataforma |
| Spam | También sancionable |

Excepciones donde sí se permite el contacto: **Autos y Motos, Inmuebles, Servicios y
MercadoProveedores** (confianza MEDIA-ALTA). Si no vendes en esas cuatro, asume que está prohibido.

> ⚠️ **Sin verificar para Colombia (sep-2026).** La escala exacta de sanciones por dar datos de
> contacto no está publicada. Lo consistente en todas las fuentes es que se elimina la publicación
> o la pregunta, y que la reincidencia sí puede terminar en sanción de cuenta.

Un bot que suelta un número de teléfono por descuido comete esta infracción **a escala**, en
decenas de publicaciones. Ver `195` y `132`.

## Bloquear a un preguntador

```
DELETE https://api.mercadolibre.com/users/$SELLER_ID/questions_blacklist/$USER_ID
```

(confianza MEDIA — la ruta está documentada pero no se pudo verificar en vivo en sep-2026.)

Úsalo con criterio: para quien insulta, hace spam o pregunta compulsivamente para reventar tu
publicación. No lo uses con un comprador difícil: un bloqueo no arregla una mala respuesta.

## La velocidad importa, pero el número no está confirmado

> ⚠️ **Sin verificar (sep-2026).** El badge de "Responde rápido" asociado a responder en menos de
> 60 minutos **no está confirmado en fuente oficial**. Circula mucho pero no se pudo verificar.

Lo que sí es cierto sin necesidad de badge: quien pregunta está a un paso de comprar, y a las
pocas horas ya compró en otra parte. **Responde rápido porque vende, no porque te den una medalla.**

## Qué automatizar y qué no

| Tipo de pregunta | Automatizar |
|---|---|
| Stock, talla, color, medidas, material | Sí, es dato duro de tu ficha |
| Tiempo y costo de envío a una ciudad | Sí, es dato del sistema |
| Compatibilidad simple | Sí, si está en los atributos |
| Descuentos, negociación, "me lo dejas en..." | **No.** Escala a humano (`195`) |
| Reclamo o problema con una compra | **No.** Va por posventa (`188`) |
| Pedido de contacto | **No.** Respuesta fija que no da contacto |
| Pregunta ambigua o larga | **No.** Escala |

## Lista de chequeo del flujo

```
□ Webhook topic "questions" suscrito (`189`)
□ Al llegar el aviso, GET la pregunta: el payload solo trae la referencia (`190`)
□ Filtrar status UNANSWERED
□ Clasificar: respondible o escalar
□ Si es respondible, POST /answers una sola vez
□ Marcar como procesada en mi base, por question_id (`192`)
□ Alarma si una pregunta lleva mas de 1 hora sin responder
```

## El error clásico

Responder solo lo que preguntaron. "¿Tienen en negro?" → "Sí". Esa respuesta la lee el que
preguntó y **la leen todos los que entran a la publicación después**: es contenido público de tu
ficha. La respuesta buena responde, agrega el dato que falta y cierra. Cómo se escribe eso para
que venda es de `ventas_lushows`.

## Relacionados

`132` prohibido dar contacto · `180` los endpoints · `188` mensajes de posventa ·
`189` webhooks · `190` topics y payload · `192` duplicados · `195` el bot de preguntas con IA
