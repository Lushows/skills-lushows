# Cuándo automatizar y cuándo no

Automatizar no es gratis: cada integración que montas es código que hay que mantener vivo cuando
Mercado Libre cambia algo. Este módulo te da el criterio para saber qué automatizar primero, qué
dejar a mano y en qué punto conviene no programar nada y pagar un integrador (`198`).

## La frontera de este bloque

Los módulos `175` a `199` te dicen **qué endpoint llamar, qué payload mandar y qué lógica de
negocio de Mercado Libre aplicar**. No te dicen cómo construir el software.

| Pregunta | Dónde se responde |
|---|---|
| ¿Qué endpoint actualiza el stock? ¿Qué trae el webhook? | Aquí, bloque `175`-`199` |
| ¿Dónde lo hospedo? ¿Cómo despliego? ¿Dónde guardo el secret? | `engineer_visualopen_lushows` |
| ¿Cómo monto la cola de trabajos, la base de datos, el reintento? | `engineer_visualopen_lushows` |
| ¿Qué le respondo al comprador para que compre? | `ventas_lushows` |
| ¿Cómo registro contablemente la venta y emito la factura DIAN? | `contador_lushows` y `198` |
| ¿Cuánto me queda de margen de verdad? | `Matematicas_lushows` y el bloque `75`-`99` |

**Esta skill decide qué hacer; la de ingeniería decide cómo construirlo.**

## El costo real de automatizar

Lo que la gente presupuesta es el fin de semana que le toma hacerlo funcionar. Lo que se paga
todos los meses es esto:

| Costo recurrente | Por qué aparece |
|---|---|
| Renovar el token cada 6 horas | Si el refresh falla, el bot muere en silencio (`178`, `179`) |
| Atender webhooks en menos de 500 ms | Si te demoras, ML desactiva tu suscripción (`191`) |
| Deduplicar notificaciones | ML reintenta y te manda el mismo evento varias veces (`192`) |
| Sobrevivir a cambios de ML | Atributos nuevos obligatorios, topics nuevos, campos que cambian |
| Vigilar que siga corriendo | Un bot caído no avisa: se nota cuando ya perdiste ventas |

Si nadie va a mirar eso, no automatices: un proceso manual lento es mejor que uno automático roto.

## El orden correcto: qué se automatiza primero

Ordenado por retorno sobre dolor de mantenimiento, de mayor a menor:

| # | Qué | Por qué primero | Módulo |
|---|---|---|---|
| 1 | **Stock** | Vender sin stock = cancelación, y cancelar = suspensión (`139`) | `183`, `196` |
| 2 | **Órdenes a tu sistema** | Es lectura pura: si falla, no rompes nada en ML | `185` |
| 3 | **Preguntas** | El mayor efecto por línea de código escrita | `187`, `195` |
| 4 | **Precio** | Solo si compites en catálogo o tienes muchos SKUs | `183` |
| 5 | **Publicar por API** | Solo con catálogo grande o rotación alta | `181`, `182` |
| 6 | **Mensajería posventa** | Alto cuidado, bajo retorno | `188` |

## La tabla de decisión honesta

| Tu situación | Veredicto |
|---|---|
| Menos de 20 SKUs, solo vendes en ML | **No automatices nada.** El panel te sobra |
| Menos de 20 SKUs, pero vendes también en tienda física o WhatsApp | Automatiza **solo el stock** |
| 20-200 SKUs, un solo canal | Automatiza stock + órdenes; preguntas con IA si te ahogan |
| 20-200 SKUs, varios canales | Stock por webhook, sin discusión (`196`) |
| Más de 200 SKUs | Integración completa, o integrador |
| Necesitas facturar a la DIAN | **No programes**: Alegra ya lo hace (`198`) |
| Quieres contabilidad e inventario | **No programes**: es software que ya existe (`198`) |
| Quieres un bot que responda preguntas con IA | Programa: eso no lo da ningún integrador (`195`) |

## La prueba de las tres preguntas

Antes de escribir una línea de código, respóndete esto:

```
□ ¿Cuántas veces por semana hago esta tarea a mano?
□ ¿Cuántos minutos me toma cada vez?
□ ¿Qué pasa si el automatismo se equivoca mientras yo no estoy mirando?
```

Si la tarea son 10 minutos a la semana, automatizarla es un pasatiempo, no un negocio. Si la
respuesta a la tercera pregunta es "vendo cosas que no tengo" o "publico un precio equivocado",
necesitas frenos antes que velocidad: límites duros, tope de cambio de precio y alarma.

## El error clásico

Empezar por lo divertido. Casi todo el mundo arranca queriendo el bot de preguntas con IA (`195`)
y deja el stock para después — que es justo al revés del riesgo real. Una respuesta mediocre a una
pregunta cuesta una venta; vender sin stock cuesta una cancelación, y las cancelaciones por encima
del **2,5%** pueden suspender tu cuenta (oficial ML Colombia, verificado sep-2026).

El segundo error: automatizar sobre una operación que todavía no está ordenada. Si tu inventario
en papel ya está mal, el bot lo único que hace es publicar el error más rápido.

## Automatiza para dormir, no para lucirte

Los tres automatismos que de verdad se pagan solos son aburridos:

| Automatismo | Lo que evita |
|---|---|
| Bajar stock a 0 cuando vendes por fuera | Cancelación y golpe a reputación |
| Alarma cuando una venta lleva X horas sin despachar | Envío fuera de término (`125` termómetro) |
| Alarma cuando una pregunta lleva más de 1 hora sin responder | Venta perdida por silencio |

Ninguno de los tres necesita IA. Los tres se hacen con webhooks y un mensaje a tu teléfono.

## Relacionados

`139` cancelaciones y riesgo de cuenta · `176` crear tu aplicación · `178` tokens ·
`183` precio y stock · `185` órdenes · `187` preguntas · `191` responder en 500 ms ·
`195` el bot de preguntas con IA · `196` sobreventa multicanal · `198` integradores ·
`199` arquitectura de referencia
