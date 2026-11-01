# 30 · Temas visuales por vertical: que cada producto se vea cinematográfico y vendible

> Vigencia: 17-sep-2026. Pedido de Luis: "si son proteínas, que se acomode una estructura de color e
> imagen según eso; si es producto de hogar igual; quiero que todo se vea cinematográfico y vendible".
> Implementado en `assets/plantilla-pdp/pdp.css`: `<body data-tema="...">` + clases `cine-*`.
> Si la marca tiene manual: el tema da la estructura y el manual reemplaza `--accion` y `--marca-*`.

## Cómo elegir y aplicar

1. Identifica el vertical (`20-29`). Si el producto mezcla (ej. masajeador deportivo), manda **quién
   compra y qué miedo tiene**, no la categoría del catálogo.
2. `<body data-tema="proteina">` y carga la fuente del tema en `<head>` (tabla abajo).
3. Aplica la **dirección de foto** del tema: es la mitad del resultado. Un tema con fotos de fábrica sobre blanco no se ve cinematográfico.
4. Coloca 4-6 efectos `cine-*` en momentos clave (no en todo).
5. Revisa contraste: el color de acción del tema debe leerse sobre su fondo (AA).

## Los 11 temas

| `data-tema` | Para | Paleta (acción · marca · capítulos) | Titulares (Google Fonts) | Forma |
|---|---|---|---|---|
| `tecnologia` | gadgets, audio, cámaras, wearables | azul eléctrico `#0A84FF` · sol `#FFB340→#FF4F6D` · negro puro | Geist 700 | radios 28 |
| `proteina` | proteína, pre-entreno, creatina, snacks deportivos | rojo sabor `#FF3B1F` · amarillo `#FFD400` · carbón `#0A0A0A` | **Anton** MAYÚSCULAS | radios 18, sólido |
| `salud` | masajeadores, sueño, postura, suplementos de bienestar | verde clínico `#1F7A6B` · aqua · pizarra `#0F1A1A` + hueso `#F3F1EC` | **Fraunces** 600 | suave |
| `belleza` | skincare, maquillaje, cabello, dispositivos de belleza | chocolate `#2B1B17` · nude `#E8B4A0→#B9826B` · cacao `#1E1512` + rosado `#F6EEE8` | **Fraunces** 500 | radios 32 |
| `hogar` | cocina, limpieza, organización, iluminación | terracota `#C2562F` · miel `#E9A15B` · nogal `#1B1612` + crema `#F1EBE1` | **Fraunces** 600 | cálido |
| `mascotas` | perros, gatos, accesorios, snacks | petróleo `#0F5C6E` · amarillo `#FFC845→#FF8A3D` · `#10222A` + `#FFF6E6` | **Bricolage Grotesque** 700 | radios 34 |
| `fitness` | bandas, accesorios, ropa deportiva, bici | volt `#C8F000` (texto negro) · aqua `#00E0B8` · negro `#050505` | **Barlow Condensed** 800 MAYÚSCULAS | radios 16 |
| `moda` | ropa, bolsos, joyería, lentes de sol, relojes | negro `#111` · latón `#B08D57` · `#0C0C0C` + `#EFEDE8` | **Playfair Display** 500 | radios 2-4, editorial |
| `bebes` | bebés, niños, juguetes educativos | azul confianza `#3E5BA9` · menta/lavanda · `#1B2238` + `#F4F1FA` | **Bricolage Grotesque** 700 | radios 36 |
| `auto` | auto, herramientas, linternas, camping | amarillo seguridad `#FFC400` (texto negro) · naranja · grafito `#0B0D0F` | **Barlow Condensed** 700 MAYÚSCULAS | radios 8-10 |
| `regalo` | temporada, novedad, personalizados | rojo `#B3122E` · dorado `#E9C46A` · `#12080A` + `#F7F0E6` | **Fraunces** 600 | cálido |

Enlaces de fuentes (agregar al `<link>` de Google Fonts junto a Geist):
- Anton: `family=Anton` · Fraunces: `family=Fraunces:opsz,wght@9..144,500;9..144,600` · Bricolage: `family=Bricolage+Grotesque:wght@600;700`
- Barlow Condensed: `family=Barlow+Condensed:wght@700;800` · Playfair Display: `family=Playfair+Display:wght@500;600`

## Dirección de foto y video por tema (lo que lo hace cinematográfico)

| Tema | Luz | Escenario / props | Movimiento de cámara | El plano héroe |
|---|---|---|---|---|
| tecnologia | Estudio oscuro, luz de borde fría + un acento cálido | Superficies negras mate, reflejo en el piso | Giro lento 360°, push-in al detalle | Producto flotando con reflejo |
| proteina | Dura y contrastada, luz lateral, humo o polvo en contraluz | Gym de concreto, shaker, polvo cayendo, gotas de sudor | Cámara lenta del polvo/splash, cortes rápidos al ritmo | Scoop cayendo en el shaker en slow-motion |
| salud | Suave de ventana, sombras largas cálidas | Sala o recámara con lino, plantas, madera clara | Lento, estable, respirado | Persona relajándose con el producto en uso |
| belleza | Difusa y cálida, piel con brillo real, macro | Mármol, lino, agua, flores secas | Macro de textura (crema, gota), gestos lentos | Textura del producto sobre piel |
| hogar | Luz de ventana de mañana (golden hour interior) | Cocina/sala real y ordenada, vapor, comida | Deslizamiento lateral, antes→después | El producto en la escena resolviendo algo (vapor, orden) |
| mascotas | Natural y alegre, exterior o sala luminosa | Mascota real, pasto, sofá | A la altura de la mascota, reacciones | Cara de la mascota usándolo |
| fitness | Contraluz dura, atardecer o gym oscuro con haces | Pista, gym, calle | Tracking siguiendo el movimiento, slow-motion | Momento de esfuerzo con el producto |
| moda | Editorial, sombra marcada o luz plana de estudio | Fondo liso color arena, arquitectura | Planos fijos, poses, detalle de textura | Look completo en modelo + detalle de material |
| bebes | Muy suave, cálida, sin sombras duras | Recámara pastel, madera, textiles | Estable, cercano, íntimo | Mamá/papá con el bebé y el producto |
| auto | Dura, industrial, lámpara de taller, noche con faros | Taller, cajuela, carretera, campamento | Push-in, primer plano de mecanismo | El producto funcionando en condición real (noche, lluvia) |
| regalo | Cálida festiva, bokeh de luces | Mesa de celebración, envoltura, papel kraft | Unboxing, reacción | La reacción al abrirlo |

Con fotos de fábrica sobre blanco (mientras llega lo propio): recortar el fondo (`preparar_medios.py recortar-fondo`)
y ponerlas sobre el fondo del capítulo con la luz `--luz-1/2` del tema + sombra de contacto. Eso ya lee "estudio".

## Efectos `cine-*` (en la plantilla, todos respetan movimiento reducido)

| Clase | Qué hace | Dónde ponerlo |
|---|---|---|
| `cine-escala` | El producto crece desde 80% al entrar (scroll nativo) | Producto héroe del capítulo "problema" |
| `cine-paralaje` | Sube y baja suavemente con el scroll | Producto del cierre, fotos grandes |
| `cine-zoom` | Foto entra con zoom lento 112%→100% | Celdas con foto, capítulos full-bleed |
| `cine-revela` | Se abre como telón (clip-path) | Demostraciones, fotos de uso |
| `cine-barrido` | Barrido de luz una vez | Garantía, sellos, tarjeta del paquete |
| `cine-titulo` | Las letras se juntan al entrar | 1-2 titulares gigantes por página |
| `cine-vineta` | Viñeta oscura en bordes | Fotos de ambiente |

Regla: **un momento de cine por capítulo**. Si todo se mueve, nada se ve caro. El bloque de compra no lleva efectos.

## Titulares cinematográficos por tema (estructura, no texto fijo)

- proteina: MAYÚSCULAS condensadas, 2-3 palabras por línea, verbo de acción ("RECUPERA MÁS. RINDE MÁS.").
- salud / hogar / belleza / regalo: serif con segunda línea en gris o en color de marca, frase completa y calmada.
- tecnologia: grotesca apretada, afirmación corta + remate en degradado.
- fitness / auto: condensadas, número grande + unidad ("1,050 LÚMENES MEDIDOS").
- moda: serif editorial, pocas palabras, mucho aire.

## Errores
- Tema "proteína" con fotos blancas de catálogo → se ve farmacia barata. La foto manda.
- Usar el color de acción para decorar → el ojo ya no sabe dónde comprar.
- Cargar 3 fuentes de temas distintos → peso y desorden. Una de titulares + Geist.
- Amarillo/volt con texto blanco → ilegible; esos temas ya fuerzan texto negro en botones.
