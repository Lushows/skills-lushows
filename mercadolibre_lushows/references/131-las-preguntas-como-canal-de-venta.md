# Las preguntas como canal de venta

Las preguntas de una publicación son **públicas**. Le respondes a una persona y la respuesta queda
ahí para todos los que lleguen después. Eso convierte cada pregunta en una oportunidad de editar tu
ficha en vivo, con las palabras exactas del comprador.

## Por qué son distintas a un chat

| | Pregunta pública | Mensaje posventa |
|---|---|---|
| Quién la ve | Cualquiera que entre a la publicación | Solo el comprador |
| Cuándo ocurre | Antes de comprar | Después de comprar |
| Qué decide | Si compra o se va | La experiencia y la opinión (`134`) |
| Se puede borrar | Puedes eliminar preguntas de tu publicación | No |

**Una respuesta bien escrita es el único contenido de tu ficha que se escribe con la duda real del
cliente en la mano.** Si tres personas preguntan lo mismo, no es que sean lentos: es que tu ficha no
lo dice (`30`).

## Las cuatro cosas que hace una buena respuesta

```
□ Responde la pregunta, primero y completa. Nada de "hola, gracias por escribir" arriba
□ Agrega el dato que la persona no sabía que necesitaba (medida, compatibilidad, qué incluye)
□ Cierra con la señal de disponibilidad: stock listo, despacho hoy, llega en X
□ Deja la respuesta escrita para los OTROS cien que van a leerla
```

Ejemplo de la diferencia:

| Mala | Buena |
|---|---|
| "Sí, sirve." | "Sí, es compatible con el modelo 2023 y con el 2022. Trae el adaptador incluido, no necesitas comprar nada aparte. Tengo stock y despacho hoy mismo." |
| "Las medidas están en la descripción." | "Mide 42 × 30 × 18 cm y pesa 1,2 kg. Cabe en un maletín de 15 pulgadas. Lo acabo de agregar a las fotos para que se vea." |

La segunda versión hace tres cosas: contesta, elimina la objeción siguiente y dice que hay stock.

## Qué hacer después de responder

Responder y quedarse ahí desperdicia la mitad del valor. El ciclo completo es:

```
□ Responde la pregunta en público
□ Si la pregunta se repite, AGRÉGALA a la descripción o a los atributos (`30`, `35`)
□ Si es sobre algo que no se ve, agrégalo a las fotos (`38`)
□ Si es sobre una duda que te hace perder ventas, revisa el título (`27`)
```

Una ficha madura es una ficha que ya absorbió sus primeras 50 preguntas. Cuando las preguntas bajan
de volumen pero las ventas suben, vas bien.

## Velocidad

No hay un badge oficial confirmado de "responde rápido", pero la velocidad sí importa por una razón
simple: el comprador que pregunta está comparando ahora. Si respondes mañana, ya compró.

> ⚠️ **Sin verificar para Colombia (sep-2026).** El badge "Responde rápido" asociado a contestar en
> menos de 60 minutos **no está confirmado en fuente oficial**. La cifra circula en blogs. Trátala
> como buena práctica, no como umbral del sistema.

El corte que sí está verificado es otro y es de posventa: si no respondes mensajes en **24 horas
hábiles** pierdes el derecho a excluir un reclamo de tu reputación (oficial ML Colombia, verificado
sep-2026). Ver `133`.

## Lo que no puedes escribir en una respuesta

Las preguntas son uno de los tres lugares donde ML prohíbe datos de contacto — junto con la
descripción y las imágenes. Nada de teléfono, WhatsApp, redes ni correo. Ver `132`, que es un
módulo de riesgo y conviene leerlo entero antes de contestar la primera pregunta.

Tampoco:

| Prohibido | Por qué |
|---|---|
| Ofrecer cerrar la venta por fuera | Es la infracción más cara del marketplace (`132`) |
| Mandar a otra publicación tuya como si fuera otro vendedor | Manipulación |
| Responder con grosería o sarcasmo | Queda público y lo leen los siguientes cien |
| Discutir con quien pregunta de mala fe | Para eso está eliminar y bloquear (`141`) |

## La persuasión

Cómo estructurar una respuesta para que convierta —manejo de objeciones, cierre, lenguaje de
beneficio en vez de característica— **no es tema de esta skill**. Rutea a `ventas_lushows`, que
tiene el oficio completo de objeción y cierre.

Lo que sí es de aquí: la objeción en Mercado Libre casi siempre es una de cuatro, y las cuatro se
responden con datos, no con retórica.

| Objeción real detrás de la pregunta | Con qué se responde |
|---|---|
| "¿Esto es lo que necesito?" | Especificación, compatibilidad, medida |
| "¿Es de verdad?" | Marca, garantía, factura, qué trae la caja |
| "¿Me llega?" | Stock, tiempo de despacho, cobertura |
| "¿Y si sale malo?" | Garantía, devolución, Compra Protegida (`137`) |

## El error clásico

Tratar las preguntas como soporte molesto en vez de como vitrina. El vendedor promedio responde
"sí", "no", "en la descripción" — respuestas que no convencen a quien preguntó y no le sirven a
nadie más. **Cada respuesta corta que das es una venta que le regalas al competidor que sí escribió
tres líneas.**

## Herramientas

| Acción | Cómo |
|---|---|
| Responder | Panel de preguntas, o `POST /answers` con `question_id` y `text` (oficial, verificado sep-2026) |
| Listar preguntas | `GET /questions/search?item_id=$ITEM_ID&api_version=4` |
| Bloquear a un preguntador | `DELETE /users/$SELLER_ID/questions_blacklist/$USER_ID` (confianza media) — ver `141` |
| Automatizar respuestas | Webhook topic `questions` (`186`, `188`) |

Automatizar respuestas de preguntas es posible y tentador. Hazlo solo para las repetitivas y
verificables; una respuesta automática equivocada queda pública igual que una buena (`188`).

## Relacionados

`132` lo que no puedes decir · `133` el tiempo de respuesta · `134` mensajes de posventa ·
`141` el comprador problemático · `30` la descripción · `35` atributos · `38` fotos ·
`137` compra protegida · `188` automatizar respuestas · `ventas_lushows` para la persuasión
