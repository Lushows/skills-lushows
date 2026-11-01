# El error invalid_grant

Es el error más común de toda la integración con Mercado Libre y el que más tiempo hace perder,
porque su mensaje lista tres causas distintas sin decirte cuál fue. Este módulo lo traduce y te da
el diagnóstico para cada una.

## El mensaje literal

```json
{
  "error": "invalid_grant",
  "message": "Error validating grant. Your authorization code or refresh token may be expired or it was already used",
  "status": 400
}
```

(oficial ML, verificado sep-2026)

Léelo con atención: dice *"tu código de autorización **o** tu refresh token"* y *"expirado **o** ya
usado"*. Son cuatro combinaciones en una sola frase. ML no te dice cuál. Tú sí puedes saberlo.

## Las tres causas y cómo se distinguen

| # | Causa | En qué `grant_type` | Señal que la delata |
|---|---|---|---|
| 1 | El `code` ya se canjeó | `authorization_code` | Falla al conectar; recargaste la página |
| 2 | El `refresh_token` no es el último | `refresh_token` | Funcionó el día 1 y murió el 2 |
| 3 | El `refresh_token` expiró de verdad | `refresh_token` | Más de 6 meses sin usar la cuenta |

Hay una cuarta que se disfraza de estas: el `redirect_uri` del canje no es idéntico al de la
autorización (`176`). Aparece siempre en el paso de `authorization_code`.

## Diagnóstico, en orden

```
□ 1. Mira QUE grant_type estabas usando: authorization_code o refresh_token
□ 2. Si era authorization_code -> es causa 1 o redirect_uri. Ve al bloque de abajo
□ 3. Si era refresh_token -> compara el token que mandaste con el ULTIMO guardado
□ 4. Revisa cuantos procesos tuyos pueden refrescar a la vez
□ 5. Mira la fecha del ultimo refresh exitoso: si pasaron >6 meses, es causa 3
```

## Causa 1: el `code` ya se usó

El `code` es de **un solo uso** y vive muy poco. Lo que casi siempre pasó:

| Situación | Por qué se rompe |
|---|---|
| Recargaste la página del `redirect_uri` | El navegador reenvía la misma URL con el mismo `code` |
| Guardaste el `code` para canjearlo después | Ya expiró |
| Lo canjeaste, falló al guardar y reintentaste | El canje sirvió; falló tu base de datos |
| El `redirect_uri` no coincide exacto | ML rechaza el canje sin decirte que es por eso |

Arreglo: canjea el `code` **una sola vez, inmediatamente**, y marca en tu base que ya lo usaste.
Si necesitas reconectar, reinicia el flujo desde cero (`177`); nunca reuses un `code`.

## Causa 2: el `refresh_token` no es el último — la causa real del 80%

Recuerda la regla de `178`: al refrescar, ML **invalida el anterior** y emite uno nuevo. Si no
guardaste el nuevo, el próximo refresh muere.

Los cuatro escenarios que producen esto:

| Escenario | Detalle |
|---|---|
| Guardaste solo el `access_token` | Tu código lee ese campo del JSON e ignora el resto |
| El `refresh_token` vive en un `.env` | No se puede reescribir en caliente |
| Dos procesos refrescaron a la vez | El segundo quedó con basura |
| Restauraste un respaldo de la base | El respaldo trae un `refresh_token` ya rotado |

El último es traicionero: restaurar un backup viejo de tu base de datos **te desconecta de
Mercado Libre**, porque el token que trae el respaldo ya fue invalidado por una rotación posterior.

## Causa 3: expiró de verdad

Seis meses sin usarlo. Pasa con cuentas de clientes que dejaron de operar, o con un entorno de
pruebas dormido. No hay arreglo por API: **toca reautorizar a mano**, el vendedor tiene que volver
a pasar por la pantalla de permisos.

Prevención: un trabajo programado que toque cada cuenta conectada al menos una vez al mes.

## La recuperación

Una vez diagnosticado, esto es lo único que se puede hacer:

| Causa | Arreglo |
|---|---|
| 1 — `code` usado | Reiniciar el flujo de autorización desde el principio |
| 1 — `redirect_uri` | Corregir la URL y reiniciar el flujo |
| 2 — token desactualizado | Reiniciar el flujo **y** arreglar la persistencia, o se repite |
| 3 — expirado | Reiniciar el flujo |

En los cuatro casos el camino es el mismo: volver a autorizar. **No hay endpoint de rescate: un
`refresh_token` perdido es un vendedor que tiene que volver a dar clic.** Por eso el patrón de
persistencia de `178` no es opcional.

## Cómo evitar que te vuelva a pasar

```
□ Un solo componente del sistema llama a /oauth/token
□ Ese componente escribe el refresh_token NUEVO antes de usar el access_token
□ Candado por user_id: dos refrescos simultaneos de la misma cuenta, imposibles
□ Alarma cuando un refresh falla: hoy, no cuando el cliente reclame
□ Nunca restaures un backup de la tabla de tokens sin reconectar despues
□ Registra en log la fecha del ultimo refresh exitoso por cuenta
```

## El error de diagnóstico más caro

Ver `invalid_grant` en un refresh y salir a "arreglar el token" pidiendo uno nuevo desde el panel,
sin entender que el problema es la persistencia. Queda funcionando otras seis horas, se vuelve a
caer, y así durante semanas. **Si el error vuelve al día siguiente, el bug no es el token: es
dónde lo guardas.**

## Su primo: el 401

No lo confundas. `invalid_grant` (400) es del endpoint de tokens. Un `401 Unauthorized` en un
endpoint normal significa que el `access_token` venció o no lo mandaste bien: eso se arregla
refrescando, y es normal. `invalid_grant` no es normal.

## Relacionados

`176` crear tu aplicación · `177` el flujo OAuth · `178` tokens y renovación ·
`180` los endpoints · `193` límites de uso · `199` arquitectura de referencia
