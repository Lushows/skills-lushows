# El costo de almacenamiento en Full

Guardar producto en la bodega de ML cuesta de dos formas: un almacenamiento corriente cuya tarifa
no está publicada, y un **cargo mensual por unidad de stock antiguo que sí es oficial y es
exponencial**. La segunda es la que decide si Full te sirve.

## Lo que SÍ es oficial: el cargo por stock antiguo

Cargo **mensual por unidad**. Arranca a los **4 meses** en general y a los **2 meses** en
Supermercado (oficial ML Colombia, verificado sep-2026).

*Resto de productos*

| Tamaño | 4 a 6 meses | 6 a 12 meses | Más de 12 meses |
|---|---|---|---|
| Pequeño | $690 | $6.500 | $13.100 |
| Mediano | $1.100 | $16.200 | $29.200 |
| Grande | $3.600 | $64.100 | $110.000 |
| Extragrande | $9.600 | $117.700 | $149.900 |

*Supermercado en Full* — el reloj arranca a los 2 meses

| Tamaño | 2 a 4 meses | 4 a 6 meses | 6 a 12 meses | Más de 12 meses |
|---|---|---|---|---|
| Pequeño | $100 | $690 | $6.400 | $13.100 |
| Mediano | $180 | $1.100 | $16.000 | $29.200 |
| Grande | $400 | $3.600 | $59.900 | $110.000 |
| Extragrande | $1.000 | $9.600 | $110.000 | $149.900 |

Los tamaños, oficiales: **Pequeño** hasta 15×20×20 cm y 10,5 kg · **Mediano** hasta 19×35×38 cm y
10,5 kg · **Grande** hasta 60×70×80 cm y 10,5 kg · **Extragrande** por encima de eso.

Mide tu producto **empacado** contra esos límites. Dos centímetros de más te cambian de columna, y
la diferencia entre mediano y grande a los 6-12 meses es de **$16.200 a $64.100 por unidad**.

## Lo que NO está publicado

> ⚠️ **Sin verificar para Colombia (sep-2026).** La **tarifa de almacenamiento corriente** (la que
> corre antes de los 4 meses) no está publicada. Las cifras que circulan —"$0,036 a $0,040 por día
> para producto mediano"— son **de México**, en pesos mexicanos. No las uses para Colombia.
>
> También sin publicar: el cargo por **comprar espacio adicional** en Full, del que ML solo dice que
> "la tarifa por unidad puede variar según la demanda".
>
> Dónde leer ambos: Panel → Ventas → Full → costos / facturación. Y el resumen de cargos mensual de
> tu cuenta, que es la fuente definitiva.

## Cómo se estructura (el concepto)

| Componente | Significa | En Colombia |
|---|---|---|
| Unidad de cobro | Por unidad, por escalón de tamaño | Confirmado en la tabla de stock antiguo |
| Periodicidad | Mensual | Oficial |
| Escalones por tamaño | Pequeño / mediano / grande / extragrande | Oficial, con medidas |
| Recargo por antigüedad | Cargo creciente por permanencia | Oficial, tablas de arriba |
| Almacenamiento corriente | Tarifa por día antes del recargo | No publicada |
| Compra de espacio | Cargo por unidad | Existe, tarifa no publicada |

## La fórmula que sí puedes usar hoy

Aunque te falte la tarifa diaria, el cargo grande sí lo puedes calcular:

```
DÍAS EN BODEGA = inventario promedio en Full ÷ unidades vendidas por día

Si DÍAS EN BODEGA < 120  →  solo pagas almacenamiento corriente (tarifa del panel)
Si DÍAS EN BODEGA > 120  →  suma el cargo mensual por unidad de la tabla, todos los meses

COSTO DE PERMANENCIA POR UNIDAD =
   (almacenamiento corriente diario × días)  +  Σ (cargo mensual del escalón que te toque)
```

El "Σ" es literal: es **mensual**, se repite. Un producto mediano que lleva 8 meses ahí no paga
$16.200 una vez: paga $16.200 cada mes mientras siga ahí.

Para correr esto con tus cifras exactas, rutea a `Matematicas_lushows`.

## Lo que la tabla te está diciendo

**El almacenamiento no lo determina la tarifa, lo determina tu rotación.** Con el mismo producto:

| Rotación | Días en bodega | Cargo de stock antiguo (mediano) |
|---|---|---|
| Rápida | 30 | $0 |
| Media | 90 | $0 |
| Al límite | 130 | $1.100 ese mes |
| Lenta | 200 | $16.200 **cada mes** |
| Olvidada | 400 | $29.200 **cada mes** |

Entre "media" y "lenta" no hay un aumento: hay un abismo. Full está diseñado para que saques el
inventario antes del mes cuatro, y te cobra en serio cuando no lo haces.

## Dónde entra en tu margen

```
precio publicado (con IVA)
  – IVA
  = base sin IVA
      – comisión de la categoría (8% a 22%, oficial; sobre el precio CON IVA)
      – envío según la tabla oficial de `100`, con tu descuento por reputación
      – empaque y costos propios  ← AQUÍ: almacenamiento, stock antiguo y traslado a bodega
      – costo del producto
  = utilidad
```

Estructura completa en `75`. El punto: el almacenamiento **no es un gasto administrativo**, es
costo variable por unidad y tiene que estar dentro del precio.

## El costo que se olvida: el traslado

El traslado a la bodega **corre por tu cuenta** (oficial). Va sumado:

```
COSTO LOGÍSTICO TOTAL POR UNIDAD EN FULL =
    (traslado a bodega ÷ unidades de ese envío)
  + (almacenamiento corriente × días en bodega)
  + cargo mensual de stock antiguo, si aplica
```

Envíos pequeños y frecuentes suben la primera línea. Envíos grandes y espaciados suben la segunda
y te acercan al mes cuatro. **El óptimo está donde se cruzan, y depende de tu ciudad** — ver `103`
sobre la ubicación del centro de fulfillment.

## Cómo auditarlo cada mes

```
□ Baja el detalle de cargos de Full del mes
□ Divide el total entre las unidades vendidas desde Full: ese es tu bodegaje por venta
□ Lista los SKUs por antigüedad y marca todos los que pasen de 90 días
□ A los 90 días tienes 30 días para actuar antes del primer cargo. Úsalos (`108`)
□ Cualquier SKU que pagó cargo de stock antiguo y vendió cero: plan de salida inmediato
□ Verifica el escalón de tamaño: un SKU mal medido puede estar pagando como grande
```

Procedimiento completo en `124`.

## El error clásico

Tratar el almacenamiento como un costo fijo mensual ("me cobran tanto por tener Full") en vez de
como un cargo por unidad, por mes y por antigüedad. Quien lo ve como fijo nunca descubre que el
70% de su factura la generan tres SKUs que llevan medio año sin venderse y pagan $16.200 cada uno,
cada mes. Quien lo ve por SKU los saca y baja la factura a la mitad sin perder una venta.

**El almacenamiento no te lo cobra Full: te lo cobra tu rotación lenta, y a partir del mes cuatro
te lo cobra con intereses.**

## Relacionados

`103` Full · `105` cuándo conviene Full · `106` ingresar inventario · `108` inventario viejo ·
`109` peso volumétrico · `116` productos grandes · `124` auditoría mensual · `75` el cálculo del
margen · `100` tarifas oficiales de envío · `79` el umbral del envío gratis
