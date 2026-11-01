# El periodo de evaluación

Tu reputación no se calcula sobre toda tu historia: se calcula sobre una ventana móvil que cambia de
tamaño según cuánto vendas. Y esa ventana no solo cambia el tiempo — **cambia los umbrales**. Es la
regla que explica por qué un vendedor chico queda marcado un año y uno grande lo borra en dos meses.

## La regla

Oficial ML Colombia, verificado sep-2026:

| Tu volumen | Ventana evaluada |
|---|---|
| **60 o más ventas concretadas** | Los últimos **60 días** |
| **Menos de 60 ventas** | Los últimos **365 días** |

Y antes de todo eso: **no tienes reputación hasta completar tus primeras 10 ventas** (oficial ML
Colombia, verificado sep-2026). Hasta ahí, termómetro gris.

El recálculo es dinámico y se actualiza diariamente. No hay día de corte mensual: cada día entra uno
nuevo y sale el más viejo de la ventana.

## Los umbrales cambian con la ventana

Este es el detalle que casi nadie nota. La columna de 365 días es **más permisiva** en dos de las
tres variables (oficial ML Colombia, verificado sep-2026):

| Variable | Con 60+ ventas (60 días) | Con menos de 60 (365 días) |
|---|---|---|
| Ventas con reclamos | ≤ 3,5% | ≤ 3,5% (igual) |
| Envíos incorrectos | ≤ 12% | ≤ **15,5%** (más holgado) |
| Canceladas por ti | ≤ 2,5% | ≤ **4%** (más holgado) |

ML reconoce que el vendedor chico tiene menos oficio y le da aire en logística. Pero en **reclamos
no hay descuento**: el 3,5% aplica igual al de 10 ventas y al de 10.000.

## Las tres etapas de tu vida como vendedor

| Etapa | Ventas | Qué pasa |
|---|---|---|
| **Gris** | 0 a 9 | Sin reputación. Igual tienes 50% de descuento en envíos (`125`). Full bloqueado |
| **Ventana larga** | 10 a 59 | Evaluado a 365 días, umbrales holgados en envíos y cancelaciones |
| **Ventana corta** | 60+ | Evaluado a 60 días, umbrales más exigentes — pero puedes olvidar rápido |

**Cruzar las 60 ventas es la decisión estratégica escondida de este módulo**: te aprieta los
umbrales pero te da capacidad de olvidar. Para un vendedor golpeado, apurar volumen limpio hasta
cruzar las 60 es literalmente el camino más corto de vuelta al verde.

## Cuánto te persigue un error

Aritmética simple: un caso dividido entre las ventas de tu ventana.

| Perfil | Ventas en la ventana | Peso de 1 reclamo | ¿Rompe el 3,5%? | Te persigue |
|---|---|---|---|---|
| 3 ventas/mes | ~36 en 365 días | 2,8% | No, pero queda al filo | **Un año** |
| 5 ventas/mes | ~60 en 365 días | 1,7% | No | **Un año** |
| 2 ventas/mes | ~24 en 365 días | 4,2% | **Sí** | **Un año** |
| 30 ventas/mes | ~60 en 60 días | 1,7% | No | 60 días |
| 200 ventas/mes | ~400 en 60 días | 0,25% | No | 60 días |

Mira la tercera fila: **con 24 ventas al año, un solo reclamo te saca del verde durante 365 días** —
y eso son $8.200 más de envío en cada venta durante todo ese tiempo (`125`). Para un vendedor muy
chico, la reputación es una cuerda floja de un caso.

## Lo que esto cambia en tus decisiones

```
□ Con menos de 60 ventas: cada venta es un examen. No experimentes con productos que no conoces
□ Con menos de 60 ventas: un lote defectuoso te arruina el año. Revisa antes de subirlo
□ Cruzar 10 ventas desbloquea reputación y Full: es hito, no trámite
□ Cruzar 60 ventas acorta la ventana de 365 a 60 días: es objetivo estratégico
□ Con volumen alto no entres en pánico por un caso: mira la tendencia de 60 días
```

## El truco del denominador y su trampa

Como el porcentaje es casos ÷ ventas, hay dos formas de bajarlo: menos casos, o más ventas. Vender
más **sí** diluye — es matemática, no truco.

La trampa es escalar con el problema puesto. Si tu tasa es estructural, vender el doble te trae el
doble de casos y el porcentaje no se mueve. **Diluir funciona con un problema puntual ya resuelto,
nunca con uno estructural.**

| Señal | Diagnóstico | Qué hacer |
|---|---|---|
| Los casos se concentran en un SKU | Puntual | Pausa ese SKU y escala el resto |
| Se concentran en un lote o una fecha | Puntual | Identifica el lote, contacta proactivamente |
| Están repartidos parejo | Estructural | **No escales.** Arregla proceso primero |

## Qué no entra en la ventana

| Cosa | ¿Entra? |
|---|---|
| Ventas en la categoría **Inmuebles** | **No.** No afectan la reputación (oficial) |
| Reclamos por arrepentimiento del comprador | No (excepción oficial) |
| Ventas canceladas **por el comprador** | No (excepción oficial) |
| Reclamos excluidos correctamente | No (`136`) |
| Reclamos con solicitud de cancelación reembolsados en 2 días hábiles | No (`136`) |
| Devoluciones | No como cancelación (`138`) |
| Opiniones y calificaciones | No al termómetro — otro sistema (`142`) |

## El error clásico

Creer que la reputación "se limpia sola con el tiempo" y dejar de vender esperando. Se limpia con el
tiempo **y con ventas limpias dentro de la ventana**. Si te congelas, el denominador se queda chico
y el porcentaje no baja: te quedas con el problema puesto y sin salida.

Lo correcto estando golpeado es **seguir vendiendo, pero solo lo que sabes que sale perfecto**.
Pausa los SKU riesgosos, mantén vivos los seguros (`128`).

## Relacionados

`125` el termómetro · `126` las tres métricas · `128` cómo se recupera una caída ·
`129` MercadoLíder · `136` reglas de exclusión · `138` devoluciones · `142` opiniones negativas ·
`144` plan de defensa de la cuenta · `105` Full · `169` tus datos y tableros
