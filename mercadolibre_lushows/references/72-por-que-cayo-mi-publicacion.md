# Por qué cayó mi publicación

Herramienta de diagnóstico. Tu publicación vendía y dejó de vender, o cayó de posición. Este
módulo es un árbol de decisión: recorre las causas en orden, con cómo confirmar cada una y qué
hacer. Recórrelo completo antes de tocar el precio, que es lo que todo el mundo hace primero y
casi nunca es la causa.

## Antes de empezar: separa los dos síntomas

| Síntoma | Qué significa | Por dónde entrar |
|---|---|---|
| **Caen las visitas** | Problema de exposición: te ven menos | Causas 1 a 6 |
| **Visitas iguales, caen las ventas** | Problema de conversión: te ven y no compran | Causas 7 a 10 |
| **Caen las dos** | Suele ser causa 1, 2 o 5 | Empieza por el principio |

Mira el panel de métricas de la publicación y contesta esto **antes** de seguir. Diagnosticar sin
separar exposición de conversión es como tomarse un antibiótico para un dolor de cabeza.

**Cuando algo cae, no cambies nada hasta saber qué cambió. El vendedor promedio arregla lo que no
estaba roto y pierde la pista de lo que sí.**

## Causa 1 · Stock cero (la más común y la más invisible)

| | |
|---|---|
| **Cómo confirmar** | Estado del ítem: `paused` con sub-estado `out_of_stock`. En el panel aparece como pausada por falta de stock. Revisa también variación por variación: puede estar en cero solo la talla que más se vende |
| **Qué pasó** | Saliste de la competencia y de la puja de catálogo. Al reponer revives "como más nuevo o menos confiable" |
| **Qué hacer** | Repón con cantidad suficiente para 30 días. No cambies precio ni título el mismo día. Trata la vuelta como un mini-lanzamiento: protocolo de 3 días de `59` |
| **Módulo** | `61` |

## Causa 2 · Publicación pausada o con infracción

| | |
|---|---|
| **Cómo confirmar** | Estado en el panel: "Inactiva para revisar", "pausada" o notificación de infracción. Revisa el correo y las notificaciones de ML |
| **Qué pasó** | Puede ser un cambio brusco de precio, ficha incompleta, datos de contacto, producto falsificado o una denuncia de un usuario cualquiera (el botón "Denunciar" está en la esquina inferior derecha de toda ficha) |
| **Qué hacer** | Corrige la causa: "Inactiva para revisar" es temporal y se reactiva al corregir. Si es infracción de marca, tienes derecho a responder con evidencia |
| **Módulo** | `73`, y `74` para apelar |

## Causa 3 · Subiste el precio

| | |
|---|---|
| **Cómo confirmar** | Historial de cambios de la publicación. ¿La caída coincide con el día del cambio? |
| **Qué pasó** | El precio es pilar del ranking y variable del catálogo. Un precio menos competitivo te baja en las dos |
| **Qué hacer** | Compara tu **precio final con envío** contra el de los 3 primeros (`70`). Si estás fuera de rango, corre el margen antes de volver a bajar (`83`). Si subiste porque el costo subió, la respuesta puede ser cambiar de producto, no de precio |
| **Módulo** | `68`, `83` |

## Causa 4 · Un competidor activó Full

| | |
|---|---|
| **Cómo confirmar** | Busca tu término en incógnito (`69`). ¿Los primeros ahora tienen "Llega mañana" o el ícono de Full y antes no? ¿Apareció un vendedor nuevo arriba? |
| **Qué pasó** | La logística es pilar del ranking y variable del catálogo. Él no te atacó: se puso Full y el algoritmo lo premió |
| **Qué hacer** | No lo peleas con precio: lo peleas con logística. Evalúa Full o baja tu tiempo de manejo. Si no puedes, considera diferenciar el producto (`64`) |
| **Módulo** | `67`, `103` |

## Causa 5 · Perdiste el catálogo

| | |
|---|---|
| **Cómo confirmar** | Abre la ficha del producto en incógnito 5 veces. ¿Sale otro vendedor con "Comprar ahora"? ¿Tú apareces solo en "Otras opciones de compra"? |
| **Qué pasó** | Alguien te ganó en precio final, cuotas, reputación, stock, tiempo de entrega, Full/Flex, envío gratis o nivel MercadoLíder. O tú caíste en una de esas |
| **Qué hacer** | Compara las ocho variables columna por columna con el ganador. Ataca en el orden de `63`: reputación, stock, logística, cuotas, envío gratis, precio. Ojo: si tu reputación pasó a naranja o roja, **no puedes ganar** aunque iguales todo lo demás |
| **Módulo** | `62`, `63`, `65` |

## Causa 6 · Cayó tu reputación

| | |
|---|---|
| **Cómo confirmar** | Mira el color de tu termómetro. ¿Cambió en el último mes? Revisa reclamos, cancelaciones y envíos incorrectos en el panel de reputación |
| **Qué pasó** | Naranja o roja activa penalizaciones de posicionamiento que ninguna publicidad compensa, y te cierra la puerta a ganar catálogo |
| **Qué hacer** | Para la pauta, responde todo mensaje pendiente hoy (tienes **24 horas hábiles** o pierdes el derecho a pedir la exclusión del reclamo), despacha a tiempo y deja de cancelar. Más del **2,5% de ventas canceladas** puede suspender la cuenta |
| **Módulo** | `66`, `125`, `133`, `136` |

## Causa 7 · Estacionalidad

| | |
|---|---|
| **Cómo confirmar** | Compara contra el mismo mes del año pasado, no contra el mes pasado. ¿Cayó toda tu categoría o solo tú? Mira si los líderes también bajaron |
| **Qué pasó** | El algoritmo ajusta por época del año. Y hay meses en que tu producto simplemente no se busca |
| **Qué hacer** | Nada estructural. No rehagas la ficha por una caída estacional: prepara la próxima temporada alta (Hot Sale 19-23 oct 2026) |
| **Módulo** | `71`, `163` |

## Causa 8 · Se acabó la campaña de Ads

| | |
|---|---|
| **Cómo confirmar** | ¿Tu presupuesto se agotó, la campaña se pausó o subió el CPC de la categoría? Mi cuenta → Marketing → Publicidad |
| **Qué pasó** | Perdiste las posiciones pagadas. Ojo: los reportes tardan **hasta 72 horas** en reflejar ventas — puede que no hayas caído tanto como crees |
| **Qué hacer** | Espera 72 horas antes de concluir. Revisa que el ACOS siga por debajo de tu margen neto (Rentabilidad 5%-15%, Crecimiento 15%-30%, Visibilidad >30%, oficial ML Colombia verificado sep-2026) |
| **Módulo** | `150`, `154` |

## Causa 9 · Cambió algo en tu ficha

| | |
|---|---|
| **Cómo confirmar** | ¿Editaste título, categoría, fotos o atributos justo antes de la caída? ¿Bajó tu indicador de calidad de "Profesional"? |
| **Qué pasó** | Editar la ficha reinicia parte de la lectura. Cambiar la categoría es lo más grave |
| **Qué hacer** | Si el cambio fue malo, revierte y espera 2-3 semanas. Si cambiaste de categoría y la nueva está mal, probablemente toque republicar (`60`) |
| **Módulo** | `40`, `41`, `48`, `60` |

## Causa 10 · No cayó nada: nunca arrancó

| | |
|---|---|
| **Cómo confirmar** | ¿La publicación es de menos de 60 días y nunca vendió bien? Entonces no "cayó": quedó etiquetada en sus primeras 72 horas |
| **Qué pasó** | Se publicó sin la ficha lista y las primeras ~100 visitas fijaron la etiqueta de conversión |
| **Qué hacer** | Ir a la tabla de decisión de `60`: arreglar y esperar, o republicar desde cero |
| **Módulo** | `59`, `60` |

## El diagnóstico en bloque de chequeo

```
□ ¿Tiene stock, incluidas todas las variaciones?              → Causa 1
□ ¿Está activa, sin pausa ni infracción?                      → Causa 2
□ ¿Cambió el precio en los últimos 30 días?                   → Causa 3
□ ¿Los 3 primeros de mi término tienen Full y antes no?       → Causa 4
□ ¿Sigo ganando el catálogo? (5 pruebas en incógnito)         → Causa 5
□ ¿Mi termómetro sigue en el mismo color?                     → Causa 6
□ ¿Cayó toda la categoría o solo yo?                          → Causa 7
□ ¿Está corriendo la campaña de Ads con presupuesto?          → Causa 8
□ ¿Edité la ficha justo antes?                                → Causa 9
□ ¿Alguna vez vendió bien de verdad?                          → Causa 10
```

Recórrelo en ese orden. Las primeras causas son las más frecuentes y las más baratas de arreglar.

## Las tres cosas que NO debes hacer mientras diagnosticas

| No hagas | Por qué |
|---|---|
| Bajar el precio "por si acaso" | Regalas margen sin saber si era la causa; y después no puedes subirlo |
| Republicar de una | Pierdes historial y opiniones sin haber arreglado nada (`60`) |
| Cambiar cinco cosas a la vez | Aunque mejore, no vas a saber cuál funcionó ni podrás repetirlo |

Cambia **una variable**, espera **dos o tres semanas**, mide. Sí, es lento. Es la única forma de
aprender algo de tu propia cuenta.

## Cuando el diagnóstico no da nada

Si recorriste las diez causas y todo está bien, quedan dos posibilidades honestas:

1. **El mercado cambió.** Entró un competidor con mejor costo o la demanda del producto bajó. Eso
   no se arregla optimizando la ficha: se arregla cambiando de producto
   (`dropshipping_lushows`) o de propuesta (`64`).
2. **Es ruido normal.** Las ventas de una publicación oscilan. Antes de declarar una caída,
   compara ventanas de 30 días, no de 3. Si el cálculo tiene que ser serio, rutea a
   `Matematicas_lushows`.

## El error clásico

Diagnosticar por sensación y actuar el mismo día. "No vendo → bajo el precio". Ocho de cada diez
veces la causa real era stock cero en una variación, una pausa que no vio, o un competidor que
activó Full. **Revisa el estado de la publicación antes de tocar cualquier número.**

## Relacionados

`40` atributos · `41` criterios de categoría · `48` indicador de calidad ·
`57` factores del ranking · `58` la conversión manda · `59` primeras 72 horas ·
`60` relanzar una publicación quemada · `61` stock cero · `62` qué es el catálogo ·
`63` cómo se gana el catálogo · `65` compartir el primer lugar · `66` reputación como filtro ·
`67` envío y posición · `68` precio como factor · `69` medir tu posición real ·
`70` espiar al líder · `71` tendencias de ML · `73` pausas e infracciones · `74` cómo apelar ·
`83` precio con margen · `103` Full · `125` el termómetro · `133` cancelaciones ·
`136` exclusión de reclamos · `150` ACOS sano · `154` quiebre de stock y pauta · `163` Hot Sale
