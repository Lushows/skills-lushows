# Webhooks: configuración

Un webhook es Mercado Libre llamando a tu servidor cuando pasa algo, en vez de tu servidor
preguntando cada rato si pasó algo. Es la diferencia entre enterarte de una venta en dos segundos
o en quince minutos, y la propia ML lo recomienda por encima del polling.

## Polling contra webhook

| | Polling | Webhook |
|---|---|---|
| Quién pregunta | Tú, cada X minutos | ML te avisa |
| Latencia | Hasta el intervalo completo | Segundos |
| Peticiones gastadas | Miles al día, casi todas vacías | Solo cuando hay algo |
| Riesgo de `429` | Alto (`193`) | Bajo |
| Si tu servidor se cae | No pasa nada, retomas | Se pierden avisos tras 8 intentos (`192`) |
| Requisito técnico | Ninguno | URL pública y responder en 500 ms (`191`) |

Lo oficial de Mercado Libre, entre sus buenas prácticas: **preferir webhooks sobre polling**.

**Webhook para la velocidad, polling lento como red de seguridad. No es o lo uno o lo otro.**

## Lo que hay que registrar

En "Mis aplicaciones", dentro de tu app (`176`):

```
□ callback_url: la URL publica que va a recibir las notificaciones
□ Los topics que quieres recibir (`190`)
```

Requisitos de la `callback_url`:

| Requisito | Detalle |
|---|---|
| Pública | Accesible desde internet. `localhost` no sirve |
| HTTPS | Certificado válido |
| Siempre viva | Si se cae seguido, ML desactiva la suscripción (`191`) |
| Rápida | HTTP 200 en menos de **500 ms** (`191`) |
| Sin autenticación propia | ML no va a pasar por tu login |

Ese último punto asusta y con razón: tu endpoint queda abierto a internet. Cómo protegerlo —
validar origen, secreto compartido en la ruta, rate limiting, WAF — es de
`engineer_visualopen_lushows`. Lo que sí es regla de negocio: **nunca confíes en el contenido del
aviso, siempre vuelve a leer el dato con un `GET`** (`190`). Eso solo ya neutraliza a alguien que
te invente notificaciones falsas.

## Una URL por entorno

| Entorno | App | `callback_url` |
|---|---|---|
| Producción | App "prod" | Tu servidor real |
| Pruebas | App "dev" | Tu entorno de pruebas, con usuarios de test (`194`) |

No mezcles. Si apuntas la app de producción a tu máquina mientras desarrollas, los avisos reales
se van a un servidor que apagas a las 6 p.m., ML acumula fallas y termina desactivando tu
suscripción.

## Elegir topics: menos es más

Suscribirte a todo suena prudente y es lo contrario. Cada topic extra es más tráfico entrando, más
eventos que deduplicar y más formas de pasarte de los 500 ms.

| Si quieres... | Suscribe |
|---|---|
| Enterarte de las ventas | `orders_v2` |
| Responder preguntas rápido | `questions` |
| Seguir envíos | `shipments` |
| Atender posventa | `messages` |
| Vigilar cambios en tus publicaciones | `items` |

Arranca con `orders_v2` y `questions`. Agrega el resto cuando tengas un motivo concreto. La lista
completa está en `190`.

## Cómo probarlo

No hay sandbox (`194`), así que las pruebas son sobre la plataforma real con usuarios de test.

```
□ 1. Levanta tu receptor y verifica que responde 200 en <500 ms
□ 2. Registra la callback_url en la app de pruebas
□ 3. Suscribe solo un topic
□ 4. Genera el evento con usuarios de test: una compra entre dos test users
□ 5. Revisa tu log: llego el aviso? con que _id y que resource?
□ 6. Confirma que hiciste el GET y trajiste el dato real
□ 7. Fuerza un duplicado: reenvia el mismo payload y verifica que no se procese dos veces
```

El paso 7 es el que la gente se salta y el que después duele (`192`).

## Qué monitorear una vez en producción

| Señal | Qué significa |
|---|---|
| Tiempo de respuesta de tu endpoint | Si sube de 500 ms, estás en la cuerda floja (`191`) |
| Avisos recibidos por día | Una caída brusca = suscripción desactivada |
| Campo `attempts` en el payload | Si llega con `attempts > 1`, ya fallaste antes |
| Errores 5xx de tu receptor | Cada uno es un reintento que se consume |

El campo `attempts` es tu alarma temprana gratis: **si empiezas a ver avisos con `attempts` mayor
que 1, tu integración ya está fallando aunque todavía funcione.**

## El error clásico

Registrar la `callback_url` antes de que el receptor exista o esté listo. Mercado Libre empieza a
enviar de inmediato, tu servidor responde 404 o tarda tres segundos, se acumulan fallas y la
suscripción se desactiva sin que nadie lo note. Después pasas días depurando código que está bien:
lo que pasa es que ya no te están mandando nada.

**Primero el receptor respondiendo 200 en menos de 500 ms. Después el registro. Nunca al revés.**

## Relacionados

`176` crear tu aplicación · `185` las órdenes · `187` las preguntas · `190` topics y payload ·
`191` responder en 500 ms · `192` duplicados y reintentos · `193` límites de uso ·
`194` usuarios de prueba · `199` arquitectura de referencia
