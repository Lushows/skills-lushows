# Precio por cantidad y B2B

Vender más barato por unidad a quien lleva más. En Mercado Libre existe la funcionalidad, pero
**está limitada a cuentas seleccionadas con perfil B2B**: no está abierta a todo vendedor. Este
módulo dice qué es, cuándo pedirla, y qué hacer mientras tanto — que casi siempre es armar un kit.

## El estado de la funcionalidad

| Dato | Valor |
|---|---|
| ¿Existe el descuento por volumen en ML? | **Sí** |
| ¿Está abierto a todos? | **No.** Limitado a cuentas seleccionadas con perfil B2B |
| ¿Cómo se consigue? | Se solicita / se habilita desde la cuenta; no es un interruptor público |

Confianza MEDIA. Si tu panel no lo muestra, no es que lo estés buscando mal: es que tu cuenta no lo
tiene habilitado.

## Por qué el descuento por volumen es distinto de un kit

Se parecen, pero el efecto sobre tus costos no es el mismo, y en Colombia la diferencia es grande:

| | Precio por cantidad | Kit (un solo ítem) |
|---|---|---|
| Qué compra el cliente | N unidades del mismo ítem | Un producto que contiene N |
| **Envío** | **Se calcula POR UNIDAD** (oficial ML Colombia, verificado sep-2026) | Un solo envío |
| Ticket del pedido | Alto | Alto |
| Efecto en el umbral de $60.000 | Lo cruza | Lo cruza |
| Comparabilidad con la competencia | Directa | Rota: nadie tiene tu combinación |

La fila del envío decide. *"El costo se calcula **por unidad**"* es texto oficial: si el comprador
lleva 4 unidades sueltas, tú pagas 4 envíos. Si lleva un kit de 4, pagas uno.

**El descuento por volumen sube tu facturación; el kit sube tu margen. No son lo mismo.**

Con envío de 1 kg sobre $60.000 en $8.200 (tabla oficial, verde), vender 4 unidades sueltas cuesta
**$32.800** de envío contra **$8.500** del kit de 4 kg. Son $24.300 de diferencia en el mismo
pedido. Por eso, mientras no tengas el perfil B2B habilitado —y muchas veces incluso teniéndolo—
la respuesta correcta es el kit (`87`).

## Cuándo sí pedir el perfil B2B

| Señal | Por qué |
|---|---|
| Te preguntan seguido "¿hacen precio por mayor?" | Hay demanda real que estás rechazando |
| Vendes insumos, repuestos o consumibles | Categorías donde el comprador profesional compra en volumen |
| Tu comprador típico es un negocio, no una persona | Restaurantes, talleres, salones, tiendas |
| Tienes capacidad de despacho para pedidos grandes | Sin esto, el volumen se convierte en cancelaciones |
| Tu costo baja de verdad al vender más unidades | Si no baja, el descuento sale enteramente de tu margen |

Esa última es la condición dura. Si tu costo unitario es el mismo vendiendo 1 o 100, un descuento
por volumen es solo un margen más chico con más trabajo.

```
□ Verifiqué en el panel si mi cuenta tiene la funcionalidad habilitada
□ Si no, pregunté por el canal de soporte de vendedores cómo se solicita
□ Tengo claro cuánto baja MI costo por comprar/producir más
□ Tengo capacidad logística para pedidos de 20+ unidades
□ Calculé el margen a cada escalón, no solo al primero
```

## Cómo diseñar los escalones

Regla: **el descuento de cada escalón nunca sale del margen, sale del ahorro real**. Tres fuentes
legítimas de ahorro:

| Fuente del ahorro | Cuánto suele ser |
|---|---|
| Menor costo unitario por compra en volumen | Lo negocias con tu proveedor |
| Menor alistamiento por unidad | Empacar 10 juntos cuesta menos que 10 veces empacar 1 |
| Menor costo de adquisición | Un pedido grande es una sola conversión, no diez |

Suma esos tres y ese es tu presupuesto de descuento. Un escalón típico honesto:

| Cantidad | Descuento sobre precio unitario | De dónde sale |
|---|---|---|
| 1-2 | 0% | — |
| 3-5 | 5% | Alistamiento + adquisición |
| 6-11 | 8% | Lo anterior + primer escalón de compra |
| 12+ | 12% | Lo anterior + costo unitario negociado |

Números ilustrativos: arma los tuyos con tus ahorros reales, no con esta tabla.

## Verifica cada escalón con el script

```
# Precio unitario normal
python scripts/margen_ml.py margen --precio 74900 --costo 38000 --comision 15 \
    --envio 8200 --otros 900 --iva 19

# Escalón de 12+: 12% menos por unidad, mismo envío POR UNIDAD
python scripts/margen_ml.py margen --precio 65900 --costo 35000 --comision 15 \
    --envio 8200 --otros 700 --iva 19
```

Cargo **15% — ejemplo dentro del rango oficial 8%-22%, verifica el tuyo** (`76`). Fíjate en que en
el segundo comando bajaron también `--costo` y `--otros`: **si esos no bajan, el escalón no se
justifica**. Un descuento por volumen sin ahorro detrás es solo margen regalado.

## El comprador B2B tiene otras exigencias

Si abres esta puerta, prepárate para lo que trae:

| Exigencia | Dónde se resuelve |
|---|---|
| Factura electrónica a nombre de la empresa | `contador_lushows`; Alegra integra con ML en Colombia |
| Plazos de pago | En ML no existen: se paga al comprar |
| Cantidades grandes con stock garantizado | Tu operación, y ojo con el quiebre (`91`) |
| Precios estables en el tiempo | Un repricer suelto arruina una relación B2B (`90`) |

## La alternativa mientras tanto

Si no tienes el perfil habilitado, tienes tres caminos abiertos hoy:

1. **Kit por cantidad** — "Pack x12" como un solo ítem. Un envío, un ticket alto (`87`).
2. **Variantes por presentación** — x1, x4, x12 como variaciones de la misma publicación (`48`).
3. **MercadoProveedores** — la categoría donde, a diferencia del resto del sitio, sí está permitido
   incluir datos de contacto (junto con Autos/Motos, Inmuebles y Servicios).

La primera es la mejor y suele dar mejor margen que el descuento por volumen, por la aritmética del
envío por unidad.

## El error clásico

Ofrecer precio por mayor respondiendo preguntas en la publicación, con un precio acordado por
mensaje. Además de que **está prohibido intercambiar datos de contacto** fuera de las categorías
exceptuadas, el pedido se termina cerrando fuera de la plataforma: pierdes la protección, el
historial de venta y el aporte a tu reputación y a MercadoLíder.

## Relacionados

`87` subir el ticket con kits · `88` precio psicológico · `91` descuentos y campañas · `93` cupones
propios · `78` el envío que pagas tú · `79` el umbral de los $60.000 · `82` la calculadora de
margen · `90` el repricer · `48` variaciones · `contador_lushows` para facturación B2B
