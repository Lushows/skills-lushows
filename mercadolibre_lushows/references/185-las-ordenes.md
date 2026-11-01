# Las órdenes

Traer las órdenes a tu sistema es la automatización más segura que existe: es lectura pura, si
falla no rompes nada en Mercado Libre. Es también la base de todo lo demás — facturar, despachar,
descontar inventario y medir de verdad cuánto te queda.

## Los dos endpoints

| Qué | Endpoint |
|---|---|
| Buscar órdenes del vendedor | `GET /orders/search?seller=$SELLER_ID` |
| Detalle de una orden | `GET /orders/$ORDER_ID` |

```
GET https://api.mercadolibre.com/orders/search?seller=123456789
Authorization: Bearer APP_USR-...
```

El `$SELLER_ID` es tu `user_id`, el que vino en la respuesta del token (`177`) o el que devuelve
`GET /users/me`.

## Qué te interesa de una orden

| Campo | Para qué |
|---|---|
| `id` | La llave. Guárdalo como texto o entero de 64 bits (`199`) |
| `status` | Estado de la orden |
| `date_created` / `date_closed` | Cuándo entró y cuándo se cerró |
| `order_items[]` | Qué compró: ítem, variación, cantidad, precio unitario |
| `total_amount` | Lo que pagó el comprador |
| `payments[]` | Cómo pagó y en qué estado va el pago |
| `buyer` | El comprador (datos limitados, ver abajo) |
| `shipping.id` | El `shipment_id` para consultar el envío (`186`) |
| `pack_id` | Si existe, agrupa varias órdenes en un mismo carrito (`188`) |

El `pack_id` es importante: cuando un comprador lleva tres productos tuyos en un carrito, puede
haber tres órdenes y **un solo envío**. Si tu sistema trata cada orden como un paquete, despachas
tres veces lo que era uno.

## Cuánto ves del comprador

Mercado Libre restringe los datos personales del comprador. Verás lo necesario para despachar y
poco más, y la dirección suele venir por el recurso de envío, no por la orden. No construyas nada
que dependa de tener el teléfono o el correo del comprador: además de que puede no venir, usarlo
para contactarlo fuera de la plataforma está prohibido (`132`).

## Cada cuánto consultar

| Estrategia | Ritmo | Veredicto |
|---|---|---|
| **Webhook `orders_v2`** | Instantáneo | **La correcta** (`189`, `190`) |
| Polling a `/orders/search` | Cada 5-15 minutos | Solo como red de seguridad |
| Polling cada minuto | — | No. Te ganas un `429` sin ganar nada (`193`) |

Lo oficial de Mercado Libre es explícito: **preferir webhooks sobre polling**. Pero el polling
lento no sobra: si tu servidor estuvo caído una hora, los webhooks de esa hora se perdieron
después de 8 reintentos (`192`), y un barrido cada 15 minutos los recupera.

**Webhook para la velocidad, polling lento para la red de seguridad. Los dos, no uno.**

## Paginación

`/orders/search` devuelve páginas. Usa `offset` y `limit` y **lee el total antes de asumir que
vino todo**. El error de traer solo la primera página y creer que son todas las ventas del mes es
frecuente y produce reportes que no cuadran.

```
□ Pide la primera pagina y lee el total de resultados
□ Recorre con offset hasta cubrirlo
□ Ordena por fecha y guarda la fecha del ultimo procesado
□ En la proxima corrida, arranca desde esa fecha, no desde cero
```

## Qué haces con cada orden

```
□ 1. Guardarla en tu base con su ID (idempotente: si ya existe, no dupliques) (`192`)
□ 2. Descontar inventario en tu sistema y empujar el stock a ML (`183`, `196`)
□ 3. Consultar el envio para saber a donde va y cuanto costo (`186`)
□ 4. Emitir la factura electronica -> integrador, no codigo propio (`198`)
□ 5. Registrar el margen real de esa venta (`75`-`99`)
□ 6. Alarma si la orden lleva X horas sin despachar
```

El punto 6 es el de mayor retorno: los **envíos incorrectos** (despacho con demora o desde
depósito incorrecto) son una de las tres variables base del termómetro (`126`).

## El margen real se calcula aquí

La orden te da el precio de venta. El costo real de esa venta necesita además la comisión de la
categoría y el costo del envío que asumiste (`186`). Cruzando eso, tu sistema puede decirte lo que
el panel no te dice de una: cuánto te dejó cada venta. La fórmula está en el bloque de margen y el
cálculo se ejecuta, no se estima: `Matematicas_lushows`.

## El error clásico

Reprocesar. Cada vez que corre el sincronizador, vuelve a traer las mismas órdenes y las vuelve a
insertar, o peor, vuelve a descontar inventario. El resultado es un stock que baja solo. La
defensa es una sola: **el `id` de la orden es tu llave de idempotencia; si ya existe, no la
proceses otra vez** (`192`).

El segundo error: tratar cada orden de un mismo `pack_id` como un envío independiente.

## Relacionados

`126` las tres métricas del termómetro · `132` prohibido sacar al comprador de la plataforma ·
`180` los endpoints · `183` precio y stock · `186` los envíos · `188` mensajes de posventa ·
`190` topics y payload · `192` duplicados y reintentos · `198` integradores
