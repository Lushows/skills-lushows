# La sobreventa multicanal

Vender la misma unidad en dos canales a la vez es el accidente más caro de un vendedor
multicanal, porque no termina en una devolución: termina en una cancelación tuya, y las
cancelaciones son la métrica que suspende cuentas.

## Lo que la API no te da

> La API de Mercado Libre **no tiene reserva de stock cross-canal ni locking atómico.**
> (análisis, confianza MEDIA-BAJA: es una ausencia comprobable, no un texto oficial)

Traducido:

| Lo que NO existe | Consecuencia |
|---|---|
| "Reservar" una unidad mientras el comprador paga | No puedes apartar nada |
| Un candado que bloquee la venta en otros canales | Cada canal vende por su cuenta |
| Una confirmación de "descontado" instantánea | Siempre hay un rato de desfase |
| Un inventario compartido con tu tienda física | No existe tal cosa |

**Mercado Libre no sabe que vendes en otra parte, y no hay forma de contárselo en tiempo real.**

## La ventana de riesgo

Es el tiempo entre que vendes en un canal y el stock queda actualizado en el otro:

```
t0   Vendes la ultima unidad en tu tienda fisica
t1   Alguien la registra en tu sistema
t2   Tu sistema dispara el PUT a Mercado Libre
t3   ML procesa y la publicacion queda en 0

     |<---------- VENTANA DE RIESGO ---------->|
     Todo lo que se venda en ML aqui, no lo tienes
```

Cuánto dura cada tramo, y qué la agranda:

| Tramo | Duración típica | Qué la agranda |
|---|---|---|
| t0 → t1 | Segundos a horas | Registro manual, caja que no está conectada |
| t1 → t2 | Inmediato o hasta el próximo barrido | **Polling en vez de webhook** (`189`) |
| t2 → t3 | Segundos | Reintentos, `429` (`193`) |

El tramo que de verdad manda es t0 → t1, y ese no es un problema de API: es de operación. Si nadie
registra la venta física hasta el cierre de caja, ninguna integración te salva.

## Las dos mitigaciones que sí funcionan

### 1. Colchón de seguridad

Publicar menos unidades de las que tienes. Restar 1 o 2 unidades al stock real que muestras en ML.

| Tu rotación | Colchón |
|---|---|
| Vendes poco, canal único | 0 |
| Multicanal, rotación baja | 1 unidad |
| Multicanal, rotación alta | 2 unidades o más |
| Producto estrella en promoción | Más colchón, y vigilancia manual |

Cuesta ventas potenciales. Cuesta menos que una cancelación.

### 2. Webhooks en vez de polling

Pasar de barrer cada 15 minutos a reaccionar en segundos reduce t1 → t2 casi a cero. Es lo que
Mercado Libre recomienda oficialmente y aquí la razón es de plata, no de elegancia (`189`, `190`).

### Lo que NO funciona

| Idea | Por qué falla |
|---|---|
| "Bajo el stock apenas alguien entra al carrito" | No te enteras: ML no avisa carritos |
| "Sincronizo cada minuto" | Te ganas un `429` y no cierras la ventana (`193`) |
| "Un Excel compartido" | El humano es el tramo lento, no la máquina |
| "Cancelo y ya" | Ahí empieza el problema, no ahí se acaba |

## Por qué la cancelación es tan cara

La cadena completa:

```
Sobreventa -> no tienes el producto -> cancelas tu la venta
  -> cuenta como VENTA CANCELADA en tu termometro
     -> mas del 2,5% de canceladas -> la cuenta PUEDE SER SUSPENDIDA
```

Las definiciones oficiales que importan (ML Colombia, verificado sep-2026):

| Dato | Valor |
|---|---|
| Venta cancelada | "El comprador recibe su dinero de vuelta antes de que hayas entregado" |
| Quién es penalizado | **Solo si cancelas tú.** Si cancela el comprador, no te afecta |
| Umbral de suspensión | **Más del 2,5% de ventas canceladas** |
| Devoluciones | **No** son cancelaciones |
| Si te piden cancelar y reembolsas en 2 días hábiles sin haber entregado | Reputación intacta |

Esa última fila es la única salida decente cuando ya metiste la pata: **si el comprador acepta
pedir la cancelación y tú reembolsas dentro de 2 días hábiles sin haber despachado, no te afecta.**
Los detalles están en `139`.

Y hay un costo extra que nadie suma: el ítem que pasa a stock 0 sale de la competencia y del
catálogo, y al reponer tiene que reconstruir sus señales (`183`, `63`).

## Lista de chequeo del vendedor multicanal

```
□ Un solo sistema es la VERDAD del inventario; los canales lo reflejan
□ Nadie edita stock directamente en el panel de ML
□ Webhook orders_v2 descontando en mi sistema al instante (`190`)
□ Colchon de seguridad configurado por SKU, no global
□ Alarma cuando un SKU baja de N unidades en total
□ Los SKU de rotacion alta se revisan a mano todos los dias
□ Protocolo escrito de que hacer cuando ya vendi algo que no tengo
```

## Qué hacer cuando ya pasó

```
□ 1. Escribele al comprador de inmediato por el canal de ML (`188`)
□ 2. Ofrece alternativa real: otra variante, o plazo concreto
□ 3. Si acepta esperar y cumples, no hay cancelacion
□ 4. Si no acepta, pidele que solicite la cancelacion y reembolsa en menos de 2 dias habiles
□ 5. Baja el stock de ese SKU a 0 YA, antes de seguir
□ 6. Registra el caso: si se repite, el colchon esta corto
```

## El error clásico

Sincronizar en un solo sentido. Descuentas en Mercado Libre cuando vendes por fuera, pero cuando
vendes en Mercado Libre nadie descuenta en el sistema. Funciona un mes y explota en diciembre, que
es cuando más caro sale. **La sincronización de stock o va en los dos sentidos o no existe.**

## Relacionados

`63` ganar el catálogo · `139` cancelaciones y riesgo de cuenta · `183` precio y stock ·
`184` stock multi-bodega · `185` las órdenes · `188` posventa · `189` webhooks ·
`190` topics y payload · `193` límites de uso · `199` arquitectura de referencia
