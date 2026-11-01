# La cancelación y su castigo

De las tres variables del termómetro, esta es la única que puede cerrarte la cuenta. Tiene el umbral
más estrecho y la definición más mal entendida del marketplace: mucha gente cree que devolver es
cancelar, y no lo es.

## La definición oficial

> **Venta cancelada: el comprador recibe su dinero de vuelta antes de que hayas entregado el
> producto.** (oficial ML Colombia, verificado sep-2026)

Dos elementos: hay reembolso, y **no hubo entrega**. Si el producto se entregó y después volvió, eso
es una devolución, no una cancelación (`138`).

## Quién la pide define todo

Excepción oficial: **las ventas canceladas por la persona que te compró no cuentan contra ti**
(oficial ML Colombia, verificado sep-2026).

| Quién cancela | ¿Cuenta en tu métrica? |
|---|---|
| **Tú** | **Sí** |
| El comprador | **No** |
| El comprador pide y tú reembolsas en 2 días hábiles | **No** (`136`) |
| El comprador pide y tú te demoras más de 2 días hábiles | **Sí** — el reembolso se hace automático y te afecta |

Esa última fila es donde se pierde plata por pura lentitud. El caso llegó limpio y lo ensuciaste
esperando.

## Los umbrales

Oficial ML Colombia, verificado sep-2026:

| Medición | Límite para ser verde |
|---|---|
| A 60 días (con 60+ ventas) | no cancelar más del **2,5%** |
| A 365 días (con menos de 60 ventas) | no cancelar más del **4%** |
| MercadoLíder | no más del **1,5%** |

Y el riesgo mayor: **superar el 2,5% de ventas canceladas pone la cuenta en riesgo de suspensión
para vender** (ALTA). Es el único umbral del bloque de reputación que no solo te baja de color, sino
que te puede sacar del juego (`143`).

En unidades reales:

| Ventas en 60 días | Cancelaciones tuyas permitidas (2,5%) | Para MercadoLíder (1,5%) |
|---|---|---|
| 40 | 1 | 0 |
| 120 | 3 | 1 |
| 300 | 7 | 4 |
| 600 | 15 | 9 |

**Con 40 ventas en dos meses, dos cancelaciones tuyas te pasan del límite.** No hay margen para
"esta semana me quedé sin stock".

## Por qué ML es tan duro con esto

Porque es la única falla que rompe la promesa base del marketplace. Un producto que llega roto es un
problema; un producto que **nunca existió** es una estafa desde la perspectiva del comprador. Si ML
permite que los vendedores publiquen stock que no tienen, el sitio deja de funcionar.

**Cancelar es decirle al comprador que le vendiste algo que no tenías. ML lo trata como lo que es.**

## Las causas, en orden de frecuencia

| Causa | Prevención |
|---|---|
| **Quiebre de stock** | La número uno con enorme diferencia. Módulo completo en `140` |
| Sobreventa multicanal | Colchón de seguridad y sincronización (`123`, `196`) |
| Error de precio publicado | Revisión antes de publicar; nunca cancelar por precio (abajo) |
| Producto descontinuado por el proveedor | Pausar apenas te enteras, no esperar el pedido |
| No poder despachar a esa zona | Configurar bien la cobertura antes, no cancelar después |

## Nunca canceles por error de precio

Tentación clásica: publicaste con un cero de menos, entra una venta, y cancelas. Mala idea por tres
razones:

```
□ La cancelación cuenta contra el 2,5% igual que cualquier otra
□ El comprador queda furioso y te deja opinión negativa (`142`)
□ Puede abrir reclamo, y el reclamo por "no despachaste" NO es excluible (`136`)
```

Lo correcto es doloroso y barato: **cumple esa venta a pérdida, corrige el precio y sigue**. Una
venta perdida cuesta lo que cuesta; una cancelación cuesta 60 o 365 días de métrica más el riesgo de
cuenta.

## Lo que NO es cancelación

| Situación | Qué es |
|---|---|
| El comprador recibe y devuelve | **Devolución** (`138`) |
| El comprador se arrepiente después de recibir | Devolución, y además excluible (`136`) |
| Pago rechazado o no completado | No es venta concretada |
| Reclamo por producto defectuoso | Reclamo, no cancelación (`135`) |
| El comprador cancela antes de que despaches | Cancelación, pero **no cuenta contra ti** |

Esta distinción importa porque cambia dónde intervienes. Si tus reembolsos vienen de devoluciones,
el problema está en la ficha (`30`). Si vienen de cancelaciones tuyas, el problema está en el stock.

## Flex: la trampa de las 21:00

Si usas Flex y no completas la entrega **antes de las 21 hs**, cuenta como envío incorrecto (oficial
ML Colombia, verificado sep-2026). No es cancelación, pero golpea la otra métrica del termómetro
(`126`). El vendedor apurado que cancela un Flex que no alcanza a entregar está cambiando un golpe
del 12% por uno del 2,5%: **mala jugada, entrega tarde antes que cancelar.**

## El protocolo de emergencia

Si ya te pasó y necesitas no cancelar:

```
□ ¿Puedes comprarlo hoy en otra parte, aunque pierdas margen?   → hazlo
□ ¿Puedes despacharlo tarde avisando al comprador?              → mejor tarde que cancelado
□ ¿El comprador acepta un equivalente superior sin cobro extra? → ofréceselo por mensaje
□ ¿El comprador prefiere cancelar él mismo?                     → pídeselo con honestidad:
   su cancelación NO cuenta contra ti (excepción oficial)
□ Solo si todo falla: cancela y pausa YA el SKU para que no vuelva a pasar
```

El cuarto punto es legítimo y poco conocido: explicarle la situación al comprador y que él decida
cancelar es honesto y te salva la métrica. Lo que no puedes es presionarlo ni engañarlo.

## Monitoreo

| Vía | Qué mirar |
|---|---|
| Mi cuenta → Reputación | Tu porcentaje de canceladas contra el 2,5% / 4% |
| `GET /users/$USER_ID` | `seller_reputation.metrics.cancellations` (`rate` y `value`) |
| Webhook `orders_v2` | Detecta cancelaciones en tiempo real (`186`) |

Pon una alarma en el 1,5%, no en el 2,5%. Para cuando llegas al umbral ya es tarde (`144`).

## El error clásico

Publicar todo el inventario disponible para "no perder ventas". El vendedor que publica 10 unidades
teniendo 10 físicas, y vende también en otro canal, va a cancelar. **Publicar de menos cuesta una
venta; publicar de más cuesta la cuenta.** El colchón de seguridad está en `140`.

## Relacionados

`126` las tres métricas · `127` el periodo de evaluación · `136` reglas de exclusión ·
`138` devoluciones · `140` el quiebre de stock · `143` suspensión de cuenta ·
`144` plan de defensa de la cuenta · `123` stock multicanal · `196` sincronización por API
