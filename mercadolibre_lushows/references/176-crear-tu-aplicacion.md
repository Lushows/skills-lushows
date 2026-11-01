# Crear tu aplicación

Antes de tocar un solo endpoint privado de Mercado Libre necesitas una "aplicación": un registro
que te entrega dos credenciales y define a dónde puede volver el usuario después de autorizarte.
El 90% de los problemas de OAuth del primer día no son de código, son de este formulario mal lleno.

## Qué es una aplicación

Es la identidad de tu software frente a Mercado Libre. No es tu cuenta de vendedor: es el programa
que va a actuar **en nombre** de una cuenta de vendedor (la tuya o la de un cliente tuyo).

| Concepto | Qué es | Dónde vive |
|---|---|---|
| Cuenta de vendedor | Tu usuario que publica y vende | mercadolibre.com.co |
| Aplicación | Tu programa registrado | Devcenter / "Mis aplicaciones" |
| `client_id` (APP_ID) | El número público de tu app | Lo puedes poner en una URL |
| `client_secret` | La clave privada de tu app | **Nunca** en el navegador ni en el repo |
| `access_token` | El permiso vivo, dura 6 horas | En tu servidor (`178`) |
| `refresh_token` | El permiso para renovar, dura 6 meses | En tu base de datos (`178`) |

## Los datos que te va a pedir

```
□ Nombre y descripción de la app (lo ve el usuario al autorizar)
□ Logo
□ redirect_uri (URL de retorno) — el campo crítico, ver abajo
□ Scopes: read, write, offline_access
□ Topics de notificación y callback_url para webhooks (`189`)
```

## Los scopes

| Scope | Qué habilita | ¿Lo necesitas? |
|---|---|---|
| `read` | Leer tus datos: ítems, órdenes, preguntas | Siempre |
| `write` | Crear y modificar: publicar, cambiar stock, responder | Sí, salvo que solo leas |
| `offline_access` | Que te entreguen `refresh_token` | **Sí, imprescindible** |

Sin `offline_access` no hay `refresh_token`, y sin `refresh_token` tu bot se muere a las 6 horas y
toca volver a autorizar a mano. **Un bot sin `offline_access` no es un bot, es un experimento.**

## El `redirect_uri`: la regla que rompe a todo el mundo

El `redirect_uri` es la URL a la que Mercado Libre devuelve al usuario después de que autoriza,
con el `code` pegado en la URL.

> **Debe ser exacto y estático: sin query params variables ni comodines, coincidiendo carácter por
> carácter con el registrado** (oficial ML, verificado sep-2026).

Qué significa "carácter por carácter":

| Registrado | Usado en la petición | ¿Funciona? |
|---|---|---|
| `https://misitio.com/cb` | `https://misitio.com/cb` | Sí |
| `https://misitio.com/cb` | `https://misitio.com/cb/` | **No** (barra final) |
| `https://misitio.com/cb` | `http://misitio.com/oauth/callback` | **No** (http vs https) |
| `https://misitio.com/cb` | `https://www.misitio.com/oauth/callback` | **No** (www) |
| `https://misitio.com/cb` | `https://misitio.com/cb?u=7` | **No** (query param) |
| `https://misitio.com/*` | cualquiera | **No** (comodines no se aceptan) |

Si necesitas llevar información propia de un lado al otro (por ejemplo, qué cliente tuyo está
autorizando), **no la metas en el `redirect_uri`**: va en el parámetro `state` del flujo (`177`).

## Una app o varias

| Situación | Veredicto |
|---|---|
| Vendes solo tú | **Una sola app.** Conecta tu propia cuenta y listo |
| Tienes dos cuentas de vendedor propias | Una app, dos juegos de tokens guardados por `user_id` |
| Vas a conectar cuentas de clientes | Una app, y guardas un juego de tokens por cada `user_id` |
| Quieres separar pruebas de producción | Dos apps distintas, con `redirect_uri` distintos |

Esa última es la buena práctica: una app "dev" apuntando a tu entorno de pruebas con usuarios de
test (`194`) y una app "prod" apuntando al servidor real.

## Guardar las credenciales

El `client_secret` es equivalente a la llave de tu negocio. Reglas mínimas:

```
□ Nunca en el código fuente ni en GitHub
□ Nunca en el frontend: el navegador lo expone siempre
□ En variables de entorno del servidor
□ Rotable: si se filtra, se regenera desde el panel de la app
□ Una app comprometida puede publicar y cambiar precios en tu cuenta
```

Cómo montar esa gestión de secretos en tu hosting es de `engineer_visualopen_lushows`; aquí solo
te digo que sin eso no sigas.

## Certificación de aplicaciones

Mercado Libre puede exigir re-certificación cuando modificas una app ya certificada, y puede
revocar certificaciones. Si tu app va a conectar cuentas de terceros, cuenta con ese proceso en el
cronograma y no cambies flujos críticos la semana del lanzamiento.

## El error clásico

Registrar el `redirect_uri` con `localhost` mientras desarrollas y olvidar cambiarlo al desplegar.
El síntoma no es un error claro: ML te rebota la autorización o te devuelve a una URL que ya no
existe, y como el `code` viaja en esa URL, lo pierdes. Registra desde el día uno la URL definitiva
de producción y usa una app aparte para el entorno local.

El segundo error clásico: guardar el `client_secret` en el frontend "porque es más fácil probar".
Cualquiera que abra las herramientas del navegador se lleva la llave de tu cuenta.

## Verificación antes de seguir

```
□ Tengo client_id y client_secret, y el secret NO está en el repo
□ El redirect_uri registrado es exactamente la URL que va a usar mi servidor
□ Marqué offline_access
□ Sé si activé PKCE o no (`177`)
□ Registré la callback_url de webhooks si la voy a usar (`189`)
```

## Relacionados

`175` cuándo automatizar · `177` el flujo OAuth · `178` tokens y renovación ·
`179` invalid_grant · `189` webhooks · `194` usuarios de prueba · `199` arquitectura
