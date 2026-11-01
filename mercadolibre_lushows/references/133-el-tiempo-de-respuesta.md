# El tiempo de respuesta

Hay tres relojes corriendo en tu operación y casi nadie sabe que existen: el de las 24 horas hábiles
para conservar el derecho a excluir un reclamo, el de las 21:00 para entregar con Flex, y el de los
2 días hábiles para reembolsar. Los tres están verificados y los tres cuestan reputación.

## Reloj 1: las 24 horas hábiles de los mensajes

> **Si no respondes los mensajes en 24 horas hábiles, pierdes el derecho a pedir la exclusión del
> reclamo de tu reputación.** (oficial ML Colombia, verificado sep-2026)

Léelo pensando en plata. Un comprador se arrepiente —caso **excluible** según las reglas oficiales
(`136`)— pero tardaste 30 horas en contestar. Resultado: el reclamo ya no es excluible y se te queda
en el termómetro los próximos 60 o 365 días según tu volumen (`127`).

**Perdiste el derecho a la exclusión no por lo que pasó con el producto, sino por lo que tardaste en
escribir.**

### Cómo se cuentan

| Concepto | Lectura práctica |
|---|---|
| Horas hábiles | No son 24 horas de reloj: se cuentan sobre días hábiles |
| El viernes en la tarde | El momento más peligroso de la semana |
| Festivos colombianos | ~18 al año, casi todos lunes |
| El contador | Se reinicia con cada mensaje nuevo del comprador |

> ⚠️ **Sin verificar para Colombia (sep-2026).** El horario exacto que ML considera "hábil" —a qué
> hora arranca, a qué hora cierra, si cuenta el sábado— no está publicado. **Trátalo como 24 horas
> de reloj y quedas siempre del lado seguro.**

## Reloj 2: las 21:00 de Flex

Si usas Mercado Envíos Flex, la regla oficial es que **completes la entrega del producto antes de
las 21 hs** (oficial ML Colombia, verificado sep-2026). Si no, cuenta como **envío incorrecto** y
golpea la métrica que tiene umbral del 12% a 60 días (`126`).

Consecuencia operativa: tu corte real de despacho con Flex no son las 6 p.m., son mucho antes. Un
mensajero que sale a las 5 p.m. con ocho paradas en Bogotá no termina a las 21:00.

```
□ Define un corte de pedidos que deje margen para completar la última entrega antes de las 21:00
□ Cuenta el tráfico real de tu ciudad, no el del mapa
□ En temporada alta, baja el corte una hora
□ Si no llegas, es mejor no ofrecer Flex ese día que entregar 21:20
```

## Reloj 3: los 2 días hábiles del reembolso

En un reclamo con solicitud de cancelación tienes **2 días hábiles para reembolsar** sin haber
entregado. Si cumples, tu reputación queda intacta. Si no, el reembolso se hace automático y **sí**
te afecta (oficial ML Colombia, verificado sep-2026). Ver `136` y `139`.

## La segunda regla de las 24 horas (no confundir)

Hay un segundo uso de las 24 horas en las reglas de exclusión, y juega a tu favor:

| Regla | Qué dice |
|---|---|
| Regla del vendedor | Si **tú** no respondes en 24 h hábiles, pierdes el derecho a excluir |
| Regla del comprador | Un reclamo abierto **antes de que pasen 24 h desde tu último mensaje** es excluible |

Por eso **responder rápido no solo protege tu derecho: puede convertir el reclamo en excluible por
sí solo** (`136`).

## La regla operativa de la bandeja

```
□ Responde TODO mensaje del comprador dentro del mismo día hábil
□ Si no tienes la respuesta, responde igual: "Estoy verificando, te confirmo hoy mismo"
□ Un mensaje que reconoce el caso YA cuenta y detiene el reloj
□ Revisa la bandeja el viernes antes de cerrar y el lunes a primera hora
□ Antes de un puente festivo, deja la bandeja en cero
```

El segundo punto salva más casos que ningún otro. No necesitas resolver en 24 horas: necesitas
**responder** en 24 horas.

## El badge de "responde rápido"

> ⚠️ **Sin verificar para Colombia (sep-2026).** El distintivo de "responde rápido" asociado a
> contestar en menos de 60 minutos **no está confirmado en fuente oficial de ML**. Circula en blogs
> sin cita. No construyas una estrategia sobre él.

Dicho eso, responder rápido a las preguntas previas a la compra sí tiene efecto comercial obvio: el
que pregunta está comparando en ese momento (`131`).

## Dónde corre cada reloj

| Canal | Reloj que corre |
|---|---|
| Preguntas públicas (antes de comprar) | Comercial: pierdes la venta, no el derecho a exclusión |
| Mensajes posventa | **Las 24 h hábiles** (`134`) |
| Reclamo abierto | Las 24 h hábiles, y se está escribiendo el expediente (`135`) |
| Solicitud de cancelación | **2 días hábiles** para reembolsar (`139`) |
| Entrega con Flex | **21:00** del día de entrega |
| Mediación | Canal exclusivo, sin contacto directo con el comprador (`135`) |

## Cómo no perder un mensaje

| Nivel | Solución |
|---|---|
| Manual | Notificaciones activadas + revisión fija 9 a.m. / 3 p.m. / 6 p.m. |
| Semi | Respuestas guardadas para los 10 casos más comunes |
| Automatizado | Webhook topic `messages` → alarma a tu canal (`186`, `188`) |
| Lectura por API | `GET /messages/packs/$PACK_ID/sellers/$SELLER_ID?tag=post_sale`, con `mark_as_read=false` para no marcar leído (oficial, verificado sep-2026) |

Ese `mark_as_read=false` importa: si tu bot lee y marca como leído, pierdes la señal visual de
"pendiente" en el panel y empiezas a olvidar casos.

## El error clásico

Priorizar los mensajes por urgencia aparente. Contestas primero al que escribe en mayúsculas y dejas
para mañana al que escribió "hola, me llegó incompleto". El segundo es el que tiene el reloj
corriendo y el que va a terminar en el termómetro.

**Ordena la bandeja por antigüedad, no por tono.** El que grita ya te tiene la atención; el que
espera callado es el que te va a costar plata.

## Relacionados

`131` las preguntas como canal de venta · `134` mensajes de posventa · `135` reclamo y mediación ·
`136` reglas de exclusión · `139` la cancelación y su castigo · `126` las tres métricas ·
`144` plan de defensa de la cuenta · `188` automatizar mensajes · `115` despacho y Flex
