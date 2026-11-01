# La retención como ventaja estructural

> Esta skill se construyó asumiendo compra única: producto ganador, anuncio, venta, siguiente. Ese
> modelo funciona y es el que se enseña de `218` a `239`. Pero deja fuera la palanca más grande que
> existe en ecommerce: **el CAC se paga una sola vez y el margen puede volver cada mes.** Este
> bloque (`300`-`309`) es el parche de ese hueco. No contradice a `230` — lo completa.

## La regla que no cambia

`230` dice que el primer pedido debe ser rentable solo. **Eso sigue siendo verdad.** La retención no
rescata una economía rota: multiplica una economía sana. Si tu primera venta pierde dinero y tu plan
es "lo recupero en la segunda", no tienes negocio, tienes una apuesta sobre un comportamiento que
todavía no observaste.

Lo que este bloque agrega: cuando la primera venta ya es rentable, la segunda vale **exactamente lo
mismo en margen pero cuesta cero en adquisición**. Ahí está la diferencia entre una tienda que vive
del CPM de Meta y un negocio.

## La aritmética, con los números verificados del proyecto México

| Concepto | USD | Origen |
|---|---|---|
| Ticket | 54,59 | bundle 999 MXN |
| Margen por venta **sin** adquisición | 26,47 | producto + envío + pasarela descontados |
| CAC Meta | 10,54 | medido, no estimado |
| **Margen de la primera venta** | **15,93** | 26,47 − 10,54 |
| Margen de la segunda venta en adelante | 26,47 | el CAC ya se pagó |

Esa última fila es todo el módulo. La segunda venta deja **66% más margen** que la primera
(26,47 vs 15,93) sin gastar un peso en pauta.

## La tabla de escenarios acumulados

| Compras del cliente | Margen acumulado (USD) | Múltiplo vs 1 compra |
|---|---|---|
| 1 | 15,93 | 1,00x |
| 2 | 42,39 | **2,66x** |
| 3 | 68,86 | **4,32x** |
| 6 | 148,26 | **9,31x** |
| 12 | 307,07 | **19,28x** |

Lee la columna del múltiplo despacio. Pasar de 1 a 2 compras **no** sube el negocio 100%: lo sube
166%, porque la compra que agregas no carga CAC. Es el efecto más subestimado del ecommerce chico.

## Por qué un consumible vale 2,66-9,31x un aparato

| | Aparato / novedad | Consumible (suplemento, cosmético) |
|---|---|---|
| Se acaba | no | sí, en 30-90 días |
| Motivo natural para volver | ninguno | se le acabó |
| Recompra a 90 días (verificar con tus datos) | 2-8% | 15-30% |
| Recompra ecommerce general 2026 | **28,2%** promedio del mercado | |
| Salud y suplementos | | **29%** |
| Suplementos USD 1M-50M a 12 meses | | **38-52%**, top quartile **64%** |
| Múltiplo de margen realista | 1,0-1,2x | 2,5-4,5x |

Un aparato de cocina viral y un kit capilar anticaída pueden tener el mismo ticket y el mismo CAC. A
los 12 meses uno dejó USD 15,93 y el otro USD 68,86. **Es el mismo dinero de pauta.** Por eso la
elección de nicho de `120`-`139` es, en realidad, una decisión de retención disfrazada de decisión
de producto.

## El techo de CAC se mueve

`11` define el techo de CAC como el margen que puedes entregar a la plataforma. Con compra única ese
techo es 26,47. Con retención:

| Supuesto de recompra | Compras promedio por cliente | Techo de CAC (USD) |
|---|---|---|
| 0% (compra única) | 1,00 | 26,47 |
| 20% compra una vez más | 1,20 | ~31,76 |
| **40% llega a 3 compras** | 1,80 | **47,64** |
| 29% del benchmark de suplementos, sostenido | ~1,5-1,8 | 39,71-47,64 |

Con 40% a tres compras puedes pagar **1,8 veces más por cliente** que tu competidor de compra única.
Eso no es una ventaja de marketing: es una ventaja estructural. Puedes ganarle todas las subastas y
seguir siendo rentable. Ver `11` y `224`.

## Las tres condiciones para usar esto

| Condición | Por qué |
|---|---|
| Producto que se consume o se repone | sin motivo natural de vuelta, la retención se fuerza con descuento y muere el margen |
| ≥90 días de datos propios de cohortes | el benchmark orienta, tus datos deciden (`302`) |
| Canal propio funcionando | sin email/WhatsApp propio, no puedes contactar a nadie (`272`, `286`) |

Si te falta alguna, **planea con recompra cero** y trata cada segunda venta como bono. Igual que en
`230`. La diferencia es que ahora sabes cuánto vale construir esa condición.

## El error de secuencia más caro

| Orden equivocado | Orden correcto |
|---|---|
| Elegir producto → escalar → "y si les vendo otra vez" | Elegir producto **por** su recompra → validar → escalar con el techo alto |
| Montar suscripción antes de tener 100 clientes | Vender 100 veces, medir cohorte, después suscripción (`303`) |
| Comprar recompra con 25% off eterno | Ganarla con producto que funciona y calendario de reposición (`308`) |

## Aplicación al proyecto México (diciembre 2026)

Los dos finalistas —kit capilar anticaída y gomitas de vitalidad— son **consumibles**. Eso ya fue una
decisión de retención aunque se tomó por otra razón.

| Decisión | Qué hacer |
|---|---|
| Tamaño de envase | el que genere recompra a 30-60 días, no el más grande |
| Mensaje del anuncio | resultado en tratamiento continuo, **sin claim terapéutico** (COFEPRIS) |
| Captura de dato | correo + WhatsApp en el checkout, obligatorio, desde la primera venta |
| Primer objetivo medible | segunda compra ≥20% a 90 días antes de escalar presupuesto |

Con capital menor a USD 500 y ~5 tests, la retención no se prueba en la fase de test: se **prepara**
en la fase de test (capturando datos) y se cobra en enero-marzo de 2027.

## Lo que este bloque cubre

| Módulo | Tema |
|---|---|
| `301` | Benchmarks de recompra y churn: normal / bueno / excelente |
| `302` | Análisis de cohortes: la tabla que dispara decisiones |
| `303` | Montar una suscripción sin matar la conversión |
| `304` | Churn involuntario y dunning — el dinero más barato que vas a recuperar |
| `305` | Provocar la segunda compra |
| `306` | Reactivar dormidos |
| `307` | Puntos y referidos: cuándo es real y cuándo es descuento disfrazado |
| `308` | Calendario de reposición |
| `309` | LTV real por cohorte (código) |

## Relacionados
`11` · `120` · `224` · `230` · `234` · `272` · `285` · `286` · `301` · `302` · `305` · `309`
