# 11 · QA antes de entregar

> Vigencia: 16-sep-2026. Una página no se entrega hasta pasar las tres capas. Luis no debería
> encontrar un solo detalle que nosotros no vimos.

## Capa 1 — Automática (1 minuto)

```bash
python ~/.claude/skills/ecommerce_lushows/scripts/revisar_pdp.py landing.html
```

- **✗ = no se entrega.** Escasez o contadores inventados, calificación escrita a mano, LCP sin
  `fetchpriority` o con lazy, video autoplay sin `muted playsinline`, `innerHTML`, sin viewport.
- **⚠ = arreglar o justificar** en el resumen (ej. "histograma pendiente: aún no hay reseñas").
- Referencia de puntaje: la v2 de las gafas sacó 89/100 · 0 ✗; baho.mx sacó 80/100 · 5 ✗.

## Capa 2 — Visual en móvil real (390×844) y desktop (1440×900)

1. Servir: `python -m http.server 8765` en la carpeta del producto (en segundo plano).
2. Playwright: `browser_resize` → `browser_navigate` → `browser_evaluate`:
   ```js
   async () => {
     for (let y = 0; y < document.body.scrollHeight; y += 400) { scrollTo(0, y); await new Promise(r => setTimeout(r, 120)); }
     document.querySelectorAll('.rv').forEach(e => e.classList.add('in'));
     const s = document.createElement('style'); s.textContent = '*,*::before,*::after{animation:none!important;transition:none!important}'; document.head.appendChild(s);
     document.querySelectorAll('img').forEach(i => i.loading = 'eager');
     await new Promise(r => setTimeout(r, 1500));
     const desborde = [...document.querySelectorAll('body *')].filter(e => e.getBoundingClientRect().right > innerWidth + 1 && !e.closest('[data-scroll-x]')).map(e => e.tagName + '.' + e.className).slice(0, 10);
     const rotas = [...document.querySelectorAll('img')].filter(i => !i.naturalWidth).map(i => i.src);
     return JSON.stringify({ ancho: document.documentElement.scrollWidth, vista: innerWidth, desborde, rotas });
   }
   ```
3. Captura de página completa → recortar en 5 tramos con PIL → **mirar cada tramo**.
4. Una llamada de Playwright a la vez.

### Qué mirar en cada tramo
- [ ] Primer pantallazo: promesa + precio + botón visibles sin bajar.
- [ ] Nada cortado ni desbordado; textos no chocan con bordes (mín. 20 px de margen).
- [ ] Todas las imágenes cargan; ninguna foto con texto en otro idioma.
- [ ] Precio idéntico en hero, bloque de compra, botón, barra fija y cierre.
- [ ] Al cambiar de paquete cambian: precio, MSI, precio por unidad, regalos, barra fija.
- [ ] La barra fija aparece al pasar el botón y **se oculta** al llegar al cierre.
- [ ] Contraste legible en cada capítulo (texto gris sobre negro ≥ #A1A1A6).
- [ ] Ritmo: ningún tramo de más de 2 pantallas con el mismo fondo.
- [ ] Tarjetas sin espacio vacío muerto en móvil.
- [ ] Tablas legibles en 375 px sin scroll horizontal oculto.

## Capa 3 — Honestidad y negocio

- [ ] Cada spec de la página está en `expediente.md` con su prueba.
- [ ] Reseñas: reales o bloque honesto de lanzamiento. Nada importado sin etiquetar.
- [ ] Medios: origen y permiso anotados.
- [ ] Precio y paquete coinciden con el modelo de `dropshipping_lushows`.
- [ ] Comparativas y costo-beneficio con precios reales verificados.
- [ ] Garantía y política de devolución que Luis de verdad puede cumplir.

## El resumen de entrega (formato)

```
**Qué recibes:** [landing.html](ruta) — revisada a 390 px y 1440 px, puntaje N/100 · 0 ✗.
**Veredicto de negocio:** ...
**Oferta:** precio, paquete preseleccionado, regalo, MSI.
**Lo que falta para publicar:** muestra física · videos a grabar · reseñas · nombre · pago.
```
