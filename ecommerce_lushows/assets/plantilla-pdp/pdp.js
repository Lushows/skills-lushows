/* =====================================================================
   pdp.js — comportamiento de la página de producto (ecommerce_lushows)
   Todo se configura desde el HTML con atributos data-*. Sin dependencias.
   Contrato:
     <body data-moneda="MXN" data-locale="es-MX" data-producto="Nombre" data-whatsapp="52155...">
     paquetes:  <input name="paquete" data-precio data-tachado data-unidades data-msi data-nombre>
     textos vivos: [data-vivo="precio|tachado|unidad|ahorro|msi|paquete|cta"]
     regalos:   [data-desbloquea="2"]
     entrega:   [data-entrega data-min="2" data-max="5" data-corte="14"]
     botones:   [data-agregar] (agrega y abre carrito) · [data-ir-compra] (sube a paquetes)
     reseñas:   window.RESENAS = [{estrellas, nombre, ciudad, fecha, texto, verificada}]
   ===================================================================== */
(() => {
  'use strict';
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const body = document.body;
  const locale = body.dataset.locale || 'es-MX';
  const dinero = new Intl.NumberFormat(locale, { style: 'currency', currency: body.dataset.moneda || 'MXN', minimumFractionDigits: 0, maximumFractionDigits: 2 });
  const fmt = n => dinero.format(Math.round(n * 100) / 100);
  const reducido = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- barra de anuncio rotativa ---------- */
  const anuncios = $$('.anuncio li');
  if (anuncios.length > 1 && !reducido) {
    let i = 0;
    setInterval(() => { anuncios[i].classList.remove('on'); i = (i + 1) % anuncios.length; anuncios[i].classList.add('on'); }, 4200);
  }

  /* ---------- galería con deslizamiento ---------- */
  const escena = $('.galeria__escena');
  if (escena) {
    const pista = $('.galeria__pista', escena);
    const slides = $$('.galeria__slide', pista);
    const minis = $$('.galeria__minis button');
    const contador = $('.galeria__contador', escena);
    let actual = 0;
    const ir = n => {
      actual = (n + slides.length) % slides.length;
      pista.style.transform = `translateX(${-actual * 100}%)`;
      minis.forEach((b, j) => b.setAttribute('aria-current', String(j === actual)));
      if (contador) contador.textContent = `${actual + 1}/${slides.length}`;
      slides.forEach((s, j) => s.setAttribute('aria-hidden', String(j !== actual)));
    };
    minis.forEach((b, j) => b.addEventListener('click', () => ir(j)));
    $('.galeria__flecha--izq', escena)?.addEventListener('click', () => ir(actual - 1));
    $('.galeria__flecha--der', escena)?.addEventListener('click', () => ir(actual + 1));
    let x0 = null, t0 = 0;
    escena.addEventListener('pointerdown', e => { x0 = e.clientX; t0 = performance.now(); });
    escena.addEventListener('pointerup', e => {
      if (x0 === null) return;
      const dx = e.clientX - x0, v = Math.abs(dx) / (performance.now() - t0);
      if (Math.abs(dx) > 40 || v > .5) ir(actual + (dx < 0 ? 1 : -1));
      x0 = null;
    });
    ir(0);
  }

  /* ---------- paquetes: todos los textos vivos salen de aquí ---------- */
  const radios = $$('input[name="paquete"]');
  const regalos = $$('[data-desbloquea]');
  const estado = () => {
    const r = radios.find(x => x.checked) || radios[0];
    const d = r.dataset, precio = +d.precio, tachado = +(d.tachado || 0), unidades = +(d.unidades || 1), msi = +(d.msi || 0);
    return { precio, tachado, unidades, msi, nombre: d.nombre || '', unidad: precio / unidades, ahorro: tachado ? tachado - precio : 0 };
  };
  const pintar = () => {
    if (!radios.length) return;
    const e = estado();
    const textos = {
      precio: fmt(e.precio), tachado: e.tachado ? fmt(e.tachado) : '', unidad: fmt(e.unidad),
      ahorro: e.ahorro > 0 ? `Ahorras ${fmt(e.ahorro)}` : '', paquete: e.nombre,
      msi: e.msi ? `${e.msi} meses sin intereses de ${fmt(e.precio / e.msi)}` : '',
      cta: `Agregar al carrito · ${fmt(e.precio)}`
    };
    $$('[data-vivo]').forEach(el => { const v = textos[el.dataset.vivo]; if (v !== undefined) el.textContent = v; });
    regalos.forEach(g => {
      const on = e.unidades >= +g.dataset.desbloquea;
      if (on && !g.classList.contains('on')) { g.classList.add('salta'); setTimeout(() => g.classList.remove('salta'), 520); }
      g.classList.toggle('on', on);
      const em = $('em', g); if (em) em.textContent = on ? 'Gratis' : `Con ${g.dataset.desbloquea} pares`;
    });
    const wa = $('[data-whatsapp-link]');
    if (wa && body.dataset.whatsapp) {
      const msg = `Hola, tengo una duda sobre ${body.dataset.producto || 'el producto'} (${e.nombre}, ${fmt(e.precio)}).`;
      wa.href = `https://wa.me/${body.dataset.whatsapp}?text=${encodeURIComponent(msg)}`;
    }
    pintarCarrito();
  };
  radios.forEach(r => r.addEventListener('change', pintar));

  /* ---------- fecha de entrega (días hábiles, sin domingos, con hora de corte) ---------- */
  $$('[data-entrega]').forEach(el => {
    const min = +(el.dataset.min || 2), max = +(el.dataset.max || 5), corte = +(el.dataset.corte || 14);
    const sumar = (desde, dias) => { const f = new Date(desde); let n = 0; while (n < dias) { f.setDate(f.getDate() + 1); if (f.getDay() !== 0) n++; } return f; };
    const hoy = new Date(); const base = hoy.getHours() >= corte ? sumar(hoy, 1) : hoy;
    const f = new Intl.DateTimeFormat(locale, { weekday: 'short', day: 'numeric', month: 'short' });
    const salida = $('[data-entrega-texto]', el) || el;
    salida.textContent = `${f.format(sumar(base, min))} y el ${f.format(sumar(base, max))}`.replace(/\./g, '');
  });

  /* ---------- pestañas ---------- */
  $$('[role="tablist"]').forEach(lista => {
    const tabs = $$('[role="tab"]', lista);
    tabs.forEach(t => t.addEventListener('click', () => {
      tabs.forEach(o => { const on = o === t; o.setAttribute('aria-selected', String(on)); $('#' + o.getAttribute('aria-controls')).hidden = !on; });
    }));
  });

  /* ---------- carrito lateral ---------- */
  const carrito = $('.carrito'), velo = $('.velo'), fija = $('.fija');
  const burbuja = $('.cab__carrito b');
  let enCarrito = false;
  function pintarCarrito() {
    if (!carrito || !radios.length) return;
    const e = estado();
    $$('[data-carrito]', carrito).forEach(el => {
      const k = el.dataset.carrito;
      el.textContent = { nombre: e.nombre, precio: fmt(e.precio), tachado: e.tachado ? fmt(e.tachado) : '', ahorro: e.ahorro > 0 ? `Ahorras ${fmt(e.ahorro)}` : '', total: fmt(e.precio), unidades: String(e.unidades) }[k] ?? el.textContent;
    });
    const meta = $('progress', carrito), metaTxt = $('[data-meta-texto]', carrito);
    if (meta) {
      const objetivo = +(meta.dataset.objetivo || 2);
      meta.max = objetivo; meta.value = Math.min(e.unidades, objetivo);
      if (metaTxt) metaTxt.textContent = e.unidades >= objetivo ? 'Ya desbloqueaste la funda de regalo y el envío gratis.' : `Te falta ${objetivo - e.unidades} par para la funda de regalo.`;
    }
    const ah = $('[data-carrito="ahorro"]', carrito); if (ah) ah.hidden = !(e.ahorro > 0);
    $$('[data-carrito-regalo]', carrito).forEach(g => g.hidden = e.unidades < +g.dataset.carritoRegalo);
  }
  const abrir = () => { carrito?.classList.add('on'); velo?.classList.add('on'); carrito?.setAttribute('aria-hidden', 'false'); fija?.classList.remove('on'); document.documentElement.style.overflow = 'hidden'; setTimeout(() => $('.carrito__cerrar')?.focus(), 350); };
  const cerrar = () => { carrito?.classList.remove('on'); velo?.classList.remove('on'); carrito?.setAttribute('aria-hidden', 'true'); document.documentElement.style.overflow = ''; revisarFija(); };
  $$('[data-agregar]').forEach(b => b.addEventListener('click', () => {
    enCarrito = true;
    if (burbuja) { burbuja.textContent = String(estado().unidades); burbuja.classList.add('on'); }
    const txt = $('[data-vivo="cta"]', b);
    b.classList.add('is-ok'); if (txt) txt.textContent = '✓ Agregado';
    if (navigator.vibrate) navigator.vibrate(10);
    setTimeout(() => { b.classList.remove('is-ok'); pintar(); }, 1200);
    pintarCarrito(); setTimeout(abrir, 250);
  }));
  $('.cab__carrito')?.addEventListener('click', () => { pintarCarrito(); abrir(); });
  $('.carrito__cerrar')?.addEventListener('click', cerrar);
  velo?.addEventListener('click', cerrar);
  document.addEventListener('keydown', e => { if (e.key === 'Escape' && carrito?.classList.contains('on')) cerrar(); });
  $$('[data-ir-compra]').forEach(b => b.addEventListener('click', ev => { ev.preventDefault(); $('#paquetes')?.scrollIntoView({ behavior: reducido ? 'auto' : 'smooth', block: 'center' }); }));

  /* ---------- pago (pendiente de conectar) ---------- */
  const aviso = $('.aviso');
  $$('[data-pagar]').forEach(b => b.addEventListener('click', () => {
    const e = estado();
    window.dispatchEvent(new CustomEvent('checkout', { detail: { paquete: e.nombre, unidades: e.unidades, precio: e.precio, moneda: body.dataset.moneda } }));
    if (aviso) { aviso.textContent = 'El pago se conecta en el siguiente paso. Tu carrito queda guardado.'; aviso.classList.add('on'); clearTimeout(aviso._t); aviso._t = setTimeout(() => aviso.classList.remove('on'), 2800); }
  }));

  /* ---------- barra fija: aparece al perder el botón principal, se oculta en el cierre y con carrito ---------- */
  const principal = $('[data-cta-principal]');
  let pasado = false, enCierre = false;
  function revisarFija() {
    if (!fija) return;
    const on = pasado && !enCierre && !carrito?.classList.contains('on');
    fija.classList.toggle('on', on);
    fija.setAttribute('aria-hidden', String(!on));
    $$('button,a', fija).forEach(x => x.tabIndex = on ? 0 : -1);
  }
  if (principal) new IntersectionObserver(([e]) => { pasado = !e.isIntersecting && e.boundingClientRect.bottom < 0; revisarFija(); }).observe(principal);
  const cierreSec = $('.cierre');
  if (cierreSec) new IntersectionObserver(([e]) => { enCierre = e.isIntersecting; revisarFija(); }).observe(cierreSec);

  /* ---------- fotocromáticas ---------- */
  $$('[data-sol]').forEach(zona => {
    const rango = $('input[type="range"]', zona), escenaSol = $('.sol', zona), est = $('.sol__estado', zona);
    const set = () => {
      const v = rango.value / 100;
      escenaSol.style.setProperty('--s', v); escenaSol.style.setProperty('--p', Math.round(v * 70) + '%');
      if (est) est.textContent = v < .34 ? 'Bajo techo' : v < .7 ? 'Nublado' : 'Pleno sol';
    };
    rango.addEventListener('input', set); set();
  });

  /* ---------- línea de pasos que se llena con el scroll ---------- */
  const pasos = $('.pasos');
  if (pasos && !reducido) {
    const barra = $('.pasos__linea i', pasos); let pedido = false;
    const act = () => { pedido = false; const r = pasos.getBoundingClientRect(); const p = (innerHeight * .6 - r.top) / r.height; barra.style.setProperty('--prog', Math.max(0, Math.min(1, p)).toFixed(3)); };
    addEventListener('scroll', () => { if (!pedido) { pedido = true; requestAnimationFrame(act); } }, { passive: true }); act();
  } else if (pasos) { $('.pasos__linea i', pasos)?.style.setProperty('--prog', 1); }

  /* ---------- carrusel de videos: tarjeta central destacada ---------- */
  const carrusel = $('.carrusel');
  if (carrusel) {
    const io = new IntersectionObserver(es => es.forEach(e => {
      e.target.classList.toggle('centro', e.intersectionRatio > .6);
      const v = $('video', e.target); if (v) e.intersectionRatio > .6 ? v.play().catch(() => {}) : v.pause();
    }), { root: carrusel, threshold: [0, .6, 1] });
    $$('.video', carrusel).forEach(v => io.observe(v));
  }

  /* ---------- reseñas: histograma real o bloque de lanzamiento ---------- */
  const zonaRes = $('[data-resenas]');
  if (zonaRes) {
    const lista = Array.isArray(window.RESENAS) ? window.RESENAS : [];
    const lanz = $('.lanzamiento', zonaRes), histo = $('.histo', zonaRes);
    if (!lista.length) { if (histo) histo.hidden = true; if (lanz) lanz.hidden = false; }
    else {
      if (lanz) lanz.hidden = true; if (histo) histo.hidden = false;
      const prom = lista.reduce((a, r) => a + r.estrellas, 0) / lista.length;
      $('[data-res-prom]', zonaRes).textContent = prom.toLocaleString(locale, { maximumFractionDigits: 1 });
      $('[data-res-total]', zonaRes).textContent = `${lista.length} ${lista.length === 1 ? 'reseña' : 'reseñas'}`;
      $$('[data-barra]', zonaRes).forEach(b => {
        const n = lista.filter(r => r.estrellas === +b.dataset.barra).length;
        $('i', b).style.setProperty('--w', (n / lista.length * 100) + '%'); $('[data-cuenta]', b).textContent = n;
      });
    }
  }

  /* ---------- aparición al scroll (una vez) ---------- */
  const rv = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); rv.unobserve(e.target); } }), { rootMargin: '0px 0px -10% 0px' });
  $$('.rv,.cine-zoom,.cine-revela,.cine-barrido,.cine-titulo').forEach(el => rv.observe(el));

  pintar();
})();
