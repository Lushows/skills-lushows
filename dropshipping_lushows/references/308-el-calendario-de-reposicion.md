# El calendario de reposición

> Tu cliente no decide cuándo recomprar. **Lo decide el frasco.** Si sabes cuántos días dura tu
> producto y cuánto tarda tu envío, sabes exactamente el día en que ese cliente está a punto de
> quedarse sin nada. Escribirle ese día vale más que cualquier campaña.

## La fórmula

```
días_de_producto = unidades_por_envase ÷ (dosis_diaria × frecuencia_diaria)
día_de_aviso     = días_de_producto × factor_adherencia − días_de_entrega − colchón
```

| Variable | Qué es | Valor típico |
|---|---|---|
| `unidades_por_envase` | cápsulas, gomitas, ml, gramos | del empaque |
| `dosis_diaria × frecuencia` | lo que consume por día según la etiqueta | del empaque |
| `factor_adherencia` | nadie lo toma todos los días | **0,75-0,90** (usa 0,85 si no mides) |
| `días_de_entrega` | de que paga a que lo recibe | MX con stock local: 2-5 |
| `colchón` | margen para que decida sin presión | 3-5 días |

El factor de adherencia es la parte que casi nadie considera y la que más desajusta el calendario: un
frasco de 30 días con adherencia 0,85 dura **35 días reales**, no 30. Si escribes el día 25 estás
vendiendo 10 días antes de tiempo y el cliente te dice "todavía tengo".

## Ejemplos trabajados

| Producto | Envase | Dosis | Días teóricos | ×0,85 | −envío −colchón | **Día de aviso** |
|---|---|---|---|---|---|---|
| Gomitas de vitalidad | 60 gomitas | 2/día | 30 | 35 | −3 −4 | **día 28** |
| Cápsulas | 60 cáps | 1/día | 60 | 70 | −3 −4 | **día 63** |
| Kit capilar (shampoo + tónico) | 300 ml tónico | ~5 ml/día | 60 | 70 | −3 −5 | **día 62** |
| Crema facial 50 ml | 50 ml | ~0,8 ml/día | 62 | 73 | −3 −5 | **día 65** |
| Pack triple de gomitas | 180 gomitas | 2/día | 90 | 106 | −3 −5 | **día 98** |

Fíjate en la última fila: **el cliente del pack triple no es un mal cliente por no recomprar en 30
días.** Si mezclas packs y unidades en la misma tabla de cohortes (`302`), el pack te va a parecer
peor cuando en realidad ya te pagó tres meses por adelantado. Sepáralos siempre.

## Cómo calibrar con datos reales en vez de suponer

| Paso | Qué haces |
|---|---|
| 1 | Exporta los clientes con ≥2 compras del mismo SKU |
| 2 | Calcula días entre compra 1 y 2 para cada uno |
| 3 | Saca la **mediana**, no el promedio (un cliente que volvió a los 300 días te arruina el promedio) |
| 4 | Compara con tu cálculo teórico; el cociente real ÷ teórico es tu `factor_adherencia` observado |
| 5 | Recalibra el día de aviso y vuelve a medir a los 90 días |

Con 15-20 clientes de repetición ya tienes una mediana usable como orientación. Con 50 ya es un
número en el que puedes basar el calendario. Antes de eso, usa 0,85 y sigue.

## Los tres disparos

| Disparo | Cuándo (ejemplo de 30 días) | Canal | Contenido |
|---|---|---|---|
| **Aviso** | día 28 | WhatsApp | "según tu pedido del [fecha], se te acaba cerca del [fecha+7]. ¿Te mando otro?" + link 1 clic |
| **Recordatorio** | día 35 | email | fecha concreta + pack doble como opción principal |
| **Rescate** | día 45 | WhatsApp o email | "¿se te acabó?" + oferta final; después pasa a dormidos (`306`) |

Lo que hace que esto funcione no es la oferta: es la **fecha concreta y personal**. "Se te acaba
alrededor del 12 de octubre" convierte mucho más que "ya es hora de reponer", porque es verificable
y el cliente lo puede comprobar mirando el frasco.

## La tabla operativa que tienes que mantener

| Columna | Ejemplo |
|---|---|
| SKU | gomitas-60 |
| Unidades por envase | 60 |
| Dosis diaria | 2 |
| Días teóricos | 30 |
| Factor adherencia observado | 0,85 |
| Días de entrega | 3 |
| **Día de aviso** | 28 |
| Día de recordatorio | 35 |
| Día de rescate | 45 |
| Mediana real observada (compra 1→2) | actualizar mensual |

Una fila por SKU y por presentación. El pack doble y el triple son **filas distintas**, no el mismo
producto. Este es el archivo más rentable de tu operación y cabe en una hoja de cálculo.

## Cómo automatizarlo

| Nivel | Cómo | Cuándo |
|---|---|---|
| Manual | hoja con fecha de pedido + días; revisas lunes y miércoles | <50 pedidos/mes |
| Semiautomático | flujo de email con retraso de N días desde la compra, por SKU | 50-500 pedidos/mes |
| Automático | flujo con ramas por SKU y por presentación, WhatsApp + email | >500 |

Aun en el nivel manual, esto funciona. **No esperes a tener la herramienta perfecta.** Diez mensajes
de WhatsApp bien cronometrados por semana valen más que un flujo automatizado que lanzas en marzo.

## Errores que arruinan el calendario

| Error | Consecuencia |
|---|---|
| Contar desde la fecha de compra y no desde la **de entrega** | avisas 3-5 días antes de tiempo, siempre |
| Usar el mismo día para todos los SKU | el del pack triple recibe la oferta cuando le quedan 2 meses |
| Ignorar la adherencia | avisas 15% antes de tiempo; el cliente aprende a ignorarte |
| Usar promedio en vez de mediana | los outliers mandan |
| Mandar el aviso y el recordatorio con el mismo texto | se lee como spam |
| Vender un producto nuevo en el aviso de reposición | el aviso tiene un solo trabajo |

## Qué pasa cuando el producto NO se consume a ritmo fijo

| Caso | Qué hacer |
|---|---|
| Uso ocasional (no diario) | pregunta en el día 14 "¿cada cuánto lo usas?" y personaliza |
| Producto estacional | calendario por temporada, no por días |
| Producto compartido en casa | el envase dura la mitad; ajusta factor a 0,5-0,6 para ese segmento |
| Producto que no se acaba | no hay calendario; ve a `307` o a producto complementario |

## Aplicación al proyecto México

| SKU finalista | Cálculo preliminar | Día de aviso |
|---|---|---|
| Gomitas de vitalidad, 60 u, 2/día | 30 × 0,85 − 3 − 4 | **28** |
| Kit capilar, tónico 300 ml | 60 × 0,85 − 3 − 5 | **62** |
| Pack doble de gomitas | 60 × 0,85 − 3 − 5 | **58** |
| Pack triple de gomitas | 90 × 0,85 − 3 − 5 | **98** |

Estos números son preliminares: se calibran con la mediana real a partir de febrero de 2027. Dos
restricciones del nicho: el mensaje de reposición **no puede llevar claims terapéuticos** (COFEPRIS,
aplica también en mensajes privados) y el stock local tiene que aguantar el pico que tú mismo estás
generando — si avisas a 300 clientes el mismo día, necesitas inventario ese día (`234`).

## Relacionados
`234` · `272` · `285` · `300` · `301` · `302` · `303` · `305` · `306` · `309`
