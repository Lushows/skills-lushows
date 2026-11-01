# Las tres métricas de la reputación

El termómetro mide tres números concretos, y una cuarta métrica que solo aparece cuando aspiras a
MercadoLíder. Los tres tienen umbral oficial publicado. Saber exactamente qué entra y qué no entra
en cada uno es la diferencia entre defenderte y resignarte.

## La tabla que manda

Umbrales oficiales para conservar el **verde** (oficial ML Colombia, verificado sep-2026):

| Variable | A 60 días | A 365 días | MercadoLíder |
|---|---|---|---|
| **Ventas con reclamos** | ≤ **3,5%** | ≤ **3,5%** | ≤ **2,5%** |
| **Envíos incorrectos** | ≤ **12%** | ≤ **15,5%** | ≤ **10%** |
| **Canceladas por ti** | ≤ **2,5%** | ≤ **4%** | ≤ **1,5%** |
| Mediaciones | — | — | ≤ **0,5%** |

Cuál columna te aplica depende de tu volumen: 60 o más ventas concretadas → columna de 60 días;
menos de 60 → columna de 365 días (`127`).

Lo que salta a la vista: **la métrica más estrecha no es la de reclamos, es la de cancelaciones**.
Con 2,5% a 60 días y 200 ventas al mes, tienes margen para 10 cancelaciones en dos meses. Y es la
única que además tiene riesgo de suspensión de cuenta (`139`).

## Reclamos

Qué cuenta y qué no (oficial ML Colombia, verificado sep-2026):

| Cuenta contra ti | No cuenta |
|---|---|
| Producto incompleto o faltante | **Arrepentimiento del comprador** (excepción oficial) |
| Problemas de calidad: defectuoso, defecto de fábrica, deja de funcionar | Reclamos excluibles que pediste excluir a tiempo (`136`) |
| Producto distinto al anunciado | Ventas en la categoría **Inmuebles** |

La excepción del arrepentimiento es enorme y muy poca gente la conoce: **el cliente que se
arrepiente y devuelve no te mancha la reputación.** Eso cambia por completo cómo debes tratar una
devolución por arrepentimiento: no es una amenaza, es un trámite (`138`).

Lo que sí es amenaza es el reclamo por calidad o por faltante. Y esos se ganan antes de que ocurran:

```
□ La descripción dice EXACTAMENTE qué va en la caja, unidad por unidad (`30`)
□ Las fotos muestran el contenido real, sin accesorios que no incluyes (`38`)
□ El empaque aguanta el transporte del producto más frágil que vendes (`110`)
□ Alguien verifica el contenido antes de cerrar la caja
```

La lista completa de reclamos excluibles y el procedimiento para pedir la exclusión están en `136`.
**No leer `136` es regalarle a ML reclamos que no te correspondían.**

## Ventas canceladas por ti

Definición oficial: *el comprador recibe su dinero de vuelta antes de que hayas entregado el
producto*. Y la clave está en el "por ti":

| Situación | ¿Cuenta contra ti? |
|---|---|
| Cancelas por falta de stock | **Sí** |
| Cancelas porque te equivocaste de precio | **Sí** |
| **Cancela el comprador** | **No** (excepción oficial) |
| El comprador recibe y devuelve | No — devolución no es cancelación |
| Reclamo con solicitud de cancelación reembolsado en 2 días hábiles | No (`136`) |

Es la métrica con más consecuencias: además del umbral de verde (2,5% / 4%), superar el 2,5% pone la
cuenta en riesgo de suspensión para vender. Todo el detalle en `139`.

## Envíos incorrectos

Dos causas, ambas tuyas:

| Causa | Qué es |
|---|---|
| Despacho con demora | No entregaste el paquete al transportador dentro del tiempo prometido |
| Depósito incorrecto | Despachaste desde un origen distinto al declarado |

Y una tercera que aplica solo si usas Flex: **la entrega debe completarse antes de las 21:00 horas**
o cuenta como envío incorrecto (oficial ML Colombia, verificado sep-2026). Si haces Flex con un
mensajero propio, esa hora es tu corte real de operación, no las 6 p.m.

Es la métrica con el umbral más holgado (12% a 60 días) y, aun así, la que más se rompe en
temporada alta. Con Full prácticamente desaparece, porque el despacho lo hace ML (`105`).

## Mediaciones

Cuarta métrica, solo para MercadoLíder, con el límite más duro de todos: **0,5%**. Con 120 ventas en
60 días eso es literalmente **cero mediaciones permitidas**.

Una mediación es un reclamo que no resolviste en la primera etapa y ML tuvo que entrar a decidir
(`135`). ML no te penaliza por tener problemas: te penaliza por no resolverlos tú.

## Cómo se ven tus números

| Vía | Qué te muestra |
|---|---|
| Mi cuenta → Reputación | Los porcentajes actuales de cada variable y el periodo evaluado |
| `GET /users/$USER_ID` | `seller_reputation.metrics` con `claims`, `delayed_handling_time`, `cancellations` — cada uno con `rate` y `value` |

Guarda el histórico cada lunes. ML te muestra la foto de hoy; la película la tienes que llevar tú
(`144`, `169`).

## El error clásico

Confundir "tuve un problema con un cliente" con "me bajó la reputación". Un comprador furioso que te
deja una opinión de una estrella **no mueve el termómetro** si no abrió reclamo por calidad o
faltante. Las opiniones son otro sistema (`142`).

Y al revés: un comprador amabilísimo que abre reclamo porque llegó incompleto **sí** te golpea,
aunque lo hayas resuelto en media hora con el mejor trato del mundo. **El termómetro mide
expedientes, no simpatía.**

## Dónde se pelea cada métrica

| Métrica | Se gana en |
|---|---|
| Reclamos | La ficha (`25`-`40`) y el empaque (`110`) |
| Canceladas | El stock (`140`) |
| Envíos incorrectos | El proceso de despacho (`115`), o directamente Full (`105`) |
| Mediaciones | Velocidad de respuesta y tono (`133`, `135`) |

## Relacionados

`125` el termómetro · `127` el periodo de evaluación · `129` MercadoLíder ·
`133` el tiempo de respuesta · `135` el reclamo y la mediación · `136` reglas de exclusión ·
`138` devoluciones · `139` la cancelación y su castigo · `140` el quiebre de stock ·
`144` plan de defensa de la cuenta
