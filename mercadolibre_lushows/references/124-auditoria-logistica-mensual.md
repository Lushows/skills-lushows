# Auditoría logística mensual

Módulo de cierre del bloque. Una hora al mes, siempre el mismo día, con los mismos seis números.
Herramienta autónoma: no necesitas leer nada más para ejecutarla, y si un número se sale de rango,
el módulo te dice a dónde ir.

## Los seis números

| # | Métrica | Fuente | Umbral de alarma |
|---|---|---|---|
| 1 | Costo real de envío por venta | `GET /shipments/$ID/costs`, panel | >12% del precio promedio |
| 2 | Tasa de envíos incorrectos | Panel de reputación | 12% a 60 d · 15,5% a 365 d · 10% ML |
| 3 | Tasa de reclamos por daño o faltante | Tu registro + panel | 3,5% de ventas con reclamos |
| 4 | Inventario viejo en Full | Panel de Full, antigüedad | Cualquier SKU con más de 90 días |
| 5 | Tasa de cancelaciones tuyas | Panel de reputación | 2,5% a 60 d · 4% a 365 d · 1,5% ML |
| 6 | Zonas problemáticas | Tu propio historial | Destino con el doble de tu tasa promedio |

Los umbrales de las filas 2, 3 y 5 son oficiales ML Colombia, verificados sep-2026. Son los
límites para **conservar el verde** — y conservar el verde vale el 50% de descuento en todos tus
envíos.

## Por qué esa hora al mes se paga sola

Perder el verde te deja sin descuento en envíos: un producto de más de $60.000 y 1 kg pasa de
**$8.200 a $16.400** (oficial). Con 150 ventas al mes, eso son **$1.230.000 mensuales**.

**La auditoría no es orden: es la hora mejor pagada de tu mes.**

## 1. Costo real de envío por venta

```
□ Exporta las ventas del mes con su costo de envío real (no el estimado)
□ COSTO PROMEDIO POR VENTA = total de envíos asumidos ÷ número de ventas
□ % SOBRE PRECIO = costo promedio ÷ precio promedio de venta
□ Compara contra la tabla oficial de `100`: ¿coincide con el escalón que esperabas?
□ Si no coincide, tu peso facturable es mayor al que crees → peso volumétrico (`109`)
```

| Resultado | Acción |
|---|---|
| Menos del 8% del precio | Sano |
| 8% a 12% | Vigila: revisa empaque (`110`) |
| Más del 12% | Problema de escalón o de precio. Ver `109`, `110`, `116` |
| Mucho mayor a lo esperado | Estás pagando volumen, no peso (`109`) |

## 2. Tasa de envíos incorrectos (demora)

```
□ Panel → Reputación → envíos incorrectos (se recalcula a diario)
□ O: GET /users/$USER_ID → seller_reputation.metrics.delayed_handling_time
□ Confirma si te miden a 60 o a 365 días (depende de si tienes 60+ ventas)
□ Lista las demoras del mes y anota la CAUSA de cada una
```

| Nivel | Acción |
|---|---|
| Menos de 5% | Sano |
| 5% a 8% | Alerta temprana: revisa la rutina diaria (`114`) |
| 8% a 12% | Sube el tiempo de preparación HOY (`112`) |
| Más de 12% | Ya perdiste o estás por perder el verde (`113`) |

## 3. Tasa de daño y faltantes

```
□ Cuenta los reclamos del mes que fueron de CALIDAD o de PRODUCTO INCOMPLETO
□ Divide por ventas del mes: esa es la tasa que cuenta contra ti
□ Desglósala POR SKU: casi siempre uno o dos generan todo
□ Desglósala POR DESTINO: puede ser una ruta, no el producto
```

| Nivel | Acción |
|---|---|
| Menos de 1% | Sano |
| 1% a 2% | Revisa embalaje del SKU culpable (`111`) |
| 2% a 3,5% | Zona de alerta: el techo del verde es 3,5% |
| Más de 3,5% | Pausa el SKU o evalúa viabilidad (`117`) |

## 4. Inventario viejo en Full

El cargo es **mensual por unidad** y arranca a los 4 meses (2 meses en Supermercado), oficial:

| Tamaño | 4 a 6 meses | 6 a 12 meses | Más de 12 meses |
|---|---|---|---|
| Pequeño | $690 | $6.500 | $13.100 |
| Mediano | $1.100 | $16.200 | $29.200 |
| Grande | $3.600 | $64.100 | $110.000 |
| Extragrande | $9.600 | $117.700 | $149.900 |

```
□ Lista los SKUs en Full ordenados por antigüedad
□ ANTIGÜEDAD PROYECTADA = inventario actual ÷ unidades vendidas por día
□ Marca todo lo que pase de 90 días: quedan 30 días de ventana barata
□ Marca todo lo que pase de 120 días: ya está pagando
□ Marca todo lo que pase de 180 días: el cargo se multiplicó entre 9 y 18 veces
□ Para cada marcado: liquidar, pautar, retirar o dejar. Decide, no dejes correr (`108`)
□ Verifica los escalones de tamaño: un SKU mal medido paga como grande
```

## 5. Tasa de cancelaciones tuyas

El techo más estrecho de todos, y el único con riesgo de suspensión: **más del 2,5% de ventas
canceladas puede llevar a la suspensión de la cuenta para vender** (oficial).

```
□ Panel → Reputación → canceladas por ti
□ Recuerda: las que cancela el COMPRADOR no cuentan contra ti (oficial)
□ Las devoluciones NO son cancelaciones (oficial)
□ Para cada cancelación del mes, anota la causa real
□ Si la causa fue falta de stock, el problema está en `123`, no en logística
```

## 6. Zonas problemáticas

```
□ Agrupa las ventas del mes por ciudad o departamento
□ Calcula por destino: % reclamos, % entregas fallidas, días de entrega
□ Con menos de 10 envíos a un destino, no saques conclusiones
□ Marca en rojo los destinos con el doble de tu tasa promedio
□ Decide: reforzar embalaje, avisar antes, o dejar de vender allá (`115`)
```

## El cierre: tres decisiones

Toda auditoría termina en decisiones escritas, no en observaciones:

```
□ UNA cosa que cambio en el empaque este mes
□ UN SKU que saco, liquido o repongo distinto
□ UN número que quiero mover el mes que viene, con meta concreta
```

Más de tres cambios a la vez y no vas a saber cuál funcionó.

## El error clásico

Hacer la auditoría solo cuando algo ya salió mal. Para entonces el termómetro ya cayó, el cargo de
stock antiguo ya se facturó, y las decisiones baratas —subir el tiempo de preparación, liquidar al
día 90— ya no están disponibles. La auditoría vale porque se hace cuando todo parece estar bien.

**Fija el día. El primer lunes de cada mes, una hora, estos seis números.**

## Relacionados

`100` tarifas oficiales de envío · `104` colecta y puntos · `105` cuándo conviene Full · `107`
costo de almacenamiento · `108` inventario viejo · `109` peso volumétrico · `110` empacar sin
perder plata · `111` embalaje que evita reclamos · `112` el tiempo que prometes · `113` la demora
y su costo · `114` el flujo diario · `115` zonas difíciles · `117` frágiles · `123` inventario en
dos canales · `126` las tres métricas · `136` reclamos excluibles · `75` el cálculo del margen
