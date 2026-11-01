# El tiempo de despacho que prometes

Lo que declaras como tiempo de preparación no es una estimación: es un contrato. Incumplirlo entra
directo a **envíos incorrectos**, una de las tres variables base del termómetro, y el techo para
conservar el verde es **12% a 60 días** (oficial ML Colombia, verificado sep-2026).

## Los tres números oficiales

| Medición | Envíos incorrectos: techo para seguir verde |
|---|---|
| A 60 días (tienes 60 o más ventas) | no superar **12%** |
| A 365 días (tienes menos de 60 ventas) | no superar **15,5%** |
| Si eres MercadoLíder | no superar **10%** |

(Oficial ML Colombia, verificado sep-2026.)

"Envíos incorrectos" cubre despacho con demora y despacho desde depósito incorrecto. Es la
variable que más se incumple por optimismo y la que más barato se arregla.

## La cuenta que casi nadie hace

12% suena holgado. En ventas reales no lo es:

| Ventas en el periodo | Envíos con demora que te dejan verde |
|---|---|
| 20 | 2 |
| 50 | 6 |
| 100 | 12 |
| 300 | 36 |

Pero mira la fila de 20: con menos de 60 ventas te miden a **365 días**, así que esos 2
incumplidos te acompañan un año entero. **Cuando estás arrancando, cada demora pesa doce meses.**

## Cómo elegir tu tiempo de preparación

La regla es una sola: **promete el tiempo que puedes cumplir tu peor día, no tu mejor día.**

```
□ Mide cuánto tardas de verdad, con cronómetro, durante una semana normal
□ Toma el día MÁS LENTO de esa semana, no el promedio
□ Súmale un margen para el día que te enfermas o se acaba el empaque
□ Resta los días no hábiles de tu operación
□ Ese número, redondeado hacia arriba, es tu promesa
```

Un tiempo de preparación más largo baja un poco tu atractivo. Un tiempo incumplido te baja la
reputación, y perder el verde **duplica tu costo de envío**: de $8.200 a $16.400 en un producto de
más de $60.000 y 1 kg (oficial, ver `100`). La aritmética no deja duda.

## El calendario colombiano

Colombia tiene muchos lunes festivos y esa es la causa número uno de rachas de demora.

| Situación | Qué hacer |
|---|---|
| Puente festivo | Ajusta el tiempo de preparación la semana anterior |
| Semana Santa | Define desde marzo qué días operas y declara en consecuencia |
| Hot Sale (19-23 oct 2026) | Sube el tiempo si no tienes equipo extra, o contrata antes |
| Diciembre | El mes donde más se pierde el verde. Planea desde noviembre |
| Tus vacaciones | Pausa las publicaciones o activa modo vacaciones. No improvises |

El último punto: irse una semana dejando las publicaciones activas es la forma más rápida de pasar
de verde a naranja. Vale más una semana sin vender que un trimestre de flete doble.

## Cuándo puedes prometer menos

| Modalidad | Promesa realista |
|---|---|
| Full | **Entrega al día siguiente** (oficial): ML se encarga, tú no despachas |
| Flex | Mismo día, con entrega **antes de las 21 hs** (oficial) |
| Colecta con volumen | Depende de tu hora de corte contra la ventana del camión |
| Punto de despacho | Depende de tu disciplina diaria (`114`) |

Full es la única modalidad donde la promesa corta no depende de ti. Esa es buena parte de su
valor: no es solo velocidad, es **velocidad que no puedes incumplir**. La contracara son los
cargos de `107` y `108`.

## Lo que gana un tiempo corto

| Efecto | Tamaño |
|---|---|
| Aparece en los filtros de entrega rápida | Alto en categorías competidas |
| Sube conversión, que es el factor más pesado del ranking | Alto |
| Variable del desempate en catálogo (`63`) | Medio |
| Reduce preguntas de "¿cuándo llega?" | Medio |

Pero vale solo si lo cumples. **Una promesa corta incumplida vale menos que una promesa larga
cumplida**, porque la primera te cobra en reputación y la segunda solo en conversión.

## Cómo saber si estás cerca del límite

```
□ Panel → Reputación: mira el porcentaje de envíos incorrectos, se recalcula a diario
□ GET /users/$USER_ID → seller_reputation.metrics.delayed_handling_time
□ Cuenta cuántas ventas llevas: define si te miden a 60 o a 365 días
□ Si superas 8%, ya estás en zona de alerta: revisa antes de llegar a 12
□ Si estás cerca del límite, sube el tiempo de preparación HOY, no la semana que viene
```

La última línea es la acción correcta y la que nadie toma a tiempo. Subir la promesa es gratis y
reversible; recuperar el verde toma 60 días.

## El error clásico

Poner el tiempo de preparación más corto disponible porque "así vendo más", el primer mes, cuando
todavía no sabes cuánto tardas de verdad. El vendedor nuevo tiene poco volumen, se mide a 365
días, y arranca acumulando demoras que le van a pesar durante todo su primer año.

**Arranca con la promesa larga y acórtala cuando tengas datos. Nunca al revés.**

## Relacionados

`113` la demora y su costo · `114` el flujo diario · `102` Flex · `103` Full · `104` colecta y
puntos · `115` zonas difíciles · `124` auditoría mensual · `126` las tres métricas · `136`
reclamos excluibles · `100` tarifas oficiales de envío · `63` ganar el catálogo
