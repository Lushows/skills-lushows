# Entrega fallida

El paquete llegó al destino y no se pudo entregar: nadie estaba, la dirección estaba mal, o el
comprador lo rechazó. Cada una tiene una consecuencia distinta para tu reputación y para tu
bolsillo, y la peor salida es la que la mayoría toma: cancelar.

## Los tres casos

| Caso | Culpa | ¿Cuenta contra tu reputación? | Costo típico |
|---|---|---|---|
| **No estaba nadie** | Del comprador | No, si tú despachaste a tiempo | Reintento o devolución |
| **Dirección mala o incompleta** | Del comprador | No: error del comprador, excluible | Reintento |
| **Rechazo en la puerta** | Del comprador | Depende del motivo | Devolución completa |

En los tres, la clave oficial es la misma: **el "error del comprador" está en la lista de reclamos
excluibles**, igual que el "arrepentimiento con producto en perfecto estado" (oficial ML Colombia,
verificado sep-2026). Lo que te puede hundir no es la entrega fallida: es cómo la manejas.

## La regla de oro: no canceles tú

| Acción | Variable del termómetro | Techo para seguir verde |
|---|---|---|
| Cancelas tú la venta | **Canceladas por ti** | 2,5% a 60 d · 4% a 365 d · 1,5% ML |
| El comprador cancela | No cuenta contra ti | — |
| Despachaste tarde | Envíos incorrectos | 12% a 60 días · 15,5% a 365 días · 10% ML |

(Oficial ML Colombia, verificado sep-2026.)

El techo de canceladas es el más estrecho de los tres. Con 50 ventas en el periodo, **una sola
cancelación tuya ya es 2%**: estás al borde. Y hay un umbral aparte, también oficial: **más del
2,5% de ventas canceladas puede llevar a la suspensión de la cuenta para vender.**

**Nunca cierres una entrega fallida cancelando tú. Deja que el comprador la pida.**

## Qué hacer, paso por paso

```
□ 1. Mira el estado real del envío: GET /shipments/$SHIPMENT_ID
□ 2. Escribe al comprador el MISMO día, antes de que él escriba
□ 3. Pregunta si quiere reintento, cambio de dirección, o punto de retiro
□ 4. Responde cualquier mensaje suyo en menos de 24 HORAS HÁBILES (oficial)
□ 5. Si quiere cancelar, que lo pida él: tienes 2 días hábiles para reembolsar sin afectación
□ 6. Si vuelve el paquete, revísalo antes de reingresarlo a stock
□ 7. Registra el caso con ciudad y motivo: alimenta tu mapa de `115`
```

El paso 5 es oficial y salva reputaciones: **los reclamos con solicitud de cancelación no afectan
la reputación desde el inicio**; tienes 2 días hábiles para reembolsar sin haber entregado y
quedas intacto. Si no cumples, el reembolso es automático y **sí** te afecta.

## El costo en plata

```
COSTO DE UNA ENTREGA FALLIDA =
    envío de ida (ya pagado, tabla oficial de `100`)
  + envío de retorno o reintento
  + tu tiempo de gestión
  + riesgo de que el producto vuelva dañado
  + costo de oportunidad: el producto estuvo fuera de stock varios días
```

En producto pesado esto se dispara: un paquete de 10-20 kg de más de $60.000 ya costó **$25.200**
de ida (oficial). Si hay retorno y reintento, el flete puede superar el margen del producto
entero. Por eso en producto grande vale la pena confirmar la dirección antes de despachar (`116`).

## Cómo bajar la tasa

| Medida | Efecto |
|---|---|
| Mensaje automático de "tu pedido va en camino, confirma que puedas recibir" | Alto |
| Revisar direcciones raras antes de despachar (sin número, sin barrio) | Alto |
| Despachar temprano en la semana, no el viernes | Medio: menos paquetes en fin de semana |
| Ofrecer punto de retiro cuando existe en su ciudad | Medio |
| No prometer horarios que no controlas | Medio: evita el "no estaba" |

Un detalle: cuidado con qué mandas en esos mensajes. Están prohibidos los datos de contacto
—teléfono, WhatsApp, redes, correo— en la publicación y en los canales de mensajería, con
excepciones solo en Autos/Motos, Inmuebles, Servicios y MercadoProveedores. Ver `132`.

## Flex: el caso especial

En Flex la entrega fallida es tuya de principio a fin. No hay transportadora que reintente:
vuelves tú, o no vuelve nadie. Y la entrega debe completarse **antes de las 21 hs** (oficial), así
que un fallido a las 19:30 te deja sin ventana.

```
□ Avisa al comprador cuando salgas, con rango de hora
□ Si no contesta, intenta antes de llegar, no en la puerta
□ Si no está, reprograma para el día siguiente: no marques "entregado"
□ Una entrega fallida en Flex sí puede volverse envío incorrecto si no la resuelves
```

Marcar "entregado" sin entregar, para salvar la métrica, es riesgo de sanción de cuenta. No lo
hagas nunca. Ver `143`.

## Cuándo la culpa sí es tuya

| Situación | Lectura |
|---|---|
| Dirección mal transcrita por ti al generar la guía | Tuya |
| Etiqueta ilegible y el repartidor no pudo leer el destino | Tuya (`114`) |
| Etiqueta vieja sin quitar en caja reutilizada | Tuya |
| Despachaste tarde y llegó cuando el comprador ya viajó | Tuya |

En esos casos no pidas exclusión: arregla el proceso. La exclusión se pide con evidencia, y
pedirla sin tenerla te desgasta el canal para cuando sí la necesites.

## El error clásico

Cancelar la venta para "cerrar el tema" cuando el comprador no responde. Es cambiar un problema
sin consecuencia —una entrega fallida por error del comprador, que es excluible— por el peor
indicador del termómetro: canceladas por ti, con techo de 2,5% y riesgo de suspensión de cuenta
por encima de ese número.

**La entrega fallida no te hace daño. Cancelarla sí.**

## Relacionados

`113` la demora y su costo · `114` el flujo diario · `115` zonas difíciles · `116` productos
grandes · `118` el paquete perdido · `102` Flex · `124` auditoría mensual · `126` las tres
métricas · `136` reclamos excluibles · `138` devoluciones · `132` lo que no puedes decir · `143`
suspensión de cuenta · `100` tarifas oficiales de envío
