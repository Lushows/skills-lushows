# La demora y su costo

No despachar a tiempo cuesta tres veces: te entra a envíos incorrectos, te quita el derecho a
excluir el reclamo, y si te tumba del verde te **duplica el costo de envío de todas las ventas**.
Es la falla operativa más cara del marketplace colombiano.

## Los tres costos, en orden

**1. Entra al termómetro.** "Despacho con demora" es exactamente lo que mide la variable **envíos
incorrectos**. Techo para seguir verde: **12% a 60 días**, **15,5% a 365 días**, **10% si eres
MercadoLíder** (oficial ML Colombia, verificado sep-2026).

**2. Pierdes la exclusión del reclamo.** La demora es un reclamo **excluible solo si despachaste a
tiempo**. Si la demora es tuya, el reclamo **no es excluible** y cuenta contra tu reputación
(oficial ML Colombia, verificado sep-2026).

| Situación | ¿El reclamo por demora cuenta? |
|---|---|
| Despachaste a tiempo, se demoró la transportadora | **No cuenta**, es excluible |
| No despachaste a tiempo | **Sí cuenta**, no es excluible |

**3. Si pierdes el verde, se te duplica el flete.** El descuento por reputación es 50% para verde,
40% para amarilla y **ninguno** para naranja o roja (oficial). En un producto de más de $60.000 y
1 kg: **$8.200 si eres verde, $16.400 si caes a naranja**.

## La factura real de caer de verde

| Ventas al mes (>$60.000, 1 kg) | Costo verde | Costo naranja | Sobrecosto mensual |
|---|---|---|---|
| 50 | $410.000 | $820.000 | **$410.000** |
| 100 | $820.000 | $1.640.000 | **$820.000** |
| 200 | $1.640.000 | $3.280.000 | **$1.640.000** |
| 500 | $4.100.000 | $8.200.000 | **$4.100.000** |

Y eso sin contar la caída de posición y de conversión, que es probablemente mayor.

**Una demora no cuesta una venta: cuesta un porcentaje de todas tus ventas futuras.**

## Qué hacer el día que ya vas tarde

El daño no es binario. Hay una secuencia que reduce el golpe:

```
□ 1. Despacha HOY lo que puedas, aunque sea tarde: cada hora cuenta
□ 2. Escribe al comprador ANTES de que él pregunte, con fecha concreta
□ 3. Responde cualquier mensaje suyo en menos de 24 HORAS HÁBILES (oficial)
□ 4. Si no vas a poder cumplir, dilo y ofrece solución, no excusa
□ 5. NO canceles tú la venta para "limpiar" la demora: ver la trampa abajo
□ 6. Si el comprador pide cancelar, tienes 2 días hábiles para reembolsar sin afectación
```

El punto 3 es un corte oficial: **si no respondes mensajes en 24 horas hábiles, pierdes el derecho
a pedir la exclusión del reclamo de tu reputación** (oficial ML Colombia, verificado sep-2026). Es
gratis responder y carísimo no hacerlo.

## La trampa: cancelar para evitar la demora

Parece la salida elegante y es la peor. **Cancelar tú es una variable propia del termómetro**, con
sus propios techos: no cancelar más del **2,5% a 60 días** ni del **4% a 365 días**, y **1,5%** si
eres MercadoLíder (oficial ML Colombia, verificado sep-2026).

| Acción | Variable afectada | Techo para seguir verde |
|---|---|---|
| Despachar tarde | Envíos incorrectos | 12% (60 d) / 15,5% (365 d) |
| Cancelar tú la venta | Canceladas por ti | 2,5% (60 d) / 4% (365 d) |

El techo de canceladas es **cinco veces más estrecho** que el de envíos incorrectos. Cambiar una
demora por una cancelación es cambiar una falla barata por una cara.

Dos aclaraciones oficiales que sí te ayudan: las ventas canceladas **por la persona que te
compró** no cuentan, y una venta cancelada es "cuando el comprador recibe su dinero de vuelta
antes de que hayas entregado el producto". Las **devoluciones no son cancelaciones**.

## Las causas reales de la demora

| Causa | Frecuencia | Arreglo |
|---|---|---|
| Sin stock real: vendiste lo que no tenías | Alta | Colchón de seguridad (`123`) |
| Se acabó el empaque | Alta | Stock de empaque para 3 semanas (`110`) |
| No revisaste el panel ese día | Alta | Rutina diaria a hora fija (`114`) |
| Puente festivo sin ajustar la promesa | Alta | Calendario (`112`) |
| Prometiste un tiempo que nunca pudiste cumplir | Media | Sube la promesa hoy (`112`) |
| Producto que llega del proveedor tarde | Media | No publiques lo que no tienes en mano |

Las tres primeras son operativas y se arreglan con disciplina, no con plata. Son también las tres
más comunes.

## La demora que no es tuya

Si despachaste a tiempo y la transportadora se demoró, el reclamo es **excluible** — pero la
exclusión hay que pedirla, y solo puedes pedirla si respondiste en las 24 horas hábiles.

```
□ Guarda la evidencia del despacho a tiempo: la etiqueta escaneada y la hora
□ Responde al comprador ese mismo día, con el número de rastreo
□ Cuando el reclamo se abra, pide la exclusión citando el despacho en fecha
□ Revisa mensualmente que las exclusiones que pediste se hayan aplicado (`124`)
```

El último paso lo ignora casi todo el mundo y es el que recupera puntos de reputación ya perdidos.

## El error clásico

Enterarse de la demora por el reclamo. El vendedor no mira el panel dos días, el comprador abre
reclamo, y ahí recién se entera. A esa altura ya perdió: la demora está registrada, el reclamo
está abierto, y probablemente ya pasaron las 24 horas hábiles de respuesta.

**La demora se gestiona antes de que exista, mirando el panel todos los días.** El procedimiento
está en `114`.

## Relacionados

`112` el tiempo que prometes · `114` el flujo diario · `102` Flex · `104` colecta y puntos · `115`
zonas difíciles · `119` entrega fallida · `123` inventario en dos canales · `124` auditoría
mensual · `126` las tres métricas · `136` reclamos excluibles · `100` tarifas oficiales de envío
