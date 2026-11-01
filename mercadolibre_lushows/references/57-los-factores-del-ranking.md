# Los factores del ranking

Mercado Libre **no publica** los pesos de su algoritmo, y reconoce que no es estático: ajusta por
categoría, contexto y época del año. Lo que sí es consistente son los pilares. Este módulo te da
los pilares y te enseña a desconfiar de cualquiera que te venda porcentajes.

## La advertencia que va primero

**Si alguien te dice "la conversión pesa 40% y la reputación 25%", te lo está inventando.** Esos
números no existen en ninguna fuente oficial. Circulan en blogs de agencias que se copian entre
sí. Lo único verificado es que ML **no** publica la fórmula (oficial: la ausencia de fórmula
pública es el hecho, verificado sep-2026).

Lo que sí puedes hacer es trabajar los pilares y medir el efecto en tu propio caso.

## Los cinco pilares consistentes

| Pilar | Qué mira | Módulo |
|---|---|---|
| **Conversión** | Cuántas de las visitas que recibes terminan en venta | `58` |
| **Reputación** | Color del termómetro, reclamos, cancelaciones | `66`, `125` |
| **Precio / competitividad** | Tu precio final frente al de la misma categoría | `68` |
| **Calidad de ficha** | Atributos, fotos, video, indicador 0-100 | `40`, `42`, `48` |
| **Logística** | Full/Flex, tiempo de entrega prometido, envío gratis | `67`, `103` |

De estos cinco, el más pesado es la **tasa de conversión** (confianza media, sin cifra oficial).
No es una opinión suelta: todos los demás pilares terminan afectando la conversión, así que el
algoritmo puede usarla como resumen de todo.

**La conversión no es un factor más: es el examen final del que los otros cuatro son la
preparación.**

## Señales secundarias que también pesan

| Señal | Efecto |
|---|---|
| Stock disponible | Stock cero te saca de la competencia (ver `61`) |
| Antigüedad y ventas de la publicación | Historial acumulado; se pierde al republicar (ver `60`) |
| Estar en catálogo | Las publicaciones de catálogo aparecen más arriba que las libres equivalentes |
| Cuotas sin interés | No existen en publicación Gratuita; pesan en catálogo y en la decisión |
| Mercado Ads | Los clics pagados aceleran el aprendizaje y retroalimentan el orgánico (`145`) |
| Preguntas respondidas | Señal de servicio; además evita perder la venta |
| Personalización por usuario | Historial, ciudad, Meli+ del comprador que busca |

Sobre Mercado Ads: una publicación puede aparecer **dos veces** en la misma página, como anuncio
pagado y como resultado orgánico. Eso no es trampa, es cómo funciona.

## Los pesos cambian por categoría

Se dice — sin fuente oficial — que en electrónica pesa más el precio, en hogar la ficha y en moda
la velocidad de envío. Trátalo como una hipótesis razonable, no como dato:

> ⚠️ **Sin verificar (sep-2026).** La variación de pesos por categoría circula en fuentes
> especializadas pero ML no la confirma. Úsala para decidir dónde poner tu esfuerzo primero, no
> para justificar una estrategia entera.

La forma honesta de averiguarlo en tu categoría es mirar quiénes están arriba y qué tienen en
común (ver `70`).

## Lo que NO es factor de ranking

| Mito | Realidad |
|---|---|
| "Pagar Mercado Ads te sube el orgánico directamente" | Acelera el aprendizaje vía ventas y conversión, no hay compra directa de posición |
| "Tener muchas publicaciones te da autoridad de cuenta" | No hay evidencia; publicaciones malas te bajan la conversión promedio |
| "Editar la publicación todos los días la refresca" | No; editar el precio bruscamente puede pausarla (ver `73`) |
| "Tu web o tus redes suman" | El ranking interno no ve nada fuera de ML |
| "Poner más palabras clave en la descripción" | Casi no pesa, y menos con buscador semántico (`56`) |

## El orden en que debes trabajarlos

No trabajes los cinco a la vez. Este es el orden por retorno:

```
1. Reputación → si estás en naranja o rojo, nada de lo demás funciona (`66`)
2. Ficha      → atributos y fotos completos ANTES de publicar (`59`)
3. Logística  → Full o tiempos rápidos, es la palanca más visible (`67`)
4. Precio     → ajústalo con el margen calculado, no a ciegas (`68`, `83`)
5. Conversión → es el resultado de los cuatro anteriores, no se ataca directo (`58`)
```

Intentar "subir la conversión" sin arreglar los otros cuatro es como querer subir la nota sin
estudiar.

## El error clásico

Buscar el truco. El vendedor promedio pasa semanas buscando el hack del algoritmo y no llena los
atributos de su propia publicación. Los pilares son aburridos y públicos: ficha completa, buen
precio, entrega rápida, reputación limpia. El truco es hacerlos todos, no encontrar el que falta.

## Checklist de auditoría de ranking

```
□ Mi reputación está en verde o verde claro
□ El indicador de calidad de la ficha dice "Profesional"
□ Todos los atributos con tags.required están llenos
□ Tengo al menos 4 fotos y, si la categoría lo permite, video
□ Mi precio final (con envío) está dentro del rango de los 3 primeros
□ Uso Full o prometo un tiempo de entrega competitivo
□ Nunca he tenido stock cero en esta publicación
□ Si la categoría tiene catálogo, estoy compitiendo en él
```

## Relacionados

`40` atributos · `42` fotos · `48` indicador de calidad · `55` cómo funciona el buscador ·
`56` buscador con IA · `58` la conversión manda · `59` primeras 72 horas · `61` stock cero ·
`66` reputación como filtro · `67` envío y posición · `68` precio como factor ·
`70` espiar al líder · `72` por qué cayó mi publicación · `145` Mercado Ads
