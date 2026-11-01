# Tráfico externo hacia tu publicación

Llevar gente desde Meta, TikTok o Google hasta una publicación de Mercado Libre. A veces es la
jugada correcta; muchas veces es regalarle margen a ML por un cliente que tú conseguiste. Este
módulo te da el criterio; la ejecución de las campañas no es de esta skill.

## La frontera, explícita

| Qué | Skill |
|---|---|
| Mercado Ads: Product Ads, Brand Ads, Display de ML — **retail media interno** | **Esta skill** (`145` a `164`) |
| Facebook e Instagram | `facebook_ads_lushows` |
| Google Ads, Shopping, YouTube | `google_ads_lushows` |
| TikTok | `tiktok_ads_lushows` |
| Qué producto vender y de dónde traerlo | `dropshipping_lushows` |
| Si conviene tener tienda propia en vez de ML | `economist_lushows` |

Aquí decidimos **si** mandar tráfico externo y **hacia dónde**. Cómo armar la campaña, los
creativos, los públicos y el píxel lo resuelven las skills de ads.

## El costo escondido: la comisión

Esto es lo que casi nadie calcula antes de encender la campaña. Si tú pagas el clic **y** ML cobra
su comisión, estás pagando dos veces por la misma venta.

Producto de $80.000, comisión 14% (rango oficial 8%-22%, ML Colombia, verificado sep-2026):

| Destino del tráfico externo | Comisión de ML | Costo de la pasarela | Se te va |
|---|---|---|---|
| Publicación de Mercado Libre | $11.200 | — | **$11.200** |
| Tienda propia (Shopify, WooCommerce) | $0 | ~3,5% = $2.800 | **$2.800** |
| Diferencia por venta | | | **$8.400** |

**Si tú pones el tráfico y ML pone la comisión, ML te está cobrando por un cliente que él no
trajo.** Sobre 100 ventas al mes, esos $8.400 son $840.000 mensuales.

Eso no cierra el caso: hay razones legítimas para mandar tráfico a ML de todos modos. Pero la
cuenta hay que tenerla en la cabeza.

## Cuándo SÍ tiene sentido

| Situación | Por qué se justifica |
|---|---|
| **No tienes tienda propia** | La comisión es el precio de no tener que construir nada |
| **La confianza es el freno de compra** | En Colombia mucha gente compra en ML porque no le da confianza pagar en una web desconocida. La compra protegida vale plata |
| **Estás empujando una publicación nueva** | Las visitas externas también alimentan la conversión y el ranking (`153`) |
| **Peleas el catálogo** | Ventas y conversión son variables que deciden el ganador (`63`) |
| **Fecha caliente** | Sumar tráfico propio a un momento de alta conversión (`162`) |
| **Full y entrega al día siguiente** | La logística de ML es tu argumento y no la tienes en tu web |
| **Producto de ticket alto con cuotas** | Las cuotas sin interés de ML cierran ventas que tu web no cierra |

## Cuándo NO

| Situación | Por qué es regalar margen |
|---|---|
| Margen neto por debajo del 20% | Comisión + clic externo no caben (`150`, `154`) |
| Ya tienes tienda propia funcionando | Manda el tráfico ahí y usa ML para el tráfico que ML ya tiene |
| Tu objetivo es construir lista de clientes | ML no te da el dato del comprador. Cero retención (`159`) |
| El producto es de recompra frecuente | El segundo pedido debería ser tuyo, no de ML |
| Estás pautando en Meta "para posicionar en ML" | Product Ads hace eso más barato y con intención (`146`) |
| Tu ficha no convierte | Vas a pagar clic caro para mostrar una ficha mala (`164`) |

**El último punto vale doble: el tráfico externo no perdona una ficha mala, la castiga más caro.**
El clic de Meta cuesta y no viene con intención de compra; si llega a una publicación floja, se va
sin dejar nada — ni venta ni señal buena para el algoritmo.

## La estrategia mixta, que es la que suele ganar

No es "ML o tienda propia". Es cada canal haciendo lo suyo:

| Canal | Trabajo |
|---|---|
| **Product Ads** (`146`) | Capturar la demanda que ya está dentro de ML |
| **Google Search** | Capturar la demanda que busca en Google → `google_ads_lushows` |
| **Meta / TikTok** | Generar demanda que no existía → `facebook_ads_lushows`, `tiktok_ads_lushows` |
| **Tienda propia** | Recibir el tráfico que TÚ generaste, quedarte con el dato y la recompra |
| **ML** | Recibir a quien necesita la confianza, las cuotas o la logística de ML |

La regla que ordena todo: **el tráfico que ML trae, se paga con comisión. El tráfico que tú traes,
debería llegar a tu casa.** La excepción es cuando la confianza o la logística de ML valen más que
la comisión — y eso se calcula, no se intuye.

## Cómo medirlo sin engañarte

El problema práctico: la atribución externa hacia ML es mala. No hay píxel tuyo en la publicación
de Mercado Libre, así que no vas a poder cerrar el círculo con precisión.

```
□ Manda el tráfico a UNA sola publicación, no a tu tienda ML completa
□ Corre la campaña externa en un periodo limpio, sin fecha caliente encima
□ Compara las ventas de ESA publicación contra su promedio de las 4 semanas previas
□ Descuenta el efecto de Product Ads si está corriendo sobre el mismo SKU
□ Suma los dos costos: el clic externo Y la comisión de ML
□ Compara ese costo total contra el margen neto del SKU (`150`)
□ Espera 14 días antes de concluir: la atribución de ML tarda (`151`)
```

Si el número no se puede construir con esa precisión mínima, la respuesta honesta es que no sabes
si funcionó — y no saber es motivo suficiente para no escalar.

## El error clásico

Pautar en Meta hacia una publicación de Mercado Libre porque "es más fácil que montar una tienda".
Es más fácil, sí, y también más caro por venta y para siempre: cada venta que traes te cuesta la
comisión completa, y nunca acumulas nada — ni lista de clientes, ni píxel maduro, ni recompra.
**Es alquilar clientes que tú mismo conseguiste.** Puede ser la decisión correcta al arrancar; es
una decisión mala como estado permanente.

## Relacionados

`145` qué es Mercado Ads · `146` Product Ads · `148` las tres estrategias ·
`150` el ACOS sano según tu margen · `151` la ventana de atribución ·
`153` el efecto sobre lo orgánico · `154` el error de pautar sin margen ·
`159` Mi Página y el fin de Mercado Shops · `160` Meli+ ·
`162` preparar una fecha caliente · `164` cuándo no es la respuesta ·
`63` ganar el catálogo · `76` las comisiones · `82` la calculadora de margen · `103` Full
