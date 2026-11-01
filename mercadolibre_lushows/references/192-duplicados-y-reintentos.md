# Duplicados y reintentos

Mercado Libre te va a mandar el mismo evento más de una vez. No es un error suyo: es cómo funciona
cualquier sistema de notificaciones que quiere garantizar entrega. La deduplicación es
responsabilidad tuya, y si no la haces, tu inventario y tus reportes se ensucian solos.

## Las cifras

| Dato | Valor |
|---|---|
| Ventana de reintentos | **1 hora** |
| Intentos máximos | **8** |
| Después de 8 intentos fallidos | **El mensaje se pierde** |
| Deduplicación | **Responsabilidad de quien integra** |

(oficial ML, verificado sep-2026)

Dos lecturas de esa tabla. La primera: puedes recibir hasta ocho copias del mismo evento. La
segunda, más incómoda: **un aviso que fallaste ocho veces no vuelve nunca.** Por eso el polling
lento de respaldo no es paranoia (`185`, `189`).

## Por qué llegan duplicados

| Causa | Detalle |
|---|---|
| Respondiste lento | ML no vio el 200 a tiempo y reintentó (`191`) |
| Respondiste error | Un 500 tuyo, o un 502 de tu proxy |
| Tu servidor se reinició a mitad | Recibiste, no alcanzaste a responder |
| Eventos genuinamente distintos sobre el mismo recurso | La orden cambió dos veces |
| Varios topics sobre lo mismo | `orders_v2` y `shipments` hablan de la misma venta |

La última fila es la que la gente no ve venir: no todos los "duplicados" son duplicados. Una orden
que pasa a pagada y luego a enviada genera dos avisos legítimos.

## Las dos llaves de deduplicación

| Llave | Cuándo usarla | Qué hace |
|---|---|---|
| `_id` de la notificación | Siempre | Descarta el reenvío exacto del mismo aviso |
| `resource` + timestamp | Para eventos repetidos del mismo recurso | Descarta trabajo redundante |

Se usan juntas, en ese orden:

```
1. Ya procese este _id?            -> si: descartar, responder 200
2. Ya procese este resource con un evento igual o mas nuevo?  -> si: descartar
3. Procesar
4. Registrar _id y resource con la hora
```

## El patrón de idempotencia

Idempotente significa: correrlo diez veces deja el mismo resultado que correrlo una.

```
□ Tabla de eventos procesados: _id (llave unica), resource, topic, procesado_en
□ Inserta el _id ANTES de procesar, no despues
□ Si el insert choca con la llave unica -> alguien ya lo tomo: descarta
□ Las operaciones de negocio se escriben por ID de recurso, no por "sumar"
□ Purga la tabla cada cierto tiempo: los _id viejos ya no sirven de nada
```

El cuarto punto es el verdadero seguro, y conviene decirlo como regla:

| Operación | ¿Idempotente? |
|---|---|
| "Restar 1 al stock" | **No.** Dos avisos restan dos |
| "Fijar el stock en 29" | Sí. Dos avisos lo dejan en 29 |
| "Insertar la orden" | **No** sin llave única. Duplica filas |
| "Insertar la orden si el `order_id` no existe" | Sí |
| "Responder la pregunta" | **No.** ML no deja responder dos veces, pero tu log queda sucio |

**Escribe estados, no incrementos. Un sistema que suma se rompe con el primer duplicado; uno que
fija valores sobrevive a todos.**

Y hay una ayuda gratis: como el payload solo trae la referencia y tú siempre haces un `GET` para
traer el estado actual (`190`), procesar un aviso repetido te devuelve el mismo estado actual. Eso
neutraliza buena parte del riesgo por sí solo.

## Fuera de orden

Además de duplicados, los avisos pueden llegar desordenados: el de "enviado" antes que el de
"pagado". Defensa:

```
□ No asumas secuencia: lee el estado actual y actua sobre el, no sobre el evento
□ Guarda la hora sent del aviso y descarta lo mas viejo que lo ya aplicado
□ Si tu logica necesita el paso anterior, verificalo leyendo, no asumiendo
```

## Los 8 intentos y lo que se pierde

Si tu servidor estuvo caído una hora, esos avisos se perdieron. Qué se perdió y qué duele:

| Lo perdido | Consecuencia |
|---|---|
| Una venta | No descontaste stock: riesgo de sobreventa (`196`) |
| Una pregunta | Venta perdida |
| Un mensaje de posventa | El reloj de 24 horas hábiles corriendo (`188`) |
| Un cambio de envío | Reporte de costos incompleto (`186`) |

La recuperación es siempre la misma: barrido de polling hacia atrás, desde la última fecha
procesada con éxito. Por eso guardar esa fecha por topic es parte del diseño, no un lujo.

## Qué NO hacer con un aviso que no puedes procesar

Responder error para que ML te lo reintente es tentador y es mala idea: consumes intentos, te
acumulas fallas y te acercas a la desactivación de la suscripción (`191`). Lo correcto:

```
□ Responder 200 SIEMPRE que hayas recibido el aviso, aunque no lo puedas procesar
□ Guardarlo en tu cola marcado como fallido
□ Reintentar TU, con tu propia politica de reintentos
□ Alarma si un aviso lleva N reintentos tuyos sin exito
```

**El reintento de ML es para cuando no recibiste. El reintento de lo que no pudiste procesar es
tuyo.**

## El error clásico

Descubrir los duplicados por el inventario. El síntoma típico: el stock baja más de lo que
vendiste, o el reporte del mes muestra más ventas que las que pagó Mercado Pago. Para cuando
alguien lo nota, hay semanas de datos sucios que hay que reconstruir orden por orden.

Cuesta cinco líneas de código prevenirlo y dos días arreglarlo. Ponlas el primer día.

## Relacionados

`185` las órdenes · `186` los envíos · `188` mensajes de posventa · `189` webhooks ·
`190` topics y payload · `191` responder en 500 ms · `193` límites de uso ·
`196` la sobreventa multicanal · `199` arquitectura de referencia
