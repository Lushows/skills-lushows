# Elasticidad precio-demanda

## La fórmula

```
PED = % de cambio en la cantidad vendida ÷ % de cambio en el precio
```

Sale negativa casi siempre (subes precio, bajas unidades). En la práctica se habla del valor
absoluto.

| |PED| | Nombre | Qué significa para ti |
|---|---|---|
| < 1 | **inelástica** | subes precio y la facturación SUBE. Sube el precio |
| = 1 | unitaria | la facturación no se mueve. El margen sí — ver abajo |
| > 1 | **elástica** | subes precio y la facturación BAJA |

## Cómo calcularla con tus propios datos

Necesitas dos periodos comparables con precios distintos. La prueba secuencial de `318` te los da.

Ejemplo con números del proyecto activo (MXN):

| Periodo | Precio | Unidades / 7 días |
|---|---|---|
| Bloque A | 999 | 40 |
| Bloque B | 1.099 | 34 |

```
% cambio precio    = (1.099 − 999) ÷ 999            = +10,01%
% cambio cantidad  = (34 − 40) ÷ 40                 = −15,00%
PED                = −15,00 ÷ 10,01                 = −1,50   → elástica
```

Usa la **fórmula de punto medio (arco)** cuando el cambio es grande (>15%), porque el resultado no
debe depender de cuál periodo llamas "antes":

```
PED_arco = [(Q2−Q1) / ((Q1+Q2)/2)] ÷ [(P2−P1) / ((P1+P2)/2)]
         = (−6 / 37) ÷ (100 / 1.049) = −0,1622 ÷ 0,0953 = −1,70
```

Los dos métodos dan números distintos y **ambos son correctos** para lo que miden. Declara cuál
usaste. Verificación exacta: `Matematicas_lushows`.

## La trampa: la elasticidad de facturación no es la que te importa

Facturar más no es ganar más. Lo que decide es el **margen total**, y ahí el punto de indiferencia
se mueve a tu favor.

Con la economía verificada (USD, ticket 54,59 ≈ 999 MXN, margen sin adquisición 26,47, CAC 10,54,
utilidad 15,93):

| Precio | Margen/pedido (aprox.) | Unidades para igualar la utilidad de 40 × 15,93 = 637,20 |
|---|---|---|
| 999 MXN (54,59) | 15,93 | 40 (base) |
| 1.099 MXN (≈60,05) | ~20,18 | **32** |
| 1.199 MXN (≈65,51) | ~24,42 | **27** |
| 899 MXN (≈49,13) | ~11,69 | **55** |

Lee esto despacio: subiendo 10% puedes **perder 20% de las unidades y ganar lo mismo**. Bajando 10%
necesitas **vender 37% más solo para empatar**. Las cifras de margen por precio salen de `321`;
confirma con tus costos reales.

| Umbral de indiferencia | Regla |
|---|---|
| Subir precio | gana si la caída de unidades es **menor** que el aumento de margen por pedido |
| Bajar precio | gana casi nunca, porque el costo fijo por pedido (flete 8,74) no baja contigo |

## Por qué en dropshipping casi siempre conviene subir

| Razón | Mecánica |
|---|---|
| **El costo por pedido es rígido** | flete 8,74 + comisión 5,5% + producto. Bajar precio solo te quita a ti |
| **Menos pedidos = menos operación** | menos soporte, menos devoluciones, menos reembolsos, menos WhatsApp |
| **Sube el techo de CAC** | de 30,73 sube con el ticket → puedes pagar más por el clic y **ganar la subasta**. Ver `11`, `226` |
| **El precio alto filtra clientes malos** | el cazador de ofertas es el que más devuelve y más reclama |
| **El precio comunica** | un precio bajo dice "producto genérico", justo lo que estás tratando de no ser |
| **El bundle no paga flete extra** | dos unidades en la misma caja: el segundo tiene margen mucho mayor. Ver `218` |

El tercero es el decisivo y el menos entendido. Tu límite de escala en Meta no es tu creativo: es
cuánto puedes pagar por adquisición. Un precio 10% más alto te compra **capacidad de puja**, y esa
capacidad vale más que la unidad que perdiste. Ver `facebook_ads_lushows`.

## Cuándo la elasticidad SÍ te castiga

No es siempre verdad que subir gana. Casos donde el mercado te parte:

| Situación | Por qué |
|---|---|
| Producto idéntico y comparable (marketplace) | el algoritmo premia la competitividad. `mercadolibre_lushows` |
| Categoría con precio ancla fuerte | todos venden a 299; a 399 eres "el caro" sin razón |
| Sin diferenciación de oferta | si vendes exactamente lo mismo, solo queda el número |
| Público de bajo poder adquisitivo con producto opcional | la elasticidad es real y alta |
| Temporada de descuentos | en Buen Fin el marco mental es rebaja. Ver `238` |

Señal de alarma: si tu |PED| medida da **> 2,5**, no tienes un problema de precio, tienes un
problema de oferta. La respuesta no es bajar; es cambiar la promesa o armar bundle (`215`, `218`).

## Elasticidad por tramo — no es una constante

La PED cambia según dónde estés en la curva. Los precios psicológicos (`217`) crean escalones: el
salto de 999 a 1.099 duele más que de 1.099 a 1.199, porque 999 vive del efecto de dígito.

| Tramo | Comportamiento típico |
|---|---|
| Justo por debajo de un número redondo | elasticidad baja: hay colchón hasta el umbral |
| Cruzando el número redondo (999 → 1.000+) | pico de elasticidad: el escalón se siente |
| Entre redondos (1.199 → 1.299) | vuelve a bajar |

Consecuencia operativa: **prueba precios que crucen el escalón o que se queden dentro del tramo,
pero sabe cuál estás haciendo.** Medir 999 vs 1.099 no te dice nada sobre 1.199 vs 1.299.

## El elástico del MSI

En México, con meses sin intereses, el cliente no evalúa el precio: evalúa **la mensualidad**. Eso
baja la elasticidad percibida en tickets altos.

| Precio | 3 MSI | 6 MSI |
|---|---|---|
| 999 | 333 | 166,50 |
| 1.299 | 433 | 216,50 |
| 1.599 | 533 | 266,50 |

De 999 a 1.599 son 600 pesos de diferencia, pero a 6 MSI son 100 pesos al mes. Por eso el Buen Fin
es la ventana para probar el precio ALTO, no el bajo. Ojo: el MSI tiene costo de comisión que debe
entrar al modelo antes de celebrar. Verificar la tasa real con tu pasarela — cambia por banco y
plazo. Ver `238`, `228` y `contador_lushows` para el tratamiento del cobro.

## Protocolo de medición honesto

| Paso | Detalle |
|---|---|
| 1 | Dos bloques de 7 días, alternados A-B-A-B si puedes (`318`) |
| 2 | Presupuesto, público y creativo constantes |
| 3 | Registra CPM de cada bloque; si varía >20%, el dato está sucio |
| 4 | Calcula PED con arco y también margen total por bloque |
| 5 | Si los dos bloques de A no coinciden entre sí, tu ruido es mayor que el efecto: **no concluyas** |
| 6 | Verifica el cálculo en `Matematicas_lushows` |

La regla que evita el ridículo: **si no puedes reproducir el mismo precio dos veces con el mismo
resultado, no mediste elasticidad, mediste una semana.**

## Frontera

| Necesitas | Skill |
|---|---|
| Cálculo exacto, regresión, intervalos | `Matematicas_lushows` |
| Estrategia de precio del negocio | `economist_lushows` |
| Capacidad de puja y escala | `facebook_ads_lushows` |
| Precio competitivo en marketplace | `mercadolibre_lushows` |

## Relacionados
`11` · `103` · `215` · `216` · `217` · `218` · `220` · `226` · `228` · `238` · `316` · `317` · `318` · `320` · `321`
