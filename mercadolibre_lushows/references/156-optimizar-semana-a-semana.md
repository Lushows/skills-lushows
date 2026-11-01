# Optimizar semana a semana

La rutina de mantenimiento de Mercado Ads: qué se toca, cada cuánto y — sobre todo — por qué no se
toca a diario. La mayor parte del trabajo de optimizar consiste en **no hacer nada** durante el
tiempo correcto.

## Por qué no se optimiza todos los días

Las ventas tardan **hasta 72 horas** en reflejarse en el reporte (oficial ML Colombia, verificado
sep-2026) y la atribución llega hasta **14 días** después del clic (`151`). Consecuencia directa:

| Si optimizas… | Qué estás haciendo en realidad |
|---|---|
| A diario | Reaccionando a un ACOS inflado que no existe |
| Cada 3 días | Igual: la ventana de 14 días ni empezó |
| **Cada 14 días** | **Leyendo datos casi cerrados. Esta es la rutina correcta** |
| Cada mes | Perfectamente válido, sobre todo con presupuesto chico |

Además, cada cambio **reinicia el reloj**: el sistema necesita volver a estabilizar. Optimizar
semanalmente significa no tener nunca un periodo limpio que leer.

**El mejor optimizador de Mercado Ads es un calendario, no un panel.**

## La rutina, por frecuencia

| Frecuencia | Qué se hace | Qué NO se hace |
|---|---|---|
| **Diario (2 min)** | Verificar stock de los SKU pautados. Responder preguntas | Mirar el ACOS. Tocar presupuesto |
| **Semanal (10 min)** | Vistazo: ¿algún SKU se disparó?, ¿el presupuesto se agota antes de la tarde? | Cambiar estrategia. Apagar por impaciencia |
| **Quincenal (45 min)** | La lectura real: exportar Excel, semáforo por SKU, **UN** cambio (`155`) | Cambiar dos cosas a la vez |
| **Mensual (1 h)** | ACOS + TACOS del negocio, cruce con órdenes reales, limpieza de SKU muertos | — |
| **Trimestral** | Recalcular márgenes por SKU y rearmar campañas por rango de margen (`97`, `99`) | — |

## Las únicas intervenciones de emergencia

Hay tres cosas que sí se tocan el mismo día, sin esperar los 14:

| Emergencia | Acción inmediata |
|---|---|
| Te quedaste sin stock de un SKU pautado | Reponer o pausar ese anuncio. Seguir pagando clics hacia un producto agotado es puro desperdicio (`61`) |
| Publicaron tu SKU con un error de precio | Corregir. Cambios bruscos de precio pueden pausar la publicación (`73`) |
| La reputación cayó a naranja o roja | Apagar la pauta y arreglar la reputación primero (`125`, `164`) |

Nada más. Un ACOS feo a los tres días **no** es una emergencia.

## La regla de un solo cambio

En cada ventana quincenal se mueve **una** variable. Si mueves dos, no vas a saber cuál funcionó.

| Situación (dato de 14 días limpios) | El único cambio |
|---|---|
| ACOS por debajo del objetivo y presupuesto agotado temprano | Subir presupuesto **20-30%** |
| ACOS por debajo del objetivo y presupuesto sin agotar | No tocar nada. Ya está optimizado |
| ACOS entre el objetivo y el techo | No tocar nada. Es zona amarilla, aún ganas |
| ACOS por encima del techo (el margen neto) | Bajar a una estrategia más conservadora (`148`) |
| ACOS por encima del techo y ya estás en Rentabilidad | Apagar ese SKU y revisar ficha y precio (`164`) |
| Clics sin ventas | **No es un problema de pauta.** Arreglar foto, título o precio (`42`, `68`) |
| Casi sin clics | Tu ficha no compite en el listado. Arreglar antes de subir presupuesto |

Nunca dobles el presupuesto de golpe. Los saltos grandes cambian el comportamiento de la campaña y
pierdes la lectura que te acababa de costar dos semanas conseguir.

## La bitácora

Sin registro no hay optimización, hay improvisación con buena memoria. Una hoja simple:

| Fecha | Campaña | Qué cambié | ACOS previo | ACOS a los 14 días | Veredicto |
|---|---|---|---|---|---|
| 02-oct | Combos | Presupuesto +25% | 11% | 13% | Sostener |
| 16-oct | Combos | Nada | 13% | 12% | Estable |
| 30-oct | Accesorios | Apagué SKU-441 | 38% | — | Ficha mala |

A los tres meses esta tabla vale más que cualquier curso: es el único benchmark que de verdad
aplica a tu cuenta.

## El ciclo completo de 14 días

```
Día 0   → Hacer UN cambio. Anotarlo en la bitácora con fecha
Día 1-10→ No mirar el ACOS. Solo verificar stock a diario
Día 11  → Vistazo rápido: ¿algo se disparó?, ¿el presupuesto se agota temprano?
Día 14  → Exportar Excel de día 0 a día 11 (los últimos 3 no cuentan, ver `151`)
Día 14  → Semáforo por SKU contra el margen neto (`150`)
Día 14  → Decidir UN cambio y volver al día 0
```

## Limpieza mensual

```
□ Apagué los SKU con ACOS por encima del techo dos periodos seguidos
□ Pausé los anuncios de publicaciones sin stock o pausadas
□ Revisé que ningún SKU pautado haya cambiado de precio sin recalcular margen
□ Calculé ACOS y TACOS del mes y los anoté (`149`)
□ Comparé contra mi propio mes anterior, no contra un benchmark de internet
□ Verifiqué que la reputación sigue en verde (`125`)
□ Si viene una fecha caliente, ya tengo campaña aparte creada (`162`)
```

## El error clásico

Optimizar por ansiedad. El vendedor promedio abre el panel cada mañana, ve el gasto del día
corriendo y las ventas en cero — porque tardan 72 horas —, se asusta y baja el presupuesto. Al día
siguiente entran las ventas atribuidas, el ACOS se ve bien, y lo vuelve a subir. Ese sube-y-baja
mantiene la campaña permanentemente en fase de aprendizaje y nunca produce un dato limpio.
**No tocar durante 14 días no es pereza: es la técnica.**

## Relacionados

`145` qué es Mercado Ads · `146` Product Ads · `147` la subasta y el CPC ·
`148` las tres estrategias · `149` ACOS y TACOS · `150` el ACOS sano según tu margen ·
`151` la ventana de atribución · `153` el efecto sobre lo orgánico · `155` leer los reportes ·
`162` preparar una fecha caliente · `164` cuándo no es la respuesta · `42` fotos ·
`61` stock cero · `68` precio como factor · `73` pausas · `97` margen por SKU ·
`99` revisión de precios mensual · `124` auditoría mensual · `125` reputación
