# Programa de puntos y referidos

> La pregunta correcta no es "¿monto un programa de puntos?". Es: **"¿esto hace que alguien compre
> algo que no iba a comprar, o solo le estoy regalando margen a quien ya iba a comprar?"** La mayoría
> de los programas de puntos de tiendas chicas son un descuento del 5% con interfaz bonita.

## La prueba de fuego

| Pregunta | Si la respuesta es no |
|---|---|
| ¿Cambia el comportamiento de alguien? | es descuento disfrazado |
| ¿Se lo gana solo el que vuelve, no el que ya compró? | es descuento disfrazado |
| ¿El costo sale del margen incremental, no del margen base? | te va a comer la utilidad |
| ¿Tienes ≥3 SKU o ≥6 meses de operación? | todavía no; monta `305` primero |
| ¿Puedes calcular cuánto te cuesta un punto? | no lo lances |

Un programa de puntos sobre un catálogo de un solo producto que se compra cada 60 días es
matemáticamente idéntico a un descuento en la segunda compra. Si es lo mismo, **usa el descuento:
es más simple, más entendible y no te cobra una app mensual.**

## Puntos: cuándo sí

| Condición | Por qué |
|---|---|
| Catálogo de ≥5 SKU coherentes | el punto sirve para descubrir otro producto |
| Frecuencia de compra alta (mensual o menor) | el saldo de puntos se acumula rápido y se siente real |
| Margen sano (≥45% de contribución) | el programa cuesta 3-6% del ingreso |
| Base de ≥500 clientes | por debajo, el costo de la app supera el retorno |
| Competencia con marca fuerte | el programa es un motivo para no irse |

Con la economía verificada del proyecto (margen 26,47 sobre ticket 54,59 = 48,5%), un programa que
cueste 5% del ticket (2,73 USD) deja el margen en ~23,74. **Cabe, pero solo si genera compras que no
habrían ocurrido.** Si el 80% de los puntos los redime gente que igual iba a comprar, estás perdiendo
plata con una hoja de Excel de por medio. Verifica el cálculo con `Matematicas_lushows`.

## Diseño mínimo de un programa de puntos que no se desangra

| Parámetro | Valor razonable | Nota |
|---|---|---|
| Acumulación | 1 punto por cada 1 unidad monetaria gastada | simple de entender |
| Valor de redención | 100 puntos = 5% del ticket | costo efectivo 3-5% |
| Expiración | **12 meses sin actividad** | evita pasivo eterno; declararlo claro |
| Redención mínima | equivalente a ~10% del ticket | fuerza a volver, no a descontar la primera |
| Bonos que sí sirven | reseña con foto, referido que compra, segunda compra | premian comportamiento, no gasto |
| Bonos que no | seguir en redes, cumpleaños genérico | ruido |
| Lo que NUNCA se premia con puntos | la primera compra | eso es un descuento de adquisición, cárgalo al CAC |

**Pasivo contable:** los puntos emitidos y no redimidos son una deuda. En una operación chica es
ignorable, pero cuando crece hay que registrarlo. Rutea a `contador_lushows`.

## Referidos: el mecanismo que sí se paga solo

Un referido es distinto en naturaleza: **no descuentas margen, compras un cliente nuevo a un precio
que tú fijas.** Compáralo contra el CAC, no contra el descuento.

| Concepto | Valor del proyecto (USD) |
|---|---|
| CAC Meta | 10,54 |
| Margen por venta sin adquisición | 26,47 |
| Techo teórico de recompensa total (referidor + referido) | 26,47 |
| **Recompensa recomendada, combinada** | **6-10** (por debajo del CAC de Meta) |
| Reparto típico | mitad y mitad, o 60% al referido |

| Estructura | Ejemplo con el ticket de 999 MXN | Costo real |
|---|---|---|
| Doble cara | $100 MXN de descuento para el referido + $100 de crédito para quien refiere | ~USD 11 combinado si ambos se usan; el crédito solo cuesta cuando se redime |
| Solo al referido | $150 MXN al que llega nuevo | más barato y más limpio, menos viral |
| Producto gratis al referidor cada 3 referidos | costo = costo de producto, no precio de venta | el más rentable si tienes stock local |

**Dato incómodo:** la mayoría de los programas de referidos en ecommerce chico generan menos del 5%
de los pedidos. No es un canal de crecimiento; es un extra que mejora el LTV de los clientes que ya
te quieren. Si tu plan de escalado depende de referidos, no tienes plan.

## Cuándo un programa es disfraz de descuento (banderas rojas)

| Bandera | Diagnóstico |
|---|---|
| El 90% de los puntos se redimen en la compra siguiente inmediata | es un descuento diferido |
| El ticket promedio no cambió tras lanzarlo | no cambió comportamiento |
| La cohorte con programa retiene igual que la anterior (`302`) | no funciona; apágalo |
| Tienes que "recordarles que tienen puntos" cada mes | no les importa |
| El costo de la app supera el margen incremental medible | pérdida neta |

**Cómo probarlo bien:** no lo lances a todos. Actívalo para los clientes de un mes y compara esa
cohorte contra la anterior a 90 días en dos métricas: tasa de segunda compra y margen acumulado por
cliente. Si la diferencia no supera ~3 puntos de recompra, no vale la molestia. Con cohortes de
menos de 100 clientes el resultado será ruido: mira `302` antes de creerte el número.

## Alternativas que casi siempre rinden más

| Alternativa | Por qué gana |
|---|---|
| **Pack multi-mes** (`303`) | sube ticket hoy en vez de descontar mañana |
| Calendario de reposición (`308`) | cero costo, ataca el momento exacto |
| Dunning (`304`) | recupera plata que ya era tuya |
| Un producto complementario real | sube LTV sin regalar margen |
| Mejorar el día 7 posventa (`285`) | un cliente que usa bien el producto vuelve solo |

Orden de implementación honesto para una tienda nueva: `304` → `305` → `308` → `303` → **y solo
después** `307`. Los puntos son lo último que deberías montar, no lo primero.

## Aplicación al proyecto México

| Elemento | Decisión para 2026 |
|---|---|
| Programa de puntos | **no**, un solo producto y sin base de clientes |
| Referidos | **sí, versión simple**: código con descuento para el nuevo y crédito para el referidor, tope combinado ~USD 8 |
| Cuándo activarlo | después de las primeras 100 ventas, no antes |
| Restricción | recompensa nunca redimible contra la primera compra propia |
| Legal/fiscal | tratamiento de descuentos y créditos → `contador_lushows`; **cero claims de salud** en el copy del programa |

## Relacionados
`230` · `285` · `286` · `300` · `302` · `303` · `304` · `305` · `306` · `308` · `309`
