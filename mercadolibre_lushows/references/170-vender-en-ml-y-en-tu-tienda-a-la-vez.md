# Vender en ML y en tu tienda a la vez

Mercado Libre te presta tráfico y te cobra comisión. Tu tienda propia te deja el margen y el
cliente, pero el tráfico lo pagas tú. No es una elección: es una secuencia. Este módulo dice cuándo
abrir el segundo canal, qué precio poner en cada uno y cuál es el riesgo que hunde a casi todos.

## Lo que da cada canal

| | Mercado Libre | Tienda propia |
|---|---|---|
| Tráfico | Ya está ahí: **~8 millones de usuarios y +80 millones de visitas/mes en Colombia** | Cero. Lo traes tú o no hay nadie |
| Costo por venta | Comisión de la categoría + cargos de envío | Pasarela de pago + costo de adquisición del cliente |
| Dueño del cliente | Mercado Libre. Tienes la orden, no la relación | Tú: correo, teléfono, historial |
| Confianza | Prestada, instantánea (Compra Protegida, Mercado Pago) | Hay que construirla desde cero |
| Control del checkout | Ninguno | Total |
| Reglas | Las de ML: prohibido dar contacto, prohibido sacar al cliente | Las tuyas |
| Datos | Los que ML te muestra | Todos |
| Riesgo | Una suspensión apaga el negocio (`143`) | Un bloqueo de pasarela o de cuenta publicitaria |

(cifras de tráfico: ALTA, verificado sep-2026)

## El veredicto

**Primero ML hasta que el canal sea estable y rentable; la tienda propia después, y no como
reemplazo sino como el sitio donde le vendes por segunda vez al cliente que ML te presentó.**

Razón: en ML el tráfico es gratis y la conversión alta porque la confianza ya existe. En tu tienda,
cada visita cuesta plata y la conversión arranca muy abajo. Abrir tienda propia antes de tener
producto validado y reputación verde es cambiar un canal que funciona por uno que hay que financiar.

Señales de que ya es momento:

```
□ Reputación verde estable y más de 4 meses vendiendo (`129`)
□ Margen conocido por SKU y positivo sin pauta (`165`)
□ Al menos un SKU de recompra: algo que el mismo cliente vuelva a necesitar
□ Caja para pagar tráfico 3-6 meses sin que el negocio dependa de esas ventas
□ Un sistema de stock que ya no vive en tu cabeza (`196`)
```

## Mercado Shops ya no es la opción

| Fecha | Qué pasó |
|---|---|
| 16-ene-2025 | Dejaron de crearse tiendas nuevas |
| 30-abr-2025 | Se cerraron las inactivas |
| 31-dic-2025 | Se eliminaron todas; los dominios dejaron de funcionar |

(ALTA como decisión global, verificado sep-2026). El reemplazo dentro de ML es **"Mi Página"**, que
vive en el marketplace: sin dominio propio y sin control del checkout. Costo en Colombia: **3 meses
gratis y luego $44.990 COP/mes**, cobro automático, cancelable pausando la página (MEDIA-ALTA,
verificado sep-2026).

Léelo claro: **Mi Página es una vitrina dentro de ML, no una tienda propia.** No resuelve el
problema del dueño del cliente. Sirve para consolidar marca y campañas de Brand Ads (`157`), no para
escapar de la comisión.

## ¿El mismo precio en ambos canales?

La pregunta que todos hacen. La respuesta corta: **sí al mismo precio de lista, no al mismo valor
percibido.**

| Estrategia | Qué pasa |
|---|---|
| Más barato en tu tienda | La peor. El comprador te encuentra en ML, compara, compra afuera, y tú pierdes la señal de conversión que sostiene tu posición (`58`) |
| Más caro en tu tienda | Nadie compra ahí. Canal muerto |
| **Mismo precio, mejor oferta propia** | El veredicto: igualas el precio de lista y diferencias con lo que ML no replica — packs, obsequio, garantía extendida, suscripción |

Cómo se ve en la práctica:

| Canal | Producto | Precio | Diferenciador |
|---|---|---|---|
| Mercado Libre | Unidad suelta | $89.900 | Entrega Full en 24-48 h |
| Tienda propia | Unidad suelta | $89.900 | — |
| Tienda propia | Pack de 3 | $229.900 | No existe en ML |
| Tienda propia | Suscripción mensual | $79.900/mes | No existe en ML |

Así el canal propio gana ticket y recurrencia sin canibalizar tu posición en el marketplace.

## Lo que no puedes hacer

Estas son reglas de Mercado Libre, no sugerencias:

```
✗ Poner teléfono, WhatsApp, correo, redes o URL en título, descripción, imágenes o respuestas
✗ Meter volantes o tarjetas con tu web dentro del paquete
✗ Escribirle al comprador por el chat para ofrecerle comprarte por fuera
✗ Usar las preguntas como canal de contacto
```

Prohibido dar datos de contacto en descripción, imágenes y preguntas/respuestas (excepciones:
Autos/Motos, Inmuebles, Servicios y MercadoProveedores) — MEDIA-ALTA, verificado sep-2026. El
castigo típico es la eliminación de la publicación o la pregunta, con riesgo de sanción si es
reiterado (`131`).

El camino legítimo para que el cliente de ML llegue a tu tienda es la **marca**: que el producto y
el empaque tengan tu nombre, y que ese nombre sea buscable. Nada más.

## El riesgo que de verdad hunde: la sobreventa

Dos canales, un solo inventario. Vendes la última unidad en tu tienda y en ML al mismo tiempo; una
de las dos la tienes que cancelar. Y la cancelación por falta de stock es la métrica con el único
umbral oficial publicado: **más del 2,5% de ventas canceladas → la cuenta puede ser suspendida para
vender** (oficial ML CO, verificado sep-2026).

Lo peor: la API de ML **no tiene reserva de stock cross-canal ni bloqueo atómico**. No hay una
función que te salve; hay que diseñarlo.

| Mitigación | Cómo |
|---|---|
| Colchón de seguridad | Publica en ML 1-2 unidades menos de las que tienes (`196`) |
| Webhooks, no polling | Reacciona a `orders_v2` en el momento, no cada 15 minutos (`190`) |
| Un solo maestro de stock | Un sistema manda; los demás obedecen. Nunca dos fuentes de verdad (`123`) |
| SKUs separados por canal | Si el volumen es bajo, parte el inventario físicamente y no lo compartas |
| Multi-bodega, con la API correcta | Con stock multi-origen, `PUT /items` con `available_quantity` se ignora o falla (`196`) |

## Dónde termina esta skill

| Tema | Rutea a |
|---|---|
| Montar la tienda propia, plataforma, checkout, contraentrega, proveedores | `dropshipping_lushows` |
| Traer tráfico a la tienda propia (Meta, Google, TikTok) | `facebook_ads_lushows`, `google_ads_lushows`, `tiktok_ads_lushows` |
| Facturación electrónica de dos canales | `contador_lushows` |
| Si el negocio aguanta financiar un segundo canal | `economist_lushows` |

**Mercado Ads sí es de esta skill** (`145`-`155`): es subasta interna del marketplace. La pauta que
lleva gente a tu dominio propio, no.

## El error clásico

Abrir la tienda propia para "dejar de pagarle comisión a Mercado Libre" y descubrir a los tres
meses que el costo de traer un cliente por Meta es más caro que la comisión que estaba pagando. La
comisión de ML no es un impuesto: es el precio del tráfico y de la confianza, y viene con
conversión mucho más alta. **La tienda propia no ahorra comisión: cambia comisión por costo de
adquisición, y hay que correr el número antes, no después.**

## Relacionados

`58` la conversión manda · `100` cómo funciona Mercado Envíos · `123` stock y multi-bodega ·
`129` MercadoLíder · `131` lo que está prohibido en preguntas y descripción ·
`139` la cancelación y su castigo · `143` suspensión de cuenta · `145` qué es Mercado Ads ·
`157` Brand Ads y Tienda Oficial · `158` Mi Página · `165` las métricas que de verdad miras ·
`171` cuándo abrir otro país · `190` webhooks · `196` sincronizar stock multicanal
