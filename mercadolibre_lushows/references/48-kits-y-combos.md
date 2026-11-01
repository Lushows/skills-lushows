# Kits y combos

Empaquetar sube el ticket, reparte el costo de envío entre más unidades y te saca de la comparación
directa contra el producto suelto. En Colombia además resuelve un problema concreto: **el precio
mínimo de publicación**.

## El caso obligatorio: productos de menos de $2.900

> "El precio de tu producto debe ser **igual o superior a $2.900**. Esto te permitirá cubrir las
> tarifas de venta. **Puedes vender productos de menor valor ofreciendo packs o combos**"
> (oficial ML Colombia, verificado sep-2026).

Si tu unidad no llega a $2.900, no hay decisión que tomar: el pack es la única forma de publicarla.

## Por qué el kit gana plata

| Efecto | Detalle |
|---|---|
| Sube el ticket | Más ingreso por transacción, mismo trabajo de despacho |
| Diluye el envío | Un solo paquete para varias unidades (`109`) |
| Te saca de la guerra de precios | Nadie compara tu kit contra el producto suelto del vecino |
| Concentra el historial | Un kit que vende acumula conversión en una publicación (`41`) |
| Mejora la conversión | Resuelve un problema completo, no una pieza |

## El umbral de $60.000: el cálculo que casi nadie hace

El costo de envío da un salto brutal al cruzar los $60.000 (oficial ML Colombia, verificado
sep-2026). Con reputación verde, MercadoLíder, sin reputación o con Full:

| Peso | Producto $30.000-$59.999 | Producto de más de $60.000 |
|---|---|---|
| Hasta 0,3 kg | $4.100 | $8.000 |
| 0,5 a 1 kg | $4.300 | $8.200 |
| 1 a 2 kg | $4.500 | $8.500 |
| 3 a 4 kg | $4.700 | $10.100 |

**Cruzar los $60.000 casi duplica tu costo de envío por paquete.** Por encima de ese umbral, en
cambio, ofreces envío gratis con descuentos importantes y el comprador lo ve como beneficio.

Consecuencia para armar kits:

| Rango del kit | Lectura |
|---|---|
| Justo debajo de $60.000 | La zona más eficiente en costo de envío |
| Justo encima de $60.000 | Pagas casi el doble de envío por un peso ganado: la peor zona |
| Muy por encima de $60.000 | El envío pesa poco sobre un ticket grande: bien |

Si tu kit queda en $61.000, o lo bajas a $59.000 o lo subes a algo que justifique el salto. Corre el
número: `python scripts/margen_ml.py margen --precio X --costo Y --comision Z --iva 19`, y si tiene
que ser exacto, rutea a `Matematicas_lushows`.

Nota adicional: "los productos de menos de **$15.000** pagan como máximo la mitad del precio del
producto" en envío (oficial ML Colombia, verificado sep-2026). Ver `79`.

## Cómo se arma un kit que se vende

| Tipo de kit | Lógica | Ejemplo |
|---|---|---|
| Por cantidad | Descuento por volumen | Pack x3, x6, docena |
| Por uso completo | Todo lo que necesitas para una tarea | Set de repostería: molde + espátula + manga |
| Producto + consumible | El repuesto que va a necesitar igual | Máquina + repuesto de filtros |
| Producto + accesorio | Lo que iba a comprar aparte | Termo + funda |
| Regalo armado | El empaque es parte del valor | Set presentado en caja |

Reglas:

```
□ Las piezas se usan juntas de verdad, no son un revoltijo
□ El kit cuesta menos que comprar las piezas por separado, y se nota
□ Todas las piezas están en la foto, contables (`36`)
□ La descripción lista pieza por pieza, y dice qué NO incluye (`33`)
□ El título nombra el kit como un producto, sin listar cada pieza (`28` `29`)
□ El peso total real está en los atributos: el envío se cotiza con eso (`109`)
```

## El título de un kit

ML prohíbe "mencionar más de un producto ni sus variantes" en el título (oficial ML Colombia,
verificado sep-2026). Un kit se nombra como una unidad:

| ❌ | ✅ |
|---|---|
| `Molde y Espátula y Manga y Boquillas Repostería` | `Set Repostería 4 Piezas Molde Espátula Manga` |
| `Pack Vasos + Jarra + Bandeja` | `Juego Vasos Jarra Y Bandeja Acrílico 8 Piezas` |
| `Sartén x3 Rojo Azul Negro` | `Set 3 Sartenes Antiadherentes 20 24 28 Cm` |

## Kit vs variaciones vs publicación aparte

| Pregunta | Respuesta |
|---|---|
| ¿El pack se busca con otras palabras ("x3", "set", "docena")? | Publicación aparte |
| ¿La categoría tiene "cantidad" como atributo de variación? | Puede ir como variante (`40`) |
| ¿El ticket del pack es más del doble del unitario? | Publicación aparte (`41`) |

Veredicto general: **el kit va en publicación aparte**, salvo que la categoría claramente agrupe
cantidades como variantes.

## Riesgos

| Riesgo | Prevención |
|---|---|
| Reclamo por producto incompleto | Foto contable + lista en descripción (`33` `136`) |
| Una pieza se agota y el kit queda sin stock | Stock del kit = la pieza más escasa (`45`) |
| Peso mal declarado | Pesa el kit armado, con empaque (`109`) |
| Devolución parcial | Define y comunica que se devuelve completo (`138`) |

## El error clásico

Armar el kit juntando lo que no rota. El comprador nota de inmediato cuando el "regalo" es el
producto que nadie quiere, y el kit hereda la mala fama. **Un kit se arma alrededor de lo que ya
vende, agregándole lo que falta; no para desocupar bodega.**

## Relacionados

`41` estructura · `40` variaciones · `28` `29` el título · `33` la descripción · `36` fotos ·
`45` stock · `77` el piso de $2.900 · `86` `87` ticket promedio y bundling · `79` costos de
envío · `109` peso y dimensiones · `136` reclamos · `138` devoluciones · cálculos →
`Matematicas_lushows`
