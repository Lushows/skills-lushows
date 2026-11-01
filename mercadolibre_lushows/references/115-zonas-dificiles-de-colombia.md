# Zonas difíciles de Colombia

Hay destinos donde el paquete tarda el doble, la cobertura es parcial o la entrega falla más. Eso
no cambia tu tarifa —la tabla oficial de `100` es por peso y precio, no por destino— pero sí
cambia tu tasa de reclamos y de entregas fallidas.

## La honestidad primero

> ⚠️ **Sin verificar para Colombia (sep-2026).** **No tengo la lista oficial de zonas de cobertura
> limitada ni los tiempos de entrega por municipio.** Mercado Libre no publica una tabla de destinos
> difíciles, y cualquier lista que encuentres en un blog es de una transportadora particular o está
> desactualizada.
>
> Cómo consultarlo de verdad:
> - El calculador de envíos de la publicación, poniendo códigos postales o ciudades concretas
> - `GET /shipments/$SHIPMENT_ID` sobre envíos reales a ese destino: trae la promesa y el estado
> - Tus propios datos: el historial de entregas ya realizadas es la fuente más confiable que tienes
> - El mapa de cobertura de la transportadora que te asigna ML, si lo publica

Lo que sigue es **método para construir tu propio mapa**, no una lista que puedas copiar.

## Construye tu mapa con tus datos

Nadie tiene mejor información sobre tus destinos difíciles que tu propio historial:

```
□ Exporta tus ventas de los últimos 6 meses con ciudad de destino
□ Marca cuáles terminaron en reclamo, demora de entrega o entrega fallida
□ Agrupa por departamento y por ciudad
□ Calcula, por destino: % de reclamos, % de entregas fallidas, días promedio de entrega
□ Con 10 o más envíos a un destino, el número ya te dice algo
□ Marca en rojo los destinos con tasa de problema del doble de tu promedio
```

Ese cuadro, actualizado cada trimestre, es tu mapa real. Vale más que cualquier lista genérica.

| Métrica por destino | Bandera |
|---|---|
| Días de entrega | Más del doble de tu promedio nacional |
| Tasa de entrega fallida | Más del doble de tu promedio (`119`) |
| Tasa de reclamos | Acércate al 3,5% y ya es problema (`126`) |
| Volumen | Con menos de 10 envíos, no saques conclusiones |

## El patrón geográfico que sí es razonable esperar

Sin datos oficiales, la logística colombiana tiene una lógica conocida que puedes usar como
hipótesis a verificar, **no como hecho**:

| Tipo de destino | Expectativa razonable |
|---|---|
| Bogotá, Medellín, Cali, Barranquilla, Bucaramanga | Cobertura completa, tiempos cortos |
| Capitales intermedias | Cobertura buena, un día o dos más |
| Municipios pequeños de la zona andina | Cobertura vía agencia, tiempos variables |
| Costa Pacífica, Amazonía, Orinoquía, archipiélago | Cobertura limitada, tiempos largos |
| Zonas con acceso solo fluvial o aéreo | Puede no haber cobertura terrestre |

Trátalo como hipótesis y **verifícalo con tus envíos reales**, no con esta tabla.

## Cómo afecta tu promesa

La promesa de entrega la calcula ML, no tú. Lo que tú controlas es el **tiempo de preparación**, y
ese es el mismo para todos los destinos. Por eso el destino difícil no te genera "envíos
incorrectos" si despachaste a tiempo: la demora del transporte es **excluible** siempre que tú
hayas cumplido (oficial ML Colombia, verificado sep-2026).

| Quién se demoró | ¿Cuenta contra ti? |
|---|---|
| Tú, al despachar | **Sí**, envío incorrecto y reclamo no excluible |
| La transportadora, hacia un destino lejano | **No**, si despachaste a tiempo: es excluible |

Pero la exclusión **hay que pedirla**, y solo puedes pedirla si respondiste los mensajes en menos
de 24 horas hábiles (oficial). En destinos difíciles esa disciplina vale doble.

## Lo que sí puedes hacer

```
□ Guarda siempre evidencia de despacho a tiempo: es tu defensa en destinos lentos
□ Escribe al comprador de destino lejano ANTES de que pregunte, con el número de rastreo
□ Responde en menos de 24 horas hábiles, sin excepción
□ En la descripción, nada de prometer tiempos: la promesa la pone ML y tú no la controlas
□ Si un destino te da una tasa de problemas altísima, evalúa si conviene seguir vendiendo allá
□ En productos frágiles, refuerza el embalaje para rutas largas (`111`, `117`)
```

El penúltimo punto es incómodo pero real: hay destinos donde tu tasa de reclamos puede no valer el
volumen. Revisa el número antes de decidir por sentimiento.

## El riesgo de la entrega fallida

En zonas con direcciones poco estandarizadas, la entrega fallida es más frecuente. Cada una cuesta
tiempo, a veces un reenvío, y puede terminar en cancelación —y **canceladas por ti** tiene un
techo de apenas **2,5% a 60 días** para conservar el verde (oficial). Detalle en `119`.

## El error clásico

Asumir que "no hay cobertura" cuando en realidad hay cobertura lenta, y perder ventas por miedo. O
el opuesto: vender a cualquier destino sin mirar nunca la tasa de problemas por región, y
descubrir a los seis meses que el 30% de los reclamos vienen del 5% de las ventas.

**No adivines el mapa: constrúyelo con tus propios envíos, y revísalo cada trimestre.**

## Relacionados

`100` tarifas oficiales de envío · `112` el tiempo que prometes · `113` la demora y su costo ·
`117` frágiles · `118` el paquete perdido · `119` entrega fallida · `124` auditoría mensual ·
`126` las tres métricas · `136` reclamos excluibles · `111` embalaje que evita reclamos
