# Análisis de cohortes

> El promedio de tu tienda te miente todos los días. Si en octubre traes 500 clientes nuevos, tu
> "tasa de recompra global" se desploma aunque tu producto esté mejor que nunca — porque acabas de
> meter 500 personas que todavía no tuvieron tiempo de volver. La cohorte es el único corte que no
> se deja engañar por el ritmo de la pauta.

## Qué es una cohorte

**Cohorte = grupo de clientes que hicieron su PRIMERA compra en el mismo periodo** (normalmente el
mismo mes). Una vez que entras a la cohorte de septiembre, eres de septiembre para siempre. No te
mueves.

| Concepto | Definición |
|---|---|
| Cohorte | clientes con primera compra en el mes M |
| Mes 0 | el mes de la primera compra (siempre 100%) |
| Mes N | N meses después; se mide qué % de esa cohorte compró en ese mes |
| Retención acumulada | % de la cohorte que ha comprado ≥1 vez más desde el mes 0 |
| Margen acumulado | USD de margen de contribución por cliente de esa cohorte a la fecha |

Cuidado con la confusión más común: **retención mensual** (compró en ese mes) y **recompra
acumulada** (compró alguna vez más) son dos tablas distintas. Un negocio de reposición cada 60 días
tiene retención mensual baja y recompra acumulada alta. No las mezcles.

## Cómo se arma la tabla

1. Exporta pedidos: `email`, `fecha`, `total`, `margen_contribucion`.
2. Normaliza el identificador de cliente (email en minúsculas, sin espacios). Si el mismo humano
   compra con dos correos, es un cliente nuevo para tu tabla. Asúmelo y sigue.
3. Por cliente: `mes_cohorte = mes de su fecha mínima`.
4. Por pedido: `offset = meses entre la fecha del pedido y el mes_cohorte`.
5. Tabla dinámica: filas = mes_cohorte, columnas = offset, valores = clientes distintos que
   compraron ÷ tamaño de la cohorte.

Con 200 pedidos esto se hace en una hoja de cálculo en 20 minutos. Con 2.000, usa `309`.

## Ejemplo trabajado (cifras ilustrativas, no medidas)

Tienda de consumible, 4 cohortes. Retención acumulada (% de la cohorte que ya compró ≥1 vez más):

| Cohorte | n | Mes 1 | Mes 2 | Mes 3 | Mes 4 | Mes 5 |
|---|---|---|---|---|---|---|
| Mayo | 180 | 6% | 14% | 19% | 22% | 24% |
| Junio | 240 | 7% | 15% | 20% | 23% | — |
| Julio | 410 | 5% | 10% | 13% | — | — |
| Agosto | 520 | 9% | 18% | — | — | — |

Qué dispara cada fila:

| Observación | Diagnóstico | Acción |
|---|---|---|
| Mayo y junio casi idénticas | el producto entrega lo que promete, la base es estable | no toques nada, es tu línea base: ~20% al mes 3 |
| **Julio se cae a 13% al mes 3** | algo pasó en julio | investigar: ¿escalaste pauta con un ángulo nuevo? ¿hubo demora de envío? ¿cambió el proveedor? |
| Agosto rebota a 18% en el mes 2 | mejor que todas | ¿qué cambiaste? Si fue el flujo de reposición de `308`, ya sabes qué escalar |

**La lectura de julio es el valor entero del ejercicio.** Con el promedio global de la tienda ese
hueco no se ve: queda enterrado bajo el volumen de agosto. La cohorte lo aísla.

## Las decisiones que dispara una tabla de cohortes

| Lo que ves | Lo que significa | Lo que haces |
|---|---|---|
| Cohortes nuevas peor que viejas | escalaste hacia público de peor calidad, o el producto se degradó | revisar públicos (`facebook_ads_lushows`), revisar proveedor (`116`) |
| Cohortes nuevas mejor que viejas | tu operación mejoró | sube el techo de CAC y escala (`11`) |
| Todas planas después del mes 3 | el cliente ya no vuelve solo | ahí es donde entra el calendario de reposición (`308`) y reactivación (`306`) |
| Una cohorte de un canal muy superior | ese canal trae mejor cliente aunque el CAC sea más caro | reasignar presupuesto por LTV, no por CPA |
| La curva se aplana en 25-30% | estás en el rango normal-fuerte de mercado (`301`) | consolidar antes de perseguir el 52% |

## Cortes que valen la pena (y uno que no)

| Corte | ¿Vale? | Por qué |
|---|---|---|
| Por canal de adquisición (Meta vs TikTok vs orgánico) | **sí** | cambia decisiones de presupuesto |
| Por producto de entrada | **sí** | el producto de la primera compra predice la recompra |
| Por oferta (unidad simple vs pack doble vs triple) | **sí** | el pack triple compra 3 meses de producto: su recompra llega más tarde, no es peor |
| Por descuento de entrada (con cupón vs sin cupón) | **sí** | el cazador de cupones suele retener peor; medirlo, no suponerlo |
| Por ciudad / estado | casi nunca | ruido, salvo problema logístico localizado |

## Margen acumulado por cohorte: la tabla que de verdad decide

Retención en % es diagnóstico. **Plata acumulada es decisión.** Con la economía verificada de México
(margen 26,47 sin CAC; CAC 10,54; primera venta deja 15,93):

| Compras acumuladas | Margen acumulado por cliente (USD) | Múltiplo |
|---|---|---|
| 1 | 15,93 | 1,00x |
| 2 | 42,39 | 2,66x |
| 3 | 68,86 | 4,32x |
| 6 | 148,26 | 9,31x |
| 12 | 307,07 | 19,28x |

Si tu cohorte de mayo llegó a 1,4 compras promedio a 5 meses, su margen por cliente es ~26,5 USD.
Si la de agosto va camino a 1,8, su margen será ~42. **Misma pauta, mismo CAC, 58% más de plata.**
Eso es lo que autoriza (o no) subir presupuesto. Ver `11`, `234` y el cálculo exacto en `309`.

## Errores que arruinan la tabla

| Error | Consecuencia |
|---|---|
| Cohortar por fecha de pedido en vez de por primera compra del cliente | la tabla no significa nada |
| Incluir el mes en curso como si estuviera completo | la última columna siempre parece un desastre |
| Cohortes de menos de 50 clientes | ruido puro; agrega por trimestre |
| Contar pedidos en vez de clientes distintos | un cliente que pidió 3 veces infla la retención |
| Mezclar devoluciones y pedidos cancelados | infla todo; filtra por pedido pagado y no reembolsado |
| Mirar la tabla una vez y no volver | el valor es la comparación mes a mes |

## Frecuencia y disciplina

| Cuándo | Qué |
|---|---|
| Mensual, día 5 | actualizar la tabla del mes cerrado |
| Antes de subir presupuesto | mirar si la cohorte más reciente mantiene la línea base |
| Después de cambiar proveedor, envase o promesa del anuncio | marcar la fecha en la tabla; esa cohorte se lee aparte |

Una regla práctica: **cada cambio grande de operación abre una cohorte nueva de lectura.** Anótalo en
la misma hoja. En tres meses no te vas a acordar de qué cambiaste en julio.

## Aplicación al proyecto México

Con ~5 tests y capital bajo, tus primeras cohortes serán de 30-80 clientes: demasiado chicas para
decidir presupuesto. Úsalas igual, pero como **semáforo cualitativo** (¿alguien vuelve?, ¿en cuántos
días?), no como número. La primera cohorte con peso estadístico saldrá del Buen Fin (13-17 nov) y de
diciembre. Esa es la que vas a leer en febrero-marzo de 2027 para decidir si hay negocio recurrente.

## Relacionados
`11` · `223` · `224` · `230` · `234` · `300` · `301` · `305` · `306` · `308` · `309`
