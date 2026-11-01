# OAuth: el flujo

Mercado Libre usa **OAuth 2.0 con Authorization Code Grant** (oficial, verificado sep-2026). En
cristiano: el vendedor autoriza en la página de ML, ML te devuelve un código de un solo uso, y tú
cambias ese código por un token desde tu servidor. Nunca le pides la contraseña al vendedor.

## Por qué existe este baile

Si le pidieras usuario y contraseña al vendedor, tendrías su cuenta completa para siempre y él no
podría quitarte el permiso sin cambiar la clave. OAuth resuelve tres cosas: permisos limitados
(scopes), permiso revocable y credenciales que nunca pasan por tu código.

## El flujo, paso a paso

```
  VENDEDOR                TU SERVIDOR                 MERCADO LIBRE
     |                        |                             |
     |  1. clic "Conectar"    |                             |
     |----------------------->|                             |
     |                        |  2. redirige a /authorization
     |<-------------------------------------------------------|
     |  3. inicia sesion y aprueba los permisos              |
     |------------------------------------------------------>|
     |                        |                             |
     |  4. ML lo devuelve a tu redirect_uri con ?code=...    |
     |<------------------------------------------------------|
     |----------------------->|                             |
     |                        |  5. POST /oauth/token       |
     |                        |     grant_type=authorization_code
     |                        |---------------------------->|
     |                        |  6. access_token + refresh_token
     |                        |<----------------------------|
     |                        |  7. GUARDAR AMBOS YA        |
     |  8. "listo, conectado" |                             |
     |<-----------------------|                             |
```

## Paso 2: mandarlo a autorizar

La URL de autorización lleva estos parámetros:

| Parámetro | Valor |
|---|---|
| `response_type` | `code` |
| `client_id` | Tu APP_ID (`176`) |
| `redirect_uri` | Exacto al registrado, carácter por carácter (`176`) |
| `state` | Una cadena tuya, aleatoria, para reconocer la vuelta |
| `code_challenge` | Solo si activaste PKCE |
| `code_challenge_method` | `S256`, solo si activaste PKCE |

El `state` no es opcional en la práctica: es lo que te protege de que alguien te empuje una
autorización ajena, y es donde metes tu propio identificador interno. **Nunca metas datos propios
en el `redirect_uri`: para eso está `state`.**

## Paso 5: canjear el código

```
POST https://api.mercadolibre.com/oauth/token
Content-Type: application/x-www-form-urlencoded
Accept: application/json
```

Cuerpo:

```
grant_type=authorization_code
client_id=TU_APP_ID
client_secret=TU_SECRET
code=EL_CODE_QUE_LLEGO_EN_LA_URL
redirect_uri=EL_MISMO_REGISTRADO
```

La respuesta trae, en forma típica:

```json
{
  "access_token": "APP_USR-...",
  "token_type": "bearer",
  "expires_in": 21600,
  "scope": "offline_access read write",
  "user_id": 123456789,
  "refresh_token": "TG-..."
}
```

`expires_in: 21600` son **6 horas** en segundos. El `user_id` es la cuenta que te autorizó: esa es
tu llave para guardar los tokens (ojo con el tamaño del número, ver `199`).

## Las reglas duras del `code`

| Regla | Consecuencia si la rompes |
|---|---|
| Es de **un solo uso** | Reintentar el canje da `invalid_grant` (`179`) |
| Vive muy poco | Cánjealo apenas llega, no lo encoles |
| El `redirect_uri` del canje debe ser idéntico al de la autorización | `invalid_grant` |
| Viaja en la URL | Queda en logs del navegador y del servidor: no lo imprimas |

## PKCE

PKCE ("Proof Key for Code Exchange") es una capa extra: en vez de confiar solo en el
`client_secret`, generas un secreto temporal por cada intento de login.

| Dato | Estado |
|---|---|
| ¿Está disponible? | Sí |
| ¿Es obligatorio? | **No por defecto** |
| ¿Cómo se activa? | Por aplicación, desde "Mis aplicaciones" |
| ¿Qué pasa al activarlo? | **Queda obligatorio para esa app**: sin PKCE deja de funcionar |

(Confianza MEDIA — comportamiento documentado por ML, no verificado en vivo en una cuenta de
Colombia en sep-2026.)

Cómo funciona, en tres pasos:

```
1. Generas un "code_verifier": cadena aleatoria larga, la guardas en sesión
2. Calculas code_challenge = BASE64URL( SHA256(code_verifier) ) y lo mandas en el paso 2
3. Al canjear el code, mandas el code_verifier original
```

Veredicto: si tu integración es un servidor privado que solo conecta tu propia cuenta, PKCE no te
aporta gran cosa y te suma una forma más de romperte. Si vas a conectar cuentas de clientes,
actívalo. **Y no lo actives a mitad de camino sin desplegar el código nuevo primero: el día que
lo prendes, todo login viejo deja de funcionar.**

## Paso 7: guardar

Esto es la parte que la gente hace mal y se paga en `179`. Al recibir la respuesta:

```
□ Guarda access_token, refresh_token, user_id y la hora de expiracion
□ Guardalos ANTES de responderle nada al vendedor
□ Guardalos por user_id, no en una variable global
□ Si ya existia un registro para ese user_id, REEMPLAZALO
□ Nunca guardes dos refresh_token vivos de la misma cuenta
```

## El error clásico

Probar el flujo varias veces en el navegador recargando la página del `redirect_uri`. Cada recarga
reenvía el mismo `code` ya canjeado y ML responde `invalid_grant`, y como el mensaje habla de
"expirado o ya usado", la gente cree que el token expira en segundos y sale a buscar un bug que no
existe. Es el `code`, no el token (`179`).

## Relacionados

`176` crear tu aplicación · `178` tokens y renovación · `179` el error invalid_grant ·
`180` los endpoints · `194` usuarios de prueba · `199` arquitectura de referencia
