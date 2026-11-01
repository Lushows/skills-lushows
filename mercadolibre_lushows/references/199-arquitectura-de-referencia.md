# Arquitectura de referencia

El plano completo de una integración con Mercado Libre bien hecha, con la tabla de los errores
clásicos y en qué pieza ocurre cada uno. Si vas a construir, esta es la forma que funciona; si
algo ya se te rompió, aquí está el mapa para encontrar dónde.

## El diagrama

```
   MERCADO LIBRE
        |
        |  POST notificacion (topic + resource)            (`190`)
        v
 +------------------------+
 | 1. RECEPTOR DE WEBHOOK |   unico oficio: apuntar y contestar
 |    HTTP 200 < 500 ms   |   NADA de red aqui                (`191`)
 +-----------+------------+
             | encola {_id, resource, topic, user_id}
             v
 +------------------------+
 | 2. COLA                |   sobrevive a reinicios
 |    duradera            |   guarda intentos y estado        (`192`)
 +-----------+------------+
             |
             v
 +------------------------+     lee     +------------------------+
 | 3. WORKERS             |<----------->| 4. ALMACEN DE TOKENS   |
 |    dedup por _id       |             |    una fila por cuenta |
 |    GET del recurso     |             |    access + refresh    |
 |    procesan por topic  |             |    UN SOLO renovador   |
 +--+----+----+-----------+             +------------------------+
    |    |    |                                    ^      (`178`, `179`)
    |    |    |                                    |
    |    |    +----> 6. BOT DE PREGUNTAS ----------+
    |    |              clasifica: responder o escalar
    |    |              filtro de salida obligatorio     (`195`)
    |    |
    |    +---------> 5. SINCRONIZADOR DE STOCK ----------+
    |                   colchon de seguridad              (`183`, `196`)
    |                   verifica leyendo de vuelta
    |
    +--------------> 7. ORDENES / ENVIOS / MARGEN         (`185`, `186`)

 +------------------------+
 | 8. BARRIDO DE RESPALDO |   polling lento cada 15 min
 |    red de seguridad    |   recupera lo que se perdio   (`192`)
 +------------------------+

 +------------------------+
 | 9. VIGILANCIA          |   latencia p95, attempts>1, refresh fallido,
 |    alarmas             |   avisos por hora, colas atascadas
 +------------------------+
```

## Las nueve piezas, una línea cada una

| # | Pieza | Su única responsabilidad |
|---|---|---|
| 1 | Receptor | Contestar 200 en menos de 500 ms. Nada más |
| 2 | Cola | Que ningún aviso se pierda si algo se cae |
| 3 | Workers | Deduplicar, hacer el `GET`, procesar por topic |
| 4 | Almacén de tokens | Una fila por cuenta, un solo renovador |
| 5 | Sincronizador de stock | Que ML nunca muestre más de lo que tienes |
| 6 | Bot de preguntas | Responder lo verificable, escalar lo demás |
| 7 | Órdenes y margen | Guardar la venta y lo que de verdad dejó |
| 8 | Barrido de respaldo | Recuperar lo que los webhooks perdieron |
| 9 | Vigilancia | Enterarte antes que tu cliente |

**Cada pieza hace una cosa. Si tu receptor de webhooks también consulta la API, no tienes
arquitectura: tienes un solo archivo con suerte.**

## La tabla de errores clásicos y dónde ocurren

| Error | Pieza | Síntoma | Módulo |
|---|---|---|---|
| Procesar antes de responder 200 | 1 | Suscripción desactivada, silencio total | `191` |
| Sin cola en serverless | 1-2 | Avisos que llegan y nunca se procesan | `191` |
| No deduplicar | 3 | Stock que baja solo, reportes inflados | `192` |
| No guardar el `refresh_token` nuevo | 4 | Funciona el día 1, muere el día 2 | `178` |
| Dos procesos refrescando a la vez | 4 | `invalid_grant` intermitente | `178`, `179` |
| `refresh_token` en un `.env` | 4 | Muere a las 6 horas de la primera renovación | `178` |
| Reusar el `code` de OAuth | 4 | `invalid_grant` al conectar | `179` |
| `redirect_uri` con barra de más | 4 | La autorización nunca completa | `176` |
| `PUT /items` en cuenta multi-origen | 5 | 200 que no cambia nada | `184` |
| Sincronizar en un solo sentido | 5 | Sobreventa, cancelación, suspensión | `196` |
| Pelear con el repricer | 5 | Tu precio vuelve solo | `183` |
| Barrer todo el catálogo cada 5 minutos | 5, 8 | `429` intermitentes | `193` |
| Bot que promete lo que no leyó | 6 | Reclamos no excluibles | `195` |
| Bot que da contacto | 6 | Infracción a escala | `132`, `195` |
| Marcar leídos los hilos al consultarlos | 7 | Mensajes sin responder, reloj de 24 h | `188` |
| Traer solo la primera página | 7, 8 | Reportes que no cuadran | `185` |
| No tener barrido de respaldo | 8 | Ventas perdidas tras una caída | `192` |
| No vigilar nada | 9 | Te enteras por un reclamo | `191` |

## Dos datos que truenan sistemas enteros

### Los IDs no caben en 32 bits

> Desde **dic-2024** los `user_id` nuevos exceden Int32 (2.147.483.647) y usan **Int64**, hasta 20
> dígitos. (oficial ML, verificado sep-2026)

Si guardas IDs en columnas de 32 bits, tu sistema **funciona con las cuentas viejas y truena con
los usuarios nuevos**: compradores recientes, vendedores recién registrados. El fallo es
intermitente y por eso cuesta encontrarlo.

```
□ user_id, order_id, item_id, question_id, shipment_id: 64 bits o texto
□ Revisa tambien el JSON de tu lenguaje: hay lenguajes que pierden precision en enteros grandes
□ Si ya guardaste IDs truncados, no los "arregles": reimportalos
```

Veredicto: **guarda todos los identificadores como texto.** No vas a hacer aritmética con ellos y
te ahorras el problema para siempre.

### Un 200 no prueba que llegaste al sitio correcto

El centro de ayuda de Mercado Libre cambió su esquema de URLs y **las direcciones viejas no dan
404: redirigen en silencio a una página distinta** (verificado sep-2026). La lección de
integración es directa:

| Regla | Por qué |
|---|---|
| Nunca confíes en que una URL guardada sigue sirviendo lo mismo | Puede redirigir sin avisar |
| Valida la **forma** de la respuesta, no solo el código HTTP | Un 200 puede traer otra cosa |
| Tras un `PUT` crítico, lee de vuelta y compara | `183`, `184` |
| Un campo que esperabas y no vino es un error, no un `null` | Fállalo ruidosamente |

**Verificar que hubo respuesta no es verificar que hubo resultado.**

## El orden de construcción

```
□ 1. OAuth completo: autorizar, refrescar, y el refresh persistido bien (`177`, `178`)
□ 2. Receptor que responde 200 en <500 ms, sin hacer nada mas (`191`)
□ 3. Cola y un worker que solo escribe en un log (`192`)
□ 4. Dedup por _id, probada reenviando el mismo aviso a mano
□ 5. Ordenes: guardar cada venta (`185`)
□ 6. Stock: descontar y verificar leyendo de vuelta (`183`, `184`)
□ 7. Barrido de respaldo cada 15 minutos (`185`)
□ 8. Alarmas: latencia, attempts>1, refresh fallido, avisos por hora
□ 9. Solo ahora, el bot de preguntas (`195`)
```

Del 1 al 8 son los cimientos. **El bot va al final, no al principio: es lo más divertido y lo
menos urgente.** Y todo se prueba con usuarios de test, nunca con la cuenta real (`194`).

## La frontera, otra vez

Qué endpoint, qué payload y qué lógica de negocio: esta skill. Cómo montar la cola, dónde corre el
worker, cómo proteges el endpoint, cómo despliegas y cómo guardas los secretos:
`engineer_visualopen_lushows`. El plano es de aquí; los materiales son de allá.

## Relacionados

`175` cuándo automatizar · `178` tokens · `179` invalid_grant · `183` precio y stock ·
`184` multi-bodega · `185` órdenes · `188` posventa · `190` topics y payload ·
`191` responder en 500 ms · `192` duplicados · `193` límites · `194` usuarios de prueba ·
`195` el bot con IA · `196` sobreventa · `198` integradores
