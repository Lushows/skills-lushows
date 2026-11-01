# Cuándo conviene Full y cuándo no

Módulo de decisión. Con las tarifas oficiales de stock antiguo en la mano, la respuesta dejó de
ser ambigua: **Full se paga con rotación, y el castigo por no tenerla es exponencial.** Este
módulo te dice de qué lado estás antes de mandar la primera caja.

## La tabla honesta

| Variable | Full GANA cuando | Full PIERDE cuando |
|---|---|---|
| Rotación | Alta: sale en semanas | Lenta: meses (mira la tabla de cargos abajo) |
| Tamaño | Pequeño: $690 a los 4 meses | Grande: $3.600 a los 4 meses, $110.000 al año |
| Valor unitario | Desde $60.000: aplica el 50% de descuento | Muy bajo: el bodegaje se lo come |
| Ticket bajo con volumen | Gana por la agrupación de carrito entre vendedores | — |
| Predictibilidad | Vendes parejo | Picos impredecibles, reposición difícil |
| Capital | Puedes inmovilizar inventario | Estás justo de caja |
| Ubicación | Cerca de la Sabana (el traslado lo pagas tú) | Lejos: flete nacional cada vez |
| Fragilidad | Producto robusto | Frágil: no controlas el empaque (`117`) |
| Canales | Vendes solo en ML | Vendes también por fuera con el mismo stock (`123`) |
| Dimensiones | Dentro de las permitidas | Fuera: ni siquiera es apto |

## El número que decide: días de inventario

Todo se reduce a esto, y ahora con cifras oficiales (cargo **mensual por unidad**, resto de
productos, oficial ML Colombia verificado sep-2026):

| Días parado | Meses | Pequeño | Mediano | Grande | Extragrande |
|---|---|---|---|---|---|
| < 120 | < 4 | $0 | $0 | $0 | $0 |
| 120-180 | 4 a 6 | $690 | $1.100 | $3.600 | $9.600 |
| 180-365 | 6 a 12 | $6.500 | $16.200 | $64.100 | $117.700 |
| > 365 | +12 | $13.100 | $29.200 | $110.000 | $149.900 |

En Supermercado el reloj arranca a los **2 meses**, no a los 4 (oficial). Tabla completa en `108`.

**El salto de 4-6 meses a 6-12 meses multiplica el cargo por casi 10 en producto pequeño y por 18
en producto grande.** No es una penalización proporcional: es un despeñadero. Full está diseñado
para que saques el inventario antes del mes cuatro.

## El veredicto por perfil

| Perfil | Veredicto |
|---|---|
| Accesorio pequeño, 50+ unidades/mes, categoría competida | **Entra.** Es el caso ideal |
| Producto de $15.000-$30.000 con volumen | **Entra**, por la agrupación de carrito (`103`) |
| Producto desde $60.000 que rota en 30 días | **Entra.** El 50% de descuento en envío pesa |
| Nicho, 5 unidades/mes, margen alto | **No entres.** Flex o colecta desde tu bodega |
| Muebles, electrodomésticos, grandes | **No entres.** Ver `116` y la fila "grande" arriba |
| Menos de 10 ventas totales | **No puedes:** aún no tienes reputación (requisito oficial) |
| Vendes también en web o WhatsApp | **Entra solo con parte del stock** (`123`) |
| Producto estacional | **Entra con fecha de salida en el calendario** (`108`) |

## El modelo de decisión, con tus números

```
DÍAS DE INVENTARIO = unidades enviadas a Full ÷ unidades vendidas por día

COSTO FULL POR UNIDAD =
    (traslado a bodega ÷ unidades de ese envío)     ← lo pagas tú, oficial
  + (almacenamiento diario × DÍAS DE INVENTARIO)    ← ver `107`
  + cargo por stock antiguo si DÍAS supera 120      ← tabla de arriba
  + envío con 50% de descuento                      ← tabla oficial de `100`
  + comisión de la categoría (8%-22%, oficial)

COSTO PROPIO POR UNIDAD =
    empaque + tu tiempo de despacho + transporte al punto
  + envío con el descuento de TU reputación (50% si eres verde) ← tabla de `100`
  + comisión

GANANCIA DE FULL = (ventas extra por mejor posición × margen unitario)
                   − (COSTO FULL − COSTO PROPIO) × unidades
```

Fíjate en un detalle que cambia el resultado: **si ya eres verde, el descuento de envío del 50% ya
lo tienes sin Full** (oficial: verde, MercadoLíder y sin reputación tienen 50%). Full no te regala
ese descuento: te lo garantiza aunque pierdas el color. El beneficio real de Full está en la
velocidad, la posición y la agrupación de carrito, no en la tarifa.

Para cálculos exactos, rutea a `Matematicas_lushows`. Para viabilidad del negocio,
`economist_lushows`.

## Lo que sigue sin verificarse

> ⚠️ **Sin verificar para Colombia (sep-2026).** Dos números que faltan para cerrar el modelo:
> - La **tarifa diaria de almacenamiento** por unidad y por escalón de tamaño. Léela en
>   Panel → Ventas → Full → costos. Las cifras que circulan son **de México**.
> - La **tarifa de comprar espacio adicional**: ML dice que "varía según la demanda", sin cifra.
>
> Lo que sí está cerrado y es oficial: los cargos por stock antiguo, los requisitos de ingreso,
> los beneficios y la tabla de costos de envío de `100`.

## Cómo probar Full sin arriesgar el negocio

```
□ Elige 2 o 3 SKUs de rotación comprobada, nunca todo el catálogo
□ Manda inventario para 30-45 días, calculado con datos reales
□ Deja stock propio de los mismos SKUs para no depender de la reposición
□ Anota el costo del traslado: es parte del costo por unidad
□ A los 30 días compara: unidades vendidas, posición, cargos reales del panel
□ A los 60 días decide. A los 90 días, si algo no rota, sácalo: el mes 4 cobra
□ Pon en el calendario la fecha del mes 4 de cada envío. Esa alarma vale plata
```

La última línea es el hábito que separa al que gana con Full del que lo financia.

## El error clásico

Entrar a Full para "mejorar la posición" sin tocar nada más. Full mueve una variable de un ranking
que tiene varias, y ninguna logística compensa una reputación naranja, una ficha incompleta o un
precio fuera de mercado. Si tu problema es conversión, Full te trae las mismas visitas que no
compran, ahora pagando bodegaje.

**Full no arregla un producto que no vende: lo vuelve más caro de no vender.**

## Relacionados

`100` tarifas oficiales de envío · `103` Full · `106` ingresar inventario · `107` costo de
almacenamiento · `108` inventario viejo · `109` peso volumétrico · `116` productos grandes · `117`
frágiles · `123` inventario en dos canales · `124` auditoría mensual · `75` el cálculo del margen
· `63` ganar el catálogo · `55` algoritmo
