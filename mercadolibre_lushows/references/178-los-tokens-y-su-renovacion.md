# Los tokens y su renovación

El `access_token` dura **6 horas** y el `refresh_token` dura **6 meses** si no se usa (oficial ML,
verificado sep-2026). Toda integración que se cae sola de madrugada se cae aquí. Este módulo tiene
la regla que más integraciones rompe en Mercado Libre y el patrón exacto para no romperla.

## Los dos tokens

| Token | Para qué sirve | Duración | Dónde vive |
|---|---|---|---|
| `access_token` | Firmar cada llamada | **6 horas** (`expires_in: 21600`) | Memoria o base |
| `refresh_token` | Pedir un token nuevo | **6 meses** sin usarse | Base de datos, siempre |

Se usa así en cada llamada:

```
GET https://api.mercadolibre.com/users/me
Authorization: Bearer APP_USR-...
```

## LA REGLA CRÍTICA

> **Solo sirve el ÚLTIMO `refresh_token` emitido, y sirve UNA SOLA VEZ.** Al refrescar, Mercado
> Libre invalida el anterior y te entrega uno nuevo que tienes que persistir de inmediato.
> (oficial ML, verificado sep-2026)

Esto se llama "rotación de refresh token" y cambia por completo cómo tienes que escribir el
código. Las consecuencias, una por una:

| Si haces esto | Lo que pasa |
|---|---|
| Guardas el `access_token` nuevo y no el `refresh_token` | El próximo refresh: `invalid_grant` |
| Dos procesos refrescan a la vez | Uno gana, el otro queda con un token muerto |
| Guardas el refresh en un `.env` que no puedes escribir | Funcionas 6 horas y mueres |
| Te quedas 6 meses sin refrescar | El refresh expira y toca reautorizar a mano |
| Guardas el refresh en memoria y reinicias el servidor | Lo pierdes: reautorizar a mano |

**El `refresh_token` no es una configuración, es un dato que cambia. Va en base de datos, no en
un archivo de entorno.**

## La llamada de renovación

```
POST https://api.mercadolibre.com/oauth/token
Content-Type: application/x-www-form-urlencoded
Accept: application/json
```

Cuerpo:

```
grant_type=refresh_token
client_id=TU_APP_ID
client_secret=TU_SECRET
refresh_token=EL_ULTIMO_QUE_TIENES_GUARDADO
```

Respuesta, en forma típica:

```json
{
  "access_token": "APP_USR-nuevo...",
  "token_type": "bearer",
  "expires_in": 21600,
  "scope": "offline_access read write",
  "user_id": 123456789,
  "refresh_token": "TG-nuevo..."
}
```

Fíjate: viene un `refresh_token` **nuevo**. Ese es el que hay que guardar. El viejo ya no sirve.

## El patrón de persistencia correcto

Este es el orden que importa. Guardar primero, usar después:

```
1. LEER de la base: refresh_token vigente para este user_id
2. LLAMAR POST /oauth/token con grant_type=refresh_token
3. Si responde 200:
     3a. ESCRIBIR en la base: access_token nuevo + refresh_token nuevo + expira_en
     3b. Solo despues de que la escritura confirmo, usar el access_token
4. Si responde error:
     4a. NO borres el refresh_token guardado todavia
     4b. Registra el error con cuerpo completo y avisa (`179`)
```

Reglas alrededor del patrón:

```
□ Un solo proceso puede refrescar por cuenta a la vez (candado o cola)
□ Refresca por anticipado: cuando falten ~30 minutos, no cuando ya venza
□ Guarda tambien la hora exacta de emision para poder auditar
□ Guarda tokens por user_id: una fila por cuenta conectada
□ Toca la cuenta al menos una vez al mes para que el refresh no llegue a los 6 meses
```

## Dos estrategias para decidir cuándo renovar

| Estrategia | Cómo funciona | Veredicto |
|---|---|---|
| **Por reloj** | Renueva cada ~5 h 30 min, programado | La buena para un bot que corre siempre |
| **Por reacción** | Te da 401, renuevas y reintentas una vez | Necesaria como red de seguridad |
| Renovar en cada llamada | Refrescas aunque sirva | **Nunca**: rotas de más y provocas carreras |

Lo correcto es tener las dos primeras: reloj como principal, reacción al 401 como respaldo, con
un solo reintento para no entrar en bucle.

## La condición de carrera, que es real

Si tienes un webhook receiver, un sincronizador de stock y un bot de preguntas, son tres procesos.
Si los tres descubren a la vez que el token venció, los tres refrescan. El primero rota el token,
los otros dos quedan con un `refresh_token` que ML ya invalidó y empieza el desastre.

La solución que funciona: **un solo componente renueva**. Los demás leen el token de la base o de
un caché compartido y jamás llaman a `/oauth/token`. Cómo implementar ese candado (Redis, bloqueo
de fila, un worker dedicado) es de `engineer_visualopen_lushows`.

## Qué guardar exactamente

| Campo | Para qué |
|---|---|
| `user_id` | Llave. Ojo: puede exceder Int32, guárdalo en 64 bits (`199`) |
| `access_token` | Firmar llamadas |
| `refresh_token` | Renovar |
| `expira_en` | Saber cuándo refrescar por anticipado |
| `actualizado_en` | Detectar tokens huérfanos y depurar |
| `scope` | Saber si tienes `write` antes de intentar escribir |

## El error clásico

Guardar el `refresh_token` a mano en el archivo `.env` cuando conectas la cuenta por primera vez.
Funciona seis horas, refresca una vez, y como el archivo no se actualiza, el próximo refresh usa
uno muerto. El síntoma es el más confuso de todos: **funciona perfecto el primer día y se cae
solo al segundo**, sin que nadie haya tocado nada.

## Relacionados

`176` crear tu aplicación · `177` el flujo OAuth · `179` el error invalid_grant ·
`180` los endpoints · `191` responder en 500 ms · `199` arquitectura de referencia
