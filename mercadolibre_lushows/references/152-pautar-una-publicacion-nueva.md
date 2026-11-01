# Pautar una publicación nueva

El caso más delicado: encender pauta sobre una publicación que todavía no tiene historia. Bien
hecho, arranca la curva de aprendizaje del algoritmo. Mal hecho, quema la publicación y el dinero
al mismo tiempo.

## Por qué tiene sentido

Mercado Libre evalúa una publicación nueva en sus **primeras 48-72 horas** y las primeras visitas
fijan su etiqueta de conversión, difícil de revertir después (`59`). El problema del que empieza es
que **no le llegan visitas**: sin historial no hay posición, y sin posición no hay visitas con las
que construir historial.

Product Ads rompe ese círculo: compras las primeras visitas. Si la ficha convierte, el algoritmo
registra conversión real y te empieza a dar posición orgánica (`153`).

| Situación de la categoría | ¿Pautar la publicación nueva? |
|---|---|
| Muy competitiva, decenas de vendedores con historial | **Sí.** Sin pauta no vas a recibir visitas en semanas |
| Producto de nicho, poca competencia | No hace falta. El orgánico te va a encontrar |
| Producto de temporada con fecha fija | Sí, y agresivo: el tiempo no se recupera (`162`) |
| Estás probando si el producto vende | No. Primero valida con poco stock y orgánico |
| Producto en catálogo donde no eres el ganador | Sí, pero primero pelea el catálogo (`63`) |

## Los tres requisitos previos innegociables

Si falta uno solo, no enciendas nada.

| Requisito | Por qué es innegociable |
|---|---|
| **1. Stock real** | Quedarte sin stock apaga los anuncios, reinicia el aprendizaje y encarece la pauta futura sobre esa publicación (`61`, `147`) |
| **2. Precio final** | Cambiar el precio durante la prueba invalida los 14 días de atribución (`151`) y un cambio brusco puede pausarte la publicación (`73`) |
| **3. Margen suficiente** | Un margen por debajo del 15% no aguanta ni el piso de la estrategia Rentabilidad (`150`, `154`) |

**Stock real, precio final, margen suficiente. Sin los tres, pautar es prender fuego a los
billetes con estilo.**

## Lo que debe estar listo ANTES del primer clic

El anuncio es tu ficha (`146`). Pagar visitas hacia una ficha a medias es pagar por que te vean
mal:

```
□ Título con producto, marca, modelo y característica principal (`28`)
□ TODOS los atributos obligatorios llenos (`40`)
□ Foto principal sobre blanco puro #FFFFFF, 1200×1200 px mínimo (`42`)
□ Al menos 4 fotos; video si la categoría lo permite
□ Descripción completa, sin datos de contacto
□ Indicador de calidad en "Profesional", o lo más cerca posible (`48`)
□ Envío configurado: Full o tiempo de entrega competitivo (`103`, `112`)
□ Stock para al menos 30 días al ritmo esperado
□ Margen neto calculado con `82` y ACOS objetivo fijado (`150`)
```

Cuesta menos demorarte un día armando la ficha que un mes intentando recuperar una publicación
etiquetada como de baja conversión.

## El plan de las primeras cuatro semanas

| Semana | Qué haces | Qué NO haces |
|---|---|---|
| **0** (antes) | Completar ficha, calcular margen, fijar ACOS objetivo | Publicar a medias "para ir arrancando" |
| **1-2** | Encender con estrategia Rentabilidad y presupuesto chico. Vigilar solo stock y preguntas | Mirar el ACOS. No está cerrado (`151`) |
| **3** | Primera lectura real, descartando los últimos 3 días (`155`) | Cambiar dos cosas a la vez |
| **4** | Un solo ajuste: presupuesto ±20-30% o cambio de estrategia | Apagar por impaciencia |

Si la categoría es muy disputada y el producto es un lanzamiento con fecha, **Crecimiento** o
incluso **Visibilidad** durante 14-21 días es defendible — con fecha de apagado escrita de
antemano y solo si el margen lo aguanta (`148`).

## Cómo saber si funcionó

No mires solo el ACOS. En una publicación nueva lo que estás comprando es **aprendizaje**:

| Señal a los 14-21 días | Lectura |
|---|---|
| Hay clics y hay ventas, ACOS dentro del objetivo | Funcionó. Sube presupuesto 20-30% |
| Hay clics y no hay ventas | La ficha o el precio no convierten. **Apaga y arregla** (`164`) |
| Casi no hay clics | Tu ficha no compite: foto, título o precio (`68`, `42`) |
| Hay ventas y el orgánico también empezó a moverse | El objetivo se cumplió (`153`) |
| Ventas solo pautadas, orgánico plano | La pauta es muleta, no motor. Revisa `149` (TACOS) |

La segunda fila es la más valiosa y la que más se ignora: **clics sin ventas no es un problema de
pauta, es un diagnóstico gratis de que tu ficha no convence.**

## El error clásico

Publicar y encender la pauta el mismo minuto, con la ficha a medio llenar, "porque después la
completo". Las primeras visitas — las que fijan la etiqueta de conversión — llegan a la peor
versión de tu publicación. Después completas la ficha y no pasa nada, porque el algoritmo ya midió.
**La ventana de las primeras 72 horas se abre una sola vez por publicación.**

## Checklist de encendido

```
□ La ficha está completa y en calidad "Profesional" (`48`)
□ Tengo stock para 30 días y lo verifiqué físicamente, no en el sistema
□ El precio es el definitivo: no lo voy a mover en 14 días
□ Ejecuté `scripts/margen_ml.py` y el margen neto supera el 15% (`82`)
□ Elegí estrategia según el árbol de `148`
□ Leí el presupuesto mínimo diario en el panel (no está publicado, ver `147`)
□ Escribí en el calendario la fecha de la primera lectura: hoy + 14 días
□ Si elegí Visibilidad, escribí también la fecha de apagado
```

## Relacionados

`145` qué es Mercado Ads · `146` Product Ads · `147` la subasta y el CPC ·
`148` las tres estrategias · `150` el ACOS sano según tu margen ·
`151` la ventana de atribución · `153` el efecto sobre lo orgánico · `155` leer los reportes ·
`156` optimizar semana a semana · `162` preparar una fecha caliente ·
`164` cuándo no es la respuesta · `28` el título · `40` atributos · `42` fotos ·
`48` indicador de calidad · `59` las primeras 72 horas · `61` stock cero ·
`63` ganar el catálogo · `68` precio como factor · `73` pausas · `82` la calculadora de margen ·
`103` Full · `112` el tiempo que prometes
