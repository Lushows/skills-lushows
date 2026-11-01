# Planear el inventario

Comprar de más congela tu plata y, en Full, te cobran por tenerla ahí. Comprar de menos te hace
cancelar ventas — y las cancelaciones son la única métrica con umbral publicado que puede cerrarte
la cuenta. El inventario es donde el marketplace castiga los dos extremos, y no los castiga igual.

## Los dos castigos, cara a cara

| Te quedas corto | Te quedas largo |
|---|---|
| Cancelas por falta de stock → **penaliza tu reputación**, y esa cancelación **no** es excluible | Plata congelada que no puedes usar en el SKU que sí rota |
| Más de **2,5% de canceladas → suspensión de la cuenta** (oficial, sep-2026) | En Full, cargo extra por inventario viejo tras ~120 días (**no verificado para CO**, `108`) |
| El cero saca la publicación de la competencia y de la puja de catálogo (`140`) | Producto que se pasa de moda o de temporada: se liquida bajo costo |
| Al reponer, la publicación "revive como más nueva o menos confiable" | Mercancía que ocupa el cupo que necesitaba otro SKU |
| El quiebre **reinicia el aprendizaje de la pauta** y la encarece | — |

**Los dos duelen, pero solo uno te quita la cuenta.** Ante la duda, quédate largo en tu SKU
estrella y corto en los experimentos.

## Las tres cifras que gobiernan todo

| Cifra | Cómo se calcula | Para qué |
|---|---|---|
| **Venta diaria promedio** | Unidades vendidas en 28 días ÷ 28 | Base de todo lo demás |
| **Días de inventario** | Stock actual ÷ venta diaria | Cuánto aguanto sin reponer |
| **Rotación anual** | 365 ÷ días de inventario promedio | Cuántas veces al año recupero mi plata |

Toma 28 días, no 30: 28 son exactamente cuatro semanas y no te distorsiona el promedio según cuántos
fines de semana cayeron en el mes.

## El punto de reposición

La fórmula que evita el 90% de los quiebres:

```
Punto de reposición = (venta diaria × días que tarda el proveedor) + colchón de seguridad

Colchón de seguridad = venta diaria × 7      (piso; sube a 14 en temporada, ver `167`)
```

Ejemplo: vendes 6 unidades/día, tu proveedor tarda 20 días.
Punto de reposición = (6 × 20) + (6 × 7) = 120 + 42 = **162 unidades**.
Cuando el stock toque 162, la orden de compra ya debió salir.

**El error no es comprar poco: es comprar tarde.** Verifica cualquier número con
`Matematicas_lushows` antes de girar plata.

## Cuántos días de inventario conviene tener

| Situación | Días de inventario objetivo | Por qué |
|---|---|---|
| SKU estrella, venta estable, propio | 45 - 60 | El quiebre aquí te borra el mes (`172`) |
| SKU nuevo en prueba | 15 - 21 | Todavía no sabes si vende |
| Producto de temporada | Lo que dure la temporada + 0 | Lo que sobra se liquida, no se guarda |
| Proveedor de importación (60-90 días) | 90 - 120 | El tiempo de tránsito manda |
| Producto con caducidad | Nunca más de la mitad de su vida útil | El resto lo consume el canal |

> ⚠️ **Sin verificar para Colombia (sep-2026).** Estos rangos son criterio de gestión de
> inventario, no una política de Mercado Libre. Ajústalos con tu propio histórico de `166`.

## Full cambia la ecuación

Full acelera la venta y mejora tu posición en el catálogo (`105`), pero convierte el inventario
largo en un costo explícito: el almacenamiento se cobra por día y hay un cargo adicional cuando el
producto lleva mucho tiempo sin venderse.

| Dato | Estado |
|---|---|
| Costo de almacenamiento en Full Colombia | **No verificado.** Las cifras que circulan son **de México** |
| Cargo por inventario viejo | Patrón regional de ~120 días sin venderse. **No verificado para CO** |
| Centro de fulfillment en Colombia | **Funza, Cundinamarca** (una sola fuente) |

> ⚠️ **Sin verificar para Colombia (sep-2026).** Lee la tarifa real en tu panel de Full antes de
> mandar mercancía: es la única fuente confiable, y cambia por peso y dimensiones.

Regla práctica mientras no tengas la tarifa: **al SKU que rota manda 45-60 días de inventario a
Full y guarda el resto en tu bodega.** Reponer a Full es barato; sacar mercancía vieja de Full es
caro y lento (`109`).

## El plan de compra en seis pasos

```
□ 1. Saca la venta diaria de los últimos 28 días por SKU
□ 2. Réstale los días en que estuviste en cero (esas ventas nunca se contaron)
□ 3. Ajusta por el calendario: ¿viene pico o viene cuesta de enero? (`167`)
□ 4. Calcula el punto de reposición con el tiempo REAL de tu proveedor, no el prometido
□ 5. Revisa la caja: ¿esta compra te deja sin plata para reponer el SKU estrella?
□ 6. Decide por SKU, nunca "un pedido grande al proveedor para ahorrar en flete"
```

El paso 2 es el que nadie hace. Si estuviste 6 días sin stock en un mes, tu venta diaria real es
sobre 22 días, no sobre 28 — y estás subestimando la demanda un 27%.

## Rotación contra margen: la tabla que decide

Un producto con 40% de margen que rota una vez al año rinde menos que uno con 12% que rota ocho
veces. La plata que importa es la que vuelve.

| SKU | Margen | Rotaciones/año | Retorno anual sobre el capital |
|---|---|---|---|
| A | 40% | 1,5 | 60% |
| B | 25% | 4 | 100% |
| C | 12% | 8 | 96% |

Con capital chico gana la velocidad, no el margen. Con capital grande y bodega propia puedes
aguantar el A. **Pregúntate cuántas veces al año da la vuelta tu plata, no cuánto margen tiene la
etiqueta.**

## El error clásico

Comprar el lote grande porque el proveedor da mejor precio por volumen, sin mirar cuántos meses de
inventario son. El descuento del 8% por comprar el doble no compensa seis meses de plata quieta,
más el riesgo de que el producto se quede — y en Full, más el cargo por inventario viejo. **Un
descuento por volumen es un préstamo que le haces a tu proveedor con tu propia caja.**

## Señales de que la planeación está mal

| Señal | Diagnóstico |
|---|---|
| Cancelaste 2 ventas o más este mes | Colchón de seguridad demasiado corto (`139`) |
| Tienes SKUs con más de 120 días de inventario | Compraste con ilusión, no con dato |
| Liquidas bajo costo cada trimestre | Estás comprando SKUs que no rotan (`172`) |
| Te quedas sin caja justo antes del pico | Compraste el lote grande en el mes equivocado (`167`) |
| Mismo colchón para todos los SKUs | No estás planeando, estás promediando |

## Dónde termina esta skill

Elegir **qué** producto comprar, negociar con el proveedor, importar de China o evaluar un agente
de sourcing es de `dropshipping_lushows`. Financiar la compra, evaluar si el negocio aguanta el
capital de trabajo o proyectar la caja es de `economist_lushows`. Aquí solo resolvemos **cuánto**
de lo que ya vendes debe estar disponible y dónde.

## Relacionados

`105` Full: cuándo conviene · `107` enviar mercancía a Full · `108` el cargo por inventario viejo ·
`109` sacar inventario de Full · `126` las tres métricas · `139` la cancelación y su castigo ·
`140` el quiebre de stock · `165` las métricas que de verdad miras · `166` el tablero semanal ·
`167` estacionalidad en Colombia · `172` el SKU estrella y la dependencia ·
`196` sincronizar stock multicanal
