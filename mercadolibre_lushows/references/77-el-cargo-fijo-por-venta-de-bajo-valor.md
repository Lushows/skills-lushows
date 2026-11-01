# El cargo fijo por venta de bajo valor

Este módulo existe para desmentirlo. **En Colombia no hay cargo fijo por venta de bajo valor.** La
cifra que devuelven los buscadores —$33.000 de umbral, $1.330 de cargo, desde el 1-sep-2026— es de
Argentina, en pesos argentinos. Lo que sí tiene Colombia es otra cosa: un piso de publicación de
$2.900 y un tope de envío para productos baratos.

## Lo que dice la página oficial colombiana

La página de costos de vender de Mercado Libre Colombia **no menciona ningún cargo fijo en pesos**.
Solo habla del cargo porcentual de 8% a 22% (`76`) y de esto:

> *"El precio de tu producto debe ser **igual o superior a $2.900**. Esto te permitirá cubrir las
> tarifas de venta. Puedes vender productos de menor valor **ofreciendo packs o combos**."*
> (oficial ML Colombia, verificado sep-2026)

Eso es todo el mecanismo colombiano para productos baratos: **un piso, no un peaje**. Y fíjate que
la propia ayuda te da la salida —packs o combos—, que es exactamente `87`.

**En Colombia el producto barato no paga un cargo fijo: simplemente no se puede publicar por debajo
de $2.900, y si vale poco, el envío se lo come.**

## La trampa argentina, en detalle

| | Argentina | Colombia |
|---|---|---|
| Mecanismo | Cargo fijo por venta de bajo valor | **No existe** |
| Umbral | $33.000 ARS | — |
| Monto | $1.330 / $2.740 / $3.320 ARS por rango | — |
| Vigencia citada | 1-sep-2026 | — |
| Fuentes | Página/12, iProfesional, iProUp | — |
| Lo que sí hay en CO | — | **Precio mínimo de publicación $2.900 COP** |

Por qué esta confusión sobrevive: el signo `$` es el mismo en las dos monedas, los buscadores
mezclan resultados regionales, y los blogs de agencia copian entre sí sin verificar el país. Si
alguien te dice "$33.000 y $1.330" sobre Colombia, esa persona leyó un medio argentino.

## Los dos mecanismos colombianos reales para producto barato

### 1. El piso de $2.900

Por debajo de $2.900 no puedes publicar. Punto. La salida oficial es armar packs o combos (`87`).

### 2. El tope de envío del 50%

> *"Los productos de **menos de $15.000** pagan como máximo **la mitad del precio del producto**"*
> en costo de envío (oficial ML Colombia, verificado sep-2026).

Esto es un techo, no un cargo. Pero léelo al derecho: significa que Mercado Libre considera
perfectamente normal que un producto barato pague **hasta el 50% de su precio en envío**. Con un
producto de $12.000, el envío puede llevarse $6.000. Ahí está el verdadero castigo al ticket bajo
en Colombia, y es mucho más grande que cualquier cargo fijo argentino.

### La tabla que sí manda: el envío por rango de precio

Costo de envío para reputación verde / MercadoLíder / sin reputación (oficial ML Colombia,
verificado sep-2026), extracto de los pesos comunes:

| Peso | $0–$14.999 | $15.000–$29.999 | $30.000–$59.999 | Más de $60.000 |
|---|---|---|---|---|
| Hasta 0,3 kg | $2.500 | $2.600 | $4.100 | $8.000 |
| 0,5 a 1 kg | $2.700 | $2.800 | $4.300 | $8.200 |
| 1 a 2 kg | $2.800 | $2.900 | $4.500 | $8.500 |
| 3 a 4 kg | $3.000 | $3.200 | $4.700 | $10.100 |
| 7 a 10 kg | $3.300 | $3.500 | $5.000 | $15.200 |

Mira la primera columna: el envío de un producto de $9.000 cuesta $2.700 si pesa 1 kg. Eso es el
30% del precio, y ML no te lo cobra como "cargo fijo" pero se siente igual. Tabla completa en `78`.

## Lo que esto significa para tu precio

| Precio del producto | Qué te pega |
|---|---|
| Menos de $2.900 | **No puedes publicarlo.** Arma un pack (`87`) |
| $2.900 – $14.999 | Cargo porcentual + envío que puede llegar al 50% del precio |
| $15.000 – $29.999 | Cargo porcentual + envío de tabla, todavía bajo |
| $30.000 – $59.999 | El envío da un primer salto (de ~$2.800 a ~$4.300 en 1 kg) |
| Desde $60.000 | Envío gratis obligatorio y el costo **casi se duplica** (`79`) |

Los tres saltos de esa columna —$15.000, $30.000 y $60.000— son las fronteras reales del precio en
Colombia. No hay cargo fijo, hay **escalones de envío**. Ver `85`, `86` y `88`.

## Qué hacer con la bandera `--cargo-fijo` del script

`margen_ml.py` tiene `--cargo-fijo` porque el mecanismo existe en otros países de la región. **Para
Colombia, déjala en 0** (es su valor por defecto, así que basta con no ponerla):

```
# Colombia: sin cargo fijo. El golpe está en --envio
python scripts/margen_ml.py margen --precio 14900 --costo 6000 --comision 14.5 \
    --envio 2800 --iva 19
```

Si algún día ML Colombia introduce un cargo fijo, esa bandera está lista. Mientras tanto, usarla
con un número inventado es meterse un costo que no existe y descartar productos que sí servían.

## Lista de chequeo

```
□ No uso la cifra argentina de $33.000 / $1.330 en ningún cálculo
□ Ningún producto mío se publica por debajo de $2.900
□ Para los de menos de $15.000 verifiqué el envío: puede ser hasta el 50% del precio
□ Busqué mi costo de envío en la tabla oficial por rango de precio, no lo estimé
□ Dejé --cargo-fijo en 0 en margen_ml.py
□ Los productos que no aguantan el envío los convertí en pack (ver 87) o los maté (ver 98)
□ Si alguien me cita un cargo fijo colombiano, le pido la URL de mercadolibre.com.co
```

## El error clásico

Descartar un catálogo entero de productos baratos porque una IA o un blog le aplicó a Colombia el
cargo fijo argentino. El error inverso también existe y es peor: ignorar que en productos de menos
de $15.000 el envío puede llevarse la mitad del precio, publicar con envío gratis "para vender más",
y financiar cada venta.

## Relacionados

`75` estructura de costos · `76` el cargo por venta 8%-22% · `78` el envío que pagas tú · `79` el
umbral de los $60.000 · `82` la calculadora de margen · `85` el ticket que aguanta ML · `86` por
qué los productos baratos pierden · `87` subir el ticket con kits · `88` precio psicológico · `98`
qué hacer con el SKU que no deja
