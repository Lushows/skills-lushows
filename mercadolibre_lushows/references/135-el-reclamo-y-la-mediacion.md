# El reclamo y la mediación

Un problema con un comprador tiene dos etapas y son muy distintas: primero negocian ustedes dos,
después entra Mercado Libre a decidir. Todo tu esfuerzo debe ir a que nunca llegue a la segunda,
porque el límite de mediaciones para MercadoLíder es del 0,5% — con 120 ventas, cero casos.

## Las dos etapas

| | Reclamo | Mediación (disputa) |
|---|---|---|
| Quién decide | Ustedes dos | **Mercado Libre** |
| Canal | Mensajes normales con el comprador | Canal exclusivo, **sin contacto directo** |
| Qué se puede hacer | Negociar, reponer, reembolsar, explicar | Presentar evidencia y esperar |
| Efecto en reputación | Cuenta si no es excluible (`136`) | Cuenta como reclamo **y** como mediación |
| Reversible | Sí: se puede cerrar de acuerdo | No: ML decide y se acabó |

Confianza MEDIA-ALTA para el flujo (documentación ML, verificada sep-2026).

**La mediación no es una instancia de apelación: es el reconocimiento de que no resolviste.** Por
eso pesa doble.

## Por qué el 0,5% es tan brutal

Para MercadoLíder el límite de mediaciones es 0,5% de tus ventas (oficial ML Colombia, verificado
sep-2026):

| Ventas en 60 días | Mediaciones permitidas |
|---|---|
| 120 | **0** |
| 300 | 1 |
| 600 | 3 |

No hay margen. La estrategia obligada es: **resolver en la etapa de reclamo cueste lo que cueste**,
incluso cuando tengas la razón. Ver la sección de aritmética abajo.

## Cómo se responde un reclamo para no perder

```
□ 1. Responde el mismo día. Siempre. Aunque no tengas la solución (`133`)
□ 2. Reconoce el hecho sin discutir la culpa: "Veo que llegó incompleto, lo resolvemos"
□ 3. Ofrece UNA solución concreta con fecha: reposición el jueves, reembolso hoy
□ 4. Deja TODO escrito en el canal de ML. Lo que no está ahí, no existe
□ 5. Si es excluible, pide la exclusión — pero resuelve primero (`136`)
□ 6. Cierra el caso de acuerdo antes de que el comprador escale
```

El paso 4 es el que gana mediaciones. Si el caso escala, **el expediente es el hilo de mensajes**.
Un hilo donde se ve que respondiste en horas, reconociste, ofreciste solución y diste fecha, gana.
Un hilo con dos mensajes secos y una semana de silencio, pierde.

Corolario: **nunca resuelvas "por fuera" aunque el comprador te lo pida.** Si acordaron algo por
teléfono, escríbelo en el canal: "Como hablamos, te reenvío la pieza faltante el jueves".

## La aritmética que decide si peleas o cedes

Cuando tienes la razón pero el comprador insiste, la pregunta no es quién tiene razón: es cuánto
cuesta cada camino.

| Camino | Costo |
|---|---|
| Reponer / reembolsar y cerrar | El producto + el envío |
| Dejar que escale a mediación | El producto (probablemente igual) + un reclamo + **una mediación** |

Una mediación con 120 ventas te saca de MercadoLíder. Si tu producto vale $40.000 y el nivel te vale
más que eso, **la decisión económica es ceder, aunque tengas la razón**. Eso no es debilidad: es
aritmética.

Dónde sí vale la pena pelear: cuando el reclamo es excluible por reglas oficiales (arrepentimiento,
error del comprador, entrega no reconocida). Ahí no cedes: pides la exclusión y sigues (`136`).

## Lo que NO se hace

| Error | Consecuencia |
|---|---|
| Discutir la culpa | Alarga el caso y llena el expediente de argumentos, no de soluciones |
| No responder porque "es obvio que el cliente miente" | Pierdes el derecho a excluir a las 24 h (`133`) |
| Prometer sin fecha: "lo vamos a revisar" | El comprador escala |
| Pedirle que cierre el reclamo a cambio de algo | Presionar al comprador es sancionable |
| Sacar la conversación a WhatsApp | Prohibido, y además borra tu evidencia (`132`) |
| Responder con plantilla genérica a una queja | Enciende al comprador. Automatiza lo que sale, no lo que entra (`134`) |

## Qué pasa en la mediación

ML abre un canal exclusivo. Ya no hablas con el comprador: hablas con Mercado Libre. Lo que puedes
hacer es presentar evidencia:

```
□ Capturas del hilo de mensajes (aunque ML ya lo tiene)
□ Guía y tracking que demuestre despacho a tiempo
□ Fotos del producto empacado antes del despacho, con fecha
□ La descripción de la publicación tal como estaba al momento de la compra
□ Comprobantes de la solución ofrecida
```

El punto tres es barato y salva casos: una foto del paquete cerrado sobre la báscula, con la guía
pegada, tomada el día del despacho. Cuesta cinco segundos y desarma el reclamo de "llegó vacío".

## Prevención: dónde nacen los reclamos

| Origen | Antídoto |
|---|---|
| El comprador esperaba otra cosa | Ficha honesta y completa (`30`, `35`) |
| Faltó una pieza | Checklist de empaque y verificación antes de cerrar (`110`) |
| Llegó roto | Empaque para el peor transporte, no para el mejor (`110`) |
| No sabe usarlo | Mensaje de posventa con la instrucción clave (`134`) |
| No sabía dónde estaba su pedido | Mensaje de despacho con guía (`134`) |
| Se arrepintió | No es amenaza: es excluible por regla oficial (`136`, `138`) |

## Seguimiento por API

| Recurso | Cómo |
|---|---|
| Webhook de reclamos | Topic `claims` (oficial, verificado sep-2026) |
| Mensajes del caso | `GET /messages/packs/$PACK_ID/sellers/$SELLER_ID?tag=post_sale` |
| Métricas acumuladas | `GET /users/$USER_ID` → `seller_reputation.metrics.claims` |

Suscribirse a `claims` y mandarte una alarma inmediata es de las automatizaciones que más rinden:
convierte "me di cuenta el lunes" en "me enteré en 30 segundos" (`186`).

## El error clásico

Tratar el reclamo como una acusación personal y responder defendiéndose. El comprador no quiere
tener la razón: quiere su producto o su plata. **El vendedor que escribe "yo lo mandé bien" pierde;
el que escribe "te lo repongo el jueves" cierra el caso.**

## Relacionados

`133` el tiempo de respuesta · `134` mensajes de posventa · `136` reglas de exclusión de reclamos ·
`126` las tres métricas · `129` MercadoLíder · `138` devoluciones · `139` la cancelación ·
`141` el comprador problemático · `110` empaque · `144` plan de defensa de la cuenta
