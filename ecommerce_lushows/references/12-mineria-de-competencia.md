# 12 · Minería de competencia: páginas, reseñas y videos de quien ya vende lo mismo

> Vigencia: 17-sep-2026. Pedido de Luis: "buscar en la web páginas que vendan los mismos productos,
> sacar su contenido, las reseñas de clientes y los videos para analizarlos y usarlos".
> Scripts: `minar_competencia.py` → `analizar_resenas.py` → `analizar_video.py`.

## La línea que no se cruza (y por qué conviene)

| Se puede (investigación) | No se publica (riesgo real) |
|---|---|
| Leer y **analizar** todas sus reseñas: dolores, objeciones, frases, calificaciones | Poner sus reseñas en nuestra página como si fueran de nuestros clientes (PROFECO art. 32, SIC Ley 1480 art. 30; la FTC sancionó hasta generadores de reseñas) |
| Ver y **desarmar** sus videos: gancho, orden, duración, pruebas que muestran | Subir sus videos a nuestra página o anuncios (derechos de autor; reclamos que tumban la página o la cuenta de anuncios) |
| Estudiar su oferta, precio, paquetes, garantía, secciones | Copiar textos literales, fotos o su marca |
| Citar internamente frases de clientes para redactar | Inventar reseñas "inspiradas" en las de ellos |

**Modo prueba (para ver cómo se vería la página mientras llega lo propio):** el contenido de competencia
puede ponerse en una página de PRUEBA si va marcado:

```html
<figure data-origen="competencia" data-fuente="tienda-x.mx"> … </figure>
```

La plantilla le pone una franja roja "PRUEBA · contenido de tienda-x.mx · reemplazar antes de publicar"
y `revisar_pdp.py` marca ✗ (no se entrega) mientras exista un solo bloque así. Nunca se sube a producción.

## Flujo completo (≈30-60 min)

### 1. Encontrar competidores que venden LO MISMO
Buscar con WebSearch (no con Playwright en paralelo) por:
- Número de modelo exacto (`"M02S" gafas`, `"M02S" smart glasses`), nombre genérico en español e inglés.
- Nombre de la app compañera si la tiene (`HeyCyan glasses`).
- `site:myshopify.com` + palabras, y dominios de país (`.mx`, `.co`, `.cl`, `.es`).
- Biblioteca de anuncios de Meta (quién pauta el producto hoy) → sus tiendas.
- Mercado Libre, Amazon MX/US, AliExpress, TikTok Shop: aunque no se minen con el script, sus reseñas
  y preguntas son la mejor voz del cliente (copiar a un CSV `tienda,estrellas,titulo,texto`).

Criterio: 6-10 tiendas, priorizando las que **tienen reseñas y videos** y las de **tu país**.
Guardar en `competencia/urls.txt` (una por línea).

### 2. Minar
```bash
python ~/.claude/skills/ecommerce_lushows/scripts/minar_competencia.py competencia/urls.txt competencia --bajar-videos
```
Saca por tienda: producto, precio y tachado, tema y apps, oferta, **reseñas** (Loox, Judge.me, Yotpo,
Okendo, schema.org, o bloques del tema marcados "puede ser plantilla") y **videos** (mp4 alojados,
YouTube, Vimeo, TikTok). Genera `resumen.md` y `resenas_todas.csv`.

Cuidado con la calidad del dato:
- Reseñas "html-tema" suelen ser texto de plantilla → no cuentan como voz del cliente.
- Ratings escritos a mano sin widget (ver `01`) → descartar.
- Tiendas con productos del mismo modelo pero otra versión → anotar la diferencia.

### 3. Sumar la voz de marketplaces
Copiar al mismo CSV las reseñas de Amazon/Mercado Libre/AliExpress (texto y estrellas) y las
**preguntas** de Mercado Libre (con estrellas vacías). Son las objeciones antes de comprar.

### 4. Analizar reseñas
```bash
python ~/.claude/skills/ecommerce_lushows/scripts/analizar_resenas.py competencia/resenas_todas.csv competencia/voz_del_cliente.md
```
Temas por vertical: pasar `--temas temas.json` con las palabras del rubro (ej. proteína: `sabor, se disuelve, grumos, inflama, digestión`).

Leer `voz_del_cliente.md` y producir (en `expediente.md`):
| Salida | Cómo |
|---|---|
| 3 titulares | Frases candidatas "por fin / ya no / vale la pena", reescritas en español del país |
| 6 beneficios con prueba | Temas con más menciones en 4-5★ |
| 8 objeciones → FAQ | Temas con más menciones en 1-3★ + decepciones |
| ¿Es para ti? sí/no | Decepciones que nacen de expectativas equivocadas |
| Pestaña de limitación | El tema negativo #1 (ej. batería de video) dicho con número real |
| Qué medir en la muestra | Todo lo que los clientes contradicen del fabricante |

### 5. Analizar videos
```bash
python ~/.claude/skills/ecommerce_lushows/scripts/analizar_video.py competencia competencia/videos-analisis --transcribir
```
Leer cada `_hoja.jpg` con Read y anotar en una tabla:

| Video | Tipo (demo / POV / testimonio / unboxing / antes-después / giro de producto) | Gancho 0-2 s | Prueba que muestra | Texto en pantalla | Cierre | ¿Funciona? por qué |

Con eso se escriben **guiones propios** (formato de `20-29` sección 6) para grabar con la muestra:
mismo tipo de prueba, otro contenido.

### 6. Tabla de competidores (va al expediente)
| Tienda | Precio | Paquetes y regalos | Garantía | Reseñas reales (★) | Videos | Ángulo | Lo que hace mejor | Su grieta |

"Su grieta" es lo que nos hace ganar: reseñas falsas, garantía confusa, specs infladas, página lenta,
sin fecha de entrega, sin decir limitaciones.

### 7. Llevarlo a la página
- Estructura y secciones: las que 4 de 6 competidores tienen (estándar) + las raras de valor (`02`).
- Precio: dentro del rango de mercado y con margen (`dropshipping_lushows`).
- Copy: 100% propio desde la voz del cliente.
- Medios: propios; en PRUEBA, competencia marcada con `data-origen`.

## Trampas técnicas
- Loox trae el id de tienda con barras escapadas en el JS → el script ya lo maneja.
- Judge.me: el endpoint público `reviews_for_widget` puede cambiar; si falla, copiar a mano desde el
  navegador (Playwright `browser_evaluate` sobre `.jdgm-rev`).
- Videos de Shopify vienen en varias resoluciones: el script se queda con la más alta por id.
- Descargas pesadas en la PC de Luis (i7-960): usar `--max-mb` y no más de 12 videos por tienda.
