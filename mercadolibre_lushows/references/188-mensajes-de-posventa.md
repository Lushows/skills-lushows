# Mensajes de posventa

Las preguntas (`187`) son antes de comprar; los mensajes de posventa son después, cuando ya hay
una venta de por medio. Es un canal distinto, con su propio endpoint, y es el canal donde se ganan
o se pierden los reclamos — porque el reloj de las 24 horas corre aquí.

## El endpoint

```
GET https://api.mercadolibre.com/messages/packs/$PACK_ID/sellers/$SELLER_ID?tag=post_sale
Authorization: Bearer APP_USR-...
```

Tres cosas que hay que entender de esa URL:

| Pieza | Detalle |
|---|---|
| `$PACK_ID` | El identificador del carrito. **Si no hay `pack_id`, usa el `order_id`** |
| `$SELLER_ID` | Tu `user_id` |
| `tag=post_sale` | Marca que es el hilo de posventa, no otro tipo de conversación |

## El parámetro que salva el reloj

```
GET .../messages/packs/$PACK_ID/sellers/$SELLER_ID?tag=post_sale&mark_as_read=false
```

Por defecto, leer el hilo lo marca como leído. Con `mark_as_read=false` lo lees sin marcarlo.

Esto importa más de lo que parece: si tu bot lee todos los hilos cada cinco minutos y los marca
leídos, **pierdes la señal de "hay algo nuevo que nadie atendió"**. El bot deja de ser un ayudante
y se convierte en la razón por la que no viste el mensaje.

**Tu bot lee con `mark_as_read=false`; solo un humano —o el bot cuando efectivamente responde—
marca leído.**

## `pack_id` o `order_id`

Un `pack` agrupa varias órdenes compradas juntas. Si el comprador llevó tres productos tuyos en un
carrito, la conversación es **una sola** aunque haya tres órdenes.

```
□ Lee la orden (`185`)
□ Si trae pack_id, usa el pack_id en la URL
□ Si no trae pack_id, usa el order_id en el mismo lugar
□ Nunca abras tres hilos para tres ordenes del mismo pack
```

## El reloj de las 24 horas

Esta es la regla dura de todo el canal:

> Si **no respondes mensajes en 24 horas hábiles**, pierdes el derecho a pedir la exclusión del
> reclamo de tu reputación. (oficial ML Colombia, verificado sep-2026)

Y en la lista oficial de reclamos excluibles aparece explícitamente el "reclamo abierto antes de
24 h desde tu último mensaje". Traducido a integración: **cada mensaje sin responder es un reclamo
que ya no vas a poder sacar de tu termómetro**. El detalle de qué se excluye y qué no está en
`135` y `136`.

Lo que tu sistema debe hacer con eso:

```
□ Registrar la fecha del ULTIMO mensaje del comprador en cada hilo
□ Alarma a las 4 horas, alarma fuerte a las 12
□ Tablero con los hilos ordenados por antiguedad del pendiente
□ Nunca dejar que un hilo cruce las 24 horas habiles
```

## Qué se automatiza aquí y qué no

| Caso | Automatizar |
|---|---|
| Acuse de recibo y número de guía | Sí, es dato del sistema (`186`) |
| Aviso de despacho | Sí |
| Responder "¿cuándo llega?" con el estado real del envío | Sí |
| Reclamo, defecto, faltante, devolución | **No.** Humano, siempre |
| Negociación de una solución | **No.** Humano |
| Mediación abierta | **No.** Canal exclusivo con ML, sin contacto directo (`136`) |

Veredicto: en posventa el bot sirve para **informar**, no para resolver. Un cliente molesto que
recibe una respuesta automática se molesta el doble, y de ahí sale el reclamo que no vas a poder
excluir.

## La migración de mensajería de feb-2026

> ⚠️ **Sin verificar para Colombia (sep-2026).** Mercado Libre anunció desde el **2-feb-2026** una
> migración de mensajería para **MLB (Brasil) y MLC (Chile)**, en la que el `to.user_id` debe
> apuntar al ID del "Agente" del país en vez de al comprador. **No está verificado que aplique a
> `MCO`.** Si operas solo Colombia, sigue el formato actual; si además operas Brasil o Chile,
> revisa la documentación antes de reutilizar el mismo código para los tres sites.

Es un buen recordatorio de por qué la mensajería es la parte más frágil de la API: cambia por país
y sin previo aviso largo.

## Lo prohibido, igual que en preguntas

Nada de teléfono, WhatsApp, correo ni redes, y nada de invitar a cerrar por fuera. Las excepciones
(Autos y Motos, Inmuebles, Servicios, MercadoProveedores) son las mismas de `187`. Un bot de
posventa que suelta un número de contacto lo hace en el peor momento posible: en un hilo asociado
a una venta concreta, con evidencia.

## El error clásico

Montar el bot de posventa antes que el de preguntas, porque suena más "profesional". Es al revés:
en preguntas cada respuesta automatizada puede ganar una venta; en posventa cada respuesta
automatizada mal puesta puede costarte un reclamo que sí cuenta para el termómetro. **Automatiza
primero donde el error es barato.**

El segundo error: leer todos los hilos con un barrido programado sin `mark_as_read=false`, y
quedarte ciego frente a tu propia bandeja.

## Relacionados

`135` reclamos excluibles · `136` mediaciones · `180` los endpoints · `185` las órdenes ·
`186` los envíos · `187` las preguntas · `190` topics y payload · `195` el bot con IA
