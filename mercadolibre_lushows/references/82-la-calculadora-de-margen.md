# La calculadora de margen

`scripts/margen_ml.py` responde las dos preguntas que deciden si un producto va o no va a Mercado
Libre: cuánto te queda vendiendo a un precio, y a cuánto tienes que vender para ganar lo que
quieres. Usa aritmética decimal exacta (nada de float) y, a propósito, **no sabe cuánto es la
comisión**: esa la traes tú del simulador logueado.

## Los dos modos

| Modo | Pregunta que responde | Argumento propio |
|---|---|---|
| `margen` | Si vendo a este precio, ¿cuánto me queda? | `--precio` |
| `minimo` | ¿A cuánto vender para ganar X%? | `--margen-objetivo` |
| `test` | ¿La aritmética del script está bien? | ninguno |

## Todas las banderas

| Bandera | Qué es | Obligatoria | Por defecto |
|---|---|---|---|
| `--precio` | Precio publicado, **con IVA** | Sí en modo `margen` | — |
| `--margen-objetivo` | Margen % que quieres sobre la base sin IVA | Sí en modo `minimo` | — |
| `--costo` | Costo del producto puesto en tu bodega | Sí | — |
| `--comision` | Cargo por venta % de TU categoría (rango oficial CO: 8-22) | **Sí, siempre** | — |
| `--cargo-fijo` | Cargo fijo por venta de bajo valor. **En Colombia va en 0: no existe** (`77`) | No | 0 |
| `--envio` | Envío que asumes, de la tabla oficial según peso, precio y reputación (`78`) | No | 0 |
| `--iva` | IVA % incluido en el precio (0 si no eres responsable) | No | 0 |
| `--otros` | Empaque, etiqueta, mano de obra por unidad | No | 0 |
| `--comision-sin-iva` | Calcula el cargo sobre la base, no sobre el precio total | No | apagado |

Tres banderas se malinterpretan siempre:

- **`--cargo-fijo` en Colombia va en 0.** El cargo fijo con umbral de $33.000 es de Argentina. La
  bandera existe porque el mecanismo sí opera en otros sites. Ver `77`.
- **`--envio` es lo que asumes tú.** Búscalo en la tabla oficial: fila del peso × columna del rango
  de precio × tu color de reputación (`78`). No lo estimes.
- **`--comision-sin-iva`** cambia un supuesto del modelo. El estándar de ML es cobrar sobre el
  precio **con** IVA, y así viene por defecto.

## Ejemplo real, modo `margen`

Producto de 1 kg que te cuesta $42.000, lo publicas a $89.900, responsable de IVA, reputación
verde, empaque $900. Envío de tabla oficial (0,5-1 kg, producto sobre $60.000, verde) = **$8.200**.
Cargo **14,5% — ejemplo dentro del rango oficial 8%-22%, verifica el tuyo** (`76`):

```
python scripts/margen_ml.py margen --precio 89900 --costo 42000 --comision 14.5 \
    --envio 8200 --otros 900 --iva 19
```

El informe imprime la cascada completa: precio, IVA extraído, base sin IVA, cargo, envío, otros,
costo, y al final **utilidad en pesos**, **margen sobre base sin IVA** y **markup sobre el costo**.
No confundas los dos últimos: margen es sobre la venta, markup es sobre el costo, y el markup
siempre se ve más bonito.

## Ejemplo real, modo `minimo`

La pregunta inversa: mismo costo, quieres 25% de margen, producto de 3 kg (envío oficial $10.100
sobre $60.000, verde).

```
python scripts/margen_ml.py minimo --costo 42000 --margen-objetivo 25 --comision 14.5 \
    --envio 10100 --iva 19
```

Devuelve el **precio mínimo viable** y después imprime el informe completo a ese precio, para que
veas la cascada. Al final te manda a compararlo con el líder de tu categoría (`70`, `83`).

Si pides un margen imposible, no devuelve un absurdo: lanza un error explícito.
`--margen-objetivo 90 --comision 20` responde que cargo + margen consumen el 100% del precio y te
dice que bajes el objetivo o cambies de categoría. Eso es intencional.

## Cómo leer el veredicto

El script no se queda en el número: clasifica.

| Margen sobre base sin IVA | Veredicto | Qué significa operativamente |
|---|---|---|
| Utilidad ≤ 0 | **Pierdes plata en cada venta** | Vender más te hace perder más rápido. Sube precio, baja costo, o el producto no es para ML (`84`) |
| < 10% | **Muy delgado** | Una devolución se come varias ventas (`95`). **No pautes**: el ACOS mínimo de la estrategia Rentabilidad arranca en 5-15% (`150`) |
| 10% – 20% | **Justo** | Aguanta la operación, casi no deja espacio para publicidad. Sube el ticket con un kit antes de pautar (`87`) |
| 20% – 35% | **Sano** | Hay espacio para Mercado Ads si el ACOS se mantiene debajo del margen |
| > 35% | **Alto** | Puedes competir en precio o invertir en posición. **Y revisa el cargo que usaste**: con un rango oficial de 8%-22%, un margen así suele venir de un dato mal traído |

Ese último renglón es la parte más útil. Si el script te felicita, desconfía del dato de entrada
antes de celebrar.

## Lo que el script NO sabe

**El cargo por venta.** Es un parámetro obligatorio, y es deliberado. El rango oficial colombiano
es **8% a 22%** (oficial ML Colombia, verificado sep-2026), pero **el porcentaje exacto de tu
categoría solo se ve logueado**, en el simulador de costos o en `/landing/costos-de-venta`.

> ⚠️ **Cambió en 2026.** `GET https://api.mercadolibre.com/sites/MCO/listing_prices` **ya no es
> pública**: responde `403 PA_UNAUTHORIZED_RESULT_FROM_POLICIES` y exige token OAuth. Si no tienes
> app autenticada, tu vía es el simulador logueado.

Tampoco sabe la probabilidad de devolución (`95`), ni los cargos por stock antiguo en Full, ni tu
gasto en Ads. El script es una calculadora honesta, no un oráculo.

**Un número exacto calculado sobre un supuesto inventado sigue siendo un número inventado, pero con
más decimales.**

## Barrer el rango oficial cuando aún no tienes tu número

```
for c in 8 11 14.5 19 22; do
  python scripts/margen_ml.py margen --precio 89900 --costo 42000 --comision $c \
      --envio 8200 --iva 19 | grep -E "GANAS|PIERDES|Margen"
done
```

Si el producto sobrevive al 22%, sobrevive a cualquier categoría de Colombia. Si solo sobrevive al
8%, estás apostando a caer en la más barata del marketplace.

## La autoverificación

Antes de confiarle una decisión de precio:

```
python scripts/margen_ml.py test
```

Verifica seis cosas: el caso simple sin IVA; la descomposición del IVA ($119.000 → base $100.000 +
IVA $19.000); que el cargo se calcule sobre el precio con IVA por defecto y sobre la base con la
bandera; el **ida y vuelta** (que `minimo` devuelva un precio que al pasarlo por `margen` dé
exactamente el margen pedido, en las cuatro combinaciones de IVA y base); la detección de venta a
pérdida; y el rechazo de un margen imposible.

| Código de salida | Significado |
|---|---|
| 0 | Corrió bien (y en modo `margen`, la utilidad es positiva) |
| 2 | Modo `margen`: utilidad ≤ 0 · Modo `minimo`: margen imposible |
| 1 | Error de uso |

## Lista de chequeo antes de creerle al informe

```
□ El cargo lo saqué del simulador logueado, con fecha, y cae dentro de 8%-22%
□ Si activé cuotas extra, sumé exactamente 3 puntos (ver 80)
□ El envío lo busqué en la tabla oficial: peso × rango de precio × mi reputación (ver 78)
□ Usé el peso MAYOR entre real y volumétrico
□ Dejé --cargo-fijo en 0: en Colombia no existe (ver 77)
□ Puse --iva 19 si soy responsable; --iva 0 solo si de verdad no lo soy
□ En --otros metí empaque, etiqueta y lo que me cuesta alistar
□ Corrí `test` y todas las pruebas pasaron
□ Si el veredicto dice margen alto, volví a mirar el cargo
```

## Relacionados

`75` estructura de costos · `76` el cargo por venta 8%-22% · `77` el mínimo de $2.900 · `78` el
envío que pagas tú · `79` el umbral de los $60.000 · `81` IVA y el precio que publicas · `83`
precio mínimo viable · `86` por qué los productos baratos pierden · `95` costo oculto de la
devolución · `97` margen por SKU · `150` ACOS sano · `Matematicas_lushows` para auditar
