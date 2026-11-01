# 330 · Modo "producto de referencia → página lista para vender"

> Vigencia: 16-sep-2026. Estrenado con las gafas con cámara de baho.mx.
> Disparador: Luis pega un link de producto o nombra un producto y dice "investígalo / replícalo".
> **Luis NO quiere el proceso: quiere el resultado final de venta.** Investiga todo en silencio,
> habla solo para avisar el estado y entrega la página + los números + lo que falta para publicar.
> El medio de pago NO se toca hasta que Luis lo pida (el botón queda con un evento `checkout`).

## El orden (no saltarse pasos)

| # | Qué | Cómo (lo que funcionó) |
|---|---|---|
| 1 | **Producto y precio** | Si es Shopify: `GET <url>.json` → título, variantes, `price`, `compare_at_price`, fotos, descripción, `created_at` (¿es un test de ayer o un ganador de meses?) |
| 2 | **Stack de conversión** | `grep` en el HTML: `kaching` (bundles), `loox`/`judge.me`/`yotpo` (reseñas), `timer`/`countdown`, `gempages`/`pagefly`, `klaviyo`. La config de Kaching viene en JSON dentro del HTML: niveles, % de descuento, preselección, regalos progresivos |
| 3 | **Estructura visual y fx** | Playwright a 390×844: recorrer `.shopify-section` en orden (id + texto), `document.styleSheets` → keyframes, elementos `sticky`/`fixed`, `<video>` con autoplay. Captura por tramos (la de página completa se cuelga con animaciones) |
| 4 | **Reseñas: ¿son reales?** | Abrir el iframe del widget (`loox.io/widget/.../reviews/<productId>`). Si dice 0 y la página dice "4.8/5 · +2.500 clientes", **son inventadas** (texto del tema). No se copian |
| 5 | **Videos** | URLs `cdn/shop/videos/...mp4`. Son de la marca/creadores: **no se reusan**. Se replica el FORMATO (POV 9:16, 8-12 s) y se lista qué grabar |
| 6 | **Costo real** | Precio FOB en made-in-china / Global Sources / Alibaba por modelo (ej. "M02S"). AliExpress al detal solo como techo. Con Playwright, `WebFetch` a AliExpress falla |
| 7 | **Precio de mercado local** | Mercado Libre del país con Playwright: `.poly-card` → precio + título. Da el rango donde cabe tu precio |
| 8 | **Economía unitaria en código** | Costo puesto en bodega (FOB + flete + arancel `16` + empaque), margen, techo de CAC, CAC por escenario (`228`), **precio mínimo para 20% neto**. Si el precio de la referencia pierde plata, se dice primero |
| 9 | **Manual de marca** | ¿La marca del PRODUCTO tiene manual? → `desingweb-lushows` ref `37` y usar sus colores como toques. Si es marca blanca (casi siempre en dropshipping), el color sale del producto mismo + un acento |
| 10 | **Construir** | **`ecommerce_lushows`** (desde 16-sep es la dueña de la página: radiografía, anatomía, copy, reseñas/videos legales, plantilla `assets/plantilla-pdp/`, QA con `revisar_pdp.py`). Esta skill solo le pasa precio, paquete y veredicto |

## Dirección visual por defecto (Luis, 16-sep: la v1 oscura-monocromática le pareció "suave")

"Capítulos" estilo Apple / Ray-Ban Meta, sin perder el camino a la compra:
- **Ritmo:** alternar negro cinematográfico ↔ claro `#F5F5F7`/blanco. Nunca toda la página del mismo gris.
- **Momento producto:** hero con el producto recortado GRANDE, haz de luz desde arriba, reflejo en el piso,
  titular 3–7,5rem con tracking −.045em, un botón de Comprar + la línea de precio real.
- **Color vivo con roles:** azul eléctrico (`#0A84FF` / `#0071E3` en claro) SOLO para acción;
  un degradado de marca (aquí sol ámbar→coral) SOLO para números clave y la historia del producto.
- **Compra estilo tienda Apple** justo después de los números: galería blanca, paquetes en tarjetas con
  anillo azul al elegir, regalos que se prenden en verde, garantías en lista limpia.
- Sin monoespaciada ni bordes punteados en todo; grano apagado. Se lee "caro".
- Precio del hero coherente con la oferta (no mezclar "desde $X c/u" de un paquete con MSI de otro).

## Lo que se copia y lo que no (`105`)

| Se copia | NO se copia |
|---|---|
| Orden de secciones, tipo de bundle, regalos progresivos, sticky ATC, ticker, tarjetas apiladas, bloque "mira lo que puedes capturar" | Textos, fotos de la marca, videos, reseñas |
| La idea de la garantía y el FAQ | Reseñas y "+2.500 clientes" inventados (PROFECO/FTC) |
| | Escasez falsa ("solo quedan 13 regalos") |
| | Specs infladas (fotos "6560×5428" de un sensor de 8 MP) → usar el dato del sensor |

Fotos: las de fábrica del proveedor (recortar el texto en inglés con PIL) sirven para arrancar; las
que venden son **propias**, y el video **grabado con el producto**.

## Entregable (carpeta `Desktop\dropshipping-productos\<producto>\`)

- `landing.html` + `img/` — página móvil-first lista, checkout pendiente.
- En el chat, corto: veredicto (¿da o no da?), precio y bundle con números, lo que falta para
  publicar (muestra física para verificar specs, videos a grabar, nombre de tienda, pago).

## Trampas técnicas ya resueltas

- Chrome headless no baja de ~500 px de ancho: para ver móvil usar Playwright servido por
  `python -m http.server` (Playwright no abre `file://` fuera del proyecto).
- El hook de seguridad bloquea `innerHTML`: usar `textContent`.
- Recorte de fondo blanco con PIL (umbral brillo+saturación) si `sharp` no está a mano.

## Caso 1 — gafas con cámara M02S (baho.mx, 16-sep-2026)

- Referencia: $990 MXN (tachado $1.409), 2ª unidad −50%, creada el 15-sep = **test, no ganador**. 0 reseñas reales.
- FOB US$36-41 → puesto en bodega ~$1.003-1.052 MXN (arancel 33,5%, TC 18,50 supuesto).
- **A $990 pierde $123 por venta** (a US$33). Mínimo para 20% neto: ~$1.705-1.773 (CAC creativo $126).
- Mercado Libre MX: $1.299-2.099. Elegido **$1.899 · 2 pares $3.398 (preseleccionado) + funda de regalo** → ~$472-521 y ~$812-911 de utilidad por pedido con CAC creativo.
- Se ve como: mundo oscuro + cian fotocromático, Geist/Geist Mono, slider de micas que se oscurecen.
