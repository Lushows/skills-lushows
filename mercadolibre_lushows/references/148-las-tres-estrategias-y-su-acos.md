# Las tres estrategias y su ACOS

Mercado Ads no te pide una puja: te pide elegir una de tres estrategias, y cada una trae su propio
rango de ACOS objetivo. **Estos rangos son oficiales de Mercado Libre Colombia** (verificado
sep-2026), no estimaciones de blog. Elegir mal aquí es la decisión más cara de toda la campaña.

## Los tres rangos oficiales

| Estrategia | ACOS objetivo | Qué hace el sistema | Para cuándo |
|---|---|---|---|
| **Rentabilidad** | **5% a 15%** | Puja conservador, busca solo los clics que convierten barato | Producto con margen probado que quieres ordeñar |
| **Crecimiento** | **15% a 30%** | Puja intermedio, acepta pagar más por más volumen | Ganar participación en una categoría donde ya vendes |
| **Visibilidad** | **más de 30%** | Puja agresivo, prioriza aparecer sobre ganar plata | Lanzamiento, fecha caliente, defender el catálogo |

(oficial ML Colombia, `vendedores.mercadolibre.com.co`, verificado sep-2026)

**Elegir estrategia es elegir cuánta plata estás dispuesto a perder por cada venta.** Nada más.
"Visibilidad" no es un modo turbo gratis: es la instrucción explícita de gastar más de 30 centavos
de cada peso vendido en publicidad.

## Cuál elegir: el árbol de decisión

```
¿Ya calculaste el margen neto del SKU con `82`?
   NO  → PARA. No enciendas nada. Ve a `154`.
   SÍ  ↓

¿El margen neto es menor al 15%?
   SÍ  → No pautes este producto. Ni Rentabilidad alcanza (`150`, `164`)
   NO  ↓

¿El producto ya vende orgánicamente y quieres más plata del mismo?
   SÍ  → RENTABILIDAD
   NO  ↓

¿Es un producto nuevo o estás entrando a una categoría donde no existes?
   SÍ  → ¿el margen neto supera el 30%?
           SÍ  → CRECIMIENTO durante 30 días, luego reevalúa
           NO  → RENTABILIDAD y paciencia
   NO  ↓

¿Es una fecha caliente, un lanzamiento o estás peleando el catálogo?
   SÍ  → VISIBILIDAD, con presupuesto acotado y fecha de apagado escrita
   NO  → RENTABILIDAD
```

Por defecto, **Rentabilidad**. Es la respuesta correcta en la gran mayoría de los casos y la única
que no te puede arruinar el mes.

## Qué significa cada una en plata real

Sobre una venta de $80.000, esto es lo que la estrategia autoriza a gastar en publicidad:

| Estrategia | ACOS | Gasto publicitario por venta de $80.000 |
|---|---|---|
| Rentabilidad (piso) | 5% | $4.000 |
| Rentabilidad (techo) | 15% | $12.000 |
| Crecimiento (piso) | 15% | $12.000 |
| Crecimiento (techo) | 30% | $24.000 |
| Visibilidad | 30%+ | más de $24.000 |

Ahora cruza eso con el margen. En un producto de $80.000 con costo de $30.000, comisión del 14%,
envío de $8.200 y empaque de $1.500, la utilidad antes de publicidad es de **$16.327** — un
**20,4%** (cálculo con la fórmula de `75`, comisión dentro del rango oficial 8%-22%).

| Estrategia | Gasto por venta | Utilidad que queda | Veredicto |
|---|---|---|---|
| Rentabilidad al 5% | $4.000 | $12.327 | Sano |
| Rentabilidad al 15% | $12.000 | $4.327 | Justo, pero vive |
| Crecimiento al 30% | $24.000 | **−$7.673** | Pierdes plata en cada venta |
| Visibilidad | $24.000+ | más negativo | Solo si sabes por qué lo haces |

**Un producto con 20% de margen no puede usar Crecimiento.** Y eso es un producto con margen
decente. Ver `150` para la tabla completa.

## Cuándo Visibilidad sí se justifica

Es una estrategia legítima, pero solo cuando la pérdida compra algo que vale más que la plata:

| Situación | Por qué se justifica | Condición |
|---|---|---|
| Lanzamiento de un SKU nuevo | Arrancar la curva de conversión del algoritmo (`59`, `152`) | Máximo 14-21 días, con fecha de apagado |
| Hot Sale u otra fecha caliente | El volumen de búsqueda es 10× y no vuelve (`161`) | Presupuesto cerrado, campaña aparte |
| Defender el catálogo | Perder la oferta principal cuesta más que el ACOS (`63`) | Solo si el SKU es tu columna vertebral |
| Liquidar stock viejo de Full | El cargo por inventario antiguo crece exponencialmente (`107`) | Compara el ACOS contra el cargo que evitas |

Fuera de esos cuatro casos, Visibilidad es una forma cara de sentirse ocupado.

## Cambiar de estrategia: las reglas

```
□ No cambies de estrategia antes de 14 días corridos (`151`)
□ Cambia UNA cosa: o la estrategia, o el presupuesto. Nunca las dos juntas
□ Anota la fecha del cambio y el ACOS que traías
□ Después del cambio, vuelve a esperar 14 días antes de juzgar
□ Si bajas de Visibilidad a Rentabilidad, espera una caída de volumen: es lo esperado
```

## El error clásico

Elegir Visibilidad "porque quiero vender más". El sistema obedece: te muestra en todas partes,
gasta el presupuesto entero y factura mucho. Las ventas suben y el vendedor celebra — hasta que
al cierre del mes descubre que facturó 40% más y ganó 30% menos. **Vender más no es el objetivo;
el objetivo es que quede plata.** Si vas a usar Visibilidad, que sea una decisión con fecha de
vencimiento escrita, no un estado permanente.

## Relacionados

`145` qué es Mercado Ads · `146` Product Ads · `147` la subasta y el CPC · `149` ACOS y TACOS ·
`150` el ACOS sano según tu margen · `151` la ventana de atribución ·
`152` pautar una publicación nueva · `154` el error de pautar sin margen ·
`155` leer los reportes · `156` optimizar semana a semana · `161` el calendario comercial ·
`162` preparar una fecha caliente · `164` cuándo no es la respuesta · `59` primeras 72 horas ·
`63` ganar el catálogo · `75` estructura de costos · `82` la calculadora de margen ·
`107` costo de almacenamiento en Full
