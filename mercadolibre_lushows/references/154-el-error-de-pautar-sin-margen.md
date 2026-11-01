# El error de pautar sin margen

El error que más plata cuesta en Mercado Ads no es elegir mal la estrategia ni pujar de más: es
definir el margen **después** de vender. Este módulo muestra la matemática con cifras oficiales de
Colombia para que no quede como opinión.

## El error, descrito

El vendedor calcula su margen así: precio menos lo que le costó el producto. "Compro a $42.500,
vendo a $50.000, gano 15%." Con ese número enciende la pauta, elige Rentabilidad y se queda
tranquilo porque el ACOS objetivo de 5-15% "cabe" dentro de su 15%.

No cabe. Ese 15% no existe: es margen **bruto**, calculado antes de la comisión, el IVA y el
envío. Ya estaba en negativo antes de pautar.

## La matemática, con números oficiales

Cifras oficiales de Mercado Libre Colombia (verificado sep-2026): el cargo por venta es de
**8% a 22%** del precio según categoría y cuotas, y el envío de un paquete de 1 kg en un producto
de $30.000-$59.999 con reputación verde cuesta **$4.300**.

Producto de **$50.000**, costo $42.500, comisión 14%, envío asumido:

| Concepto | Valor |
|---|---|
| Precio publicado | $50.000 |
| − IVA 19% (19/119 del precio) | −$7.983 |
| − Cargo por venta 14% | −$7.000 |
| − Envío 1 kg | −$4.300 |
| − Costo del producto | −$42.500 |
| **= Resultado** | **−$11.783** |
| **Margen real** | **−23,6%** |

Pierde $11.783 en cada venta. **Con pauta encendida, pierde más rápido.**

Y si no es responsable de IVA, la cuenta tampoco salva: $50.000 − $7.000 − $4.300 − $42.500 =
**−$3.800**. Sigue en negativo (sobre el IVA y quién lo paga, ver `81` y `contador_lushows`).

## Por qué un margen de 15% no aguanta pauta

Supón ahora que el margen **sí** es neto: 15% real después de comisión, IVA y envío. Aun así:

| Estrategia | ACOS | Margen que queda de un 15% neto |
|---|---|---|
| Rentabilidad (piso) | 5% | 10% |
| Rentabilidad (medio) | 10% | 5% |
| **Rentabilidad (techo)** | **15%** | **0% — trabajas gratis** |
| Crecimiento (piso) | 15% | 0% |
| Crecimiento (techo) | 30% | **−15%** |

Con 15% de margen neto, **toda la estrategia Rentabilidad cabe justo hasta borrar tu utilidad** y
cualquier otra te pone en rojo. Y eso sin contar devoluciones (`95`), stock que no rota o el
primer reclamo.

## El doble mordisco: comisión + ACOS

Los dos costos se cobran sobre la misma base — el precio de venta — y se suman:

| Comisión oficial | ACOS 5% | ACOS 10% | ACOS 15% | ACOS 30% |
|---|---|---|---|---|
| 8% (categoría barata, hasta 3 cuotas) | 13% | 18% | 23% | 38% |
| 14% (categoría media) | 19% | 24% | 29% | 44% |
| 19% (categoría cara) | 24% | 29% | 34% | 49% |
| 22% (cara + cuotas extra) | 27% | 32% | 37% | 52% |

Esa es la porción del precio que se van **Mercado Libre y Mercado Ads juntos**, antes del IVA,
antes del envío y antes del costo del producto. En la esquina peor, más de la mitad.

Nota el detalle: ofrecer **cuotas extra cuesta exactamente 3 puntos porcentuales** de comisión
adicional (oficial ML Colombia, verificado sep-2026). Tres puntos es más de lo que muchos tienen
de margen sobrante.

**Comisión y ACOS no son dos costos: son el mismo mordisco dado dos veces sobre la misma torta.**

## Los tres autoengaños que sostienen el error

| Autoengaño | La realidad |
|---|---|
| "Vendo a volumen y lo compenso" | El volumen multiplica la pérdida por unidad, no la compensa |
| "Es inversión para posicionarme" | Posicionar con margen negativo te deja arriba y quebrado (`164`) |
| "El ACOS me dio 12%, está bien" | El ACOS no resta comisión, IVA ni envío. Un ACOS bajo sobre margen negativo sigue siendo pérdida (`149`) |

El tercero es el más peligroso porque el panel te da la razón: las métricas de Mercado Ads se ven
verdes mientras tu banco se pone rojo. **El panel mide la campaña; solo tu calculadora mide el
negocio.**

## La orden operativa

Antes de crear cualquier campaña, ejecuta la calculadora. No la estimes, no la recuerdes de la
última vez, no la hagas "más o menos":

```
python scripts/margen_ml.py margen --precio 50000 --costo 42500 --comision 14 --iva 19
```

```
□ Corrí la calculadora para ESTE SKU (`82`)
□ Metí la comisión REAL leída logueada en el panel, no un promedio (`76`)
□ Metí el envío REAL de la tabla oficial según peso y rango de precio (`78`)
□ Revisé si ofrezco cuotas extra: son 3 puntos más (`80`)
□ El margen neto resultante supera el 15%
□ Fijé el ACOS objetivo en ~2/3 de ese margen neto (`150`)
□ Si el margen no da, arreglé precio o costo ANTES de pautar, no después (`83`)
□ Si las cifras deciden plata, las verifiqué con `Matematicas_lushows`
```

## Qué hacer si el margen no da

En orden de facilidad, no de deseo:

| Palanca | Cómo | Módulo |
|---|---|---|
| Subir el precio | Ojo con el umbral de $60.000: cruzarlo casi duplica el costo de envío | `83`, `79` |
| Bajar el costo | Negociar con el proveedor, comprar más volumen | `dropshipping_lushows` |
| Quitar las cuotas extra | Recuperas 3 puntos de comisión al instante | `80` |
| Reducir el envío | Peso y volumen del empaque; revisar el volumétrico | `109` |
| Subir el ticket con combos | El precio mínimo de publicación es $2.900 | `86` |
| **No pautar ese SKU** | Es una decisión válida y a veces la correcta | `164` |

## Relacionados

`145` qué es Mercado Ads · `148` las tres estrategias · `149` ACOS y TACOS ·
`150` el ACOS sano según tu margen · `155` leer los reportes ·
`164` cuándo no es la respuesta · `75` estructura de costos · `76` las comisiones ·
`78` el envío que pagas tú · `79` umbral del envío gratis · `80` cuotas sin interés ·
`81` IVA y el precio que publicas · `82` la calculadora de margen · `83` precio mínimo viable ·
`86` por qué los productos baratos pierden · `95` costo oculto de la devolución ·
`97` margen por SKU · `109` peso volumétrico
