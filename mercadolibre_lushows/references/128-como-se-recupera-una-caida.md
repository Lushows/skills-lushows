# Cómo se recupera una caída de reputación

Caer de verde a amarillo o naranja no es el fin, pero el camino de vuelta es lento, tiene reglas y
cuesta plata mientras dura. Hay además un mecanismo oficial que compra color —el Programa de
Despegue— y funciona dejando dinero en garantía.

## Primero, cuánto te está costando la caída

Antes de hablar de cómo volver, pon el número encima de la mesa. El descuento en envíos depende del
color (oficial ML Colombia, verificado sep-2026):

| Color | Descuento en envíos | Envío de 1 kg, producto >$60.000 |
|---|---|---|
| Verde / MercadoLíder | 50% | **$8.200** |
| Amarilla | 40% | ~$10.200 |
| Naranja o roja | Ninguno | **$16.400** |

Multiplica la diferencia por tus ventas del mes. Ese número es el presupuesto que tienes disponible
para arreglar el problema, y casi siempre es mucho mayor de lo que cuesta arreglarlo.

## La verdad incómoda

No existe botón de "resetear reputación". No existe apelación de color. Se recupera de una sola
forma: **acumulando ventas limpias dentro de la ventana de evaluación** (`127`). Con 60+ ventas eso
son 60 días; con menos, hasta 365.

Tampoco sirve abrir cuenta nueva: es violación de términos y, si ML detecta la relación, deshabilita
la nueva **y las asociadas** (`143`). **Abrir una cuenta paralela para huir de la reputación es el
suicidio más común del vendedor desesperado.**

## El orden correcto

```
□ 1. Diagnostica CUÁL variable rompió el umbral. No "la reputación": reclamos (3,5%),
     envíos incorrectos (12%/15,5%) o canceladas (2,5%/4%) — ver `126`
□ 2. Encuentra la causa raíz de ESA variable. Casi siempre es una sola cosa
□ 3. Corta la hemorragia: pausa el SKU, el lote o el proveedor que la causa
□ 4. Revisa reclamos abiertos y pide exclusión donde corresponda (`136`)
□ 5. Sigue vendiendo lo que sale perfecto — necesitas denominador (`127`)
□ 6. Mide semanalmente los tres porcentajes, no el color (`144`)
□ 7. Solo con 3-4 semanas limpias, vuelve a escalar
```

El paso 3 es el que la gente se salta. Vender con el problema puesto no recupera nada.

## Causa raíz por variable

| Rompió | Causas más frecuentes | Dónde se arregla |
|---|---|---|
| Reclamos (>3,5%) | Ficha que promete de más · faltan piezas · producto frágil mal embalado · lote malo | `25`-`40`, `110` |
| Canceladas (>2,5%) | Quiebre de stock, sobreventa multicanal, stock fantasma | `140`, `123`, `196` |
| Envíos incorrectos (>12%) | Cortes de despacho irreales, fines de semana, origen mal declarado, Flex entregado después de las 21:00 | `105`, `115` |
| Mediaciones (>0,5%) | No responder a tiempo, tono defensivo | `133`, `135` |

## El Programa de Despegue

Mecanismo oficial: **dejar dinero en Mercado Pago Financiera te da el color verde claro** (oficial
ML Colombia, verificado sep-2026).

| Cómo funciona | Detalle |
|---|---|
| Qué haces | Dejas un monto en garantía en Mercado Pago Financiera |
| Qué obtienes | Tu perfil pasa a mostrarse en **verde claro** mientras te evalúan |
| Si te va bien | Mantienes buen desempeño y recuperas el dinero |
| Si te va mal | Pierdes la garantía y vuelves a tu color original |

El monto que circula en fuentes secundarias es **$90.360 COP**, pero no aparece en el texto oficial
leído.

> ⚠️ **Sin verificar para Colombia (sep-2026).** El monto exacto de la garantía y la duración de la
> ventana de evaluación del Programa de Despegue no están en la página oficial. La cifra de $90.360
> COP viene de fuente secundaria. Míralo en el panel: la oferta aparece en Mi cuenta → Reputación
> cuando eres elegible.

**Veredicto:** el Despegue tiene sentido **solo si ya cortaste la causa raíz**. Es una apuesta a que
tus próximas semanas serán limpias. Si lo tomas con el problema activo, pierdes la plata y vuelves
al mismo color. Compra vitrina, no perdón.

Ojo con lo que el verde claro **no** te devuelve: el descuento del 50% en envíos está asociado a
verde y MercadoLíder. Si el Despegue te deja en verde claro, verifica en tu propio panel qué tarifa
de envío te está cobrando ML antes de asumir que recuperaste los $8.200.

## Lo que NO funciona

| Idea | Por qué falla |
|---|---|
| Comprarte a ti mismo con otra cuenta | ML detecta el patrón; es fraude y termina en suspensión (`143`) |
| Pedirle al cliente que cierre el reclamo | El reclamo ya contó, y presionar al comprador es sancionable |
| Bajar el precio al piso para vender mucho | Diluyes con margen negativo; si el problema es estructural, empeoras |
| Pausar todo y esperar | Sin ventas no hay denominador: te congelas en el color malo (`127`) |
| Pagar Ads para "recuperarte" | La penalización de posicionamiento no se compensa con inversión (`145`) |
| Cuenta nueva | Deshabilitan la nueva y la vieja (`143`) |

## Lo que sí funciona y nadie hace

Revisar si los reclamos que te tumbaron eran **excluibles**. Dos excepciones oficiales borran una
cantidad enorme de casos (oficial ML Colombia, verificado sep-2026):

```
□ Los reclamos por ARREPENTIMIENTO del comprador no cuentan contra tu reputación
□ Las ventas canceladas POR EL COMPRADOR no cuentan como cancelación tuya
```

Si tu porcentaje incluye casos de estos, algo se contabilizó mal o no pediste la exclusión a tiempo.
El procedimiento y el corte de 24 horas hábiles están en `136`.

## El error clásico

Tratar la caída como problema de imagen en vez de problema de operación. El vendedor golpeado sale a
escribir mensajes bonitos y a responder opiniones, y no toca el proceso que genera los reclamos.
**El termómetro no se arregla con palabras: se arregla con cajas que llegan bien.**

## Cuánto tarda de verdad

| Escenario | Tiempo realista |
|---|---|
| 60+ ventas, causa raíz cerrada | ~60 días (una ventana completa) |
| 60+ ventas, causa raíz a medias | Nunca: el porcentaje se estabiliza donde está |
| Menos de 60 ventas | Hasta 365 días |
| Menos de 60 ventas, pero cruzas las 60 | La ventana se acorta a 60 días: atajo real (`127`) |

## Relacionados

`125` el termómetro · `126` las tres métricas · `127` el periodo de evaluación ·
`136` reglas de exclusión · `139` la cancelación y su castigo · `140` el quiebre de stock ·
`142` opiniones negativas · `143` suspensión de cuenta · `144` plan de defensa de la cuenta ·
`118` costos de envío
