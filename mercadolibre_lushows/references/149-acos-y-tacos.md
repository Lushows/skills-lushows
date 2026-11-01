# ACOS y TACOS

Las dos métricas con las que se gobierna Mercado Ads. El ACOS te dice si la campaña se paga sola;
el TACOS te dice si el negocio completo mejoró. Mirar una sola de las dos es la causa más común
de decisiones equivocadas con la pauta.

## ACOS: la definición oficial

**ACOS = inversión en publicidad ÷ ingresos generados por la publicidad × 100**

El ejemplo es de Mercado Libre (oficial ML Colombia, verificado sep-2026):

> Invierto **$100** en publicidad y genero **$1.000** en ventas atribuidas a esa publicidad.
> ACOS = 100 ÷ 1.000 × 100 = **10%**.

Léelo así: **de cada $100 que vendiste por publicidad, $10 se los llevó la publicidad.** Es un
costo, y como todo costo, cuanto más bajo mejor — siempre que no te deje sin volumen.

| ACOS | Significa |
|---|---|
| 10% | Gastas $1 por cada $10 vendidos |
| 25% | Gastas $1 por cada $4 vendidos |
| 50% | La mitad de lo que vendes se va en publicidad |
| 100% | Estás regalando el producto y además pagando por regalarlo |

## ROAS: la misma cosa al revés

Si vienes de Meta, estás acostumbrado al ROAS. Es el inverso del ACOS:

| ACOS | ROAS equivalente |
|---|---|
| 5% | 20× |
| 10% | 10× |
| 15% | 6,7× |
| 20% | 5× |
| 30% | 3,3× |
| 50% | 2× |

`ROAS = 100 ÷ ACOS`. No son métricas distintas, es la misma división leída al derecho o al revés.
En Mercado Ads se habla de ACOS porque las tres estrategias oficiales están definidas en ACOS
(`148`).

## TACOS: el ACOS del negocio completo

**TACOS = inversión en publicidad ÷ ingresos TOTALES × 100**

La diferencia es el denominador: el TACOS mete en la cuenta **también las ventas orgánicas**, las
que habrías hecho sin pautar. Como el denominador siempre es mayor, **el TACOS siempre es menor
que el ACOS**. Si alguna vez ves lo contrario, hay un error de cálculo.

| | ACOS | TACOS |
|---|---|---|
| Denominador | Solo ventas atribuidas a la pauta | Todas tus ventas del periodo |
| Qué responde | ¿La campaña se paga sola? | ¿Cuánto pesa la publicidad en mi negocio? |
| Se usa para | Decidir presupuesto y estrategia | Decidir si la pauta es una muleta o un motor |
| Se compara contra | El margen neto del SKU (`150`) | Tu propio TACOS del mes anterior |

## Por qué hay que mirar los dos

Un ejemplo de un mes cualquiera:

| | Mes 1 | Mes 2 |
|---|---|---|
| Inversión en pauta | $500.000 | $500.000 |
| Ventas atribuidas a la pauta | $3.000.000 | $2.500.000 |
| Ventas orgánicas | $2.000.000 | $4.500.000 |
| Ventas totales | $5.000.000 | $7.000.000 |
| **ACOS** | 16,7% | **20,0%** (empeoró) |
| **TACOS** | 10,0% | **7,1%** (mejoró) |

Mirando solo el ACOS, apagarías la campaña en el mes 2. Mirando el TACOS ves lo que de verdad
pasó: la pauta empujó el orgánico (`153`) y el negocio completo se volvió más eficiente. Facturas
$2.000.000 más con el mismo gasto publicitario.

**El ACOS juzga la campaña; el TACOS juzga el negocio. Solo el segundo paga el arriendo.**

## Cómo leer la pareja

| ACOS | TACOS | Lectura | Qué hacer |
|---|---|---|---|
| Bajo | Bajo | Campaña sana y negocio sano | Sube presupuesto |
| Bajo | Alto | Casi todo lo que vendes es pautado: el orgánico no existe | Arregla ficha y reputación (`164`) |
| Alto | Bajo | La pauta es cara pero pesa poco en el total | Optimiza o apaga; no es urgente |
| Alto | Alto | Dependes de la pauta y además es cara | Apaga y revisa el producto entero |
| Sube | Baja | El orgánico está creciendo gracias a la pauta | Buena señal: sostén el gasto |
| Baja | Sube | Estás recortando pauta y perdiendo orgánico con ella | No recortes más de golpe |

## Trampas de estas dos métricas

| Trampa | Por qué importa |
|---|---|
| El ACOS incluye **ventas indirectas** (otro producto tuyo, ver `151`) | La campaña de un SKU puede inflarse con ventas de otro |
| Una publicación aparece pagada **y** orgánica a la vez (`146`) | Parte de lo "atribuido" habría pasado igual |
| Los reportes tardan hasta **72 horas** en cerrar (`151`) | El ACOS de ayer siempre se ve peor de lo que fue |
| El ACOS no resta comisión, IVA ni envío | **Un ACOS de 10% no significa que ganaste 90%** |
| Comparar tu ACOS con el de otro vendedor | Sin su margen, el número no dice nada (`150`) |

La cuarta es la más peligrosa y merece su propio módulo: ver `150`.

## Checklist de lectura mensual

```
□ Calculé el ACOS del mes: inversión ÷ ventas atribuidas × 100
□ Calculé el TACOS del mes: inversión ÷ ventas totales × 100
□ Verifiqué que el TACOS es menor que el ACOS (si no, revisé la cuenta)
□ Comparé ambos contra el mes anterior, no contra un benchmark de internet
□ Comparé el ACOS contra el margen neto del SKU, no contra una cifra "buena" (`150`)
□ Los datos tienen más de 72 horas de antigüedad (`151`)
□ Si las cifras deciden plata, las verifiqué con `Matematicas_lushows`
```

## Relacionados

`145` qué es Mercado Ads · `146` Product Ads · `148` las tres estrategias y su ACOS ·
`150` el ACOS sano según tu margen · `151` la ventana de atribución ·
`153` el efecto sobre lo orgánico · `154` el error de pautar sin margen ·
`155` leer los reportes · `156` optimizar semana a semana · `164` cuándo no es la respuesta ·
`75` estructura de costos · `82` la calculadora de margen · `97` margen por SKU ·
`99` revisión de precios mensual
