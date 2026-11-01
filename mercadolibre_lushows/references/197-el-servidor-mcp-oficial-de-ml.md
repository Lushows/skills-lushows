# El servidor MCP oficial de ML

Mercado Libre publicó un servidor MCP oficial: te deja operar tu cuenta hablándole en español a
Claude o a Cursor, sin escribir código. Es real y es de ellos. También es muy nuevo, y para lo que
tu negocio no puede permitirse que falle, sigue siendo más confiable el REST directo.

## Qué es MCP, para quien no lo sabe

MCP (Model Context Protocol) es un estándar para que un modelo de IA pueda **usar herramientas de
verdad**, no solo hablar de ellas. Un "servidor MCP" es un programa que expone un conjunto de
acciones; el modelo las ve, elige cuál usar y la ejecuta.

| Sin MCP | Con MCP |
|---|---|
| "Escríbeme el código para bajar el stock" | "Baja el stock del MCO123 a 5" y lo hace |
| Tú copias, pegas y ejecutas | El modelo llama al endpoint |
| El modelo no ve tus datos reales | El modelo lee tu cuenta y responde con datos tuyos |

Es el mismo mecanismo que ya usas cuando Claude lee archivos de tu computador: alguien expuso esas
acciones y el modelo las invoca.

## El servidor de Mercado Libre

| Dato | Valor |
|---|---|
| Repositorio | `github.com/mercadolibre/mercadolibre-mcp-server` |
| Endpoint | `https://mcp.mercadolibre.com/mcp` |
| Autenticación | El **access_token OAuth** en el header del cliente MCP |
| Clientes compatibles | Claude Desktop, Cursor y otros que hablen MCP |

(oficial ML, verificado sep-2026: que existe es ALTA; su madurez es MEDIA.)

Existe además un servidor MCP hermano de **Mercado Pago**, más documentado.

## Cómo se conecta

El token es el mismo `access_token` que obtienes del flujo OAuth de `177`. No hay un camino
distinto ni credenciales aparte.

```
□ 1. Tienes una aplicacion registrada con sus scopes (`176`)
□ 2. Completas el flujo OAuth y obtienes un access_token (`177`)
□ 3. Configuras el cliente MCP apuntando a https://mcp.mercadolibre.com/mcp
□ 4. Pasas el access_token en el header del cliente
□ 5. El modelo ya puede consultar y operar la cuenta conectada
```

Y aquí llega el detalle que nadie menciona: **el `access_token` dura 6 horas** (`178`). El cliente
MCP de escritorio no renueva tokens por ti. En la práctica, cada jornada larga de trabajo implica
volver a poner un token fresco.

## Para qué sirve de verdad

| Uso | Veredicto |
|---|---|
| Explorar tu cuenta y entender los datos | **Excelente.** Es lo que mejor hace |
| Consultas puntuales: "¿qué órdenes tengo sin despachar?" | Muy bueno |
| Descubrir categorías y atributos antes de publicar (`182`) | Muy bueno |
| Prototipar antes de escribir la integración | Muy bueno |
| Un cambio manual ocasional | Sirve |
| Actualizar stock cada día, sin falta | **No.** Eso es un proceso, no una conversación |
| Responder preguntas automáticamente | **No.** Necesita un webhook, no una persona (`195`) |
| Cualquier cosa que deba correr sola a las 3 a.m. | **No** |

**MCP es una silla de trabajo, no un motor. Lo que tiene que correr sin ti, corre en REST.**

## La honestidad sobre la madurez

El repositorio es **pequeño y reciente**: pocas estrellas, un commit visible al momento de
verificarlo (sep-2026). Eso no lo hace malo — lo hace nuevo. Lo que implica:

| Riesgo | Detalle |
|---|---|
| Cobertura desconocida | No está claro qué parte de la API expone |
| Puede cambiar sin aviso | Un servidor de un commit no tiene compromiso de estabilidad |
| Poca documentación | Menos ejemplos y menos gente con quien comparar errores |
| Sin garantía de soporte | No es un producto comercial con SLA |

Veredicto: **úsalo para pensar y explorar; construye en REST lo que el negocio necesita que no
falle.** Si el bot de preguntas o el sincronizador de stock dependen de un servidor MCP nuevo,
tienes una dependencia que no controlas en el camino crítico.

## Un aviso de seguridad propio de MCP

Cuando conectas un servidor MCP con tu `access_token`, le estás dando al modelo la capacidad de
**escribir** en tu cuenta: publicar, cambiar precios, responder. No es lectura.

```
□ Conecta solo servidores MCP de origen verificable (este lo es: repo oficial de ML)
□ Revisa que operacion va a ejecutar antes de aprobarla, sobre todo si cambia precios
□ No dejes un token de produccion pegado en la configuracion de tu escritorio
□ Si vas a explorar sin miedo, hazlo con un usuario de test (`194`)
```

Ese último punto es el buen hábito: para aprender, usuario de test; para operar, atención.

## Una lección que aplica también aquí

El centro de ayuda de Mercado Libre cambió su esquema de URLs y **las direcciones viejas no dan
404: redirigen en silencio a una página distinta** (verificado sep-2026). Es el mismo tipo de
fragilidad que tiene una herramienta nueva: responde, parece que funcionó, y lo que devolvió no es
lo que pediste. Por eso la regla vale igual para MCP que para REST: **verifica la forma de la
respuesta, no solo que no haya error** (`199`).

## El error clásico

Enamorarse de la conversación y montar la operación encima. "Le pido a Claude que actualice el
stock todas las mañanas" funciona hasta la mañana en que estás ocupado, el token venció, o el
servidor cambió una herramienta de nombre. Los procesos que sostienen el negocio no pueden
depender de que alguien abra una aplicación de escritorio.

## Relacionados

`176` crear tu aplicación · `177` el flujo OAuth · `178` tokens y renovación ·
`180` los endpoints · `182` atributos de categoría · `194` usuarios de prueba ·
`195` el bot de preguntas con IA · `198` integradores · `199` arquitectura de referencia
