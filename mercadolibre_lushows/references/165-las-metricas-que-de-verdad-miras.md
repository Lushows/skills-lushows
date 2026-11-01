# Las métricas que de verdad miras

Mercado Libre te muestra decenas de números. La mayoría no sirve para decidir nada. Este módulo
separa las métricas que te hacen sentir bien de las que te obligan a hacer algo, y te dice qué
hacer con cada una. Si una métrica no dispara una decisión, no la mires.

## La prueba del algodón

Antes de agregar cualquier número a tu tablero, respóndete: **¿qué haría distinto mañana si este
número sube o baja un 20%?** Si la respuesta es "nada", es métrica de vanidad.

| Métrica de vanidad | Por qué engaña | Métrica de decisión que la reemplaza |
|---|---|---|
| Visitas totales | Suben con pauta, temporada o un competidor agotado. No dicen si vendes | Conversión por publicación |
| Ventas totales del mes | Esconde que vendes más y ganas menos | Utilidad en pesos por SKU |
| ROAS de la campaña | Se ve hermoso y aun así puedes perder plata | ACOS contra tu margen neto (`150`) |
| Cantidad de publicaciones | Un catálogo grande de publicaciones muertas pesa, no ayuda | % de SKUs que vendieron en 30 días |
| Seguidores / preguntas recibidas | No se depositan en Mercado Pago | Tasa de respuesta y su efecto en conversión |
| "Estoy en la primera página" | La posición cambia por comprador y por hora | Conversión y participación de visitas |

## Las métricas de decisión, una por una

| Métrica | Dónde se ve | Qué decisión dispara | Cada cuánto |
|---|---|---|---|
| **Conversión por publicación** | Métricas de la publicación | Visitas sin ventas = precio, foto o ficha; no falta tráfico (`58`) | Semanal |
| **Utilidad en pesos por SKU** | Tu hoja. ML **no** la tiene | Cuál repones, cuál subes de precio, cuál matas (`172`) | Semanal |
| **Margen % por SKU** | `scripts/margen_ml.py` | Techo del ACOS que puedes pagar (`150`) | Al cambiar precio o costo |
| **Costo de envío por venta** | `GET /shipments/$ID/costs` | Subir precio, cambiar empaque o modalidad (`100`) | Semanal |
| **Tasa de reclamos** | Reputación · `metrics.claims` | Revisar ficha y empaque antes que nada (`126`) | Semanal |
| **Ventas canceladas** | Reputación · `metrics.cancellations` | Arriba de 2,5% **te pueden suspender la cuenta** (`139`) | Semanal, sin falta |
| **Envíos con problemas** | Reputación · `metrics.delayed_handling_time` | Mover el corte de despacho, o pasar a Full (`105`) | Semanal |
| **ACOS por campaña** | Marketing → Publicidad → Reportes | Subir, bajar o apagar puja (`150`) | Semanal, con 72 h de rezago |
| **Días de inventario** | Tu hoja: stock ÷ venta diaria | Cuándo y cuánto reponer (`168`) | Semanal |
| **Concentración del top-1** | Tu hoja | Si pasa el 50%, urgencia de diversificar (`172`) | Mensual |

## Los números duros que ya tienes verificados

Estos son límites oficiales, no opiniones. Póngalos como líneas rojas en el tablero:

| Límite | Valor | Consecuencia |
|---|---|---|
| Ventas canceladas | más de **2,5%** | La cuenta puede ser suspendida para vender |
| Reclamos (para MercadoLíder) | menos de **2,5%** | Pierdes o no alcanzas el nivel |
| Mediaciones (para MercadoLíder) | menos de **0,5%** | Pierdes o no alcanzas el nivel |
| Canceladas (para MercadoLíder) | menos de **1,5%** | Pierdes o no alcanzas el nivel |
| Envíos incorrectos (para MercadoLíder) | menos de **10%** | Pierdes o no alcanzas el nivel |

(oficial ML Colombia, verificado sep-2026). Estos son los cortes de MercadoLíder más el umbral de
suspensión. Los umbrales para **conservar el verde** son distintos y cambian según te evalúen a 60
o a 365 días: la tabla completa está en `126`, y es la que debes copiar a tu tablero.

## Tres trampas de lectura

**Rezago de la pauta.** Los reportes de Mercado Ads pueden tardar **hasta 72 horas** en reflejar
ventas (oficial, verificado sep-2026), y la atribución cuenta **14 días post-clic**. El martes no
sabes cómo te fue el domingo. Nunca apagues una campaña mirando datos de ayer (`151`).

**Periodo móvil de la reputación.** Con 60 o más ventas concretadas te miden los últimos **60
días**; con menos, los últimos **365** (oficial, verificado sep-2026). Un vendedor nuevo arrastra
sus errores un año entero. Esa diferencia sola justifica apurar las primeras 60 ventas (`127`).

**Promedios que tapan.** "Mi margen es 22%" no existe: existe el margen de cada SKU. Un promedio
sano puede esconder tres productos que venden a pérdida y uno que los sostiene. Mide por SKU o no
midas (`172`).

## ACOS: la única forma correcta de leerlo

ACOS = inversión ÷ ingresos generados por la publicidad × 100. Invertí $100, generé $1.000 → ACOS
10% (oficial, verificado sep-2026). Los tres objetivos oficiales:

| Estrategia | ACOS objetivo |
|---|---|
| Rentabilidad | 5% - 15% |
| Crecimiento | 15% - 30% |
| Visibilidad | más de 30% |

(oficial `vendedores.mercadolibre.com.co`, verificado sep-2026). **El ACOS objetivo tiene que ser
menor que tu margen neto o la campaña destruye plata aunque el panel se vea verde.** Con margen del
15%, la franja de Rentabilidad ya te come todo. Desarrollo completo en `150`.

## Lo que ML no te mide y tienes que medir tú

```
□ Utilidad en pesos por venta (ML no conoce tu costo)
□ Costo del empaque y del material por unidad
□ Horas tuyas por semana en atender, empacar y despachar
□ Devoluciones: cuántas y cuánto te costaron netas
□ Quiebres de stock: cuántos días estuviste en cero (`140`)
□ Precio del competidor en tus 5 SKUs principales
```

## El error clásico

Mirar el panel todos los días. La conversión de una publicación con 40 visitas diarias tiene tanto
ruido que el lunes y el jueves parecen negocios distintos, y el vendedor termina cambiando el precio
tres veces por semana — que es exactamente lo que descalibra al algoritmo y dispara las revisiones
por cambio brusco de precio (`67`). **Mira diario solo lo que te puede cerrar la cuenta; todo lo
demás, semanal.**

## La regla de las tres decisiones

Un tablero sirve si de su lectura salen, como máximo, tres acciones para la semana. Si salen diez,
no tienes un tablero: tienes un desahogo. El formato de una sola página está en `166`.

## Relacionados

`58` la conversión manda · `75` estructura de costos · `100` cómo funciona Mercado Envíos ·
`105` Full · `125` el termómetro · `126` las tres métricas · `127` el periodo de evaluación ·
`139` la cancelación y su castigo · `140` el quiebre de stock · `150` ACOS sano ·
`151` leer los reportes de Ads · `166` el tablero semanal · `168` planear el inventario ·
`172` el SKU estrella y la dependencia · `180` datos por API
