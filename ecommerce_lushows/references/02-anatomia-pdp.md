# 02 · Anatomía de la página de producto (orden, propósito y receta de cada sección)

> Vigencia: 16-sep-2026. Síntesis de Elixir (`05`), 20 plantillas de GemPages, Baymard (`03`),
> Apple / Ray-Ban Meta (`04`) y la prueba real con las gafas (plantilla `assets/plantilla-pdp/`).

## Lo estándar vs lo que diferencia

**Estándar (aparece en 7-8 de 8 plantillas top — si falta, se pierde por omisión):** galería con
sellos · estrellas/prueba arriba del título · beneficios con íconos · reseñas · paquetes 2-3 niveles con
"más elegido" · FAQ acordeón · franja envío/garantía/soporte · botón repetido.

**Raras y de mucho valor (lo que nos pone arriba):** "¿es para ti? sí / no" (autocalificación) ·
paquetes **por caso de uso** ("para ti / para regalar"; "una habitación / casa entera") · regalos con
tarjeta propia · **fecha de entrega** junto al botón · etiquetas sobre la foto señalando componentes ·
**limitaciones dichas en el FAQ** · rutina por fases (consumibles) · letra pequeña legal de la promoción.

## El orden (móvil primero)

| # | Sección | Trabajo | Receta |
|---|---|---|---|
| 0 | Anuncio | Quitar la duda #1 antes de empezar | 2-3 mensajes que rotan con fundido cada ~4 s (envío, garantía, MSI) |
| 1 | Header | Orientar + carrito | Logo, links en desktop, bolsa con burbuja de unidades |
| 2 | **Galería** | Mostrar | Foto 1 = infografía (producto + 4 datos con íconos); luego en uso, a escala, detalle, caja. Deslizable, contador 1/N, miniaturas |
| 3 | **Panel de compra** | Vender | Etiqueta (Lanzamiento / Más vendido real) · H1 nombre + caso de uso · subtítulo con resultado · 3-4 píldoras · precio con "IVA incluido · envío" · MSI calculado |
| 4 | **Paquetes** | Subir ticket | Tarjetas-radio por caso de uso, precio por unidad, ahorro en $, tachado solo si es la suma real, preselección del que más conviene al negocio |
| 5 | Regalos | Recompensar el paquete grande | Filas que se encienden en verde al desbloquear |
| 6 | **Entrega** | Quitar ansiedad | "Pide hoy y recíbelas entre el sáb 19 y el mié 23" (JS, días hábiles, hora de corte) |
| 7 | **Botón** | Cerrar | Precio adentro, 60 px, relieve; debajo micro-garantías, pagos, WhatsApp |
| 8 | Pestañas | Resolver sin salir | Ficha · limitación principal (ej. "Batería real") · Envío y devolución |
| 9 | Franja de confianza | Reforzar | 4 íconos: envío, garantía, pago seguro, atención humana |
| 10 | **Problema (PAS)** | Emocionar | Oscuro, tipografía gigante: dolor (literal del cliente) → consecuencia → mecanismo; producto con luz y reflejo |
| 11 | Cifras | Recordar | 4 números con degradado de marca + nota honesta de la limitación |
| 12 | **¿Es para ti?** | Autocalificar | Tarjeta "sí, si…" (4) + tarjeta "no, si…" (3) — baja devoluciones y sube confianza |
| 13 | Cómo funciona | Quitar miedo a lo técnico | 3 pasos con línea que se llena al hacer scroll; el paso 3 incluye el consejo que evita la queja #1 |
| 14 | Beneficios (bento) | Profundizar | 1 celda con foto en uso grande + celdas con números y una oscura |
| 15 | **Demostración interactiva** | Probar | Slider/antes-después del beneficio visible (micas, limpieza, tamaño) |
| 16 | **Costo-beneficio** | Justificar el precio | 3 columnas: alternativa cara · nosotros (resaltada) · no comprar; con lo que se conserva y lo que no; precio de referencia con fecha |
| 17 | Videos | Prueba real | Carrusel 9:16, central destacada; solo grabados con el producto o licenciados |
| 18 | Qué incluye | Tangibilizar | Foto + lista numerada; regalo marcado |
| 19 | **Reseñas** | Confianza | Histograma 5→1 + reseñas verificadas con foto; si no hay: bloque honesto de lanzamiento |
| 20 | Garantía | Revertir riesgo | Sello SVG con días + 3 pasos para devolver |
| 21 | **FAQ** | Matar objeciones | Orden: limitación principal, uso, compatibilidad, legal/seguridad, clima, pago y entrega, devolución; cierra con WhatsApp |
| 22 | Cierre | Recordar la oferta | Oscuro, titular, píldora con paquete y precio vivos + Comprar (sube a paquetes) |
| 23 | Pie legal | Cumplir | Razón social, contacto, políticas, derechos del consumidor, marcas de terceros |
| — | Barra fija | Tener el botón siempre | Aparece al perder el botón principal; se oculta en el cierre y con carrito abierto |
| — | Carrito lateral | No perder la venta | Meta con `<progress>`, línea con ahorro, regalos, total con IVA, "Pagar seguro", garantía, pagos |

## Reglas de composición

- **Compra antes del primer scroll y medio.** Los capítulos convencen a quien sigue bajando; nunca
  empujan el botón fuera de alcance.
- **Botón intermedio = ir a paquetes**, no agregar directo (el cliente elige paquete primero).
- **Ritmo**: alternar fondo cada 1-2 pantallas (blanco → negro → grafito → papel → negro → blanco…).
- **Congruencia**: mismo precio, misma garantía, mismo envío en toda la página (Elixir falló aquí).
- Sección que no tenga contenido real (videos, reseñas, prensa) → hueco honesto o se quita. Nunca relleno.

## Variantes por tipo de producto

| Tipo | Ajuste |
|---|---|
| Gadget / electrónica | Infografía con specs, "batería real", compatibilidad, FAQ técnico, video demo/POV |
| Belleza / cuidado | Antes/después real, ingredientes (INCI), tipo de piel "¿es para ti?", rutina de uso |
| Salud / suplemento | Sin claims de enfermedad (COFEPRIS/INVIMA), rutina por fases, transparencia de fabricación |
| Hogar / cocina | Costo-beneficio por reemplazo, medidas y foto a escala, "qué incluye" con piezas |
| Regalo / temporada | Paquete "para regalar", fecha límite de entrega real para la fecha especial |
