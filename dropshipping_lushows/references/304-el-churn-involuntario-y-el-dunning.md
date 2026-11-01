# El churn involuntario y el dunning

> Este es el dinero más barato que vas a recuperar en toda tu operación. No requiere mejorar el
> producto, ni bajar el precio, ni comprar más tráfico. Requiere **reintentar el cobro y escribir
> tres correos**. Y casi nadie lo hace bien.

## El dato que cambia la conversación

Red Recurly, julio de 2026 (miles de comercios de suscripción):

| Componente | Valor |
|---|---|
| Churn total mensual | **3,60%** |
| Voluntario (el cliente decidió irse) | **2,34%** |
| **Involuntario (falló el cobro)** | **1,25%** |
| Involuntario como % del churn total | **~35%** |
| Reactivación en 30 días tras cancelar | **15,4%** |

**Uno de cada tres clientes que pierdes no te odia. Su tarjeta falló.** Se venció, cambió de banco,
el emisor rechazó por antifraude, no tenía saldo ese día, o el descriptor le pareció sospechoso.
Ninguna de esas causas tiene que ver con tu producto. Todas son recuperables.

## Por qué falla una tarjeta

| Causa | % aproximado del fallo (verificar con tu pasarela) | Recuperable |
|---|---|---|
| Fondos insuficientes | el bloque más grande | **sí**, reintentando otro día |
| Tarjeta vencida | alto, y predecible | **sí**, avisando antes |
| Rechazo del emisor (antifraude, "do not honor") | medio | parcialmente, reintentando |
| Tarjeta reportada/cancelada | bajo | solo si el cliente actualiza |
| Límite de cobros recurrentes del banco | bajo | sí, con otro método |

Las dos primeras son la mayoría y son las más fáciles: **el tiempo las arregla solo.** Un reintento
al día 3 pega a la gente que ya recibió su quincena.

## El cálculo: qué vale arreglarlo

Partimos de 100 suscriptores y un horizonte de 12 meses.

| Escenario | Churn mensual | Suscriptores vivos al mes 12 |
|---|---|---|
| Sin dunning (churn Recurly completo) | 3,60% | **64,4** |
| Recuperando **la mitad** del involuntario (1,25% → 0,625%) | 2,975% | **69,6** |
| **Diferencia** | | **+5,2 suscriptores por cada 100** |

Monetizado con el margen verificado del proyecto (USD 26,47 por venta sin adquisición):

```
5,2 suscriptores × USD 26,47 = USD 137 al mes, por cada 100 suscriptores
```

Con 500 suscriptores son ~USD 688/mes. Con 1.000, ~USD 1.376/mes. **Recurrentes**, no una vez. Y el
costo de conseguirlo es una secuencia de correos automatizada.

Compáralo con lo otro que podrías hacer: USD 137 al mes de pauta a CAC 10,54 traen ~13 clientes
nuevos que dejan 15,93 cada uno = USD 207 de margen bruto de primera venta, pero **una sola vez**. El
dunning entrega los 137 todos los meses sin gasto adicional. Verifica el cálculo con
`Matematicas_lushows` antes de usarlo en un plan.

## La secuencia de reintentos (dunning) que funciona

| Intento | Cuándo | Qué pasa además |
|---|---|---|
| **Aviso pre-cobro** | −3 días | correo/WhatsApp: "el día X te cobramos $Y por tu envío de Z" |
| Cobro original | día 0 | si falla, empieza la ventana |
| Reintento 1 | **día 1** | correo 1: "no pudimos procesar tu pago" + link para actualizar |
| Reintento 2 | **día 3** | nada (silencio, solo reintento) |
| Reintento 3 | **día 5** | correo 2: recordatorio + qué se pierde |
| Reintento 4 | **día 8** | WhatsApp (el canal que sí se lee) |
| Reintento 5 | **día 12** | correo 3: último aviso + oferta de pausar en vez de cancelar |
| Cierre | **día 15-21** | se suspende, se marca como "recuperable" y pasa a `306` |

| Parámetro | Rango sano | Nota |
|---|---|---|
| Ventana total de recuperación | **15-21 días** | más allá de 21 días el rendimiento cae mucho |
| Número de reintentos | 4-6 | más de 8 puede activar bloqueos del emisor |
| Correos de la secuencia | 3 | 1 más que eso solo molesta |
| Recuperación esperada del involuntario | **30-60%** | el cálculo de arriba usa 50%, que es conservador-medio; **verificar con tu pasarela** |

**Regla de días de la semana:** no reintentes los tres primeros días del mes ni un domingo si puedes
evitarlo. Reintentar el día 1-3 de mes y el día 15-17 (quincenas en México) sube la tasa de éxito
sin ningún esfuerzo adicional.

## Los mensajes

Regla de tono: **esto no es una cobranza, es un aviso técnico.** El cliente no hizo nada malo. Si el
correo suena a que le estás reclamando, cancela.

| Correo | Asunto | Cuerpo (idea) |
|---|---|---|
| 1 (día 1) | "Tu banco rechazó el pago de tu pedido" | "Le pasa seguido — suele ser el límite del banco o una tarjeta vencida. Lo intentamos de nuevo automáticamente. Si prefieres, actualiza aquí en 30 segundos." + botón |
| 2 (día 5) | "Tu envío de [producto] está en pausa" | recordatorio concreto de qué se detiene, fecha en que se pierde el lugar, botón |
| 3 (día 12) | "¿Lo pausamos en vez de cancelarlo?" | **ofrecer pausa de 30/60 días** antes que cancelar; botón de pausar y botón de actualizar |
| WhatsApp (día 8) | — | 2 líneas, nombre, producto, link. Nada de emojis de alarma. |

| Nunca | Por qué |
|---|---|
| "Tu pago fue RECHAZADO ⚠️" en mayúsculas | parece phishing y parece reclamo |
| Pedir los datos de la tarjeta dentro del correo | nunca; solo link a tu checkout |
| Mandar los 3 correos el mismo día | quema el remitente y al cliente |
| Cancelar al primer fallo | estás tirando el 35% de tu churn a la basura |

## Prevención: barata y casi nadie la hace

| Acción | Efecto |
|---|---|
| **Account Updater** de la red (si tu pasarela lo ofrece) | actualiza automáticamente tarjetas vencidas o renumeradas; verificar disponibilidad y costo en tu procesador |
| Aviso de vencimiento 30 días antes | ataca la causa más predecible de todas |
| Guardar un método de respaldo | segunda tarjeta o método alterno |
| Descriptor de tarjeta con el nombre de la marca | evita rechazos por "no lo reconozco" y contracargos |
| Cobrar el día que el cliente elija | el que cobra el día 20 en México pelea con el bolsillo vacío |
| Reintento con monto parcial (si aplica) | recupera fondos insuficientes en algunos casos |

## Cómo medirlo

| Métrica | Fórmula | Meta |
|---|---|---|
| Tasa de fallo de cobro | cobros fallidos ÷ cobros intentados | <8% |
| % de churn involuntario | churn involuntario ÷ churn total | **<25%** es bueno; 35% es el promedio de red |
| Tasa de recuperación de dunning | recuperados ÷ fallados | **30-60%** |
| Días medios a la recuperación | — | si pasa de 10, revisa la cadencia |
| Ingreso recuperado por mes | recuperados × margen | esto es lo que reportas |

Si tu % de churn involuntario supera 40%, **tu problema no es el producto**: es la pasarela, el
descriptor o la cadencia. Arregla eso antes de tocar el precio o la oferta.

## Si NO tienes suscripción todavía

El concepto aplica igual a **compra única**: el checkout con pago rechazado es exactamente el mismo
dinero perdido por la misma razón.

| Situación | Acción |
|---|---|
| Pago rechazado en checkout | reintento automático + correo/WhatsApp en <15 min con link para reintentar |
| Pedido creado sin pagar (MX, prepago) | recordatorio a 1 h, 24 h y 48 h |
| Orden bump aceptado pero cobro fallido | cobrar el pedido base y ofrecer el bump aparte, no perder ambos |

En el proyecto México (prepago en web), esta es la aplicación relevante en 2026. El dunning de
suscripción entra cuando entre la suscripción (`303`).

## Relacionados
`192` · `193` · `272` · `300` · `301` · `302` · `303` · `306` · `309`
