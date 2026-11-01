# Mercado Pago: cuándo te liberan la plata

La venta se concreta hoy, el dinero es tuyo después. Ese "después" es lo que quiebra vendedores
que estaban vendiendo bien: crecer significa comprar inventario con plata que todavía no
tienes. Este módulo es sobre flujo de caja, no sobre contabilidad.

## La advertencia que manda sobre este módulo

> ⚠️ **Sin verificar para Colombia (sep-2026).** El plazo de liberación del dinero en Mercado
> Pago Colombia no se pudo confirmar en fuente oficial. El patrón que circula en la web
> (14 días corridos, bajando a ~5 días hábiles con buen historial, más ~3 días de acreditación
> bancaria) **no especifica país** y probablemente es de Argentina o México.
> Léelo en tu cuenta: **Mercado Pago → Actividad → un movimiento → "Disponible el ..."**, y la
> política vigente en **Mercado Pago → Tus tarifas / Cuándo recibes tu dinero**.

No planees tu caja con un número que no hayas visto en tu propia cuenta. Y ojo: el plazo puede
cambiar para ti cuando cambia tu reputación o tu antigüedad, así que revísalo cada tanto.

## El concepto, que sí es universal

Mercado Pago retiene el dinero porque **asume el riesgo de la transacción**. Compra Protegida
le devuelve la plata al comprador si el producto no llega o llega mal (verificado: hasta 21
días si no llegó, hasta 30 días desde que lo recibió si hay problema — ver `137`). Ese seguro
lo paga alguien: se paga reteniendo tu dinero hasta que el riesgo baja.

De ahí se deducen tres cosas que son ciertas sin importar el número exacto de días:

| Hecho | Consecuencia |
|---|---|
| El dinero se libera después de la entrega, no de la venta | Un envío lento retrasa tu plata |
| Mejor reputación = menos riesgo = liberación más rápida | La reputación es también un beneficio financiero |
| Un reclamo abierto congela esa plata | La posventa es tesorería, no solo servicio |

**El dinero no se libera cuando vendes: se libera cuando Mercado Libre deja de tener miedo de
que devuelvas la plata.**

## Los cuatro tiempos que te separan de tu plata

```
Día 0    Venta. El comprador paga. La plata entra "a liberar".
Día X    Despachas. Si te demoras, todo el reloj corre desde más tarde.
Día Y    Se entrega. Aquí empieza el plazo real de liberación.
Día Z    "Disponible". Ya puedes pedir el retiro.
Día Z+n  Acreditado en tu banco. El banco también se toma lo suyo.
```

Los cuatro plazos se suman. Por eso la pregunta correcta no es "¿cuántos días retiene Mercado
Pago?" sino **"¿cuántos días pasan entre que vendo y puedo gastar esa plata en mi banco?"**. Y
esa la mides tú, cronometrando una venta real de punta a punta.

## Cómo medir tu ciclo real (el método honesto)

```
□ Escoge una venta cualquiera ya cobrada
□ Anota la fecha de la compra
□ Anota la fecha de entrega (aparece en el envío)
□ Abre Mercado Pago → Actividad → ese movimiento → mira "Disponible el ..."
□ Anota cuándo pediste el retiro y cuándo cayó en el banco
□ Ciclo real = días entre la compra y la plata en el banco
□ Repite con 3 ventas: una con Full, una con Flex, una lenta
```

Ese número —tu ciclo real de caja— es el que va en la planeación de compras. Ver `168`.

## Por qué esto decide cuánto puedes crecer

Si tu ciclo de caja es de 20 días y vendes $1.000.000 al día, tienes **$20.000.000 flotando**
que no puedes tocar. Para crecer al doble necesitas otros $20.000.000 de capital de trabajo que
nadie te va a prestar contra "estoy vendiendo bien".

Esta es la razón #1 por la que un vendedor con ventas crecientes se queda sin inventario justo
cuando el algoritmo lo estaba premiando. Y quedarse sin stock es de lo más caro que hay: saca
la publicación de la competencia y de la puja de catálogo, y al reponer "revive como más nueva
o menos confiable" y debe reconstruir señales. Ver `61`.

**Quedarte sin caja no solo te frena: te devuelve al principio en el algoritmo.**

Si necesitas calcular exactamente cuánto capital de trabajo requiere tu tasa de crecimiento,
ejecútalo en `Matematicas_lushows`. No lo estimes.

## Palancas reales para acortar el ciclo

| Palanca | Efecto | Módulo |
|---|---|---|
| Despachar el mismo día | Adelanta todo el reloj | `101` |
| Usar Full | La entrega es más rápida y predecible | `103` |
| Subir la reputación a verde | Menos riesgo percibido = liberación más rápida | `125` |
| Evitar reclamos | Un reclamo congela esa plata | `136` |
| Retirar con calendario fijo | Reduce el tiempo muerto entre "disponible" y "retirado" | — |

La que más gente ignora: **retirar es manual**. La plata puede estar disponible hace cinco días
y seguir en Mercado Pago porque nadie pidió el retiro. Pon un día fijo a la semana.

## Adelanto de dinero: no cuentes con eso en Colombia

En otros países existe adelantar el dinero de las ventas y Mercado Crédito para vendedores.

> ⚠️ **Sin verificar para Colombia (sep-2026).** **Mercado Crédito para vendedores no tiene
> evidencia de estar activo en Colombia.** Está confirmado en Argentina, Brasil y México; para
> Colombia la única referencia hallada es de 2019 diciendo que "llegaría". Trátalo como no
> disponible hasta que lo veas ofrecido dentro de tu propio panel.

No construyas un plan de crecimiento apoyado en un crédito de plataforma que quizá no existe
aquí.

## El costo oculto de retirar

⚠️ **Sin verificar para Colombia (sep-2026).** Si Mercado Pago cobra comisión por retiro a
cuenta bancaria en Colombia, cuánto, y si depende del banco o del monto, no se pudo confirmar.
Mira el desglose al hacer un retiro pequeño de prueba antes de mover volumen. Ese retiro de
prueba también te confirma que la cuenta bancaria quedó bien asociada (`10`).

## El error clásico

Vender $15.000.000 en un Hot Sale (la segunda edición de 2026 es del **19 al 23 de octubre**,
dato verificado — ver `160`), comprometer inventario y publicidad contra esa venta, y descubrir
que la plata entra escalonada durante las tres semanas siguientes mientras los proveedores
cobran de contado. Se vendió bien y se quebró igual.

Antes de cualquier evento de alto volumen: **calcula cuánta caja te va a faltar durante el pico
y consíguela antes, no durante**.

## Checklist de tesorería

```
□ Conozco mi ciclo real de caja, medido, no supuesto
□ Sé cuánta plata tengo flotando ahora mismo (Mercado Pago → a liberar)
□ Tengo día fijo semanal para pedir retiros
□ Tengo cuenta bancaria del mismo titular, probada con un retiro pequeño
□ Descargué el reporte del periodo para el contador → `13`
□ Antes de un evento grande, tengo la caja del pico conseguida aparte
```

## Relacionados

`10` crear la cuenta · `13` retenciones y reportes · `14` facturación · `61` stock cero ·
`101` despacho a tiempo · `103` Full · `125` reputación · `136` reclamos ·
`137` compra protegida · `160` Hot Sale · `168` planeación de compras ·
`Matematicas_lushows` para el capital de trabajo
