# 10 · Sistema visual y acabados (lo que hace que se vea caro)

> Vigencia: 16-sep-2026. Fuentes: tema Elixir medido (`05`), Apple/Ray-Ban Meta (`04`), Baymard (`03`),
> `desingweb-lushows` refs 10/11/148/160/164. La plantilla `assets/plantilla-pdp/` ya implementa todo esto.

## 1. La tesis de diseño: "compra arriba, capítulos abajo"

Luis probó dos extremos el 16-sep:
- v1 oscura monocromática → "suave".
- v2 capítulos Apple con hero cinematográfico → mejor, pero la compra quedaba a 1.170 px.

La combinación ganadora (la que usan Elixir y las tiendas que facturan, con acabado Apple):

| Zona | Trabajo | Estilo |
|---|---|---|
| **Primer pantallazo** (0-844 px móvil) | Vender: foto-infografía, calificación real, título, 3-4 píldoras de beneficio, precio | Mecánica Elixir, limpio, alto contraste |
| **Primer scroll** | Cerrar: paquetes, regalos, fecha de entrega, botón con precio, garantías, pagos | Tienda Apple: tarjetas blancas/oscuras nítidas, un color de acción |
| **Capítulos** | Convencer: dolor→solución, demo, beneficios, costo-beneficio, comparativa, videos, reseñas, FAQ | Apple / Ray-Ban Meta: negro ↔ claro, producto gigante, tipografía enorme |
| **Cierre** | Recordar la oferta | Oscuro con luz, botón + precio |

## 2. Tokens base (cambiar solo la capa de marca)

```css
:root{
  /* marca — lo único que cambia por producto o por manual de marca */
  --accion:#0A84FF;          /* botones, selección, links. UN solo color de acción */
  --accion-hover:#3395FF;
  --marca-a:#FFB340; --marca-b:#FF4F6D;   /* degradado de marca: SOLO números clave e historia */
  /* neutros */
  --negro:#000; --grafito:#0B0B0D; --panel:#161618; --panel-2:#1D1D1F;
  --papel:#F5F5F7; --blanco:#FFF; --linea-claro:#D2D2D7; --linea-oscuro:rgba(255,255,255,.1);
  --texto-oscuro:#F5F5F7; --texto-oscuro-2:#A1A1A6;   /* nunca más oscuro que #A1A1A6 sobre negro */
  --texto-claro:#1D1D1F;  --texto-claro-2:#6E6E73;
  --ok:#30D158; --ok-claro:#1F9D48; --alerta:#FF453A;
  /* forma */
  --r-xl:28px; --r-lg:20px; --r-md:14px; --r-sm:8px; --r-tag:4px; --r-pill:999px;
  /* movimiento */
  --ease:cubic-bezier(.16,1,.3,1); --t-micro:.2s; --t-ui:.35s; --t-reveal:.9s;
}
```

Reglas de color:
- **Acción = un color.** Si algo es de ese color, se puede tocar. Nada decorativo lleva el color de acción.
- **Marca = números e historia.** Degradado solo en cifras grandes (8 MP, 7 h) y en el elemento firma del producto.
- **Verde = dinero ganado** (ahorro, regalo desbloqueado, envío gratis). **Nunca rojo para el precio tachado**: gris.
- Con manual de marca: `--accion` y `--marca-*` salen del manual; si el color de marca no da contraste
  AA como botón, se usa en acentos y el botón queda en negro/blanco (`desingweb-lushows` ref 37).

## 3. Tipografía

- Una familia con carácter para todo (Geist, Inter Tight NO; opciones: Geist, Satoshi, General Sans,
  Manrope para tech; DM Sans para beauty; Barlow Condensed solo titulares de suplementos/fitness).
- Escala (móvil → desktop con `clamp`):
  - Hero de capítulo `clamp(2.8rem, 10vw, 7rem)` · lh .98 · tracking −.045em
  - H2 `clamp(2.2rem, 7vw, 4.6rem)` · lh 1.02
  - Título de producto `clamp(1.9rem, 6vw, 2.6rem)` · 700
  - Cuerpo 17 px · lh 1.47 · tracking −.011em
  - Etiquetas 11 px · 700-800 · MAYÚSCULAS · tracking .04em · radio 4 px (sistema único)
- Precios con `font-variant-numeric: tabular-nums`.
- `text-wrap: balance` en títulos, `pretty` en párrafos.

## 4. Fotografía y medios

1. **Foto 1 = infografía del producto**: producto recortado con sombra de contacto + 3-4 datos con
   íconos alrededor (8 MP · 1080p · 7 h · IP65). Fondo con degradado sutil, nunca blanco puro plano.
2. **Foto a escala** (en la mano / puesta) — Baymard 42%.
3. **En uso** (persona, contexto).
4. **Detalle macro** (cámara, bisagra, puerto).
5. **Qué incluye la caja**.
6. Video 6-15 s en loop mudo con subtítulos quemados.
- Todas con el mismo tratamiento (fondo, luz, sombra). Proporción fija de galería (1:1 o 4:5).
- Recortes con `scripts/preparar_medios.py recortar-fondo`; WebP multi-ancho con `web`.
- Nunca texto en otro idioma dentro de una foto.

## 5. Componentes y su acabado

| Componente | Acabado que lo hace premium |
|---|---|
| Barra de anuncio | 1 mensaje fuerte o 2-3 que rotan con fundido; nada de marquee chillón |
| Calificación | Estrellas + número real + conteo real, link a reseñas. Sin reseñas: no se muestra |
| Píldoras de beneficio | 3-4, check de color, ≤4 palabras, fondo tenue |
| Paquetes | Tarjetas-radio: miniatura del pack · nombre · precio por unidad · ahorro en $ · precio grande · tachado gris · etiqueta 11 px sobre el borde · seleccionada = borde de acción 2 px + halo 4 px |
| Regalos | Filas que se "encienden" en verde al desbloquear, con animación de escala 1→1.03 |
| Fecha de entrega | Píldora con punto verde que late + fecha calculada con `Intl.DateTimeFormat` |
| Botón principal | 56-58 px de alto, precio adentro, relieve (borde inferior 2 px más oscuro), hover −2 px, `:active` scale .98, estado "✓ Agregado" |
| Micro-garantías | Una línea bajo el botón con íconos lineales |
| Pagos | Íconos monocromos con borde tipo tarjeta; MSI calculado |
| Pestañas en compra | Reseñas / Comparación / Ficha, subrayado animado |
| Tabla comparativa | Columna propia con fondo translúcido de acción + borde + radio; ✓ verde / — gris |
| Carrusel UGC | 9:16, central ×1.1, laterales asomando, scroll-snap, subtítulos quemados |
| Reseñas | Histograma 5→1 clicable, fotos navegables, respuesta de la marca, "compra verificada" real |
| FAQ | `<details>` con "+" que gira 45°, altura animada con `interpolate-size` donde exista |
| Barra fija | Aparece al perder el botón principal, se oculta en el cierre y con el carrito abierto, blur de fondo |
| Carrito lateral | Barra de metas `<progress>`, ahorro en píldora, candado, garantía, pagos |

## 6. Movimiento (sobrio = caro)

- Reveal: opacity + translateY(28px) → 0, .9 s, `--ease`, **una sola vez**, nunca en el primer pantallazo.
- Micro: .2 s; UI (tarjetas, carrito): .35 s. Salida más rápida que entrada.
- Máximo **un** loop permanente por pantalla (el punto de entrega o el brillo del botón, no los dos juntos).
- Solo `transform` y `opacity`. Nunca animar `blur` ni `box-shadow`.
- `prefers-reduced-motion`: todo visible y quieto.

## 7. Ritmo de página

- Alternar fondos cada 1-2 pantallas (negro · papel · blanco · grafito).
- Padding de capítulo `clamp(88px, 13vh, 160px)`; dentro del bloque de compra, compacto (12-16 px entre piezas).
- Ancho de contenido 1120 px; textos 60-70 caracteres.
- Botón de compra visible (fijo o en flujo) en todo momento después del primer scroll.

## 8. Los 30 acabados (checklist)

1. Precio dentro del botón y actualizado al cambiar de paquete.
2. Precio por unidad + ahorro en $ en cada paquete.
3. Etiquetas con sistema único (11 px/800/mayúsculas/radio 4).
4. Fecha de entrega concreta con punto que late.
5. Foto 1 infografía; galería con proporción fija y contador "1/6".
6. Foto a escala y en uso presentes.
7. Sombra de contacto en productos recortados (nunca flotando sin sombra).
8. Títulos con segunda línea en otro tono (gris o degradado de marca).
9. Degradados de fondo casi imperceptibles en lugar de planos.
10. Grano 3-5% solo sobre degradados grandes (mata el banding).
11. Botón con relieve, hover −2 px, active .98, foco visible con doble anillo.
12. Tarjeta seleccionada con borde + halo, transición .2 s.
13. Regalos que se encienden con animación corta.
14. Íconos de un solo set, trazo 1,5-1,8 px, `currentColor`.
15. Pagos en íconos monocromos del mismo tamaño.
16. Tabla comparativa sin scroll horizontal en 375 px.
17. Números grandes con degradado de marca y `tabular-nums`.
18. Videos con poster, muted, playsinline, subtítulos quemados.
19. Reseñas con histograma y fotos, o bloque honesto de lanzamiento.
20. FAQ con respuestas que cierran en la garantía.
21. Barra fija con blur, se oculta en el cierre.
22. Carrito lateral con barra de metas y ahorro.
23. Toast/confirmación al agregar (sin redirigir).
24. Márgenes laterales ≥ 20 px; nada tocando bordes.
25. Contraste AA en todos los textos (gris sobre negro ≥ #A1A1A6).
26. Formato de moneda con `Intl.NumberFormat` del país.
27. Imagen LCP con `fetchpriority="high"`; el resto lazy con width/height.
28. Favicon, title y description propios.
29. Cero texto de plantilla ("Insert answer here", "Short benefit 1").
30. Consistencia: misma garantía, mismo precio y mismo envío en toda la página.
