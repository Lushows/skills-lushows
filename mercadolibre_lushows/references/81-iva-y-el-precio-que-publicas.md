# IVA y el precio que publicas

En Mercado Libre el comprador ve un precio final: el IVA ya está adentro. Si eres responsable de
IVA, esa porción del precio **nunca fue tuya** — la recaudas para la DIAN y la devuelves. Contarla
como ingreso es la forma más común de creer que el negocio va bien hasta que llega la declaración.

## El principio

El precio publicado es precio al consumidor, con impuestos incluidos. No hay un campo "precio +
IVA" como en una factura B2B. Lo que pones en `price` es lo que paga el comprador.

Eso significa que el IVA **sale de tu precio**, no se suma encima. Subirle el IVA al precio no es
un capricho: si no lo hiciste, el IVA lo estás pagando de tu margen.

**El IVA no es un costo: es plata ajena que pasa por tu cuenta. El error es gastártela.**

## La descomposición

Con tarifa general del 19%, el precio publicado se parte así:

```
base sin IVA = precio publicado ÷ 1,19
IVA          = precio publicado − base sin IVA
```

| Precio publicado | Base sin IVA | IVA 19% |
|---|---|---|
| $19.000 | $15.966 | $3.034 |
| $50.000 | $42.017 | $7.983 |
| $59.900 | $50.336 | $9.564 |
| $89.900 | $75.546 | $14.354 |
| $119.000 | $100.000 | $19.000 |
| $250.000 | $210.084 | $39.916 |

El error aritmético clásico: **restar** el 19% al precio en vez de **dividir** entre 1,19. Restarle
19% a $119.000 da $96.390, no $100.000. Son $3.610 de diferencia por unidad, siempre a tu favor en
la hoja y en contra en la realidad.

## Por qué esto pega dos veces

Aquí está la parte que duele y que casi nadie tiene en cuenta:

1. **El IVA sale del precio**, así que tu base es menor de lo que pensabas.
2. **El cargo por venta de ML se calcula sobre el precio CON IVA**, no sobre la base.

Pagas comisión sobre plata que no es tuya. La fórmula del daño:

```
cargo efectivo sobre tu base = cargo nominal × (1 + tarifa de IVA)
```

Con IVA 19%, multiplica por 1,19. Aplicado al **rango oficial colombiano de 8% a 22%** (oficial ML
Colombia, verificado sep-2026):

| Cargo nominal (sobre precio con IVA) | Cargo efectivo sobre tu base |
|---|---|
| 8% (piso oficial) | 9,5% |
| 11% (piso con cuotas extra) | 13,1% |
| 14,5% | 17,3% |
| 19% (techo sin cuotas extra) | 22,6% |
| 22% (techo oficial) | **26,2%** |

Léelo bien: en la categoría más cara con cuotas extra, Mercado Libre se lleva **más de una cuarta
parte** de lo que de verdad es tuyo. Ese es el número con el que hay que decidir si un producto va
o no va (`84`).

## Cómo lo maneja la calculadora

`margen_ml.py` implementa exactamente este comportamiento:

- `--iva 19` descompone el precio dividiendo entre 1,19 y muestra la línea "IVA (no es tuyo)".
- Por defecto el cargo se calcula **sobre el precio con IVA**, que es el comportamiento estándar.
- `--comision-sin-iva` cambia ese supuesto. Úsala solo si verificaste que en tu caso es así.

```
# Responsable de IVA, cargo sobre el precio total (el caso normal)
python scripts/margen_ml.py margen --precio 119000 --costo 60000 --comision 14.5 --iva 19

# No responsable de IVA: el precio completo es tu base
python scripts/margen_ml.py margen --precio 119000 --costo 60000 --comision 14.5 --iva 0
```

Cargo **14,5% — ejemplo dentro del rango oficial 8%-22%, verifica el tuyo** (`76`).

El script trae una prueba que verifica esto: `python scripts/margen_ml.py test` comprueba que
$119.000 con IVA 19% da base $100.000 e IVA $19.000, y que un cargo del 10% da $11.900 sobre precio
y $10.000 sobre base. Ver `82`.

## Si NO eres responsable de IVA

Corre todo con `--iva 0`. Tu base es el precio completo y tu margen es genuinamente mayor. Es una
ventaja competitiva real en categorías de ticket bajo, y una de las razones por las que un vendedor
pequeño puede competir en precio con uno grande.

Ojo: dejar de ser responsable no es una decisión de conveniencia, depende de umbrales y actividades
definidos por la norma. Eso no es materia de esta skill.

## El IVA y el umbral de los $60.000

Detalle operativo que se pasa por alto: el umbral de envío gratis se mide sobre el **precio
publicado**, o sea **con IVA adentro** (`79`). Un producto cuya base son $50.400 se publica a
$59.976 y queda debajo del umbral; si la base sube a $50.500, el precio publicado pasa de $60.000 y
el envío casi se duplica. Un aumento de $100 en la base puede costarte $3.900 de envío. Revisa esa
frontera cada vez que ajustes costos.

## Lo que NO resuelve este módulo

| Pregunta | A dónde va |
|---|---|
| ¿Soy responsable de IVA? ¿Desde cuándo? | `contador_lushows` |
| ¿Mi producto es gravado, excluido o exento? | `contador_lushows` |
| ¿Cómo declaro y cada cuánto? | `contador_lushows` |
| ¿Qué retiene Mercado Pago y cómo lo cruzo? | `contador_lushows` |
| ¿Cómo emito la factura electrónica de la venta? | `contador_lushows`; Alegra tiene integración directa con ML en Colombia |
| ¿El cálculo de este módulo está bien hecho? | `Matematicas_lushows` |

> ⚠️ **Sin verificar para Colombia (sep-2026).** Qué retenciones tributarias aplica Mercado Pago
> Colombia por normativa DIAN no se pudo confirmar en fuente oficial. Míralo en tus reportes de
> Mercado Pago y llévaselo a tu contador; no lo asumas desde un blog regional.

## Lista de chequeo

```
□ Sé si soy responsable de IVA y con qué tarifa va cada producto mío
□ Dividí entre 1,19 — no resté el 19%
□ Entiendo que el cargo por venta se cobra sobre el precio CON IVA
□ Calculé mi cargo efectivo sobre base: nominal × 1,19
□ Todos mis cálculos corren con --iva puesto, no con --iva 0 por pereza
□ Revisé que ningún SKU quede rozando los $60.000 por culpa del IVA (ver 79)
□ El IVA recaudado está separado de la caja operativa
□ Mi contador vio los reportes de Mercado Pago, con sus retenciones
```

## El error clásico

Publicar el precio que "da bien" según el margen, sin el IVA adentro, y descubrir en la declaración
que 16 de cada 100 pesos facturados hay que devolverlos. En un negocio de margen 20%, eso no es un
ajuste: es el negocio entero.

## Relacionados

`75` estructura de costos · `76` el cargo por venta 8%-22% · `79` el umbral de los $60.000 · `82`
la calculadora de margen · `83` precio mínimo viable · `97` margen por SKU · `contador_lushows`
para todo lo tributario · `Matematicas_lushows` para verificar el cálculo
