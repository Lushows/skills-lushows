# El quiebre de stock

Es la causa número uno de cancelaciones, y las cancelaciones son lo único que te puede cerrar la
cuenta. Además el stock en cero te saca de la competencia y te obliga a reconstruir la señal de la
publicación desde abajo. Es el problema operativo más caro del marketplace.

## Los dos daños, que son distintos

| Daño | Qué pasa |
|---|---|
| **Vendiste lo que no tenías** | Cancelas → métrica de canceladas → 2,5% → riesgo de cuenta (`139`) |
| **Publicaste stock cero** | La publicación sale de la competencia y de la puja de catálogo |

El segundo se subestima. Con `available_quantity: 0` el ítem pasa a `paused` con sub-estado
`out_of_stock` (oficial, verificado sep-2026). Y al reponer, la publicación **revive como más nueva
o menos confiable** y debe reconstruir sus señales de conversión (confianza MEDIA).

**Quedarte sin stock no es una pausa: es un reinicio parcial de la publicación que tardaste meses en
posicionar.** Y si estabas pautando, reinicia también el aprendizaje de la campaña y encarece el
clic futuro (`150`).

## Cómo evitarlo: las cuatro capas

```
□ 1. Colchón de seguridad: publica 1-2 unidades MENOS de las que tienes físicas
□ 2. Sincronización: una sola fuente de verdad del inventario, no una hoja por canal
□ 3. Punto de reposición: pide antes de llegar a cero, calculado con tu rotación real
□ 4. Pausa a tiempo: mejor pausar tú que cancelar después
```

### Capa 1 — el colchón

Es la mitigación estándar y la más barata. Si tienes 10 unidades, publica 8. Pierdes 2 ventas
potenciales y evitas la cancelación que te cuesta 60 días de métrica.

El tamaño del colchón depende del riesgo:

| Situación | Colchón sugerido |
|---|---|
| Un solo canal, conteo diario | 1 unidad |
| Varios canales sin integración | 2-3 unidades |
| Producto con rotación alta | Más grande: el riesgo es de minutos |
| Full (el stock lo tiene ML) | No necesitas colchón: ML sabe cuánto hay |

Ese último punto es un argumento real a favor de Full que no suele mencionarse: **Full elimina de
raíz el quiebre por descoordinación**, porque el inventario y la venta viven en el mismo sistema
(`105`).

### Capa 2 — la sincronización

La API de Mercado Libre **no tiene reserva de stock cross-canal ni bloqueo atómico** (análisis, no
texto oficial). Nadie te va a evitar la sobreventa: la tienes que evitar tú.

| Escala | Solución |
|---|---|
| Pocos SKU, un canal | Conteo manual diario y colchón |
| Varios canales | Un sistema que sea la única fuente de verdad, y ML lee de ahí |
| Volumen | Webhooks `orders_v2` que descuentan al instante, no polling (`186`, `196`) |
| Multi-bodega | `PUT /user-products/$USER_PRODUCT_ID/stock/type/$SELLER_WAREHOUSE` — el `PUT /items` con `available_quantity` **se ignora o da error** con stock multi-origen (oficial, verificado sep-2026) |

Esa última fila rompe muchas integraciones caseras: el desarrollador actualiza por el endpoint de
siempre, la API responde sin error visible, y el stock nunca se movió. Ver `196`.

### Capa 3 — el punto de reposición

```
punto de reposición = (ventas diarias promedio × días que tarda el proveedor) + colchón
```

Ejemplo: vendes 4 al día, el proveedor tarda 7 días, colchón de 5 → pides cuando te quedan 33
unidades, no cuando te quedan 3. Ejecuta el número con la calculadora de la skill; si el cálculo
debe ser exacto, rutea a `Matematicas_lushows`.

En temporada alta las ventas diarias suben y el proveedor tarda más: **las dos variables se mueven
en tu contra al mismo tiempo**. Antes de Hot Sale (19-23 de octubre de 2026) o de diciembre, sube el
punto de reposición, no lo dejes igual (`163`).

### Capa 4 — pausar a tiempo

Si vas a quedar sin stock, **pausa tú antes de cancelar**. Pausar cuesta posición; cancelar cuesta
métrica y puede costar la cuenta.

| Opción | Costo |
|---|---|
| Pausar la publicación | Posición y visitas, recuperables |
| Bajar el stock a 1 y subir el precio | Frena la venta sin pausar del todo |
| Dejarlo publicado y cancelar | Métrica de canceladas + opinión negativa + riesgo de cuenta |

La segunda opción es un truco útil: subir el precio reduce la conversión sin sacarte de la
competencia. No abuses —el precio es variable de catálogo (`63`)— pero para tapar tres días de
espera de mercancía sirve.

## El caso especial de Full

En Full el stock lo custodia Mercado Libre, así que no cancelas por descoordinación. Pero aparece el
problema inverso: **el inventario viejo cuesta plata**, con cargo mensual por unidad desde los 4
meses (2 meses en Supermercado), y el castigo es exponencial (oficial ML Colombia, verificado
sep-2026). Un producto grande olvidado un año en Full cuesta $110.000 por unidad. Ver `108`.

Traducción: en Full el error no es quedarte corto, es quedarte largo. Son dos disciplinas distintas.

## Señales tempranas

```
□ Un SKU que pasó de 10 ventas/semana a 25 sin que hicieras nada
□ Una campaña de Ads recién encendida sobre un SKU con inventario justo (`150`)
□ El proveedor avisando que "está demorado"
□ Una publicación que entró al catálogo y empezó a vender el triple (`63`)
□ Cualquier lunes después de un fin de semana de ofertas
```

Las dos del medio son las que matan: encender pauta sobre stock corto es exactamente la forma de
convertir una campaña exitosa en una cancelación.

## El error clásico

Publicar todo el inventario disponible para "no perder ni una venta". Es la mentalidad de tienda
física aplicada a un sistema donde el cliente paga primero. **Publicar de menos cuesta una venta;
publicar de más cuesta la cuenta.**

El segundo error clásico: reponer y esperar que la publicación vuelva sola a donde estaba. No
vuelve. Después de un stock cero hay que empujar la publicación otra vez — precio, ficha, y a veces
un empujón de Ads para reconstruir la señal de conversión (`55`, `150`).

## Checklist semanal de stock

```
□ Revisar los 10 SKU de mayor rotación contra el inventario físico
□ Verificar que el colchón esté aplicado en los publicados
□ Revisar qué SKU están por debajo del punto de reposición
□ Revisar qué SKU llevan más de 3 meses en Full sin rotar (`108`)
□ Pausar lo que no va a alcanzar la semana
```

## Relacionados

`139` la cancelación y su castigo · `126` las tres métricas · `144` plan de defensa de la cuenta ·
`123` stock multicanal · `196` sincronización por API · `105` Full · `108` stock antiguo en Full ·
`55` el algoritmo · `63` ganar el catálogo · `150` ACOS sano · `163` temporadas y Hot Sale
