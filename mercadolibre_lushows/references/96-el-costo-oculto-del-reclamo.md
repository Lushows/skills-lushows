# El costo oculto del reclamo

Un reclamo cuesta dos veces: la plata de resolverlo y el punto de reputación que te deja más cerca
del amarillo. Y en Colombia el segundo golpe es cuantificable al peso, porque **el descuento en
envíos depende del color del termómetro**. Perder el verde duplica tu costo de envío en cada venta,
vendas o no vendas con reclamo.

## El golpe económico directo

| Concepto | Qué te cuesta |
|---|---|
| Tiempo de gestión | Responder, investigar, negociar. Horas, no minutos |
| Reenvío o reposición | Producto + envío otra vez |
| Reembolso | El producto y los gastos de envío si fue con Mercado Envíos |
| Producto perdido | Muchos reclamos terminan sin recuperar la unidad |

Ese es el costo visible, y es parecido al de una devolución (`95`). El invisible es más grande.

## El golpe reputacional, en pesos

Los umbrales oficiales para mantener el **verde**:

| Variable | Medido a 60 días | Medido a 365 días | Si eres MercadoLíder |
|---|---|---|---|
| **Ventas con reclamos** | no superar **3,5%** | no superar **3,5%** | no superar **2,5%** |
| **Envíos incorrectos** | no superar **12%** | no superar **15,5%** | no superar **10%** |
| **Canceladas por ti** | no más del **2,5%** | no más del **4%** | no más del **1,5%** |

(oficial ML Colombia, verificado sep-2026. Para MercadoLíder se suma **mediaciones < 0,5%**.)

Y lo que cuesta cruzarlos, en la tabla oficial de envíos (`78`), producto de 1 kg sobre $60.000:

| Reputación | Descuento en envíos | Envío que pagas |
|---|---|---|
| Verde / MercadoLíder / **sin reputación** | 50% | **$8.200** |
| Amarilla | 40% | ~$10.200 |
| **Naranja o roja** | **Ninguno** | **$16.400** |

**Un reclamo no cuesta lo que cuesta resolverlo: cuesta $8.200 por venta durante los siguientes 60
días si te saca del verde.**

Con 200 ventas al mes, eso es **$1.640.000 mensuales**. El reclamo que te pareció un problema de
$40.000 acaba de costar más de un millón y medio.

Dato que cambia la lectura: **un vendedor sin reputación tiene el mismo 50% que un verde** (oficial)
—no tendrás reputación hasta completar tus **primeras 10 ventas**—. El castigo no es no tenerla, es
perderla.

## Qué reclamos cuentan y cuáles no

Solo cuentan para la reputación los reclamos de **producto incompleto/faltante** y de **calidad**
(defectuoso, de fábrica, deja de funcionar). Esto es oficial y es la mitad de la gestión.

| Reclamos que NO cuentan (excluibles) | Reclamos que SÍ cuentan |
|---|---|
| Error del comprador | Producto defectuoso o distinto al anunciado |
| **Arrepentimiento** con producto en perfecto estado | Faltaron unidades o partes |
| Demora si despachaste a tiempo | No despachaste a tiempo |
| "Entregado" que el comprador no reconoce | Falta de stock |
| Fallas de la plataforma | El comprador alega producto falso |
| Reclamo abierto antes de 24 h desde tu último mensaje | |
| Uso del reclamo como medio de contacto | |

Todo oficial, confianza ALTA.

## La regla de las 24 horas, que vale dinero

> **Si no respondes mensajes en 24 horas hábiles, pierdes el derecho a pedir la exclusión del
> reclamo de tu reputación.** (oficial, confianza ALTA)

Traducción: un reclamo perfectamente excluible —un arrepentimiento, un error del comprador— se
vuelve NO excluible por no contestar a tiempo. Y un reclamo que cuenta te acerca al 3,5% que te
saca del verde, que te duplica el envío.

**Responder un mensaje en menos de 24 horas hábiles es la tarea mejor pagada de todo el
marketplace.**

## La cancelación: el umbral que suspende cuentas

Distinto del reclamo y más grave:

- **Venta cancelada** = *"el comprador recibe su dinero de vuelta antes de que hayas entregado el
  producto"*, sin importar quién la pidió. **Las devoluciones NO son cancelaciones** (`95`).
- **Solo te penaliza si cancelas tú.** Si cancela el comprador, no te afecta (oficial).
- **Más del 2,5% de ventas canceladas → la cuenta puede ser suspendida para vender.** Es el único
  umbral de suspensión confirmado oficialmente.
- Los reclamos **con solicitud de cancelación** no afectan la reputación desde el inicio: tienes
  **2 días hábiles** para reembolsar sin haber entregado. Si cumples, reputación intacta. Si no, el
  reembolso es automático y **sí** te afecta.

## El flujo, y dónde se pierde el control

```
Reclamo  →  (comprador y vendedor negocian)
   ↓  no se resuelve
Disputa / Mediación  →  interviene ML, canal exclusivo, sin contacto directo
```

La mediación es peor que el reclamo: para MercadoLíder es una cuarta variable del termómetro y el
límite es **0,5%**. Resolver en la etapa de reclamo, rápido y a favor del comprador cuando el monto
es chico, casi siempre sale más barato que tener la razón en la mediación.

## Cómo se presupuesta

Igual que la devolución: como una tasa, no como un imprevisto.

```
costo ajustado = costo + (tasa de reclamos × costo promedio de un reclamo)
```

Y si tu tasa te está acercando al 3,5%, súmale el costo del envío encarecido a **todas** las
ventas, no solo a las reclamadas. Ese es el cálculo que nadie hace y el que explica por qué un mes
con tres reclamos malos destruye el trimestre.

```
# Escenario verde
python scripts/margen_ml.py margen --precio 89900 --costo 42000 --comision 15 \
    --envio 8200 --iva 19

# Escenario naranja: mismo producto, envío sin descuento
python scripts/margen_ml.py margen --precio 89900 --costo 42000 --comision 15 \
    --envio 16400 --iva 19
```

Cargo **15% — ejemplo dentro del rango oficial 8%-22%, verifica el tuyo** (`76`).

## Lista de chequeo operativa

```
□ Respondo TODO mensaje en menos de 24 horas hábiles (es dinero, no cortesía)
□ Conozco mis tres porcentajes actuales: reclamos, envíos incorrectos, canceladas
□ Estoy por debajo de 3,5% / 12% / 2,5% a 60 días
□ Pido la exclusión de todo reclamo excluible, siempre, y a tiempo
□ Nunca cancelo yo: si no tengo stock, es mejor gestionar que cancelar
□ Los reclamos con solicitud de cancelación los reembolso dentro de 2 días hábiles
□ Resuelvo en etapa de reclamo, antes de que escale a mediación
□ Tengo el costo del envío encarecido presupuestado como riesgo, no como sorpresa
```

## El error clásico

Pelear el reclamo de $30.000 durante dos semanas "por principio". El principio cuesta: el reclamo
escala a mediación, la mediación cuenta, el termómetro baja, y el envío de las siguientes 200
ventas se duplica. La aritmética casi siempre favorece resolver rápido.

El segundo: no pedir la exclusión de los reclamos excluibles. Son gratis de pedir y bajan tu
porcentaje. No pedirlas es regalar puntos del termómetro.

## Relacionados

`78` el envío que pagas tú, con tablas por reputación · `82` la calculadora de margen · `95` el
costo oculto de la devolución · `97` margen por SKU · `98` qué hacer con el SKU que no deja · `99`
revisión mensual · `135` reclamos · `136` mediaciones · `125`-`144` reputación y riesgo de cuenta
