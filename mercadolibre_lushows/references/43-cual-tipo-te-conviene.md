# Cuál tipo te conviene

La nomenclatura y las reglas están en `42`. Aquí se decide: **¿pagas los 3 puntos porcentuales de
las cuotas extra, o no?** Es la decisión de margen más repetida del marketplace y se resuelve con
números, no con intuición.

## El dato que manda

| Opción | Cargo por venta |
|---|---|
| Cuotas con 0% interés (base) | **8% a 19%** |
| Cuotas extra | **11% a 22%** |

(oficial ML Colombia, verificado sep-2026.) La diferencia es **exactamente 3 puntos porcentuales**.

Cuántas cuotas te habilita cada opción depende del precio:

| Precio | Base | Con cuotas extra |
|---|---|---|
| Menos de $499.999 | hasta 3 | hasta 6 |
| $500.000 a $1.499.999 | hasta 6 | hasta 9 |
| Más de $1.500.000 | hasta 12 | — (ya son 12) |

Fíjate en la última fila: **por encima de $1.500.000 ya tienes 12 cuotas en la opción base.** Ahí no
hay decisión que tomar.

## Tabla de decisión

| Tu situación | Veredicto |
|---|---|
| Vendes usados de tu casa, pocas unidades | Gratuita (`42`) |
| Producto de menos de $2.900 | No se puede: arma un pack (`48`) |
| Producto barato, margen menor al 25% | Base, sin cuotas extra |
| Producto barato, se compra por impulso | Base: nadie financia $25.000 |
| Producto de $200.000 a $1.500.000 | Evalúa: aquí las cuotas mueven la aguja |
| Producto sobre $1.500.000 | Base (ya trae 12 cuotas) |
| Compites en catálogo (`63`) | Cuotas extra, casi siempre — ver abajo |
| Tu competencia directa ofrece más cuotas y tú no | Cuotas extra o baja el precio |
| Margen neto menor a 5 puntos sobre la comisión actual | Base, y revisa tu precio (`82`) |

## La cuenta, en una línea

Los 3 puntos se pagan solos si te hacen vender **más de 3 puntos adicionales** en volumen o si te
ganan el catálogo. La pregunta correcta no es "¿me alcanza el margen?", sino:

> ¿Cuántas ventas extra necesito para compensar 3 puntos de comisión sobre TODAS mis ventas?

Ejemplo de la forma de pensarlo (no de las cifras, que son tuyas):

| | Base | Cuotas extra |
|---|---|---|
| Precio | $400.000 | $400.000 |
| Comisión supuesta | 14% = $56.000 | 17% = $68.000 |
| Diferencia por venta | — | **$12.000 menos** |
| Si vendías 30/mes | $1.680.000 de comisión | $2.040.000 |
| Ventas extra necesarias para empatar | — | depende de tu utilidad por unidad |

**Corre el número con tus cifras reales antes de decidir**:
`python scripts/margen_ml.py margen --precio X --costo Y --comision Z --iva 19`
Si el cálculo tiene que ser exacto, rutea a `Matematicas_lushows`.

## El punto clave: cuotas y catálogo

Las cuotas sin interés son una de las variables que deciden el ganador del catálogo, junto al precio
final, la reputación, el stock, el tiempo de entrega, el uso de Full/Flex, el envío gratis y el
nivel MercadoLíder (MEDIA, ver `63`). En la tabla comparativa del catálogo, el comprador ve las
cuotas de cada oferta una al lado de la otra.

| Escenario en catálogo | Resultado probable |
|---|---|
| Tú con 3 cuotas, el rival con 6 | Desventaja visible |
| Igualas cuotas y además tienes Full | Ventaja |
| Reputación naranja o roja | **Puedes participar pero no puedes ganar** (MEDIA, `63`) |

**Sin cuotas competitivas es muy difícil ganar el catálogo, y el catálogo aparece más arriba que
las publicaciones libres equivalentes.** Si tu categoría tiene catálogo y tú quieres esa posición,
los 3 puntos dejan de ser un gasto y pasan a ser el precio de entrada.

## Cuándo los 3 puntos son un error

| Señal | Por qué |
|---|---|
| Producto de ticket bajo | Nadie financia una compra de $40.000 en 6 cuotas |
| Margen neto delgado | 3 puntos se comen la utilidad completa |
| Tu ventaja es el precio más bajo | Sube el precio para cubrirlos y pierdes tu ventaja |
| Compra por impulso, no por decisión | Las cuotas no cambian la decisión |
| Tu categoría no tiene catálogo | Pierdes el mayor beneficio de pagarlos |

## Cómo probarlo sin adivinar

```
□ Elige 2 productos comparables en ventas
□ Pon cuotas extra en uno y déjalo 30 días sin tocar nada más
□ Compara: unidades vendidas, ingreso total y UTILIDAD, no solo ventas
□ La utilidad es lo único que decide; las ventas pueden subir y la plata bajar
□ Repite la prueba antes de aplicarlo a todo el catálogo
```

## El error clásico

Activar cuotas extra en las 80 publicaciones a la vez "para vender más". Pagas 3 puntos sobre todo
tu volumen, incluidas las 60 publicaciones donde nadie iba a financiar nada, y la utilidad cae sin
que sepas por qué. **Las cuotas extra se activan producto por producto, donde compites en catálogo
o donde el ticket es alto; jamás de forma masiva.**

## Chequeo antes de decidir

```
□ Leí mi comisión real en el simulador, logueado (`76`)
□ Calculé la utilidad por unidad en las dos opciones
□ Sé si mi categoría tiene catálogo y si quiero pelearlo (`62` `63`)
□ Miré cuántas cuotas ofrece mi competencia directa
□ Mi precio está por encima de $2.900 (`77`)
□ Si es más de $1.500.000, no activo nada: ya tengo 12 cuotas
```

## Relacionados

`42` tipos de publicación · `45` stock · `62` catálogo · `63` ganar el catálogo · `75` costos de
vender · `76` leer tu comisión · `77` el piso de $2.900 · `82` margen real · `126` reputación y
dinero · `129` MercadoLíder · cálculos exactos → `Matematicas_lushows`
