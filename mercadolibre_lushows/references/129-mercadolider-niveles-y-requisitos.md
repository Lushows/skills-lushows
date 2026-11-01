# MercadoLíder: niveles y requisitos

Módulo de datos duros. Las cifras de aquí son las oficiales de **Colombia**, leídas del centro de
ayuda. No coinciden con las que circulan en blogs porque esos copian números de Argentina o México.
Si le apuntas a MercadoLíder, apúntale a estos números.

## Los tres niveles (Colombia)

Oficial ML Colombia (`/ayuda/864`), verificado sep-2026:

| Nivel | Ventas concretadas (últimos 60 días) | Monto facturado (últimos 60 días) |
|---|---|---|
| **MercadoLíder** | 120 o más | $10.000.000 COP o más |
| **MercadoLíder Gold** | 300 o más | $30.000.000 COP o más |
| **MercadoLíder Platinum** | 600 o más | $80.000.000 COP o más |

Las dos condiciones son simultáneas: necesitas **las ventas Y la facturación**.

## Qué cuenta como "venta concretada"

Definición oficial, y aquí es donde mucha gente hace mal la cuenta (oficial ML Colombia, verificado
sep-2026):

```
□ Son las ventas que YA RECIBIÓ el comprador — no las pagadas, no las despachadas: las recibidas
□ En un carrito, cada producto DIFERENTE cuenta como una venta
□ NO se tienen en cuenta las ventas con publicación Gratuita
```

Las tres tienen consecuencias operativas:

| Regla | Consecuencia |
|---|---|
| Solo las recibidas | Tus últimos 5-7 días de ventas no suman todavía. Cuenta con retraso |
| Carrito = varias ventas | Vender combos de productos distintos en un carrito te suma más rápido que un pack de uno solo |
| Gratuitas no cuentan | Si vendes con publicación gratuita, ese volumen es invisible para el nivel |

Y hay un detalle circular en la última: si eres MercadoLíder **no puedes vender de forma gratuita**
(oficial). Las gratuitas son una escalera que se retira sola al llegar arriba (`42`).

## Ticket promedio implícito

| Nivel | Ticket promedio mínimo que necesitas |
|---|---|
| MercadoLíder | $83.333 COP |
| Gold | $100.000 COP |
| Platinum | $133.333 COP |

Si vendes a $25.000, llegar a MercadoLíder te exige 400 ventas en 60 días, no 120: manda la
condición de facturación. **El nivel se define por el ticket tanto como por el volumen**, y eso
debería influir en qué catálogo armas (`75`, `80`).

## Requisitos generales (los tres niveles)

```
□ Antigüedad mayor a 4 meses
□ Reputación VERDE (verde claro no alcanza)
□ Medición sobre los últimos 60 días
```

Los 4 meses son piso duro: puedes hacer $80 millones en tu primer mes y no serás Platinum hasta el
quinto. No hay atajo.

## Requisitos de calidad (los tres niveles)

Oficial ML Colombia, verificado sep-2026. Son más estrictos que los umbrales del verde común:

| Métrica | Verde común (60 días) | MercadoLíder |
|---|---|---|
| Ventas con reclamos | ≤ 3,5% | ≤ **2,5%** |
| Mediaciones | — | ≤ **0,5%** |
| Ventas canceladas | ≤ 2,5% | ≤ **1,5%** |
| Envíos incorrectos | ≤ 12% | ≤ **10%** |

Traducido a casos reales, para que duela:

| Ventas en 60 días | Reclamos máx. | Mediaciones máx. | Canceladas máx. | Envíos incorrectos máx. |
|---|---|---|---|---|
| 120 (MercadoLíder) | 3 | **0** | 1 | 12 |
| 300 (Gold) | 7 | 1 | 4 | 30 |
| 600 (Platinum) | 15 | 3 | 9 | 60 |

**Con 120 ventas, una sola mediación te deja fuera.** El 0,5% sobre 120 es 0,6 casos: una mediación
te pone en 0,83%. Por eso `135` —resolver en la etapa de reclamo, antes de que escale— no es un
consejo de buen trato sino un requisito aritmético.

## ⚠️ Por qué los blogs no coinciden

Vas a encontrar tablas que dicen "180 ventas y $300.000" o "415 ventas y $3.820.000". Ninguna es
Colombia 2026.

> ⚠️ **Cuidado con las cifras de otros países.** Las tablas de MercadoLíder que circulan mezclan
> Argentina, México y Chile. La única válida para Colombia es la de arriba, del centro de ayuda de
> `mercadolibre.com.co`. Si una fuente no dice explícitamente "Colombia", no la uses.

## Cómo verificar dónde estás

| Vía | Qué te dice |
|---|---|
| Mi cuenta → Reputación | Tu nivel actual, tus métricas y cuánto te falta |
| `GET /users/$USER_ID` | `seller_reputation.power_seller_status`: `platinum`, `gold`, `silver` o `null` |

Los valores internos de la API no mapean uno a uno con los nombres comerciales del país. Verifica
contra tu panel antes de confiar en el mapeo (`195`).

## ¿Vale la pena perseguirlo?

| Situación | Veredicto |
|---|---|
| Cerca de 120 ventas y verde | Sí. El salto de exposición justifica apretar 60 días |
| En amarillo | No. Primero verde (`128`): el nivel exige verde, no "casi verde" |
| Ticket bajo, no llegas a la facturación | Replantea el catálogo antes que el esfuerzo (`80`) |
| Compites en catálogo | Sí, con prioridad: el nivel desempata (`63`, `130`) |
| Llevas 2 meses vendiendo | No aplicas aún. Usa el tiempo para limpiar procesos |
| Vendes con publicaciones gratuitas | Ese volumen no cuenta. Migra a publicación paga primero (`42`) |

**MercadoLíder no es un premio a la antigüedad: es un certificado de que tu operación no rompe
nada.** Las cuatro métricas de calidad son un examen de logística, no de ventas.

## El error clásico

Empujar volumen a cualquier costo los últimos 15 días para cruzar el umbral y, en el apuro, romper
el límite de cancelaciones o de envíos. Terminas con más ventas y sin nivel.

El orden correcto es al revés: **primero 60 días con las cuatro métricas holgadas, después empujas
volumen.** Las métricas son el filtro; el volumen es lo fácil.

## Relacionados

`125` el termómetro · `126` las tres métricas · `127` el periodo de evaluación ·
`128` cómo se recupera una caída · `130` beneficios reales · `135` el reclamo y la mediación ·
`42` tipos de publicación · `63` ganar el catálogo · `144` plan de defensa de la cuenta
