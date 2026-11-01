# Etiquetas y el flujo diario

La rutina operativa es lo que separa al vendedor que conserva el verde del que lo pierde sin
entender por qué. No es complicada: son seis pasos a hora fija. El que la improvisa acumula
demoras, y cada demora se paga con la mitad del descuento de envío (`113`).

## El ciclo, en seis pasos

```
□ 1. REVISAR   → abrir el panel a hora fija y ver las ventas nuevas
□ 2. IMPRIMIR  → todas las etiquetas del lote juntas
□ 3. EMPACAR   → con la lista de contenido por SKU a la vista
□ 4. ROTULAR   → etiqueta pegada, plana, sin arrugas ni cinta encima del código
□ 5. DESPACHAR → entregar a la colecta, llevar al punto, o salir en Flex
□ 6. CONFIRMAR → verificar en el panel que todo quedó "en camino"
```

El paso 6 es el que nadie hace y el que atrapa los errores: un paquete que sigue en "listo para
despachar" al día siguiente es una demora que **todavía puedes corregir**.

## Las horas fijas

Una operación sin horas fijas no es una operación, es una reacción.

| Momento | Qué se hace | Por qué a esa hora |
|---|---|---|
| Mañana temprano | Revisar ventas de la noche | Te da todo el día de margen |
| Media mañana | Imprimir y empacar el lote | El grueso del trabajo con energía |
| Hora de corte fija | Cerrar el lote del día | Todo lo que entre después va mañana |
| Antes del despacho | Contar paquetes contra la lista | Atrapa el paquete olvidado |
| Fin del día | Confirmar estados en el panel | Detectas el error el mismo día |

En Flex la hora de corte se calcula **hacia atrás desde las 21:00**, que es el límite oficial de
entrega (oficial ML Colombia, verificado sep-2026). Ver `102`.

## Las etiquetas: lo que las arruina

| Error | Consecuencia |
|---|---|
| Impresión clara pero con tóner bajo | El código no escanea, el punto lo rechaza |
| Etiqueta arrugada o pegada sobre un pliegue | No escanea |
| Cinta transparente encima del código de barras | El brillo impide la lectura en muchos escáneres |
| Etiqueta vieja sin quitar de una caja reutilizada | El paquete se va al destino equivocado |
| Imprimir una etiqueta y empacar otro producto | Reclamo de producto distinto, no excluible |

La última es la más cara y la más fácil de evitar: **pega la etiqueta del SKU antes de empacar, y
empaca contra la etiqueta.** Nunca al revés.

```
□ Etiqueta pegada en superficie plana, no en la esquina ni sobre la cinta
□ Nada de cinta sobre el código de barras
□ Cajas reutilizadas: tacha o arranca toda etiqueta anterior
□ Revisa el nivel de tinta o el rollo térmico antes de imprimir el lote
□ Si una etiqueta sale mal, reimprime: no la remiendes
```

## El control de dos listas

El método más simple que funciona: dos listas y un conteo.

```
LISTA A = ventas del día en el panel
LISTA B = paquetes físicos en la mesa

Si A ≠ B, no despachas hasta saber por qué.
```

Esa comparación de treinta segundos evita el paquete olvidado, que es la causa más común de demora
en vendedores medianos. Con más de 15 paquetes diarios, usa un marcador y tacha sobre la lista
impresa: la memoria no alcanza.

## Qué revisar todos los días en el panel

```
□ Ventas nuevas sin despachar
□ Paquetes que siguen en "listo para despachar" de días anteriores  ← el más importante
□ Preguntas sin responder
□ Mensajes posventa sin responder  ← corte de 24 horas hábiles, oficial
□ Reclamos abiertos
□ Stock bajo de tus SKUs principales
```

El cuarto punto tiene consecuencia dura: **si no respondes mensajes en 24 horas hábiles, pierdes
el derecho a pedir la exclusión del reclamo de tu reputación** (oficial ML Colombia, verificado
sep-2026). Responder es gratis; no responder cuesta puntos de termómetro.

## Cuando el volumen crece

| Paquetes/día | Herramienta |
|---|---|
| 1 a 5 | Panel web y una hoja impresa |
| 5 a 20 | Impresora térmica y lista de contenido por SKU pegada en la mesa |
| 20 a 50 | Colecta, dos personas, y separar empaque de despacho |
| Más de 50 | Considera Full para los SKUs de alta rotación (`105`), o automatiza (`175`) |

La automatización por API tiene sentido desde el cuarto renglón: `GET /orders/search?seller=$ID`
para el listado, webhook de topic `orders_v2` para enterarte al instante, y `GET /shipments/$ID`
para el estado. Los webhooks exigen **HTTP 200 dentro de 500 ms** o ML desactiva la suscripción
(verificado). Detalle en `185`, `186` y `190`.

## La rutina del lunes

Una vez por semana, diez minutos:

```
□ Mirar el porcentaje de envíos incorrectos: ¿subió o bajó? (techo verde: 12% a 60 días)
□ Contar cuántos paquetes se despacharon tarde la semana pasada, y por qué
□ Revisar el stock de empaque: ¿alcanza para tres semanas?
□ Mirar el calendario: ¿hay festivo esta semana? ¿ajusto el tiempo de preparación?
□ Revisar si alguna exclusión de reclamo que pediste quedó pendiente
```

## El error clásico

Trabajar "cuando entran los pedidos" en vez de a hora fija. El vendedor que revisa el panel cinco
veces al día y empaca de a uno cree que es más ágil, y en realidad tarda el triple, se distrae, y
un martes cualquiera se le pasa un pedido entero. Empacar por lotes a hora fija es más rápido,
menos propenso al error, y deja el día libre para lo que sí hace crecer la cuenta.

**La operación diaria no se optimiza con velocidad: se optimiza con horario.**

## Relacionados

`102` Flex · `104` colecta y puntos · `110` empacar sin perder plata · `111` embalaje que evita
reclamos · `112` el tiempo que prometes · `113` la demora y su costo · `119` entrega fallida ·
`123` inventario en dos canales · `124` auditoría mensual · `126` las tres métricas · `136`
reclamos excluibles · `175` cuándo automatizar · `189` webhooks
