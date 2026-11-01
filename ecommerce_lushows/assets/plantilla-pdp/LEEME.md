# Plantilla PDP — cómo usarla para un producto nuevo

Probada el 16-sep-2026 con las gafas con cámara: 98/100 en `revisar_pdp.py`, revisada a 390 px y 1440 px,
paquetes, regalos, fecha de entrega, carrito y barra fija funcionando. Luis aprobó esta dirección
después de rechazar dos versiones "suaves".

## Arranque (5 minutos)

```bash
P="C:/Users/user/Desktop/dropshipping-productos/<producto>"
mkdir -p "$P/assets" "$P/img" "$P/video"
cp ~/.claude/skills/ecommerce_lushows/assets/plantilla-pdp/pdp.css ~/.claude/skills/ecommerce_lushows/assets/plantilla-pdp/pdp.js "$P/assets/"
cp ~/.claude/skills/ecommerce_lushows/assets/plantilla-pdp/ejemplo-gafas-camara.html "$P/landing.html"
```

Luego se **reescribe el contenido** de `landing.html` para el producto nuevo (el ejemplo es la guía de
estructura, no el texto). Las imágenes del ejemplo no se copian: son del proveedor de las gafas.

## Qué se cambia y qué no

| Capa | Dónde | ¿Cambia por producto? |
|---|---|---|
| Marca (color de acción, degradado) | `pdp.css` → `:root` bloque MARCA | Sí (o del manual de marca) |
| Moneda, país, WhatsApp, nombre | `<body data-moneda data-locale data-producto data-whatsapp>` | Sí |
| Paquetes | `<input name="paquete" data-nombre data-precio data-tachado data-unidades data-msi>` | Sí (precios de `dropshipping_lushows`) |
| Regalos | `[data-desbloquea="N"]` (unidades mínimas) | Sí |
| Entrega | `[data-entrega data-min data-max data-corte]` | Según paquetería |
| Reseñas | `window.RESENAS = [{estrellas, nombre, ciudad, fecha, texto, verificada}]` | Solo reales; vacío = bloque de lanzamiento |
| Comportamiento | `pdp.js` | No (salvo mejora general → actualizar también la plantilla) |

Textos que se actualizan solos al cambiar de paquete: `[data-vivo="precio|tachado|unidad|ahorro|msi|paquete|cta"]`
y en el carrito `[data-carrito="nombre|precio|tachado|ahorro|total|unidades"]`.

## Orden de secciones (ver `references/02-anatomia-pdp.md`)

anuncio rotativo → header con carrito → **COMPRA** (galería con infografía, etiqueta, título, subtítulo,
píldoras, precio, MSI, paquetes, regalos, fecha de entrega, botón con precio, micro-garantías, pagos,
WhatsApp, pestañas Ficha/Batería real/Envío) → franja de confianza → **problema** (PAS, oscuro) →
**cifras** → **¿es para ti? sí/no** → **cómo funciona 3 pasos** → **bento de beneficios** →
**demostración interactiva** (aquí: micas) → **costo-beneficio 3 columnas** → **videos POV** →
**qué incluye** → **reseñas** → **garantía con sello** → **FAQ con limitaciones reales** → **cierre** →
pie legal → barra fija → carrito lateral.

Cada sección es opcional según el producto, pero **compra arriba, reseñas honestas, FAQ con
limitaciones y garantía** no se quitan.

## Trampas ya resueltas en esta plantilla

- `[hidden]{display:none!important}`: sin esto, los estilos de `.regalo` o de las etiquetas le ganan a `hidden`.
- `img,video{height:auto}`: con `width`/`height` en el HTML (para evitar saltos de diseño) y ancho por CSS,
  sin esto las imágenes salen estiradas.
- Una imagen `position:absolute` con `left`/`right` **no** se estira: necesita `width` explícito.
- El carrito cerrado lleva `visibility:hidden`; si no, su sombra se asoma por el borde derecho y sus
  botones quedan en el orden del teclado.
- Micas o piezas claras sobre fondo oscuro: bajar opacidad y agregar un contorno de 1 px de luz, o se ven como bloques blancos.
