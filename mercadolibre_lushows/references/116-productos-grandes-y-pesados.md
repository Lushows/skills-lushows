# Productos grandes y pesados

Con la tabla oficial en la mano, esto deja de ser opinión: **un producto de más de $60.000 que
pesa 10-20 kg paga $25.200 de envío; el mismo producto a 0,5-1 kg paga $8.200.** El peso no te
encarece un poco el flete: te lo triplica.

## El acantilado, con números oficiales

Costo de envío, reputación verde, producto de más de $60.000 (oficial ML Colombia, verificado
sep-2026):

| Peso facturable | Costo | Multiplicador vs 1 kg |
|---|---|---|
| 0,5 a 1 kg | $8.200 | ×1,0 |
| 3 a 4 kg | $10.100 | ×1,2 |
| 5 a 7 kg | $10.500 | ×1,3 |
| **7 a 10 kg** | **$15.200** | **×1,9** |
| **10 a 20 kg** | **$25.200** | **×3,1** |
| 20 a 30 kg | $41.400 | ×5,0 |
| 30 a 40 kg | $49.000 | ×6,0 |
| 40 a 50 kg | $66.700 | ×8,1 |
| 50 a 60 kg | $69.400 | ×8,5 |
| 100 a 120 kg | $83.400 | ×10,2 |
| Más de 381 kg | $181.300 | ×22,1 |

**El salto de 7 kg es el primero que duele y el de 10 kg es el que mata.** Entre 5-7 kg ($10.500)
y 10-20 kg ($25.200) hay $14.700 de diferencia por venta. Si tu producto está en 8 o 9 kg, bajar
de 7 kg es la palanca de margen más grande que tienes.

## Y si pierdes el verde, se duplica

Con reputación naranja o roja no hay descuento (oficial):

| Peso | Verde | Naranja/roja | Diferencia |
|---|---|---|---|
| 7 a 10 kg | $15.200 | $30.400 | $15.200 |
| 10 a 20 kg | $25.200 | $50.400 | $25.200 |
| 40 a 50 kg | $66.700 | $133.400 | $66.700 |

En producto pesado, perder el verde no es un problema de imagen: es perder **$25.200 en cada venta
de un paquete de 15 kg**. Ver `126`.

## El peso volumétrico empeora todo

ML compara el peso físico con el volumétrico y **usa siempre el valor más alto** (oficial). Los
productos grandes casi nunca facturan por su peso real: facturan por su volumen. Un mueble
desarmado de 12 kg puede facturar como 25 kg por lo que ocupa. Método de cálculo en `109`.

## Por qué el envío gratis los castiga doble

Regla oficial: en productos nuevos **desde $60.000** ofreces descuentos o envío gratis, y ahí el
costo lo asumes tú (con tu descuento por reputación). Los productos grandes casi siempre pasan de
$60.000 — es decir, caen automáticamente en la columna más cara de la tabla **y** en el tramo
donde tú pagas.

| Producto | Precio | Peso | Envío que asumes | % del precio |
|---|---|---|---|---|
| Accesorio | $70.000 | 0,8 kg | $8.200 | 11,7% |
| Electrodoméstico chico | $250.000 | 8 kg | $15.200 | 6,1% |
| Mueble | $400.000 | 18 kg | $25.200 | 6,3% |
| Mueble grande | $900.000 | 45 kg | $66.700 | 7,4% |

Ahora súmale la comisión, que es **8% a 22%** según categoría y cuotas (oficial). Un mueble de
$400.000 puede estar entregando 6,3% en flete más 15% en comisión: **21,3% antes del costo del
producto**. Esa es la razón estructural por la que Hogar/decoración tiene apenas **1,5% de
participación del e-commerce colombiano**: la logística de lo grande frena la categoría.

## Las cinco salidas

| Salida | Cuándo sirve |
|---|---|
| **Bajar de escalón de peso** | Si estás a menos de 15% del corte. La mejor de todas |
| **Vender desarmado o plegado** | Muebles, estanterías, gimnasio. Reduce volumen enormemente |
| **Flex en tu ciudad** | Entregas tú, el costo es tuyo pero controlado (`102`) |
| **Subir el precio y absorberlo** | Solo si tu categoría lo aguanta; mira a la competencia |
| **No venderlo en ML** | Veredicto honesto en algunos casos. Ver abajo |

La segunda merece énfasis: **vender desarmado puede ser la diferencia entre viable e inviable.**
Una mesa armada factura por volumen enorme; la misma mesa plana en caja puede bajar dos o tres
escalones.

## Full y lo grande: la trampa doble

Los escalones de tamaño de Full son **Pequeño** hasta 15×20×20 cm y 10,5 kg, **Mediano** hasta
19×35×38 cm, **Grande** hasta 60×70×80 cm, **Extragrande** por encima (oficial).

Cargos mensuales por unidad de stock antiguo para producto **grande**: $3.600 de los 4 a 6 meses,
**$64.100** de 6 a 12, **$110.000** pasado el año. Extragrande: hasta **$149.900 mensuales por
unidad** (oficial ML Colombia, verificado sep-2026).

**Un producto grande de rotación lenta en Full es la peor combinación posible del marketplace
colombiano.** Si es grande y no rota en menos de 120 días, no entra a Full. Punto. Ver `108`.

## Cuándo un producto grande sí funciona

```
□ Precio alto: el flete de $25.200 pesa 3% en un producto de $800.000, no 30%
□ Margen bruto grande, de los que aguantan comisión + flete
□ Se puede desarmar o plegar
□ Venta local con Flex, donde controlas el costo
□ Rotación rápida si va a Full, o directamente fuera de Full
□ Categoría donde la competencia también es grande: todos pagan lo mismo
```

El último punto es el que decide: si tu competidor vende lo mismo, él también paga $25.200. El
problema no es el flete alto, es el flete alto con precio bajo.

## El error clásico

Calcular el margen de un producto grande con un flete estimado "de unos $10.000". La tabla oficial
dice $25.200 para 10-20 kg de un producto de más de $60.000. Esa diferencia de $15.200 por venta
es la razón por la que el vendedor de muebles "vende bien pero no le queda nada".

**Antes de publicar algo grande, busca su peso facturable en la tabla de `100` y réstalo del
precio. Si después de eso no queda margen, el producto no es viable en ML.**

## Relacionados

`100` tarifas oficiales de envío · `109` peso volumétrico · `110` empacar sin perder plata · `102`
Flex · `105` cuándo conviene Full · `107` costo de almacenamiento · `108` inventario viejo · `117`
frágiles · `122` logística propia · `124` auditoría mensual · `126` las tres métricas · `75` el
cálculo del margen · `79` el umbral del envío gratis · `84` el producto que no sirve para ML
