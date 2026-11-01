# Frágiles: la tasa de rotura y cuándo el producto no es viable

Un producto frágil no es un problema de embalaje: es un problema de aritmética. Cada rotura es un
reclamo de **calidad**, y los reclamos de calidad son de los que sí cuentan contra tu reputación,
con un techo de **3,5% de ventas con reclamos** para seguir verde (oficial ML Colombia, verificado
sep-2026).

## La cuenta que decide todo

```
TASA DE ROTURA = paquetes que llegan dañados ÷ paquetes enviados

COSTO POR UNIDAD VENDIDA =
    costo del producto
  + envío de ida (tabla oficial de `100`)
  + TASA DE ROTURA × (costo del producto + envío de ida + envío de vuelta + tu tiempo)
```

La segunda línea es la que nadie incluye. Con 5% de rotura, **cada 20 ventas regalas una
completa**, más los dos fletes y la gestión.

| Tasa de rotura | Efecto sobre el margen | Efecto sobre la reputación |
|---|---|---|
| Menos de 1% | Manejable | Sin riesgo |
| 1% a 2% | Ya se siente | Vigilar |
| 2% a 3,5% | Duele | **Zona de alerta**: el techo verde es 3,5% |
| Más de 3,5% | Insostenible | Pierdes el verde y con él el 50% de descuento |

**El límite de un producto frágil no lo pone tu margen: lo pone el 3,5%.** Puedes aguantar
económicamente una rotura del 6% y aun así perder la cuenta.

## Y perder el verde duplica el flete

Con reputación naranja o roja no hay descuento en envíos (oficial). Un producto de más de $60.000
y 1 kg pasa de **$8.200 a $16.400** por venta. Si vendes 150 al mes, la rotura excesiva no te
cuesta las 9 unidades rotas: te cuesta **$1.230.000 mensuales de flete extra** sobre las 150.

## Cómo medir tu tasa real

No la estimes. Cuéntala.

```
□ Registra cada caso: fecha, SKU, destino, tipo de daño, foto del comprador
□ Calcula la tasa por SKU, no global: un solo producto puede estar generando todo
□ Calcula la tasa por destino: puede ser una ruta, no el producto (`115`)
□ Con menos de 50 envíos de ese SKU, el dato todavía no es confiable
□ Recalcula cada mes: el embalaje nuevo se evalúa contra el número viejo
```

Separar por SKU y por destino es lo que convierte "se me rompen las cosas" en un problema con
solución.

## Las cuatro causas y sus arreglos

| Causa | Señal | Arreglo |
|---|---|---|
| Falta de contención (el producto baila) | Rotura sin patrón | Relleno ajustado al producto |
| Falta de amortiguación | Golpe en un punto | Burbuja o foam en esquinas |
| Caja débil | Caja aplastada al llegar | Cartón corrugado de mayor gramaje |
| Producto intrínsecamente frágil | Rotura con cualquier embalaje | Ver abajo: puede no ser viable |

La prueba de campo, en la mesa:

```
□ Sacudón: agita la caja cerrada. Si algo se mueve, falta contención
□ Caída desde 80 cm sobre el CANTO, no sobre la cara plana
□ Peso encima: tu caja va debajo de otras en el camión
□ Vuelve a hacer las tres pruebas cada vez que cambies de proveedor de empaque
```

## El conflicto con el ahorro de volumen

Proteger bien hace la caja más grande, y el volumen te cobra dos veces: ML usa **el mayor entre
peso físico y volumétrico** (oficial), y en Full el tamaño define el escalón del cargo por stock
antiguo.

| Decisión | Ahorro | Riesgo |
|---|---|---|
| Caja ajustada, mínima protección | Un escalón de tarifa (`110`) | Rotura arriba del 3,5% |
| Caja holgada, protección alta | — | Escalón más caro en cada venta |
| Caja mínima que pasa la prueba de caída | El punto óptimo | Ninguno |

**El objetivo no es la caja más pequeña: es la caja más pequeña que pasa la prueba de caída.** Si
esas dos no coinciden, gana la prueba de caída — porque un escalón de tarifa cuesta $1.500 y un
reclamo puede costarte el verde.

## Frágil en Full: el problema de control

En Full **tú no empacas**. Mandas el producto a bodega y ML lo despacha con su empaque estándar.
Si tu producto necesita protección especial, tienes que mandarlo ya protegido desde el origen, y
eso:

- Sube su volumen y por lo tanto su escalón de tamaño (`107`).
- Te obliga a que el empaque aguante meses en bodega, no solo el viaje.
- No te garantiza cómo lo manipulan en el centro de distribución.

Veredicto: **si tu producto es muy frágil y de rotación media, Full no es tu modalidad.** Flex o
despacho propio te dejan controlar el paquete. Ver `102` y `105`.

## Cuándo un producto frágil NO es viable en ML

Sé honesto con estos cortes:

| Señal | Lectura |
|---|---|
| Tasa de rotura > 3,5% con el mejor embalaje que puedes pagar | No es viable |
| El embalaje necesario cuesta más que el margen unitario | No es viable |
| El embalaje necesario sube dos escalones de tarifa | Revisa precio o no es viable |
| La rotura se concentra en destinos lejanos | Viable, pero restringe o refuerza esas rutas |
| La rotura bajó a menos de 1% con el embalaje nuevo | Viable, sigue midiendo |

No todo producto pertenece a un marketplace de envío masivo. Un producto de vidrio soplado de
$35.000 puede ser un negocio excelente en venta local y un desastre en ML.

## El error clásico

Tratar la rotura como mala suerte en vez de como una tasa. El vendedor recuerda "unos tres casos"
y sigue vendiendo, sin saber que su tasa real es 6% y que va camino a perder el verde. La rotura
es un número, se mide por SKU, y ese número decide si el producto se queda en el catálogo.

**Si no sabes tu tasa de rotura por SKU, no sabes si ese producto te da ganancia o te la quita.**

## Relacionados

`110` empacar sin perder plata · `111` embalaje que evita reclamos · `109` peso volumétrico ·
`115` zonas difíciles · `116` productos grandes · `105` cuándo conviene Full · `102` Flex · `118`
el paquete perdido · `124` auditoría mensual · `126` las tres métricas · `136` reclamos excluibles
· `138` devoluciones · `100` tarifas oficiales de envío
