# Qué hacer con el SKU que no deja

Ya lo identificaste en la tabla de `97`: vende, se mueve, y no deja plata. Hay exactamente cuatro
salidas —subir precio, bajar costo, volverlo kit, o matarlo— y un criterio para elegir entre ellas.
Lo que no es una salida es dejarlo ahí "porque trae tráfico".

## Las cuatro salidas

| # | Salida | Qué cambia | Cuándo es la correcta |
|---|---|---|---|
| 1 | **Subir el precio** | El ingreso | Cuando estás por debajo del líder y tu ficha aguanta |
| 2 | **Bajar el costo** | El producto o el envío | Cuando hay grasa real: proveedor, empaque, reputación |
| 3 | **Volverlo kit** | El ticket | Cuando el problema es que el producto es barato |
| 4 | **Matarlo** | El catálogo | Cuando las tres anteriores ya se intentaron |

Recórrelas en ese orden. La 1 es gratis, la 2 toma semanas, la 3 toma días, y la 4 es definitiva.

## Salida 1: subir el precio

Antes de subir, mira dónde estás respecto al umbral:

| Tu precio actual | Qué hacer |
|---|---|
| Entre $60.000 y ~$66.000 | **Estás en la zona muerta.** Sube a $69.900+ o baja a $59.900 (`79`) |
| Justo debajo de $60.000 | No lo cruces por poco: cruzar cuesta $3.900-$36.200 según el peso |
| Sobre $70.000 | Sube en pasos de 3% cada 10 días, midiendo conversión |
| Bajo $15.000 | Subir no basta: vete a la salida 3 (`86`) |

Cómo subir sin romper nada:

```
□ Verifica dónde está el líder antes de mover (ver 70)
□ Sube en pasos: un salto brusco puede dejarte "inactiva para revisar"
□ Si tienes repricer activo, súbele el piso primero o te lo pisa (ver 90)
□ Mide conversión 10 días después, no al día siguiente
□ Si la conversión no cayó, vuelve a subir
```

La mayoría de los vendedores puede subir 5-8% sin perder conversión y nunca lo intenta.

## Salida 2: bajar el costo

Tres frentes, y el segundo es el que casi nadie ve:

| Frente | Palanca | Cuánto puede valer |
|---|---|---|
| **Producto** | Negociar volumen, cambiar proveedor, importar directo | Variable |
| **Envío** | Recuperar el verde: de naranja a verde el envío pasa de **$16.400 a $8.200** en 1 kg (oficial) | **$8.200 por venta** |
| **Envío** | Reducir peso volumétrico: empaque ajustado, sin aire | Un rango de peso = $100 a $10.000 |
| **Operación** | Alistar en lote, empaque más barato, menos manipulación | $500-$2.000 por unidad |

La fila de la reputación es la más rentable y la más ignorada: **no depende de negociar con nadie**.
Bajar tu tasa de reclamos por debajo de 3,5% y recuperar el verde te devuelve la mitad del costo de
envío en todo el catálogo (`78`, `96`).

Segunda palanca gratis: **el rango de peso**. Pasar de 3,1 kg a 2,9 kg te ahorra $1.500 por envío;
de 7,1 kg a 6,9 kg te ahorra $4.700. Una caja más pequeña puede valer más que una renegociación.

## Salida 3: volverlo kit

La salida correcta cuando el problema es el ticket, y la que recomienda la propia ayuda oficial:
*"Puedes vender productos de menor valor ofreciendo packs o combos."*

```
□ El kit cruza $60.000 con holgura: apunta a $70.000+, no a $61.000
□ El peso del kit queda JUSTO DEBAJO de un salto de rango (ver 87)
□ El kit es un ítem nuevo con su propio SKU, no una variante
□ Mantengo el suelto publicado como ancla de precio (ver 88)
□ Corrí margen_ml.py con el precio y el peso DEL KIT
```

Si el kit tampoco deja, el problema no era el ticket: era el producto (`84`).

## Salida 4: matarlo

Criterio de decisión. Mata el SKU si se cumplen tres o más:

```
□ Margen negativo o bajo 5% después de intentar las salidas 1, 2 y 3
□ Su utilidad total mensual es negativa
□ Su tasa de devolución supera el 15% (ver 95)
□ Genera reclamos que cuentan para la reputación (ver 96)
□ El líder de la categoría vende por debajo de tu costo (ver 83)
□ Pesa más de 10 kg y su precio está sobre $60.000 (ver 84)
□ Lleva más de 4 meses en Full sin rotar: el cargo por stock antiguo es exponencial
```

Ese último punto merece números: los cargos por stock antiguo en Full son **mensuales por unidad** y
empiezan a los **4 meses** (2 meses en Supermercado). Un producto grande olvidado un año cuesta
**$110.000 por unidad** (oficial ML Colombia, verificado sep-2026). Un SKU que no deja **y** está en
Full no es un SKU flojo: es una fuga activa.

### Cómo matarlo bien

| Paso | Detalle |
|---|---|
| 1. Liquida el stock | Precio de liquidación, con fecha de fin. Contabilízalo como pérdida, no como venta |
| 2. Saca el inventario de Full primero | Cada mes que sigue ahí cuesta, y el traslado corre por tu cuenta |
| 3. **No lo dejes en stock cero** | `available_quantity: 0` pasa el ítem a `paused` con `out_of_stock`, lo saca de la competencia y del catálogo |
| 4. Despublica de verdad | Si no vas a reponer, cierra la publicación |
| 5. Documenta por qué | Para no volver a comprarlo dentro de un año |

El paso 3 importa: dejar publicaciones en stock cero "por si acaso" ensucia tu catálogo y, al
reponer, la publicación revive como más nueva o menos confiable y debe reconstruir señales.

## Lo que NO es una salida

| Excusa | Por qué no sirve |
|---|---|
| "Trae tráfico a mi tienda" | El tráfico de ML va a la búsqueda, no a tu tienda. No hay cross-sell automático que lo justifique |
| "Es mi producto insignia" | Los productos insignia también pueden perder plata |
| "Si lo quito, bajo en el ranking" | El ranking es por publicación, no por cantidad de publicaciones |
| "Ya compré el inventario" | Costo hundido. Liquida y aprende |
| "Vendiendo más lo compenso" | Con margen negativo, vender más pierde más rápido |

**Un SKU que pierde plata no es una inversión en presencia: es una suscripción mensual a perder
plata.**

## El orden de ataque en un catálogo grande

No los arregles todos a la vez. Ordena por **utilidad total mensual ascendente** (`97`) y trabaja
de arriba hacia abajo: el SKU que pierde $277.200 al mes primero, el que pierde $12.000 después.
Los cinco peores suelen explicar casi toda la fuga.

## El error clásico

Bajar el precio del SKU que no deja, "para que rote y salga del inventario". Rota, sí, y cada
rotación cuesta más. Si el margen es negativo, vender rápido es perder rápido.

El segundo: matar el SKU sin revisar antes si el problema era la columna de envío. Un SKU a $61.000
que se mueve a $59.900 puede pasar de margen 4,8% a 12% sin tocar nada más (`79`).

## Relacionados

`78` el envío que pagas tú · `79` el umbral de los $60.000 · `82` la calculadora de margen · `83`
precio mínimo viable · `84` el producto que no sirve para ML · `86` por qué los productos baratos
pierden · `87` subir el ticket con kits · `88` precio psicológico · `90` el repricer · `95` costo de
la devolución · `96` costo del reclamo · `97` margen por SKU · `99` revisión mensual · `100`-`124`
Full y stock antiguo
