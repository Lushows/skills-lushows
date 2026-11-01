# Colecta y puntos de despacho

Las dos formas de despachar cuando tu inventario está en tu bodega y no entregas tú mismo: que la
transportadora pase a recogerte (colecta) o que tú lleves los paquetes a un punto habilitado.
Parecen equivalentes y no lo son: una te cuesta tiempo y la otra te cuesta disciplina.

## La diferencia real

| | Punto de despacho | Colecta |
|---|---|---|
| Quién se mueve | Tú | La transportadora |
| Costo directo | Transporte tuyo hasta el punto | Normalmente incluido en el envío |
| Costo oculto | **Tu tiempo y el desplazamiento** | Estar presente en la ventana horaria |
| Flexibilidad de horario | Alta: vas cuando puedas | Baja: pasan cuando pasan |
| Riesgo de demora | Tú te olvidas de ir | No tienes los paquetes listos cuando llegan |
| Bueno para | Pocos paquetes al día | Volumen constante |

> ⚠️ **Sin verificar para Colombia (sep-2026).** Los requisitos de habilitación de colecta en MCO
> (volumen mínimo diario, ciudades cubiertas, si se solicita o se asigna) no se pudieron confirmar.
> Míralo en Panel → Ventas → Envíos → Configuración de envíos, o pregúntalo por el chat de
> vendedores si ya eres MercadoLíder.

## El cálculo de cuál conviene

No lo decidas por comodidad. Decídelo con esta cuenta, que puedes hacer en una servilleta:

```
COSTO DIARIO DE IR AL PUNTO
  = (minutos ida y vuelta + minutos de fila) ÷ 60 × lo que vale tu hora
  + transporte (gasolina, pasaje, parqueadero)
  + el costo de los días que NO fuiste (demoras, ver `113`)

COSTO DIARIO DE LA COLECTA
  = minutos de tener todo empacado y rotulado antes de la ventana ÷ 60 × tu hora
  + el costo de los días que el camión llegó y no estabas listo
```

Compara, pero además aplica el umbral de sentido común:

| Paquetes por día | Recomendación |
|---|---|
| 1 a 3 | Punto de despacho. Un viaje corto no justifica esperar un camión |
| 4 a 10 | Zona gris. Gana quien tenga la operación más ordenada (`114`) |
| Más de 10 | Colecta, sin discusión. Ir al punto con 15 paquetes te consume la mañana |

**El punto de despacho no es gratis: cuesta tu mañana. Cuando tu mañana vale más que el viaje, es
hora de pedir colecta.**

## Lo que cambia en tu reputación

Ambas modalidades fallan por la misma razón: no cumpliste el tiempo de preparación que prometiste.
Y "despacho con demora" es exactamente una de las tres variables base del termómetro, bajo el
nombre de **envíos incorrectos** (oficial ML Colombia, verificado sep-2026).

Los techos oficiales para conservar el verde:

| Medición | Envíos incorrectos |
|---|---|
| A 60 días (si tienes 60 o más ventas) | no superar **12%** |
| A 365 días (si tienes menos de 60 ventas) | no superar **15,5%** |
| Si eres MercadoLíder | no superar **10%** |

(Oficial ML Colombia, verificado sep-2026.) Y perder el verde no es solo imagen: te quita el 50%
de descuento en envíos y **duplica** tu costo de flete en productos de más de $60.000. Ver `100`.

| Falla típica | Modalidad | Cómo se evita |
|---|---|---|
| Te acordaste tarde y el punto cerró | Punto | Hora fija diaria, no "cuando pueda" |
| Llegó el camión y tenías 3 sin empacar | Colecta | Empacar en la mañana, no al timbre |
| Etiqueta mal pegada, el punto la rechaza | Ambas | Checklist de `114` |
| Fin de semana largo y nadie despachó | Ambas | Ajusta el tiempo de preparación antes del puente |

La última merece su párrafo: el tiempo de preparación que declaras **debe contemplar tus festivos
reales**. Colombia tiene muchos lunes festivos. Si tu promesa no los absorbe, cada puente te mete
demoras. Ver `112`.

## La rutina que hace que funcione

```
□ Hora fija diaria para cerrar el despacho (ejemplo: 14:00, siempre)
□ Imprimir todas las etiquetas del día juntas, no de a una
□ Empacar y rotular ANTES de la hora de corte, no durante
□ Contar los paquetes contra la lista de ventas del panel
□ Llevar o entregar, y confirmar en la app el mismo día
□ Revisar al día siguiente que todos figuren "en camino"
```

El último paso es el que nadie hace y el que atrapa los errores: un paquete que sigue en "listo
para despachar" 24 horas después es una demora que todavía puedes corregir. Detalle en `114`.

## El error clásico

Quedarse en punto de despacho por costumbre mucho después de haber cruzado el volumen donde la
colecta gana. El vendedor calcula "el punto es gratis" porque no le pone precio a su tiempo. Si
gastas 90 minutos diarios en ir al punto, son 30 horas al mes: un cuarto de jornada mensual
regalada. Esa es la razón número uno por la que un vendedor que crece deja de crecer — se le acabó
el día.

Segundo error clásico, al revés: pedir colecta con dos paquetes y no tenerlos listos, acumulando
demoras porque "ya vendrán mañana". La colecta sin disciplina es peor que el punto.

## Cómo medirlo en tu auditoría mensual

Estas son las tres cifras que te dicen si estás en la modalidad correcta:

| Métrica | Dónde sale | Umbral de alarma |
|---|---|---|
| Paquetes despachados por día | Panel → Ventas, o `GET /orders/search` | >10/día → colecta |
| Tasa de demora | Panel → envíos incorrectos | 12% a 60 días y pierdes el verde (`126`) |
| Horas al mes en despacho | Tu registro, una semana basta | >20 h/mes → contrata o cambia |

El procedimiento completo está en `124`.

## Relacionados

`100` cómo funciona Mercado Envíos · `101` modalidades · `102` Flex · `103` Full · `112` el tiempo
que prometes · `113` la demora y su costo · `114` el flujo diario · `115` zonas difíciles · `124`
auditoría mensual · `126` las tres métricas
