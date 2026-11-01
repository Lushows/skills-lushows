# Las preguntas como parte de la ficha

Las preguntas de los compradores aparecen **públicas, debajo de la descripción**, y las lee gente
que nunca va a preguntar nada. Son parte de tu publicación aunque no las escribas tú. Bien
manejadas, venden solas; mal manejadas, hunden la ficha a la vista de todos.

## Por qué son parte de la ficha

| Hecho | Consecuencia |
|---|---|
| Son públicas | Un comprador ve las dudas de los otros 20 |
| Se leen antes de comprar | Es el último filtro antes del botón |
| Tu respuesta se ve | El tono con que respondes es tu servicio, en vivo |
| Quedan para siempre | Una respuesta de hace un año sigue ahí |
| Son la lista de objeciones | Materia prima de `34` |

**Nadie lee tu descripción con tanta atención como lee las preguntas de otros.**

## Cómo se responde bien

| Regla | Por qué |
|---|---|
| Rápido | La venta se enfría; el que pregunta está decidiendo hoy |
| Completo | Responder "sí" a "¿tiene garantía?" desperdicia el espacio |
| Con el dato, no con adjetivos | "Mide 38 cm", no "es de buen tamaño" |
| Amable con todos, incluso con el grosero | Lo está leyendo un comprador silencioso |
| Sin datos de contacto | Prohibido también aquí (`132`) |
| Sin prometer lo que no controlas | "Llega mañana" genera reclamos de demora |

Sobre la velocidad:

> ⚠️ **Sin verificar (sep-2026).** El badge de "Responde rápido" con un umbral de 60 minutos **no
> se pudo confirmar en fuente oficial**. No planees nada alrededor de esa cifra. Lo que sí está
> confirmado y es crítico: **si no respondes mensajes en 24 horas hábiles, pierdes el derecho a
> pedir que un reclamo se excluya de tu reputación** (ALTA, `136`).

## La plantilla de respuesta

```
[Saludo corto] + [dato exacto que responde] + [lo que evita la siguiente duda]
```

| Pregunta | ❌ Respuesta pobre | ✅ Respuesta que vende |
|---|---|---|
| ¿Es original? | "Sí" | "Sí, es original, viene sellado de fábrica con su caja y tiene 12 meses de garantía." |
| ¿Sirve para mi cocina? | "Claro que sí" | "Mide 38 cm de ancho. Un cajón de cocina integral estándar tiene 40-45 cm, así que entra. Si el tuyo mide menos de 38, no te va a servir." |
| ¿Cuándo llega? | "Rápido" | "Despacho el mismo día si compras antes de las 2 p.m. El tiempo de entrega lo calcula Mercado Libre según tu dirección y aparece en la ficha." |
| ¿Hay descuento? | "No" | "El precio publicado es el final. Si llevas 2 unidades, tengo publicación de pack con mejor precio por unidad." |

## Preguntas que no son preguntas

| Tipo | Qué hacer |
|---|---|
| Pide tu WhatsApp | Responde amable que por política se atiende por aquí. Nunca lo des (`132`) |
| Ofrece pagarte por fuera | No. Es riesgo de sanción y pierdes toda protección |
| Insulta o provoca | Responde corto y neutro, o bloquea al usuario |
| Hace publicidad de otro vendedor | Elimina y bloquea |
| Pregunta algo ya respondido en la ficha | Responde igual, y agrega ese dato a la descripción (`34`) |

Bloquear a un usuario se puede hacer por API:
`DELETE /users/$SELLER_ID/questions_blacklist/$USER_ID` (MEDIA).

## La mina de oro

Cada pregunta es una objeción que la ficha no resolvió. El ciclo correcto:

```
□ 1. Responde la pregunta en menos de unas horas
□ 2. Anótala en una lista, con su tema
□ 3. Cada semana, mira qué tema se repitió
□ 4. Sube ese tema a la descripción (`34`) o a las fotos (`36`)
□ 5. La semana siguiente esa pregunta debería aparecer menos
```

Si el mismo tema sigue apareciendo después de haberlo escrito, el problema no es la descripción: es
que está escondido o mal redactado.

Para leerlas por API:
`GET /questions/search?item_id=$ITEM_ID&api_version=4` (ALTA)
y responder: `POST /answers` con `question_id` y `text` (ALTA). Ver `187`.

## Automatizar sin sonar a robot

Se puede montar un bot que responda preguntas (`187`), y en volumen alto es necesario. Reglas para
que no te cueste ventas:

| Sí | No |
|---|---|
| Respuestas automáticas para las 5 preguntas idénticas de siempre | Respuesta genérica para todo |
| Escalar a humano lo que no reconoce | Contestar cualquier cosa por contestar |
| Revisar cada semana qué respondió el bot | Dejarlo solo |

Una respuesta automática equivocada es pública y permanente.

## El error clásico

Dejar preguntas sin responder. Una pregunta de hace cinco días sin respuesta, a la vista de todos,
dice "aquí no hay nadie". El que la hizo ya compró en otro lado, y los que la leen tampoco compran.
**Una pregunta sin responder no es una venta perdida: son todas las que la leyeron.**

## Chequeo

```
□ Cero preguntas sin responder
□ Ninguna respuesta de una sola palabra
□ Ninguna respuesta con contacto, redes ni promesas de entrega que no controlo
□ Las 5 preguntas más repetidas ya están en la descripción (`34`)
□ Reviso las preguntas de mis competidores cada mes (`53`)
□ Respondo mensajes de posventa en menos de 24 horas hábiles (`136`)
```

## Relacionados

`34` responder objeciones · `33` la descripción · `36` fotos · `52` las opiniones · `53` estudiar al
líder · `136` reclamos y el corte de 24 horas · `134` mensajería posventa · `132` contacto
prohibido · `187` preguntas por API · persuasión y cierre → `ventas_lushows`
