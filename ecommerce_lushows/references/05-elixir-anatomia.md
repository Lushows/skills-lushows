# 05 · Tema Elixir (Shopify): anatomía, tokens medidos y qué NO copiar

> Vigencia: 16-sep-2026. Revisadas 3 demos en vivo (Boosted oscuro, Radiance claro, Aero naranja) a
> 390 px y 1440 px, con carrito abierto. Página de venta: ecomelixir.com/products/elixir-shopify-theme
> (US$200, hecho sobre Dawn). **No publica ninguna cifra de conversión** ("5.000+ tiendas" y "4.500+"
> en la misma página; "CVR Optimized" es marketing).
>
> Veredicto: el **diseño y la mecánica** son de primera; la **mitad de la prueba social de las demos
> es falsa o texto de plantilla**. Se copia lo primero, nunca lo segundo.

## 1. Anatomía de la PDP (móvil, demo Boosted)

**Primer pantallazo (844 px):**
1. Barra de anuncio 45 px (en Aero, varios mensajes rotando con flechas).
2. Header: hamburguesa · logo centrado · carrito.
3. Galería cuadrada + 5 miniaturas; **la foto principal es infografía** (producto + 4 datos alrededor).
4. Calificación con link a reseñas.
5. Título condensado mayúsculas 48 px/800.
6. Subtítulo de una línea con 3 palabras clave subrayadas.
7. **4 píldoras de beneficio** (fondo oscuro, check de color, texto corto).
8. Título pequeño centrado sobre línea: "BUNDLE & SAVE".

**Primer scroll:**
9. **3 tarjetas-radio de cantidad**: miniatura del pack · "Ahorras $X" · precio grande de color · tachado
   debajo · seleccionada con borde 1 px de acento y fondo más profundo · etiquetas "MÁS POPULAR" /
   "MEJOR VALOR" (11 px, 800, radio 4 px) montadas sobre el borde.
10. **Fecha de entrega**: píldora con punto verde que late, "Pide hoy y recíbelo el **20 de septiembre**".
11. **Botón con precio adentro**: "AGREGAR — $36 ~~$48~~", padding vertical 19 px, 16 px/800 mayúsculas.
12. Micro-garantías en una línea bajo el botón.
13. Íconos de pago con borde tipo tarjeta.
14. **Pestañas Reseñas / Comparación / Ficha** dentro del bloque de compra.

**Debajo:** "Por qué confiar" (4 sellos sobre foto oscurecida) → testimonios con título bicolor →
el problema ("la verdadera causa") → imagen+texto con dato → 4 beneficios → **carrusel UGC 9:16
con tarjeta central ×1.15** y subtítulos quemados → 4 tarjetas de beneficio → **estadísticas en
anillos animados** → **línea de tiempo que se llena con scroll** (semana 1 / mes 1…) → ingredientes/
mecanismo por pasos → **tabla comparativa con columna propia resaltada** → garantía con escudo →
FAQ acordeón "+" → footer 3 columnas con "Rastrear pedido".

**Otras piezas (Radiance/Aero):** bundle en 2 tarjetas verticales con cinta "2 REGALOS", franja de
regalo incluido, logos de prensa, **antes/después con slider**, "comprados juntos" con "+ Agregar",
3 garantías con ícono, acordeón de descripción/envíos/garantía.

## 2. Tokens medidos

| | Boosted (oscuro) | Radiance (claro) | Aero (tech) |
|---|---|---|---|
| Fondo | `linear-gradient(180deg,#141720,#1C3353)`; footer #0C0C0D | `linear-gradient(215deg,#FFF,#F6F8F9 84%)` | blanco; footer #181B1D |
| Acento | #358BFF · link #9DC7FF | #D9ECFC + línea rosa | #FF5801 |
| Títulos | Barlow Condensed 800, mayúsculas, -0.1 px; H1 48/48, H2 40/44 (34-36 móvil) | DM Sans 500, H2 ~28 | Helvetica 700, **-0.9 px**, H2 40/44, título 30 |
| Texto | Inter 16/22.4 · 14/18.2 · etiquetas 11/800 | DM Sans #25282A | Helvetica |
| Botón | degradado #E9E9E9→#B3BFD3, borde 1 px #6489BD + **borde inferior 2 px** (relieve), radio 6 | degradado #25282A→#101112, radio 40, 18/500 | naranja, radio 10 |
| Radios | botón 6 · video 8 · bundle ~6 · inputs 15 · variantes 40 · imágenes 0 | píldora 40 | bundle 8 |

- **Escala fluida del tema:** h1 32-48 · h2 28-40 · h3 24-32 · h4 22 · cuerpo 19/16/14/12.
- **Duraciones:** .1 / .2 / .3 / .5 / .6 / .75 s · curva `cubic-bezier(0,0,.3,1)`.
- **Título bicolor:** 2ª línea con degradado metálico `linear-gradient(#B8B8B8 1%,#FCFCFC 52%,#A3A3A3 56%,#FFF 74%,#D1D1D1)` + `background-clip:text`.
- Íconos lineales monocromos `currentColor` dentro de círculos; checks rellenos.

## 3. Micro-interacciones (cómo están hechas)

| Efecto | Implementación |
|---|---|
| Entrada de secciones | `fadeInUp` opacity 0 + translateY(20px) → 0, .8s ease-out |
| Brillo del botón fijo | `::after` de left −100% → 200%, `shine 6s ease 2s infinite` |
| Punto de entrega | opacidad .5↔1 (1 s) + `::after` scale 1→2.2 que se desvanece |
| Anillos de estadística | SVG `stroke-dasharray/dashoffset` disparado con IntersectionObserver (0.1) |
| Línea de tiempo | en scroll: `getBoundingClientRect` → `.timeline-fill{height:%}` |
| Carrusel video | central `scale(1.15)`, `transition: transform .4s cubic-bezier(.25,1,.5,1)` |
| Botón hover | `translateY(-2px)` + sombra `0 4px 8px rgba(0,0,0,.15)` |
| Agregar al carrito | `pulse-success` scale 1→1.05 |
| Antes/después | `mousemove`/pointer sobre la pista |

**Barra de compra fija** (`sticky-add-to-cart.js`): aparece cuando el botón principal
`getBoundingClientRect().bottom < -100`; `translateY(100%)→0` en .4 s con sombra
`0 -1px 5px #0000001a`; **se esconde cuando el carrito está abierto** (MutationObserver). Móvil: un
botón ancho con brillo cada 6 s. Desktop: rating + nombre del producto.

## 4. Carrito lateral

- 480 px desktop / pantalla completa móvil, entra con `transform .2s` y oscurece el fondo.
- Encabezado "Tu carrito" + número en círculo + X fina.
- **Barra de metas** con `<progress>` nativo (umbral en centavos, varias metas: envío gratis, regalo),
  mensaje "Ya tienes envío gratis".
- Línea de producto: miniatura, nombre, variante, tachado + actual, píldora "Ahorras $30", − 1 +, papelera.
- Protección de envío con interruptor **apagado por defecto** (correcto: encenderlo por defecto es patrón oscuro).
- Pie: píldora "Ahorro −$30" · total con tachado · botón ancho **"🔒 PAGO SEGURO"** · garantía · íconos de pago.

## 5. Los 15 acabados que sí se copian

1. Precio **dentro** del botón.
2. Bundles en tarjetas-radio con miniatura, ahorro en $, etiqueta sobre el borde (`top:-8px; right:12px`).
3. Título pequeño centrado sobre línea para separar bloques sin cajas.
4. Fecha de entrega concreta con `Intl.DateTimeFormat` + punto verde que late.
5. Titulares con segunda línea en otro tono (metálico o gris).
6. Fondos con degradado vertical casi imperceptible en vez de color plano.
7. Botón con relieve (borde inferior 2 px más oscuro) y hover −2 px.
8. 4 píldoras de beneficio bajo el título.
9. Foto principal tipo infografía + miniaturas.
10. Pestañas Reseñas/Comparación/Ficha dentro del bloque de compra.
11. Tabla comparativa con columna propia resaltada (fondo translúcido + borde + radio).
12. Carrusel UGC con central ×1.15 y laterales asomando.
13. Línea de progreso con scroll + anillos animados (solo con datos reales).
14. Barra fija que aparece al perder el botón y se oculta con el carrito abierto.
15. Carrito con ahorro explícito, candado, garantía e íconos bajo el botón.
+ Sistema de etiquetas único en toda la página (11 px/800/mayúsculas/radio 4).

## 6. Lista negra (vista en las demos — NO copiar)

- Escasez fija en el HTML: "Regalo reservado para los próximos 53 pedidos", "93% VENDIDO", "Quedan pocos" con stock.
- Conteos de reseñas inventados y contradictorios (693 vs 1.422; 2.500 vs 10.839; "56M vistas").
- Estrellas verdes con logo de **Trustpilot** sin widget real (suplantación).
- Garantías contradictorias en la misma página (30/60/90/100 días; envío gratis "siempre" y "desde $100").
- Carrito que dice "ahorras en tu primera suscripción" sin suscripción.
- Tachado permanente de un precio que nunca existió; bundles que no ahorran más.
- Estadísticas "autorreportadas" (94%) sin estudio y claims de salud (riesgo INVIMA/COFEPRIS).
- Testimonios de relleno ("Dr. PhD", "Verified" sin compra) y texto de plantilla publicado.
- Bloque "Replica Warning" que asusta sin evidencia.
- Peso: 750 KB-1,3 MB de HTML, 86 `<script>`, 62 `<style>`, `console.log` activos → a mano se logra lo mismo con una fracción.

Las capturas y el HTML de las demos quedaron en el scratchpad de la sesión del 16-sep (`research-elixir/`).
