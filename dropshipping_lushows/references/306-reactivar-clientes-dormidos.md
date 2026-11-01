# Reactivar clientes dormidos

> **15,4% de los suscriptores que cancelan reactivan dentro de los 30 días siguientes** (red Recurly,
> jul-2026). Ese número dice dos cosas: la primera, que irse no siempre es definitivo. La segunda, y
> más importante, que **la ventana es corta**. El que no volvió en 30 días casi nunca vuelve solo.

## Qué es un dormido y qué no

| Estado | Definición | Tratamiento |
|---|---|---|
| Activo | compró dentro de su ciclo esperado | `305`, `308` |
| **En riesgo** | pasó 1,3× su ciclo esperado sin comprar | aún es recuperable barato |
| **Dormido** | pasó 2× su ciclo esperado | campaña de reactivación |
| **Perdido** | pasó 3× el ciclo, sin abrir nada en 90 días | supresión (ver abajo) |
| Cancelado reciente (suscripción) | canceló hace <30 días | **la ventana del 15,4%** |

El ciclo esperado no es un número redondo: sale de la mediana de días entre compra 1 y 2 de tus
cohortes (`302`, `308`). Para un consumible de 30 días, dormido ≈ día 60.

## Segmentación: no todos los dormidos valen lo mismo

| Segmento | Señal | Prioridad | Oferta |
|---|---|---|---|
| Compró 2+ veces y se detuvo | ya probó que le funciona | **máxima** | preguntar qué pasó, oferta suave |
| Canceló suscripción hace <30 días | el 15,4% | **máxima** | reactivación sin penalización, mismo precio de antes |
| Canceló por fallo de pago no resuelto | dunning agotado (`304`) | alta | link de actualización, no oferta |
| Compró 1 vez, ticket alto, abre correos | interés vivo | media | pack + razón para volver |
| Compró 1 vez con cupón agresivo | cazador de descuento | baja | no gastes esfuerzo |
| Nunca abrió un correo en 120 días | muerto | nula | suprimir |

**El error común es tratar a todos igual con un cupón del 20%.** Eso convierte a tus mejores
clientes (que hubieran vuelto a precio lleno) en compradores de descuento, y no mueve a los muertos.

## La secuencia de reactivación

| Paso | Cuándo | Canal | Mensaje | Sin oferta / con oferta |
|---|---|---|---|---|
| 1 | día 0 de "dormido" | WhatsApp | "¿te sirvió [producto]?" pregunta directa, 2 líneas | **sin oferta** |
| 2 | +4 días | email | contenido útil + resultado de otro cliente | sin oferta |
| 3 | +9 días | email | "te guardamos tu pack" + beneficio concreto | **con oferta** |
| 4 | +16 días | WhatsApp | última, corta, con link de 1 clic | con oferta |
| 5 | +30 días | email | "¿te bajamos la frecuencia o te sacamos de la lista?" | opción de salida |

La pregunta del paso 1 hace dos trabajos: reactiva a algunos y te dice **por qué** se fueron los
demás. Esa información vale más que la venta. Si 6 de 10 respuestas dicen "no vi resultados", tu
problema no es de retención: es de producto o de promesa del anuncio (`105`, `285`).

## Para cancelaciones de suscripción: la ventana de 30 días

| Día desde la cancelación | Acción |
|---|---|
| 0 | confirmar la cancelación sin fricción, agradecer, preguntar el motivo con **una** opción de un clic |
| 1-3 | si el motivo fue precio → ofrecer frecuencia más larga (cada 60 días en vez de 30), no descuento |
| 7 | si el motivo fue "tengo mucho producto" → ofrecer **pausa**, no reactivación |
| 14 | recordatorio con el beneficio concreto que perdió |
| 25-28 | **última antes de que se cierre la ventana**: reactivar al mismo precio que tenía |
| >45 | pasa a la lista de dormidos general |

| Motivo declarado | Respuesta correcta | Respuesta incorrecta |
|---|---|---|
| "Muy caro" | frecuencia más larga | descuento permanente |
| "Tengo de sobra" | pausa 60 días | insistir |
| "No me funcionó" | preguntar cómo lo usó; guía; **no vender** | cupón |
| "Problema de envío" | resolver el envío primero | cupón |
| Sin motivo | secuencia estándar | tres correos seguidos |

## Cuándo rendirse

| Criterio de supresión | Umbral |
|---|---|
| Sin abrir ningún correo | **120 días** |
| Sin compra | 3× el ciclo esperado y sin apertura |
| Rebote duro de email | inmediato |
| Pidió no recibir más | inmediato y para siempre |
| Reportó spam | inmediato, y revisa tu frecuencia |

Suprimir no es perder: **mantener muertos en la lista degrada tu entregabilidad** y hace que tus
correos a clientes vivos caigan en promociones o spam. Una lista de 3.000 activos entrega mejor que
una de 12.000 con 9.000 zombis. Ver `272` y `286`.

Regla práctica: si la tasa de apertura de una campaña de reactivación baja de ~8-10%, el segmento ya
no existe. **Verificar con tus propios números**, porque las métricas de apertura de 2026 están
distorsionadas por la protección de privacidad de los clientes de correo.

## Cuánto vale reactivar vs adquirir

| | Cliente nuevo | Dormido reactivado |
|---|---|---|
| Costo | CAC USD 10,54 | ~0 (secuencia automatizada) |
| Margen de esa venta | 15,93 | **26,47** |
| Probabilidad de conversión | tasa de conversión de la página | típicamente mayor: ya te compró |
| Techo de gasto razonable | 26,47 | puedes gastar hasta ~10 USD por reactivación y seguir ganando más que con un nuevo |

Traducción operativa: **si una campaña de reactivación te cuesta menos de USD 10 por cliente
recuperado, es mejor negocio que la pauta.** Casi siempre cuesta menos de 1.

## Tabla de métricas

| Métrica | Fórmula | Referencia |
|---|---|---|
| Tasa de reactivación a 30 días | reactivados ÷ dormidos contactados | **15,4%** (suscripción, red madura) |
| Tasa de reactivación de compra única | igual | típicamente más baja; **verificar** |
| Costo por reactivación | costo de la campaña ÷ reactivados | meta <USD 2 |
| Margen recuperado | reactivados × 26,47 | lo que reportas |
| % de la lista en estado dormido | dormidos ÷ total clientes | si supera 60%, el problema está en `305`, no aquí |

Esa última fila es la trampa del módulo: **si la mitad de tu base está dormida, no necesitas mejores
campañas de reactivación, necesitas arreglar la segunda compra.** Reactivar es curativo; `305` y
`308` son preventivos, y siempre rinden más.

## Aplicación al proyecto México

| Qué | Decisión |
|---|---|
| Primera campaña de reactivación | enero 2027, sobre los compradores de nov-dic 2026 |
| Segmento prioritario | los del Buen Fin que compraron pack simple (no triple) |
| Canal | WhatsApp primero, email de respaldo |
| Oferta | pack doble con envío incluido; **sin claims terapéuticos** (COFEPRIS) |
| Supresión | limpiar la lista antes de la temporada siguiente |

Para la mecánica de la conversación de reactivación uno a uno (objeciones, cierre por WhatsApp),
rutea a `ventas_lushows`. Este módulo define a quién escribir y cuándo; esa skill define qué decir
cuando contestan.

## Relacionados
`105` · `272` · `285` · `286` · `300` · `301` · `302` · `304` · `305` · `307` · `308`
