# La encuesta post-compra (manual completo)

> Vigencia: 15-sep-2026. Precios y tasas: rangos, **verificar** con el proveedor y con tus propios datos.

## La regla de oro

**Se pregunta cuando la compra está fresca y el cliente está contento**: la página de gracias, justo
después del checkout. Diez minutos después ya cerró la pestaña; dos días después no recuerda dónde te
vio. Y segunda regla: **una pregunta en el momento de la compra, el resto por correo**. Cada pregunta
extra en la página de gracias te cuesta tasa de respuesta.

## Arquitectura de tres momentos

| Momento | Cuándo | Cuántas preguntas | Objetivo | Tasa de respuesta esperable |
|---|---|---|---|---|
| **M1 — Página de gracias** | 0 segundos post-checkout | 1 (máx. 2) | Atribución: "¿cómo nos conociste?" | Alta (es el momento de mayor disposición). Establece tu propio piso con los primeros 100 pedidos |
| **M2 — Correo post-entrega** | 3–5 días después de entregado | 2–3 | Motivo de compra, dudas previas, alternativa considerada | Baja. Muy por debajo de M1 |
| **M3 — Correo de resultado** | 25–35 días después (ciclo de uso del suplemento) | 2–3 + invitación a entrevista | Experiencia, reseña, recompra, reclutar para `313` | La más baja de las tres |

No hagas los tres desde el día uno: **empieza solo con M1**; cuando lo estés leyendo cada semana, agregas M2, y M3 al mes siguiente.

## Dónde va, técnicamente

| Plataforma | Cómo montar M1 |
|---|---|
| Shopify | App del App Store (Fairing, KnoCommerce). Sin app: campo en la página de estado del pedido, guardado como nota o etiqueta del pedido |
| WooCommerce | Plugin de encuestas o campo extra en la página de "pedido recibido" |
| Tienda propia / landing directa | Redirigir a una página de gracias propia con un formulario embebido (Tally, Typeform, Google Forms) |
| Venta por WhatsApp (COD o prepago asistido) | El mensaje de confirmación del pedido incluye la pregunta. Tasa de respuesta alta porque ya hay conversación |

Para este proyecto (México, **prepago**, stock local): el checkout es estándar, así que **M1 va en la
página de gracias** y M2/M3 salen por correo, que ya tienes porque el prepago te obliga a pedir mail.

## Herramientas 2026

| Herramienta | Qué es | Fuerte en | Cuándo te conviene |
|---|---|---|---|
| **Fairing** | Especializada en "how did you hear about us" | Liga **cada respuesta al pedido y al valor de vida del cliente** (LTV) | Cuando tu pregunta principal es atribución y quieres saber qué canal trae clientes que valen más |
| **KnoCommerce** | Plataforma de dato de parte cero | IA sobre las respuestas abiertas, modelos de atribución **primer clic / último clic / personalizado**, benchmarking contra otras marcas. Procesa **casi 2 millones de respuestas al mes** de **más de 1.200 marcas** | Cuando quieres leer respuestas abiertas a escala y comparar contra un benchmark |
| **Bizrate Insights** | Encuestas de experiencia de compra | Encuestas de sitio y post-entrega | Enfoque más de experiencia que de atribución |
| **Cometly / AdsX** | Análisis y atribución | Cruzan encuesta con datos de campaña | Cuando ya tienes gasto suficiente para que el cruce importe |
| **Tally / Google Forms + página de gracias** | Formulario genérico | Coste cero | Arranque con capital <USD 500. Pierdes el ligado automático al pedido |

Precio: los planes de estas apps arrancan bajos y escalan por volumen de respuestas o pedidos —
**verificar el precio vigente antes de contratar**, cambia seguido. Con <USD 500 de capital, la
decisión honesta es: **arranca con formulario gratuito ligado a un campo del pedido**, y cuando pases
un volumen que te duela leer a mano (~300 pedidos/mes como referencia propia), pagas la app.

## Las preguntas exactas (español mexicano, listas para copiar)

### M1 — Página de gracias. Una sola pregunta.

```
¡Gracias por tu compra! Una última cosa, nos ayuda muchísimo:

¿Dónde nos conociste?

( ) TikTok
( ) Instagram
( ) Facebook
( ) Me lo recomendó alguien
( ) Google / buscando
( ) YouTube
( ) Ya los conocía / soy cliente
( ) Otro: ______________
```

Reglas de la lista de opciones:

| Regla | Por qué |
|---|---|
| Máximo 7 opciones + "Otro" abierto | Más opciones = más abandono y más ruido |
| "Otro" **siempre** abierto y obligatorio de escribir | Ahí aparecen los canales que no sabías que existían |
| Nunca pongas "Anuncio de Facebook" y "Facebook" como opciones separadas | El cliente no distingue anuncio de post. Te ensucia el dato |
| Rota el orden de las opciones si tu herramienta lo permite | Evita el sesgo de la primera opción |
| No pongas la opción "No recuerdo" | El que no recuerda deja "Otro" en blanco y eso ya te informa |

### M1 opcional — segunda pregunta solo si M1 ya rinde

```
En una frase, ¿qué te hizo decidirte hoy?
[ campo abierto, sin límite visible ]
```

Esta es la pregunta más rentable de todo el bloque. Sus respuestas son materia prima directa de `315`.

### M2 — Correo 3–5 días post-entrega

```
Asunto: Una pregunta rápida (30 segundos) 🙌

Hola [nombre]:
Ya te llegó tu pedido y queremos hacerlo mejor. Tres preguntas cortas:

1. ¿Qué te hizo pensar "esto sí lo necesito"?
   [ abierto ]

2. ¿Qué casi te detiene antes de comprar?
   ( ) El precio
   ( ) No sabía si iba a funcionar para mí
   ( ) No conocía la marca
   ( ) El tiempo de envío
   ( ) Dudaba de comprar por internet
   ( ) Nada, lo compré de inmediato
   ( ) Otro: ______

3. Antes de comprarnos, ¿qué otra cosa estabas considerando?
   [ abierto ]
```

### M3 — Correo 25–35 días

```
Asunto: ¿Cómo te fue? (y algo para ti)

1. ¿Lo estás usando como pensabas? ( ) Sí  ( ) Más o menos  ( ) Lo dejé
2. Si un amigo te preguntara por esto, ¿qué le dirías? [ abierto ]
3. ¿Nos regalas 15 minutos por videollamada o WhatsApp? Te damos [incentivo].
   ( ) Sí, escríbanme  ( ) Ahora no
```

La pregunta 2 de M3 produce testimonios utilizables (`185`) y la 3 alimenta `313`.

## Lo que NO debes preguntar

| Pregunta prohibida | Por qué |
|---|---|
| "¿Te gustó el producto?" | Nadie contesta que no en un correo de la marca. Dato inútil |
| "¿Qué mejorarías?" en M1 | Todavía no lo usó. Le estás pidiendo que invente |
| Cualquier pregunta sobre efectos en su salud | Con suplementos y belleza en México, recoger testimonios de efecto fisiológico te crea material que **no puedes usar** y que te expone (COFEPRIS, política de Meta). Ver `07` |
| "¿Cuánto pagarías por esto?" o datos personales que no necesitas | La gente miente sobre precio hipotético (el precio se prueba vendiendo, `103`); los datos de más bajan la respuesta y suben tu carga de protección de datos |

## Cómo se lee (el ritual de 20 minutos)

Viernes, 20 minutos, hoja de cálculo con estas columnas:

| Fecha | Pedido | Canal declarado | Frase literal | Dolor detectado | Objeción | ¿Sirve para hook? |
|---|---|---|---|---|---|---|

Reglas del ritual:

1. **Copia la frase literal.** No la resumas, no la corrijas de estilo. Solo ortografía.
2. Marca una frase como candidata a hook solo si es **específica** (menciona un momento, un objeto o
   una escena), no si es un elogio genérico.
3. Cuenta menciones. **Cinco menciones independientes del mismo dolor = patrón.** Menos de eso es
   anécdota y no mueve la oferta.
4. Las candidatas van al swipe file (`99`) con la etiqueta `voz-cliente`.

## Errores de implementación

| Error | Síntoma | Arreglo |
|---|---|---|
| La encuesta aparece antes de confirmar el pago | Respuestas de gente que no compró | Dispararla solo en la página de gracias real |
| Opciones que se solapan | 40% en "Otro" con respuestas que ya estaban en la lista | Reescribir opciones con el vocabulario del cliente, no el tuyo |
| No guardas el ID de pedido junto a la respuesta | No puedes cruzar con valor de pedido ni con LTV | Ligar respuesta ↔ pedido desde el día uno |
| Español formal, o correo M2 desde un dominio sin autenticar | Responden poco, o te vas a spam y crees que "nadie contesta" | Tuteo y frases cortas; verificar SPF/DKIM antes de culpar a la pregunta |

## Relacionados

`310` por qué el cliente sabe lo que la biblioteca no · `312` atribución de dato cero · `313` entrevistar compradores · `314` minería de reseñas · `315` del hallazgo al ángulo · `185` prueba social y reseñas · `99` swipe file · `07` ética y legalidad · `103` inteligencia de precios · `284` reseñas y reputación
