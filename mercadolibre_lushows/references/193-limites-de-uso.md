# Límites de uso

La API de Mercado Libre tiene límites y los aplica devolviendo `429 Too Many Requests`. Lo
incómodo es que la cifra exacta no está publicada, así que hay que diseñar para no acercarse
nunca, en vez de calcular cuánto cabe.

## El error que vas a ver

```
HTTP 429 Too Many Requests
```

Con el cuerpo **vacío**. Sin JSON, sin mensaje, sin explicación de cuánto esperar. (oficial ML,
verificado sep-2026)

Que venga vacío tiene una consecuencia práctica: si tu código intenta parsear el cuerpo como JSON,
**revienta con un error de parseo y te confunde el diagnóstico**. Maneja el 429 por código HTTP,
antes de tocar el cuerpo.

## La cifra que circula

> ⚠️ **Sin verificar (sep-2026).** Se cita mucho el límite de **"1500 requests por minuto por
> vendedor"**, pero **no está en la documentación oficial de Mercado Libre**. Trátala como
> orientativa, no como contrato: puede ser distinta por endpoint, por app o por momento. Lo único
> confirmado es que el `429` existe.

Diseña como si el límite fuera bastante menor y no te vas a enterar nunca de cuál era.

## Las buenas prácticas oficiales

Estas sí son de Mercado Libre (verificado sep-2026):

| Práctica | Por qué |
|---|---|
| **Usar la API en vez de scraping** | El scraping está bloqueado y es causa de baneo |
| **Restringir las IPs de tu app** | Reduce el daño si te roban credenciales |
| **Distribuir las llamadas en el tiempo** | Las ráfagas son lo que dispara el 429 |
| **Paginar con `offset` y `limit`** | Pedir todo de una es pedir un 429 |
| **Preferir webhooks sobre polling** | La medida que más peticiones ahorra (`189`) |

**La forma más eficaz de no chocar con el límite no es contar peticiones: es dejar de preguntar
cosas que ML puede avisarte.**

## De dónde sale el gasto

| Patrón | Peticiones al día | Veredicto |
|---|---|---|
| Barrer 500 ítems cada 5 minutos | 144.000 | Suicida |
| Barrer 500 ítems 2 veces al día | 1.000 | Razonable |
| Webhook + `GET` del recurso | 1 por evento real | Lo correcto |
| Polling de órdenes cada 15 min | ~96 | Red de seguridad barata |
| `GET` de atributos de categoría por producto | 1 por producto | Cacheable (`182`) |

## Cómo comportarse cuando llega el 429

```
□ Detecta por codigo HTTP, nunca parseando el cuerpo (viene vacio)
□ Espera antes de reintentar, con tiempos crecientes: 1s, 2s, 4s, 8s...
□ Agrega un poco de aleatoriedad para no reintentar todos a la vez
□ Tope de reintentos: despues, a la cola de fallidos y alarma
□ Baja el ritmo global, no solo el de esa llamada
□ NUNCA reintentes en bucle inmediato: es como te ganas un bloqueo mayor
```

## Reducir peticiones sin perder funcionalidad

| Técnica | Ahorro |
|---|---|
| Cachear `/categories/$ID/attributes` | Enorme en cargas masivas (`182`) |
| Cachear el árbol de categorías | Cambia poco |
| Guardar el `user_id` en vez de llamar `/users/me` cada vez | Una llamada por operación |
| Actualizar solo lo que cambió, no todo el catálogo | El mayor de todos (`183`) |
| Un solo componente renueva el token | Evita refrescos simultáneos (`178`) |
| Deduplicar avisos | Cada duplicado procesado es un `GET` regalado (`192`) |

## ML está cerrando accesos que antes eran abiertos

Este es el punto que conviene tener presente al diseñar. El endpoint de costos de publicación,
`GET /sites/MCO/listing_prices?price=50000`, **era consultable sin token** y hoy no lo es:
responde **403** con el código `PA_UNAUTHORIZED_RESULT_FROM_POLICIES` y exige autenticación
(verificado 14-sep-2026).

Qué enseña eso:

| Lección | Consecuencia de diseño |
|---|---|
| Lo público hoy puede exigir token mañana | Manda el token también donde no parezca necesario |
| El cambio no se anuncia en tu bandeja | Tu alarma es el propio 403 |
| Un 403 nuevo no siempre es culpa tuya | Antes de depurar tu código, prueba el endpoint a mano |
| Las políticas de acceso son móviles | No construyas nada crítico sobre un endpoint sin token |

**Un endpoint abierto es un permiso prestado, no un derecho adquirido.**

## Los códigos que conviene distinguir

| Código | Significa | Reacción |
|---|---|---|
| `401` | Token vencido o ausente | Refrescar y reintentar una vez (`178`) |
| `403` | No tienes permiso, o el acceso se cerró | Revisar scope; probar a mano |
| `429` | Demasiadas peticiones | Esperar con tiempos crecientes |
| `5xx` | Problema del lado de ML | Reintentar con espera; no es tuyo |

Tratar los cuatro igual es el error de arquitectura más común: un `401` se arregla refrescando, un
`429` se arregla esperando, y reintentar un `403` mil veces no lo arregla nunca.

## El error clásico

Montar un "sincronizador completo" que cada pocos minutos recorre todo el catálogo preguntando por
cada ítem. Funciona con 20 productos y colapsa con 300, justo cuando el negocio empezó a andar. Y
el colapso no es limpio: son 429 intermitentes que hacen fallar unas actualizaciones sí y otras
no, dejando el stock en un estado que nadie entiende.

**Sincroniza por evento, no por barrido. El barrido es la red de seguridad, no el motor.**

## Relacionados

`178` tokens · `180` los endpoints · `182` atributos de categoría · `183` precio y stock ·
`185` las órdenes · `189` webhooks · `192` duplicados y reintentos · `199` arquitectura
