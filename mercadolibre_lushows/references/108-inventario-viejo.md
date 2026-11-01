# Inventario viejo en Full

El cargo por stock antiguo es el mecanismo que hace que Full sea hostil con la rotación lenta, y
en Colombia está publicado con cifras exactas. Es **mensual, por unidad, y crece de forma
exponencial**: un producto grande olvidado un año cuesta **$110.000 por unidad**.

## Las tablas oficiales

Cargo **mensual por unidad**. Supermercado arranca a los **2 meses**; el resto, a los **4 meses**
(oficial ML Colombia, verificado sep-2026).

*Resto de productos*

| Tamaño | 4 a 6 meses | 6 a 12 meses | Más de 12 meses |
|---|---|---|---|
| Pequeño | $690 | $6.500 | $13.100 |
| Mediano | $1.100 | $16.200 | $29.200 |
| Grande | $3.600 | $64.100 | $110.000 |
| Extragrande | $9.600 | $117.700 | $149.900 |

*Supermercado*

| Tamaño | 2 a 4 meses | 4 a 6 meses | 6 a 12 meses | Más de 12 meses |
|---|---|---|---|---|
| Pequeño | $100 | $690 | $6.400 | $13.100 |
| Mediano | $180 | $1.100 | $16.000 | $29.200 |
| Grande | $400 | $3.600 | $59.900 | $110.000 |
| Extragrande | $1.000 | $9.600 | $110.000 | $149.900 |

Tamaños oficiales: **Pequeño** hasta 15×20×20 cm y 10,5 kg · **Mediano** hasta 19×35×38 cm y 10,5
kg · **Grande** hasta 60×70×80 cm y 10,5 kg · **Extragrande** por encima.

## El castigo es exponencial, no lineal

Esta es la lectura que cambia decisiones. Multiplicadores al pasar de tramo:

| Tamaño | 4-6 m → 6-12 m | 6-12 m → +12 m |
|---|---|---|
| Pequeño | ×9,4 | ×2,0 |
| Mediano | ×14,7 | ×1,8 |
| Grande | ×17,8 | ×1,7 |
| Extragrande | ×12,3 | ×1,3 |

**El salto letal es el mes 6.** Entre el mes 4 y el mes 6 el cargo es una molestia; pasado el mes
6 es una amputación. Un producto mediano que costaba $1.100 al mes pasa a $16.200 al mes — y sigue
costando eso cada mes hasta que salga.

Si tienes 20 unidades de un producto grande varadas un año: 20 × $110.000 = **$2.200.000 al mes**.
Esa es la factura que aparece sin que nadie la haya decidido.

## Por qué mata al vendedor de rotación lenta

| Etapa | Qué pasa |
|---|---|
| Meses 1-3 | Almacenamiento corriente. Molesto pero manejable |
| Mes 4 | Arranca el cargo mensual por unidad |
| Mes 6 | El cargo se multiplica entre 9 y 18 veces |
| Mes 12 | Vuelve a subir y ya llevas medio año pagándolo |

Y un costo que no aparece en la factura: **la plata que pagaste por ese inventario está quieta**.
Un producto que rota en 15 días te deja 24 vueltas de caja al año; uno que rota en 200 te deja
menos de
2. Con capital pequeño, la velocidad de caja pesa más que el margen.

**El inventario viejo no te cobra una vez: te cobra todos los meses, cada vez más, y además te
tiene la plata secuestrada.**

## Las señales de alarma, con fechas

| Señal | Día | Acción |
|---|---|---|
| El SKU vende menos de lo proyectado | 30 | Revisa precio, ficha y fotos (`25`, `54`) |
| Inventario para más de 60 días | 60 | Deja de reponer ese SKU |
| Cero ventas en 45 días | 45 | Decide: bajar precio, pautar o sacar |
| **Día 90** | 90 | **Última ventana barata: quedan 30 días antes del cargo** |
| Día 120 | 120 | Ya estás pagando. Liquida o retira ya |
| Día 180 | 180 | El cargo se multiplicó. Cualquier descuento es más barato |

El día 90 es el hito. Ponlo en el calendario el mismo día que mandas el envío a bodega (`106`).

## Las cuatro salidas, ordenadas

**1. Venderlo con descuento.** Casi siempre gana. Perder 30% de margen hoy es más barato que pagar
$16.200 por unidad al mes. Dos cuidados: la SIC vigila los "descuentos falsos" —el precio final
debe corresponder al promocional, sin costos ocultos— y un cambio brusco de precio puede disparar
una pausa de "inactiva para revisar" (`73`). Baja en dos o tres pasos, no de un salto.

**2. Pautarlo para liquidar.** Product Ads se cobra por CPC (oficial CO). Aquí el ACOS alto es
deliberado: estás comprando salida de inventario, no rentabilidad. Es el caso de la estrategia de
**Visibilidad, ACOS mayor a 30%** (oficial ML Colombia, verificado sep-2026). Ver `150`.

**3. Retirarlo de Full.** Detienes el sangrado pero pagas el retiro y el flete, y recuperas
producto que sigue sin venderse. Sirve si lo vendes por otro canal (`123`).

**4. Dejarlo "a ver si sale".** La peor y la más común. Es pagar cada mes, cada vez más, por una
apuesta que ya perdiste.

```
□ Regla: si en 30 días de descuento agresivo no rota, retíralo o liquídalo
□ Nunca repongas un SKU que ya tiene inventario viejo en bodega
□ El costo hundido no cuenta: la pregunta no es cuánto te costó, es cuánto te sigue costando
```

Si la decisión toca la viabilidad del negocio completo, rutea a `economist_lushows`.

## La prevención, que vale diez veces más

| Práctica | Efecto |
|---|---|
| Mandar solo 30-45 días de venta comprobada (`106`) | Nunca te acercas al mes 4 |
| Revisar antigüedad cada mes (`124`) | Detectas al día 60, no al día 200 |
| Probar SKUs nuevos desde tu bodega, no desde Full | El SKU que fracasa no te cuesta cargos |
| Medir bien el producto empacado | Un SKU mal clasificado paga como grande |
| Planear la salida del estacional | Navidad entra en octubre y sale en enero |
| Nunca reponer "por si acaso" | El "por si acaso" es el 80% del inventario viejo |

Hot Sale Colombia tiene edición del **19 al 23 de octubre de 2026** (verificado) y diciembre es
diciembre. Si mandas para esas fechas, escribe la fecha de retiro de lo que sobre **el mismo día
que mandas el envío**. Enero + 4 meses = mayo: ahí empieza a correr el cargo de lo que no
vendiste.

## La cuenta que puedes hacer hoy

```
ANTIGÜEDAD PROYECTADA = inventario actual en Full ÷ unidades vendidas por día

> 120 días  →  vas a pagar cargo. Mira tu escalón de tamaño en la tabla
> 180 días  →  vas a pagar el cargo multiplicado. Actúa esta semana
```

Córrela sobre todos tus SKUs en Full una vez al mes. Siempre aparecen dos o tres que llevan meses
ahí y nadie había mirado.

## El error clásico

Ver el inventario en Full como "activo" y no como "costo corriendo". En el balance es un activo;
en la caja es un cargo mensual creciente. El vendedor que revisa Full solo cuando llega la factura
ya perdió: cuando el cargo aparece, el producto lleva cuatro meses ahí y la salida barata
(liquidar al día 90) ya no existe.

## Relacionados

`103` Full · `105` cuándo conviene Full · `106` ingresar inventario · `107` costo de
almacenamiento · `116` productos grandes · `123` inventario en dos canales · `124` auditoría
mensual · `150` ACOS sano · `75` el cálculo del margen · `73` pausas e infracciones
