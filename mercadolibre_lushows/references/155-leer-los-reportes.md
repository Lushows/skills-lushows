# Leer los reportes

Dónde están los números de Mercado Ads, en qué orden mirarlos y qué ignorar. El panel muestra
muchas métricas y casi todas son ruido: hay tres que deciden y el resto son contexto.

## Dónde están

**Mi cuenta → Marketing → Publicidad** (oficial ML Colombia, verificado sep-2026). Ahí encuentras
tres pestañas:

| Pestaña | Qué muestra | Para qué sirve |
|---|---|---|
| **Campañas** | Gasto, ventas, ACOS por campaña | La vista de gobierno: ¿sigo o paro? |
| **Anuncios** | Lo mismo pero por publicación | La vista de trabajo: ¿qué SKU apago? |
| **Reportes** | Descarga a **Excel** del periodo que elijas | La vista de verdad: aquí se hace el análisis |

Trabaja en el Excel, no en la pantalla. En pantalla el panel te empuja a mirar totales; en el
Excel puedes ordenar por SKU, cruzar con tu margen y ver dónde se está yendo la plata.

## El orden correcto de lectura

No empieces por el ACOS. Empieza por las condiciones de validez del dato:

```
1. ¿El rango termina hace 3 días o más?   → si no, el dato no sirve (`151`)
2. ¿Llevo 14 días sin tocar nada?         → si no, no hay qué leer todavía
3. Recién ahora: ACOS por campaña
4. Después: ACOS por anuncio (por SKU)
5. Al final: clics, CTR, impresiones      → contexto, no decisión
```

## Las tres métricas que deciden

| Métrica | Qué te dice | Contra qué se compara |
|---|---|---|
| **ACOS por SKU** | Si esa publicación se paga sola | El **margen neto de ese SKU** (`150`), nunca un benchmark |
| **Clics sin ventas** | Que la ficha o el precio no convencen | Cero: clics que no convierten son diagnóstico gratis |
| **TACOS del mes** | Si el negocio completo mejoró | Tu propio TACOS del mes anterior (`149`) |

**Ninguna de las tres se lee sola: las tres se leen contra un número tuyo.** El ACOS contra tu
margen, los clics contra tus ventas, el TACOS contra tu mes pasado.

## Lo que es contexto y no decisión

| Métrica | Por qué no decide |
|---|---|
| Impresiones | Son gratis. Tener muchas no significa nada |
| CTR | Útil para diagnosticar foto y título, no para mover presupuesto |
| CPC promedio | Es un resultado, no una palanca (`147`) |
| Ventas totales de la campaña | Sin el costo al lado, es una cifra de vanidad |
| Posición promedio | No la controlas y cambia por búsqueda |

Un CTR bajo con muchas impresiones sí tiene lectura útil: tu foto principal o tu precio no están
compitiendo en el listado (`42`, `68`). Pero eso se arregla en la ficha, no en la campaña.

## El cruce que hay que hacer en el Excel

Ninguna columna del reporte trae tu margen. Hay que agregarla a mano una vez y reutilizarla:

| Columna | De dónde sale |
|---|---|
| SKU / publicación | Del reporte |
| Inversión | Del reporte |
| Ventas atribuidas | Del reporte |
| ACOS | Del reporte |
| **Margen neto %** | **Tuyo**, de `scripts/margen_ml.py` (`82`) |
| **ACOS techo** | Igual al margen neto |
| **ACOS objetivo** | 2/3 del margen neto (`150`) |
| **Semáforo** | ACOS < objetivo = verde · entre objetivo y techo = amarillo · > techo = rojo |

Ese semáforo es toda la decisión: verde sube presupuesto, amarillo se queda quieto, rojo se apaga
o se arregla.

## Trampas del reporte

| Trampa | Cómo evitarla |
|---|---|
| Ventas que aún no aparecen (hasta **72 h**) | Descarta los últimos 3 días del rango (`151`) |
| Ventas indirectas de otro SKU infladas al anuncio pautado | Cruza con tus órdenes reales antes de celebrar (`151`) |
| El reporte no descuenta devoluciones | Tu ACOS real es peor que el del panel (`95`) |
| Comparar meses con distinta cantidad de días | Normaliza por día o compara periodos iguales |
| Mirar el total de la cuenta y no el SKU | El promedio esconde al SKU que te está sangrando |
| Fechas calientes mezcladas con meses normales | Saca Hot Sale a una campaña aparte (`162`) |

La penúltima es la más cara: una cuenta con ACOS promedio de 14% puede tener tres SKU en 8% y uno
en 60%. **El promedio nunca es el paciente.**

## Cada cuánto exportar

| Frecuencia | Qué haces |
|---|---|
| Diario | Nada. Solo verificar que no te quedaste sin stock |
| Semanal | Mirada rápida: ¿algún SKU se disparó?, ¿el presupuesto se agota temprano? |
| **Cada 14 días** | **La lectura real y el único momento de ajustar** (`156`) |
| Mensual | ACOS + TACOS del negocio completo, cruzado con tus órdenes |
| Trimestral | Revisión de márgenes por SKU y limpieza de campañas (`97`, `99`) |

## El error clásico

Mirar el panel todos los días. El gasto se actualiza en tiempo real y las ventas con hasta 72
horas de retraso, así que la foto instantánea **siempre** se ve peor de lo que fue. El vendedor
que mira a diario apaga campañas sanas por pánico y vuelve a encenderlas tres días después,
reiniciando el aprendizaje cada vez. **Mirar no es gratis: mirar mucho te hace tocar, y tocar es
lo que rompe la campaña.**

## Checklist de la lectura quincenal

```
□ Exporté el Excel de un rango que termina hace 3 días o más
□ Ese rango tiene al menos 14 días sin cambios en la campaña
□ Agregué la columna de margen neto por SKU desde `82`
□ Calculé el semáforo: verde / amarillo / rojo por SKU
□ Anoté ACOS y TACOS del periodo para comparar con el siguiente
□ Identifiqué los SKU con clics y sin ventas (arreglar ficha, no pauta)
□ Voy a hacer UN solo cambio, y lo anoté con fecha (`156`)
```

## Relacionados

`145` qué es Mercado Ads · `146` Product Ads · `147` la subasta y el CPC ·
`148` las tres estrategias · `149` ACOS y TACOS · `150` el ACOS sano según tu margen ·
`151` la ventana de atribución · `153` el efecto sobre lo orgánico ·
`156` optimizar semana a semana · `162` preparar una fecha caliente ·
`164` cuándo no es la respuesta · `42` fotos · `68` precio como factor ·
`82` la calculadora de margen · `95` costo oculto de la devolución · `97` margen por SKU ·
`99` revisión de precios mensual · `124` auditoría mensual
