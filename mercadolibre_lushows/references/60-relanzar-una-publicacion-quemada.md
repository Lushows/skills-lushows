# Relanzar una publicación quemada

Ya pasó: publicaste sin la ficha lista, el algoritmo te midió mal y ahora la publicación no
levanta. Hay dos caminos — arreglar y esperar, o republicar desde cero — y ninguno es gratis. Este
módulo te da la tabla de decisión honesta, incluida la parte que las agencias no cuentan:
republicar te hace perder historial y opiniones.

## Primero: confirma que está quemada

Antes de decidir nada, descarta las otras causas de caída. La mitad de las publicaciones que la
gente cree "quemadas" tienen stock en cero, perdieron el catálogo o están pausadas. Corre el árbol
de diagnóstico de `72` **antes** de seguir leyendo.

Está quemada si, y solo si:

```
□ La publicación está activa, con stock y sin infracciones
□ Recibe visitas (pocas, pero recibe) y casi no vende
□ La ficha ya está arreglada hace más de 3 semanas y no mejora
□ Publicaciones tuyas equivalentes y más nuevas la superan
□ No perdiste el catálogo ni cayó tu reputación en ese periodo
```

## La tabla de decisión

| Situación | Veredicto |
|---|---|
| Tiene ventas y opiniones acumuladas | **Arreglar y esperar.** El historial vale más que el reinicio |
| Cero ventas, menos de 30 días, ficha ahora completa | **Arreglar y esperar** 3-4 semanas antes de decidir |
| Cero ventas, más de 60 días, ficha ya arreglada, sigue plana | **Republicar** |
| El problema era la categoría equivocada | **Republicar** (cambiar categoría rara vez se recupera) |
| El problema era el título y ya lo corregiste | Arreglar; el título sí se puede editar |
| Tiene opiniones negativas visibles | **Arreglar el producto primero.** Republicar no borra el problema real |
| Es una publicación de catálogo y perdiste la posición | Ni una ni otra: ataca las variables de `63` |
| Tiene muchas preguntas sin responder | Arreglar. Responde todo antes de cualquier decisión |

**Republicar no es un botón de reset: es empezar de cero pagando con lo que ya habías construido.**

## Qué pierdes al republicar

| Qué se pierde | Qué tan grave |
|---|---|
| Historial de ventas de la publicación | Grave: es parte de la señal de conversión |
| **Opiniones y calificaciones del producto** | Muy grave si tenías buenas: es prueba social |
| Preguntas y respuestas acumuladas | Medio: eran contenido útil y señal de servicio |
| Posición ganada en catálogo | Grave si venías ganando (ver `63`) |
| Antigüedad | Bajo, pero real |
| Enlaces que hayas compartido | El link viejo queda muerto |

Lo que **no** pierdes: tu reputación de vendedor (es de la cuenta, no de la publicación), tu nivel
MercadoLíder y tu historial de cuenta.

## Ruta A: arreglar y esperar

```
SEMANA 0
□ Corre el diagnóstico de `72` y descarta causas externas
□ Completa el 100% de los atributos, no solo los obligatorios (`40`)
□ Reemplaza la foto 1 por una con fondo blanco puro y 1200×1200 px (`42`)
□ Sube el resto de fotos a 4 o más; agrega video si puedes
□ Reescribe la descripción resolviendo las dudas reales de las preguntas (`45`)
□ Recalcula el precio con la comisión real y ajústalo (`80`, `83`)
□ Activa cuotas con 0% interés si las necesitas; las extra cuestan +3 pp (`78`)
□ Verifica que el indicador de calidad llegue a "Profesional" (`48`)

SEMANAS 1-4
□ NO toques nada más. Cada edición reinicia la lectura
□ Responde preguntas en menos de 1 hora
□ Mide visitas y ventas cada semana, misma hora, misma métrica
□ Si a la semana 4 la conversión no se movió, pasa a la Ruta B
```

Un empujón legítimo durante esta ventana: Mercado Ads con presupuesto chico y estrategia
Rentabilidad (ACOS 5%-15%, oficial ML Colombia verificado sep-2026). El clic pagado viene de gente
que ya busca comprar, y esas ventas sí alimentan la conversión. Ver `150`.

## Ruta B: republicar desde cero

```
ANTES de crear la nueva
□ Pasa el checklist completo de "listo para publicar" de `59`
□ Guarda captura de las opiniones viejas (las vas a perder)
□ Ten stock real para 3 semanas
□ Decide si vas a catálogo o publicación propia (`64`)

AL CREAR
□ Categoría confirmada con el predictor (`41`)
□ Título distinto y mejor, no copiado del viejo
□ Fotos nuevas o reeditadas, no las mismas que no convertían
□ Precio ya competitivo desde el minuto cero

DESPUÉS
□ Deja la vieja activa unos días con stock bajo, o pásala a pausada
□ NO la elimines de inmediato si tenía opiniones útiles: puede seguir vendiendo algo
□ Protocolo de 3 días de `59` a rajatabla
```

## Lo que NO funciona

| Idea | Por qué no |
|---|---|
| Republicar la misma ficha idéntica | Mismo producto, misma ficha, mismo resultado |
| Publicar 5 copias para "ver cuál pega" | Publicaciones duplicadas: riesgo de pausa (`73`) |
| Bajar el precio al costo para "reactivar" | Vendes a pérdida y después no puedes subirlo sin matar la conversión |
| Cambiar el título cada tres días | Reinicias la lectura sin darle tiempo a medir |
| Borrar y volver a publicar el mismo día | Pierdes todo y no arreglaste nada |

## El caso especial de la categoría equivocada

Si publicaste en la categoría incorrecta, ML permite cambiarla solo dentro de ciertos límites, y
el cambio arrastra el historial malo a la categoría nueva. En este caso **republicar suele ser lo
correcto**: el problema no era tu ficha, era que estabas compitiendo en otra pista. Confirma la
categoría con el predictor antes:
`GET https://api.mercadolibre.com/sites/MCO/domain_discovery/search?q=TU+PRODUCTO&limit=3`

## El error clásico

Republicar antes de arreglar. El vendedor ve que no vende, borra, vuelve a publicar la misma ficha
mediocre, y repite el ciclo tres veces. Al final tiene tres publicaciones quemadas, cero opiniones
acumuladas y la misma ficha de siempre. **Arregla primero, decide después.**

## Relacionados

`40` atributos · `41` criterios de categoría · `42` fotos · `45` descripción ·
`48` indicador de calidad · `57` factores del ranking · `58` la conversión manda ·
`59` primeras 72 horas · `61` stock cero · `63` ganar el catálogo ·
`64` cuándo no competir en catálogo · `72` por qué cayó mi publicación ·
`73` pausas e infracciones · `78` tipos de publicación · `80` comisión real · `150` ACOS sano
