# Modalidades de envío en Colombia

Las modalidades son las formas en que el paquete pasa de tus manos al comprador. La tarifa oficial
de `100` es la misma para Full, Colecta, Agencias y Correo: **lo que cambia entre modalidades no
es la tarifa, es la velocidad, el control y quién asume el error.**

## Tabla comparativa

| Modalidad | Dónde vive tu stock | Quién entrega | Velocidad | Quién asume el error |
|---|---|---|---|---|
| **Full** | Bodega de ML | ML, punta a punta | **Al día siguiente** (oficial) | ML, ya recibido |
| **Flex** | Tu bodega | Tú mismo | Mismo día, **antes de las 21 hs** (oficial) | Tú |
| **Colecta** | Tu bodega | Transportadora recoge donde estás | Media | Compartido |
| **Agencias / puntos** | Tu bodega | Tú llevas el paquete al punto | Media | Tú hasta el punto |
| **Correo** | Tu bodega | Red postal | La más lenta | Tú hasta la imposición |
| **Logística propia** | Tu bodega | Tu transportadora, tu guía | La que tú logres | Tú, todo |

(Las dos promesas marcadas como oficiales son de ML Colombia, verificado sep-2026.)

> ⚠️ **Sin verificar para Colombia (sep-2026).** La disponibilidad exacta de cada modalidad por
> ciudad y por tipo de cuenta no está publicada. Verifica cuáles tienes activas en
> Panel → Ventas → Envíos → Configuración de envíos. Dos vendedores de la misma ciudad pueden ver
> menús distintos.

## Lo que sí cambia la tarifa: tu reputación

Ninguna modalidad te sube o baja la tarifa base. Lo que la mueve es tu color:

| Reputación | Descuento | 1 kg, producto de más de $60.000 |
|---|---|---|
| Verde, MercadoLíder o **sin reputación** | 50% | **$8.200** |
| Amarilla | 40% | **$10.200** |
| Naranja o roja | Ninguno | **$16.400** |

(Oficial ML Colombia, verificado sep-2026. Tablas completas en `100`.)

**Perder el verde te cuesta $8.200 por cada venta de más de $60.000.** Eso no es una penalización
de imagen: es una línea en tu estado de resultados. Los umbrales para conservarlo están en `126`.

## Qué significa cada una en la práctica

**Full.** Le mandas inventario por adelantado; ML empaca y despacha. Beneficios oficiales: **50%
de descuento en envío gratis desde $60.000 y entrega al día siguiente**. Requiere reputación (se
activa a las 10 primeras ventas), productos aptos y dentro de dimensiones permitidas, está sujeto
a disponibilidad de espacio, y **el traslado a bodega corre por tu cuenta** (todo oficial ML
Colombia, verificado sep-2026). Detalle en `103`, decisión en `105`.

**Flex.** Tú entregas el mismo día con tu propia logística, y la entrega debe completarse **antes
de las 21 hs** (oficial). Es la única forma de competir en velocidad con Full sin ceder
inventario. Detalle en `102`.

**Colecta.** La transportadora pasa por tu bodega en una ventana horaria. Conviene con volumen.

**Agencias / puntos de despacho.** Tú llevas los paquetes. Es la entrada del vendedor que despacha
poco. El cálculo de cuándo pasar a colecta está en `104`.

**Logística propia.** Conserva el costo, pierde la posición. Tabla honesta en `122`.

## Cómo saber cuál tienes activa, sin adivinar

```
□ Panel → Ventas → Envíos → Configuración: lista las modalidades habilitadas
□ Crear una publicación de prueba: el selector solo muestra lo que puedes usar
□ Sobre un envío real: GET /shipments/$SHIPMENT_ID → modalidad asignada
□ Si Full no aparece: puede ser falta de reputación (10 ventas), producto no apto,
  dimensiones fuera de rango, o falta de espacio en el centro de distribución
```

Esa última línea es oficial y explica el caso más frustrante: **puedes cumplir todos los
requisitos y aun así no poder entrar a Full, porque no hay espacio.** No es un error tuyo.

## La decisión en tres preguntas

| Pregunta | Si la respuesta es sí |
|---|---|
| ¿Mi producto rota rápido y es pequeño? | Full es el candidato natural (`105`) |
| ¿Puedo entregar yo mismo antes de las 21 hs? | Flex da velocidad sin ceder inventario (`102`) |
| ¿Despacho menos de 4 paquetes al día? | Agencia o punto, y sube a colecta después (`104`) |

Nadie elige una sola. Lo normal en un catálogo maduro: alta rotación en Full, el resto desde tu
bodega.

## Riesgo de reputación por modalidad

"Envíos incorrectos" —despacho con demora o desde depósito incorrecto— es una de las tres
variables base del termómetro. Para conservar el verde no debes superar **12% a 60 días** (o
**15,5%** si te miden a 365 días por tener menos de 60 ventas), y **10%** si eres MercadoLíder
(oficial ML Colombia, verificado sep-2026).

| Modalidad | Riesgo de envío incorrecto |
|---|---|
| Full | Bajo una vez el stock está en bodega; el riesgo se mueve al ingreso (`106`) |
| Flex | Alto: si no entregas antes de las 21 hs, es tuyo |
| Colecta | Medio: el paquete tiene que estar listo cuando pasa el camión |
| Agencia / punto | Medio: depende de tu disciplina diaria (`114`) |

## El error clásico

Mandar todo el catálogo a Full "para simplificar". La modalidad se elige **por SKU**, no por
cuenta. El producto que vende tres unidades al mes en Full paga bodegaje todos los días y, a los
cuatro meses, entra al cargo por stock antiguo: **$690 por unidad si es pequeño, $3.600 si es
grande** (oficial ML Colombia, verificado sep-2026). Ver `108`.

**La modalidad es una decisión por producto, no por cuenta.**

## Relacionados

`100` cómo funciona y las tarifas · `102` Flex · `103` Full · `104` colecta y puntos · `105`
cuándo conviene Full · `108` inventario viejo · `114` el flujo diario · `115` zonas difíciles ·
`122` logística propia · `124` auditoría mensual · `126` las tres métricas · `63` ganar el
catálogo
