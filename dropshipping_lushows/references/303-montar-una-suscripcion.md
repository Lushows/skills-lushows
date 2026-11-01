# Montar una suscripción

> Una suscripción no es un botón en el checkout. Es un compromiso operativo: si el mes 3 se demora el
> envío, no pierdes un pedido, pierdes al cliente y a todos los pedidos que faltaban. Móntala cuando
> la operación aguante, no cuando la idea te emocione.

## Cuándo conviene y cuándo no

| Condición | Suscripción |
|---|---|
| El producto se acaba en 25-60 días | **sí** |
| Ya vendiste ≥100 unidades del mismo SKU sin quejas de calidad | **sí** |
| Tienes stock local y control de despacho | **sí** |
| Tu proveedor se demora 15-25 días desde China por pedido | **no** — el ciclo no cierra |
| El producto es novedad, regalo o de temporada | **no** |
| Todavía estás testeando 5 productos | **no** — todavía no sabes cuál es |
| Tu pasarela no soporta cobro recurrente con tarjeta guardada | **no** (`192`, `193`) |

Regla dura: **primero pruebas que la gente recompra manualmente** (`305`, `308`). Si nadie recompra
por su cuenta, nadie se va a suscribir. La suscripción amplifica una recompra que ya existe; no la
inventa.

## Los tres modelos, y cuál se parece a tu caso

| Modelo | Cómo funciona | Churn típico | Dificultad |
|---|---|---|---|
| **Reposición real** (cobro recurrente) | se cobra la tarjeta cada 30/60 días y se despacha solo | 5-8% mensual | alta: pasarela + dunning + operación |
| **Pack multi-mes** (pago único) | vende 2 o 3 unidades en un solo cobro, etiquetado como "suscripción" o "tratamiento" | no aplica: es compra única | **baja** |
| **Suscripción manual** (recordatorio + link) | no guardas tarjeta; le escribes y él recompra | equivale a recompra normal | media |

El modelo observado en `eleveitmx.shop` (competidor directo en MX) es el **segundo**: vende packs
etiquetados como suscripción sin cobro recurrente real.

| Oferta observada en eleveitmx.shop | MXN |
|---|---|
| Producto núcleo | 549 |
| Pack doble | 727 |
| Pack triple | 1.000 |
| Order bump "Procesamiento Prioritario" | 49 |
| Upsell digital "Guía" | 359 |

Fíjate en la mecánica: el pack triple cuesta 1.000 contra 1.647 de comprar tres veces el núcleo
(−39%), pero cobra **1.000 hoy** en vez de 549. Sube el ticket, financia el CAC por adelantado y
elimina el riesgo de churn — porque no hay churn, es un pago único. **Para una operación nueva con
capital bajo, este modelo gana casi siempre.**

## Descuento: cuánto y por qué

| Descuento por suscribirse | Efecto |
|---|---|
| 0% | casi nadie se suscribe; solo funciona si el valor es la comodidad |
| **10-15%** | el rango estándar de DTC; sostenible |
| 20% | funciona, pero revisa que el margen del mes 2 en adelante siga vivo |
| 25%+ | atrae cazadores de descuento que cancelan al primer cobro; empeora la cohorte (`302`) |

Con la economía verificada: ticket 54,59 y margen 26,47 (48,5% del ticket). Un 15% de descuento
(−8,19) deja el margen en ~18,28. Sigue siendo mayor que los 15,93 de la primera venta con CAC. **El
descuento cabe.** Un 30% no: deja ~10,1 y cualquier reposición, devolución o fallo de tarjeta se lo
come. Verifica tus propios números con `Matematicas_lushows` antes de fijarlo.

## Herramientas

| Plataforma | Opción | Nota |
|---|---|---|
| Shopify | apps de suscripción nativas (Shopify Subscriptions y equivalentes de terceros) | verificar precio y comisión vigentes en 2026 |
| WooCommerce | extensiones de suscripción | más control, más mantenimiento |
| Cobro directo con pasarela | tokenización de tarjeta en la pasarela | requiere que la pasarela lo soporte en tu país (`192`) |
| México | verificar que el procesador soporte cobros recurrentes con tarjetas mexicanas y MSI | **MSI y suscripción no se combinan**: en Buen Fin vende packs, no suscripción |

No elijas herramienta antes de definir el modelo. Si tu modelo es "pack multi-mes", **no necesitas
ninguna app**: es una variante de producto.

## Cómo se presenta en la página sin matar la conversión

| Regla | Detalle |
|---|---|
| Opción única marcada por defecto | radio button "Suscripción −15%" preseleccionado, "Compra única" visible al lado |
| Nunca esconder la compra única | esconderla sube suscripciones y dispara contracargos y reseñas malas |
| Decir la frecuencia en la etiqueta | "cada 30 días", no "recurrente" |
| Decir cómo se cancela, en el mismo bloque | "Cancelas cuando quieras desde tu correo" — sube conversión, no la baja |
| No pedir cuenta de usuario para suscribirse | fricción innecesaria |
| Mostrar el ahorro en pesos, no solo en % | "ahorras $150 MXN" pega más que "−15%" |

Lo que mata conversión no es la suscripción: es la **ambigüedad**. El comprador que no entiende
cuándo le vuelven a cobrar, no compra. Ver `desingweb-lushows` para el diseño del bloque.

## Lo que hay que tener montado ANTES del primer cobro recurrente

| Pieza | Por qué |
|---|---|
| Dunning / reintentos de cobro | el 35% de tu churn será tarjeta fallida (`304`) |
| Aviso pre-cobro 3 días antes | reduce contracargos y cancelaciones-sorpresa |
| Portal o flujo de "pausar" además de "cancelar" | pausar recupera una parte de los que cancelarían |
| Stock para 2 ciclos por delante | quedarte sin producto en el mes 2 mata la cohorte entera |
| Reglas fiscales del cobro recurrente | rutea a `contador_lushows`; en MX, facturación de cargos recurrentes |
| Términos claros de cancelación | requisito legal y de la pasarela |

## Riesgos específicos del nicho (México, suplementos y belleza)

| Riesgo | Mitigación |
|---|---|
| COFEPRIS: claims terapéuticos en el copy de la suscripción | **cero claims**; el permiso de importación es del importador, no tuyo; Aviso de Funcionamiento y verificar el registro del distribuidor |
| Suscripción de producto con caducidad corta | rotación de lote; no acumules stock para 6 meses |
| Contracargos por cobro no reconocido | aviso pre-cobro + descriptor de tarjeta con el nombre de la marca, no del proveedor |
| Cliente que cambia de opinión al mes 2 | flujo de pausa y de cambio de frecuencia |

## Decisión recomendada para el proyecto México (dic-2026)

| Fase | Modelo |
|---|---|
| Test (oct-nov 2026) | compra única + **pack doble y triple** (modelo eleveitmx) + order bump |
| Buen Fin (13-17 nov) | packs con MSI, sin suscripción |
| Diciembre | packs; capturar correo y WhatsApp de todos |
| Ene-mar 2027 | medir cohortes (`302`); si la recompra pasa 20%, montar reposición real |

Traducción: **no montes suscripción en 2026.** Monta packs, que dan el mismo efecto de caja sin
riesgo de churn, y guarda la suscripción para cuando tengas datos de `302` y `309`.

## Relacionados
`192` · `193` · `230` · `300` · `301` · `302` · `304` · `305` · `308` · `309`
