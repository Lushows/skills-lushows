# 01 · Radiografía de una tienda de referencia

> Vigencia: 16-sep-2026. Cuando Luis manda un link, esto se hace en silencio y en minutos.
> Se estudia la **estructura y la mecánica**; el contenido ajeno (textos, fotos, videos, reseñas) no se toca.

## Paso 1 — Sin navegador (30 segundos)

```bash
python ~/.claude/skills/ecommerce_lushows/scripts/espiar_tienda.py "<url del producto>" <carpeta>
```

Devuelve `radiografia.json`: producto (`<url>.json` en Shopify), variantes, precio y tachado, fechas
(creado/publicado → ¿test de ayer o ganador?), tema, apps de conversión, config de **Kaching** (niveles,
descuentos, preselección, regalos), **conteo real de Loox** contra el rating escrito, videos y colores.

Alertas automáticas:
- **Rating escrito sin reseñas reales** → no copiar el rating ni los testimonios.
- **Escasez escrita a mano** ("solo quedan 13") → no copiar.

Probado con baho.mx (16-sep): producto creado el día anterior, Loox con **0** reseñas y "4.8/5 +2.500
clientes" escrito en el tema.

## Paso 2 — Con navegador, en móvil (390×844)

Playwright MCP (`browser_resize` 390×844 → `browser_navigate`). Luego `browser_evaluate`:

```js
async () => {
  for (let y = 0; y < document.body.scrollHeight; y += 600) { scrollTo(0, y); await new Promise(r => setTimeout(r, 300)); }
  const txt = el => (el?.innerText || '').replace(/\n{2,}/g, '\n').trim();
  const secciones = [...document.querySelectorAll('.shopify-section, main > section')]
    .map(s => ({ id: s.id, alto: Math.round(s.getBoundingClientRect().height), texto: txt(s).slice(0, 600) }))
    .filter(s => s.alto > 20);
  const keyframes = []; for (const ss of document.styleSheets) { try { for (const r of ss.cssRules) if (r.type === 7) keyframes.push(r.name); } catch (e) {} }
  const fijos = [...document.querySelectorAll('*')].filter(e => ['sticky','fixed'].includes(getComputedStyle(e).position)).map(e => e.tagName + '.' + String(e.className).slice(0, 40));
  const fuentes = [...new Set([...document.querySelectorAll('h1,h2,h3,p,button')].map(e => getComputedStyle(e).fontFamily))];
  const videos = [...document.querySelectorAll('video')].map(v => ({ autoplay: v.autoplay, loop: v.loop, seccion: v.closest('section,.shopify-section')?.id }));
  return JSON.stringify({ secciones, keyframes, fijos, fuentes, videos });
}
```

Guardar con `filename` dentro del proyecto (Playwright no escribe fuera de sus raíces permitidas).

## Paso 3 — Capturas

- Página completa: si se cuelga (animaciones infinitas, `backdrop-filter`), inyectar antes
  `*{animation:none!important;transition:none!important}` y marcar reveals como visibles.
- Recortar en tramos con PIL para poder mirarlas.
- **No** hacer varias llamadas de Playwright en paralelo: el navegador se bloquea ("Browser is already in use").

## Paso 4 — Lo que hay que mirar y anotar

| Qué | Pregunta |
|---|---|
| Primer pantallazo móvil | ¿Se ven título, precio y botón sin bajar? |
| Galería | ¿Cuántas fotos? ¿A escala? ¿En uso? ¿Video? |
| Bloque de compra | Niveles de paquete, cuál preseleccionado, precio por unidad, regalos |
| Confianza junto al botón | Envío, fecha, garantía, pagos |
| Secciones y orden | Mapear con la plantilla de `02-anatomia-pdp.md` |
| Efectos | Marquee, tarjetas apiladas, sticky, reveals, videos en loop |
| Carrito | ¿Lateral? ¿Barra de envío gratis? ¿Upsell? (agregar al carrito sin pagar) |
| Honestidad | Reseñas reales, escasez real, specs infladas |

## Paso 5 — Contexto de mercado (siempre)

- **Precio local:** Mercado Libre del país con Playwright (`.poly-card` → precio + título).
- **Costo real:** FOB en made-in-china / Global Sources / Alibaba por número de modelo.
- **Números:** `dropshipping_lushows` (modelo financiero `228`, precio mínimo para 20% neto).
  Si el precio de la referencia pierde plata, se dice **antes** de construir.
