# Descuentos y campañas

Mercado Libre organiza eventos y campañas donde tu producto aparece con descuento y exposición
extra. Entrar puede ser el mejor mes del año o una forma cara de vender barato. La diferencia está
en un cálculo que se hace **antes** de aceptar, no después de ver el reporte.

## Las fechas que sí están confirmadas

| Evento | Fechas | Dato |
|---|---|---|
| **Hot Sale Colombia, 1ª edición** | **16-20 de marzo de 2026** | +40,4 millones de búsquedas en 5 días, descuentos hasta 65%, hasta 12 cuotas sin interés, 80+ empresas |
| **Hot Sale Colombia, 2ª edición** | **19-23 de octubre de 2026** | Confirmada |

La primera edición fue el estreno del formato en Colombia. Los 40,4 millones de búsquedas en cinco
días son el argumento para entrar; los "descuentos hasta 65%" son el argumento para calcular antes.

## Los tipos de campaña

| Tipo | Quién la arma | Qué te piden |
|---|---|---|
| **Eventos grandes** (Hot Sale) | Mercado Libre | Descuento mínimo, stock comprometido, a veces cuotas |
| **Campañas de categoría** | Mercado Libre | Descuento y disponibilidad en fechas |
| **Descuento propio en la publicación** | Tú | Nada: lo pones y lo quitas |
| **Oferta del Día** | Mercado Libre, por postulación | ⚠️ Requisitos 2026 no verificados |

> ⚠️ **Sin verificar para Colombia (sep-2026).** Los requisitos de postulación a **Oferta del Día**
> en 2026 no se pudieron confirmar en fuente oficial. Míralos en tu panel, en la sección de
> promociones; no los des por sabidos desde un blog.

## El cálculo de si conviene

Una campaña no se evalúa por el descuento: se evalúa por la **utilidad total del período**. Tres
pasos, en orden.

### Paso 1: el margen al precio de campaña

```
python scripts/margen_ml.py margen --precio 71900 --costo 42000 --comision 15 \
    --envio 8200 --otros 900 --iva 19
```

Cargo **15% — ejemplo dentro del rango oficial 8%-22%, verifica el tuyo** (`76`). Si a precio de
campaña el veredicto dice "pierdes plata" o "muy delgado", **no entres**. No hay volumen que
arregle un margen negativo: solo lo multiplica.

### Paso 2: el aumento de unidades que necesitas

```
aumento mínimo de unidades (%) = Δmargen / margen nuevo × 100
```

Con margen 25% que baja a 18% al aplicar el descuento: `7 / 18 = 39%`. Necesitas vender **39% más
unidades** en los días de campaña solo para empatar.

| Margen normal | Margen en campaña | Unidades adicionales para empatar |
|---|---|---|
| 35% | 28% | 25% |
| 30% | 22% | 36% |
| 25% | 18% | 39% |
| 20% | 13% | 54% |
| 15% | 8% | 88% |

En un Hot Sale con 40 millones de búsquedas, un +50% es alcanzable. Un +88% ya es apostar.

### Paso 3: los costos que el descuento arrastra

Esto es lo que casi nadie suma y es donde se pierde la campaña:

| Costo arrastrado | Cuándo pega |
|---|---|
| **El descuento puede cruzar $60.000 hacia abajo** | Si tu precio con descuento queda debajo de $60.000, **ahorras** envío: el envío baja de $8.200 a $4.300 en 1 kg. Esto juega a tu favor y casi nadie lo ve (`79`) |
| **El descuento puede dejarte en la zona muerta** | Si caes a $61.000, pagas el envío caro con el precio bajo. El peor escenario (`79`) |
| **Más ventas = más devoluciones** | La tasa se mantiene, el volumen sube (`95`) |
| **Más ventas = más reclamos** | Y los reclamos pegan al termómetro, que encarece el envío (`96`) |
| **Quiebre de stock** | Deja el ítem en `paused` con `out_of_stock`, saca la publicación de la competencia y del catálogo, y al reponer debe reconstruir señales |

El primero es una jugada real: **si tu precio de campaña cae justo debajo de $60.000, el descuento
se paga solo con el ahorro de envío**. Bajar de $64.900 a $59.900 te cuesta $5.000 de precio y te
devuelve $3.900 de envío. El descuento efectivo es de $1.100.

**La mejor campaña en Colombia es la que aterriza en $59.900.**

## El quiebre de stock es el verdadero riesgo

Se dice poco y cuesta más que el descuento. Quedarte sin stock en plena campaña:

- Pasa el ítem a `paused` con sub-estado `out_of_stock`.
- Lo saca de la competencia y de la puja de catálogo.
- Al reponer, la publicación "revive como más nueva o menos confiable" y debe reconstruir señales.
- Encarece la pauta futura sobre esa publicación, porque reinicia el aprendizaje del algoritmo.

```
□ Calculé el stock para el escenario de +100%, no para el esperado
□ Tengo reposición programada durante los días de campaña
□ Si uso Full, el inventario ya está en el centro ANTES del evento (el traslado corre por mi cuenta)
□ Tengo alerta de stock bajo, no una revisión manual diaria
```

## Descuento propio: el que controlas

El que pones tú en la publicación no requiere postulación ni compromiso. Reglas:

```
□ Nunca por debajo de tu precio mínimo viable (ver 83)
□ Con fecha de fin decidida antes de empezar
□ Preferible que aterrice justo debajo de $60.000 si tu producto está cerca
□ Sin inflar un precio tachado para simular descuento: riesgo legal real (ver 92)
□ Un cambio brusco puede dejarte "inactiva para revisar": mueve en pasos
```

## Cómo medir si la campaña sirvió

No mires unidades. Mira estas cuatro:

| Métrica | Compara contra |
|---|---|
| **Utilidad total del período** | El mismo número de días antes de la campaña |
| **Unidades vendidas** | Para saber si el volumen llegó |
| **Devoluciones y reclamos en los 30 días siguientes** | El costo llega después (`95`, `96`) |
| **Posición orgánica 15 días después** | La campaña deja rastro en el algoritmo, bueno o malo |

La cuarta es la que justifica entrar aunque la campaña empate: **la conversión durante el evento
alimenta el ranking orgánico posterior**.

## El error clásico

Entrar al Hot Sale con el margen normal en la cabeza y el descuento en el precio, sin recalcular.
El vendedor factura el triple, celebra, y al cerrar el mes descubre que ganó menos que en febrero —
con el triple de trabajo, el triple de envíos y el triple de devoluciones.

El segundo: quedarse sin stock el día 2 de 5. La campaña se acaba y el daño al posicionamiento dura
semanas.

## Relacionados

`76` el cargo por venta 8%-22% · `78` el envío que pagas tú · `79` el umbral de los $60.000 · `80`
cuotas sin interés · `82` la calculadora de margen · `83` precio mínimo viable · `88` precio
psicológico · `89` la guerra de precios · `92` el precio tachado y la SIC · `93` cupones propios ·
`95` costo de la devolución · `99` revisión mensual · `150` ACOS sano
