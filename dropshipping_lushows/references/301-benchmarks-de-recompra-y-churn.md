# Benchmarks de recompra y churn

> Un benchmark no te dice si tu negocio va bien. Te dice si tu número es raro. Úsalo para detectar
> anomalías, no para fijar metas. Y todo número de este módulo: **verificar contra tus propios datos
> antes de tomar cualquier decisión de plata.**

## Tabla maestra: recompra

| Métrica | Valor 2026 | Fuente / nota |
|---|---|---|
| Recompra ecommerce general | **28,2%** promedio | rango observado 15-30% |
| Ecommerce general: qué es fuerte | **25-30%** | por encima de 30% es excepcional |
| Salud y suplementos | **29%** | apenas sobre el promedio general |
| Marcas de suplementos USD 1M-50M, a 12 meses | **38-52%** | operaciones ya maduras |
| Suplementos, top quartile a 12 meses | **64%** | el techo realista del nicho |
| Producto único / novedad sin consumible | 2-8% | ver `230` |
| Regalo de temporada | 1-5% | diciembre puro |

**Lee esto:** el promedio de ecommerce (28,2%) y el de suplementos (29%) son casi iguales. La ventaja
del nicho **no está en la primera recompra, está en la duración**. A 12 meses el suplemento llega a
38-52% y el producto genérico no. La diferencia se acumula en el tiempo, no aparece en el mes 1.

## Tabla maestra: churn de suscripción

| Métrica | Valor 2026 |
|---|---|
| Churn mensual suscripción DTC, rango general | **6,5-8,5%** |
| Categorías de reposición (suplementos, consumibles, mascotas) | **5-8%** |
| Bueno | **5-7%** |
| Excelente | **<5%** |
| Red Recurly, julio 2026: churn total | **3,60%** |
| ↳ voluntario (se fue porque quiso) | **2,34%** |
| ↳ **involuntario (falló la tarjeta)** | **1,25%** |
| Reactivación en 30 días tras cancelar | **15,4%** |

El dato de Recurly es de una red de miles de comercios, así que está sesgado hacia operaciones
maduras con dunning ya montado. Tu churn arrancando será más alto. Pero la **proporción** sí te
sirve: **35% del churn no es insatisfacción, es una tarjeta que falló.** Ver `304`.

## Cómo se lee un churn

| Churn mensual | Vida media del cliente (meses) | Lectura |
|---|---|---|
| 3,6% | ~27 | red madura con dunning |
| 5% | ~20 | excelente para DTC |
| 7% | ~14 | normal, dentro de rango |
| 8,5% | ~12 | techo del rango sano |
| 12% | ~8 | hay un problema de producto o de expectativa |
| 20% | ~5 | el primer envío no cumplió lo que prometió el anuncio |

Vida media aproximada = 1 ÷ churn mensual. Es una aproximación; para el número exacto por cohorte
usa `309` y verifica con `Matematicas_lushows`.

## La curva de retención no es una línea

| Mes | Retención típica de una cohorte de suscripción (verificar) |
|---|---|
| 1 | 100% |
| 2 | 70-80% ← **aquí se cae la mayoría** |
| 3 | 60-70% |
| 6 | 45-58% |
| 12 | 30-45% |

El churn del mes 2 es 3-5 veces el churn del mes 8. **El cliente que sobrevive al segundo cobro se
queda mucho más.** Por eso `305` (la segunda compra) es el módulo que más plata mueve de todo el
bloque, y por eso un descuento agresivo de entrada que no se sostiene en el mes 2 destruye más de lo
que aporta.

## Tabla de autodiagnóstico

| Tu número | Normal | Bueno | Excelente | Si estás por debajo, mira |
|---|---|---|---|---|
| Recompra 90 días (consumible) | 15-20% | 20-30% | >30% | `305`, `308` |
| Recompra 12 meses (suplemento) | 30-38% | 38-52% | >64% | `306`, `307` |
| Churn mensual suscripción | 8-10% | 5-7% | <5% | `303`, `304` |
| % de churn que es involuntario | >40% | 30-35% | <25% | `304` — es el más fácil de arreglar |
| Reactivación a 30 días | <10% | 15% | >20% | `306` |
| Compras promedio por cliente | 1,2 | 1,8 | >2,5 | `302`, `309` |

## Los tres errores al usar benchmarks

| Error | Por qué duele |
|---|---|
| Comparar tu mes 1 contra un benchmark de 12 meses | el benchmark de 38-52% es a un año; tu cohorte de septiembre no puede tenerlo en octubre |
| Comparar tu recompra "de toda la tienda" contra la de cohorte | la tienda entera mezcla cohortes viejas y nuevas; siempre engorda o adelgaza falsamente (`302`) |
| Mover el presupuesto por un número de una sola cohorte pequeña | con 40 clientes, ±5 personas cambian el resultado 12 puntos |

**Tamaño mínimo para creerle a una cohorte:** ~100 clientes para leer tendencia, ~300 para tomar
decisiones de presupuesto. Por debajo de 50, el número es ruido.

## Qué medir desde el día 1 (aunque no tengas suscripción)

| Métrica | Cómo | Dónde vive |
|---|---|---|
| Clientes únicos por mes de primera compra | email normalizado a minúsculas, no por pedido | hoja/planilla o Shopify |
| Pedidos por cliente y fecha de cada uno | export de pedidos | `309` lo consume |
| Días entre compra 1 y 2 | mediana, no promedio | alimenta `308` |
| Margen de contribución por pedido | ticket − producto − envío − pasarela | `223` |
| Origen de adquisición del cliente | para no mezclar CAC de canales | `224` |

Si no capturas esto desde la primera venta, en marzo de 2027 no vas a poder calcular nada. Es
gratis hacerlo ahora y caro reconstruirlo después.

## Aplicación al proyecto México

| Supuesto para el plan | Valor a usar |
|---|---|
| Recompra a 90 días esperada (kit capilar / gomitas) | **15-20%**, conservador |
| Recompra a 12 meses si el producto funciona | 29-38%, verificar |
| Churn mensual si se monta suscripción en 2027 | planear 8-10% al inicio, no 5% |
| Meta operativa antes de escalar | segunda compra ≥20% a 90 días |

No planees con 52%. Ese número es de marcas de USD 1M-50M con años de operación. Planea con 15-20%
y celebra si llegas a 29%.

## Relacionados
`11` · `223` · `224` · `230` · `300` · `302` · `304` · `305` · `306` · `308` · `309`
