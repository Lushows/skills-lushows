# Mensajes de posventa

El canal de mensajes se abre cuando alguien te compra y es el único contacto directo que tienes con
él. Bien usado previene reclamos antes de que existan; mal usado —o no usado— deja al comprador
solo con su ansiedad, que es exactamente donde nacen los reclamos y las malas opiniones.

## Para qué sirve de verdad

| Uso | Efecto |
|---|---|
| Confirmar la compra | Baja la ansiedad del "¿le habrá llegado mi pedido?" |
| Avisar el despacho | Evita el mensaje "¿ya lo mandaste?" y la duda que precede al reclamo |
| Explicar algo del producto | Previene el reclamo por "no funciona" que en realidad es "no supe usarlo" |
| Resolver un problema temprano | Un problema resuelto en mensajes no llega a reclamo (`135`) |
| Pedir opinión | Las opiniones buenas no llegan solas (`142`) |

**El reclamo casi nunca nace del problema: nace del silencio después del problema.**

## La secuencia que funciona

Cuatro mensajes, no más. Cada uno tiene un trabajo.

| Momento | Mensaje | Trabajo que hace |
|---|---|---|
| Al confirmarse la venta | Agradecimiento + qué va a pasar + cuándo | Fija expectativa |
| Al despachar | Aviso de despacho + guía + fecha estimada | Elimina la incertidumbre |
| Al entregarse | "Ya llegó, avísame si todo bien" + cómo usarlo si aplica | Abre el canal antes del reclamo |
| 3-5 días después | Pedir opinión, sin condicionar | Construye la prueba social (`142`) |

Ejemplo del tercero, que es el que más rinde:

> Hola. Veo que ya te entregaron el pedido. Revísalo con calma y si algo no está como esperabas
> escríbeme por acá y lo resolvemos hoy mismo. Si es la primera vez que usas el producto, el
> [detalle que más confunde] se hace así: [instrucción de una línea].

Ese mensaje hace dos cosas a la vez: te posiciona como el primer canal (antes que el botón de
reclamo) y resuelve la confusión que genera el 30% de los reclamos por "calidad".

## Lo que NO se escribe

```
□ Ningún dato de contacto: teléfono, WhatsApp, redes, correo (`132`) — aplica también aquí
□ Nada de "si hay un problema, no abras reclamo" — presionar al comprador es motivo de sanción
□ Nada de condicionar la opinión: "te devuelvo X si me pones 5 estrellas" es prohibido
□ Nada de tono defensivo ni de explicar por qué el cliente se equivocó
□ Nada de mensajes masivos sin relación con la compra: eso es spam
```

Pedir opinión está bien. **Comprar la opinión, no.** La frontera es simple: puedes pedirla, no
puedes condicionarla ni premiarla.

## El reloj que corre en este canal

Es el canal donde aplica el corte de **24 horas hábiles** para conservar el derecho a excluir un
reclamo (oficial ML Colombia, verificado sep-2026). Ver `133` completo. Si automatizas este canal,
la automatización debe **avisarte** cuando hay un mensaje entrante, no solo enviar los salientes.

## Cuando el mensaje trae un problema

Protocolo de cuatro pasos, en orden:

```
□ 1. Responde el mismo día. Aunque no sepas la solución (detiene el reloj de 24 h)
□ 2. Reconoce el hecho sin discutir la culpa: "Veo que llegó incompleto, lo resolvemos"
□ 3. Ofrece la solución concreta y con fecha: reenvío, reposición o reembolso, con día
□ 4. Deja constancia escrita de todo en el mismo canal
```

El punto 4 es el que la gente subestima. Si el caso escala a mediación, **el expediente es el hilo
de mensajes** (`135`). Un hilo donde se ve que respondiste en horas, ofreciste solución y diste
fecha, gana. Un hilo con dos mensajes secos, pierde.

Y por eso: nunca resuelvas un caso "por fuera" del canal aunque el comprador te lo pida. Si no está
escrito ahí, para ML no pasó.

## Plantillas base

Ten escritas y guardadas las diez que más usas. Las imprescindibles:

| Plantilla | Cuándo |
|---|---|
| Confirmación de compra | Siempre |
| Aviso de despacho con guía | Siempre |
| Entregado + apertura de canal | Siempre |
| Pedido de opinión | 3-5 días después |
| Demora del transportador | Cuando el tracking se congela |
| Producto incompleto: solución | Reposición inmediata, sin discutir |
| Producto con falla: solución | Cambio o reembolso, con fecha |
| Arrepentimiento | Instrucciones de devolución (`138`) |
| Instrucción de uso del producto | Para el SKU que más confunde |
| Fuera de horario / festivo | Reconocimiento + cuándo respondes |

Personalízalas siempre con el nombre y el producto. Una plantilla que se nota plantilla hace más
daño que no escribir.

## Automatización

Los tres primeros mensajes de la secuencia son automatizables sin riesgo porque dependen de eventos
objetivos (venta confirmada, envío despachado, envío entregado). Los webhooks de `orders_v2`,
`shipments` y `messages` disparan cada uno (oficial, verificado sep-2026).

| Qué automatizar | Riesgo |
|---|---|
| Confirmación, despacho, entrega | Bajo. Son eventos objetivos |
| Pedido de opinión | Bajo, si respeta que no haya reclamo abierto |
| Respuestas a problemas | **Alto.** Nunca automatices la respuesta a una queja |
| Alarma al humano por mensaje entrante | Obligatorio si automatizas algo |

El detalle técnico está en `188`. La regla de oro: **automatiza lo que sale, nunca lo que entra.**

## El error clásico

No escribir nada hasta que el cliente escriba primero. El vendedor que despacha en silencio se
ahorra cuatro mensajes y se gana los reclamos de la gente que no sabe si su plata está viva. Los
cuatro mensajes cuestan minutos; un reclamo por calidad cuesta 60 días de termómetro (`127`).

## Relacionados

`133` el tiempo de respuesta · `135` el reclamo y la mediación · `136` reglas de exclusión ·
`131` las preguntas como canal de venta · `132` lo que no puedes decir · `142` opiniones negativas ·
`138` devoluciones · `188` automatizar mensajes · `144` plan de defensa de la cuenta
