# Responder en 500 ms

Este es el módulo que decide si tu integración vive o muere. Mercado Libre exige que tu servidor
conteste **HTTP 200 dentro de 500 milisegundos**; si no lo haces de forma repetida, **desactiva la
suscripción de tu app** y dejas de recibir avisos sin que nadie te llame a avisarte.

## La regla

> **HTTP 200 dentro de 500 ms.** Si no, ML reintenta y, si el patrón se repite, **desactiva
> automáticamente la suscripción de la app.** (oficial ML, verificado sep-2026)

Medio segundo no es mucho. Es menos de lo que tarda una consulta a la API de Mercado Libre, menos
de lo que tarda arrancar una función serverless en frío, y muchísimo menos de lo que tarda un
modelo de lenguaje en escribir una respuesta.

**Medio segundo alcanza para decir "recibido". No alcanza para nada más.**

## El patrón obligatorio

```
   ML                TU RECEPTOR              TU COLA            TUS WORKERS
    |                     |                      |                    |
    |--- POST aviso ----->|                      |                    |
    |                     |-- guardar el aviso ->|                    |
    |<---- HTTP 200 ------|                      |                    |
    |   (menos de 500ms)  |                      |                    |
    |                     |                      |<--- tomar uno -----|
    |                     |                      |                    |
    |                     |          GET del recurso a la API de ML   |
    |<-----------------------------------------------------------------|
    |                     |          procesar, guardar, responder      |
```

La línea que importa: **el 200 sale antes de que empiece el trabajo real.** El receptor no sabe
nada del negocio; su único oficio es apuntar el aviso y contestar.

## Qué puede y qué no puede hacer el receptor

| Cabe en 500 ms | No cabe |
|---|---|
| Leer el JSON | `GET` a la API de Mercado Libre |
| Verificar que traiga `_id`, `resource`, `topic` | Consultar tu sistema de inventario |
| Escribir una fila o empujar a una cola | Llamar a un modelo de IA (`195`) |
| Responder 200 | Renovar el token (`178`) |
| | Enviar un correo o un WhatsApp |
| | Generar una factura |

Si dudas de si algo cabe, la respuesta es no. **Todo lo que dependa de una red ajena va después
del 200.**

## El error que rompe integraciones serverless

Este es el caso concreto, y es tan frecuente que merece nombre propio:

```
// MAL — el 200 sale al final, despues de todo el trabajo
recibir(aviso) {
  const orden = GET(aviso.resource)     // 300-800 ms
  actualizarInventario(orden)           // 200 ms
  notificarOperador(orden)              // 400 ms
  responder(200)                        // ya pasaron 1.500 ms: TARDE
}
```

```
// BIEN — el 200 sale primero
recibir(aviso) {
  encolar(aviso)                        // 5-20 ms
  responder(200)                        // dentro de los 500 ms
}
// el worker hace el resto, sin reloj encima
```

En una función serverless esto se agrava por dos razones: el **arranque en frío** puede consumirse
los 500 ms él solo, y en muchas plataformas **el proceso se congela apenas respondes**, así que el
trabajo que dejaste "para después de responder" en la misma función simplemente no ocurre.

Dos consecuencias prácticas:

| Plataforma | Qué necesitas |
|---|---|
| Servidor que no duerme | Cola en memoria o en base, workers aparte |
| Serverless | Cola **externa** de verdad; no confíes en trabajo post-respuesta |

Si tu plan de hosting duerme el servicio cuando no hay tráfico, el primer aviso después de un rato
inactivo va a llegar tarde **siempre**. Ese es un problema de infraestructura y lo resuelve
`engineer_visualopen_lushows`; aquí solo te digo que es incompatible con webhooks de Mercado Libre.

## Cómo saber si estás en el filo

```
□ Mide el tiempo de TU endpoint, del primer byte al 200, en percentil 95
□ Si el p95 pasa de 200 ms, ya estas en riesgo: los picos se van a 500
□ Vigila el campo attempts del payload: si llega >1, ya fallaste (`190`)
□ Alarma si dejas de recibir avisos por mas de X horas en horario de ventas
□ Guarda sent y la hora en que respondiste: la diferencia es tu latencia real
```

El p95 es lo que hay que mirar, no el promedio: el promedio te consuela mientras el 5% de los
avisos llega tarde y te acumula fallas.

## Si te desactivaron la suscripción

El síntoma es silencio: tu código no da errores porque no le llega nada.

```
□ 1. Entra a "Mis aplicaciones" y revisa el estado de la suscripcion
□ 2. Arregla primero la latencia: si reactivas sin arreglar, te vuelven a desactivar
□ 3. Reactiva los topics
□ 4. Corre un barrido de polling para recuperar lo que te perdiste (`185`)
□ 5. Deja el polling lento permanente como red de seguridad
```

El paso 4 no es opcional: mientras estuviste desactivado perdiste ventas, preguntas y mensajes.
Los mensajes sin responder en 24 horas hábiles cuestan el derecho a excluir reclamos (`188`).

## El error clásico

Probar el receptor en local con una herramienta de túnel, ver que "funciona", y desplegarlo a una
plataforma serverless con arranque en frío sin cola. Funciona los primeros días mientras hay
tráfico constante y se cae los domingos por la mañana, cuando el servicio llevaba horas dormido.

**Si no tienes cola, no tienes webhooks: tienes un experimento que funciona cuando hay tráfico.**

## Relacionados

`178` tokens · `185` las órdenes · `188` mensajes de posventa · `189` webhooks: configuración ·
`190` topics y payload · `192` duplicados y reintentos · `195` el bot con IA ·
`199` arquitectura de referencia
