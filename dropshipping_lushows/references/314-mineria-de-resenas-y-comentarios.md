# Minería de reseñas y comentarios

> Vigencia: 15-sep-2026. Esto es un **método**, no leer un rato por curiosidad.

## La diferencia entre leer y minar

| Leer reseñas | Minar reseñas |
|---|---|
| Abres, lees 20, te sientes informado | Defines fuente, muestra, cuota y plantilla antes de abrir nada |
| Te quedas con lo que confirma tu idea | Registras lo que contradice tu idea |
| Resultado: una sensación | Resultado: una tabla con frases literales y conteos |
| Tiempo: indefinido | Tiempo: 90 minutos por producto, cronómetro |

La minería sirve **antes** de tener clientes propios (es tu única voz del cliente en la validación) y
**después** (para vigilar objeciones nuevas). En el arranque de este proyecto es la fuente número uno
del bloque, porque todavía no hay pedidos que encuestar.

## Las fuentes, ordenadas por señal

| Fuente | Qué te da mejor que nadie | Trampa |
|---|---|---|
| **Reseñas de 3 estrellas** (Amazon MX, Mercado Libre, Shein, farmacias online) | Objeciones reales y expectativas rotas | Escasean; hay que buscarlas con filtro |
| **Comentarios de anuncios** de competencia | Vocabulario del cliente y dudas previas a la compra | Comentarios borrados por el anunciante (`95`) |
| **Preguntas de marketplace** | Lo que no queda claro en la ficha = tu FAQ | Sesgadas a logística |
| **Reseñas de 1 estrella** | Fallas de producto y de servicio | Mucho ruido de paquetería |
| **Reseñas de 5 estrellas** | Lenguaje de beneficio y testimonios | Reseñas compradas |
| **Grupos de Facebook / hilos de Reddit / TikTok comentarios** | Contexto cultural, cómo lo nombran entre ellos | No es tu comprador necesariamente |
| **Reseñas del competidor caro y del barato** | El eje de precio real del nicho | — |

Para Mercado Libre específicamente (preguntas, reseñas, dinámica interna): rutear a
`mercadolibre_lushows`. Aquí se cubre el método general.

## Por qué las de 3 estrellas son el oro

| Estrellas | Estado mental de quien escribe | Utilidad |
|---|---|---|
| 5 | Enamorado. Escribe emociones, poco detalle | Testimonios (`185`) |
| 4 | Contento con un "pero" | Mejoras de oferta |
| **3** | **Compró, lo usó, y le faltó algo. Escribe la verdad matizada** | **Objeciones + expectativa rota + uso inesperado** |
| 2 | Molesto. Detalle útil mezclado con enojo | Fallas reales |
| 1 | Furioso o es logística | Poca señal, mucho ruido |

La de 3 estrellas contiene la frase más valiosa que existe en marketing: **"esperaba X y resultó
Y"**. X es la promesa que el mercado ya compró. Y es el hueco que tú puedes llenar.

## El método (90 minutos, cronómetro)

### Paso 1 — Definir el corpus (10 min)

| Decisión | Regla |
|---|---|
| Productos | 3 competidores: el líder, el barato, el caro |
| Volumen objetivo | 100–150 reseñas leídas en total, de las cuales al menos 40 de 2–3 estrellas |
| Idioma / país | Solo México si vendes en México. Una reseña de España no te da el modismo correcto |
| Recencia | Últimos 12 meses. Las de 2023 hablan de otro producto |

### Paso 2 — Extraer (40 min)

Copia y pega a una hoja. **No resumas mientras copias**; separar la extracción del análisis es lo que
evita que solo veas lo que ya creías.

Plantilla (una fila por reseña útil, no por reseña leída):

| # | Fuente | Estrellas | Frase LITERAL | Categoría | Palabra clave del cliente |
|---|---|---|---|---|---|

### Paso 3 — Categorizar (20 min)

Seis categorías, ni una más. Si una frase no cae en ninguna, se descarta.

| Código | Categoría | Qué es | A dónde va |
|---|---|---|---|
| **D** | Dolor | Nombra el problema que lo llevó a comprar | Ángulo (`250`), mapa de dolores (`213`) |
| **O** | Objeción | Lo que casi lo detiene o lo que le falló | Landing, FAQ, guion (`98`) |
| **E** | Expectativa rota | "Esperaba X, resultó Y" | Tu promesa diferenciada |
| **U** | Uso inesperado | Lo usa para algo que no era el plan | Ángulo nuevo |
| **V** | Vocabulario | La palabra exacta con que lo nombra | Hook y copy (`315`) |
| **P** | Prueba social | Frase de beneficio bien dicha | Testimonios (`185`, `284`) |

### Paso 4 — Contar y cortar (20 min)

| Regla | Umbral |
|---|---|
| Un hallazgo es **patrón** | ≥ 5 menciones independientes, de distintas personas |
| Un hallazgo es **anécdota** | 1–4 menciones. Se guarda, no se actúa |
| Una objeción es **crítica** | Aparece en ≥ 20% de las reseñas de 2–3 estrellas |
| Vocabulario válido | La misma palabra o giro usada por ≥ 3 personas distintas |

Entrega del paso 4: una lista corta. Tres dolores, tres objeciones, tres palabras. Nada más. Si tu
salida tiene 20 puntos, no cortaste.

## Comentarios de anuncios: el complemento

`95` cubre cómo leerlos. Lo que agrega este módulo es **qué cuota pedirle a esa fuente** dentro de la
minería:

| Sub-fuente | Cuota | Qué buscas específicamente |
|---|---|---|
| Comentarios de anuncios con 60+ días activos | 3 anuncios, 50 comentarios cada uno | Objeciones repetidas y burlas (las burlas son hooks invertidos) |
| Respuestas del anunciante | Todas | Qué objeción le duele tanto que la contesta siempre |
| Comentarios con más likes | Los 10 primeros | El consenso del público |
| Comentarios de TikTok orgánico del nicho | 2 videos virales | Modismo actual |

## Trampas del método

| Trampa | Cómo se ve | Arreglo |
|---|---|---|
| Sesgo de confirmación | Solo copiaste frases que apoyan tu ángulo favorito | Cuota obligatoria de 40 reseñas de 2–3 estrellas |
| Reseñas compradas | Redacción impecable, todas la misma semana, mismo formato | Ignóralas. Cuenta solo las que tienen faltas de ortografía y detalle específico |
| Confundir logística con producto | "Llegó tarde" no es una objeción de producto | Categoría aparte, fuera de las seis |
| Traducir del inglés | Reseñas de Amazon US traducidas no te dan el modismo mexicano | Solo fuentes en español de México |
| Resumir en vez de copiar | Perdiste el vocabulario, que era el punto | Copiar literal, siempre |
| Minar una vez y nunca más | Las objeciones cambian cuando cambia la competencia | Repetir cada 6–8 semanas |

## Aplicado al proyecto (suplementos y belleza, México)

| Fuente concreta | Qué buscar |
|---|---|
| Reseñas de kits capilares y gomitas en Amazon MX y Mercado Libre | Expectativa rota ("esperaba ver algo en 2 semanas") → define tu promesa de **tiempo** honesta |
| Preguntas en fichas de marketplace | "¿Tiene azúcar?", "¿es vegano?", "¿de dónde lo mandan?" → tu FAQ y tu ventaja de **stock local en México** |
| Comentarios de anuncios de marcas con ~552 días activos | El vocabulario legal que ya pasó el filtro: "complementa tu dieta", "boost", "actitud" |
| Grupos de Facebook de cuidado capilar en México | Cómo nombran el problema entre ellas, sin marca de por medio |

Filtro obligatorio antes de usar cualquier frase minada: **si afirma o insinúa que cura, previene o
trata una condición, no se usa en copy**, aunque lo haya dicho un cliente real. Va al archivo interno
y se traduce a lenguaje de hábito e identidad (`07`, `315`).

## Salida del módulo

Un solo documento por producto candidato, con esta forma exacta:

```
PRODUCTO: [kit capilar anticaída]
CORPUS: 132 reseñas (48 de 2-3 estrellas), 3 anuncios, 2 grupos. Fecha: [__]

DOLORES (patrón, ≥5 menciones)
1. "[frase literal]" — 11 menciones
2. ...

OBJECIONES CRÍTICAS (≥20% de las 2-3 estrellas)
1. "[frase literal]" — aparece en 14 de 48
2. ...

VOCABULARIO (≥3 personas)
"[palabra]", "[palabra]", "[palabra]"

DESCARTADO POR RIESGO DE CLAIM: [lista]
```

Ese documento entra directo a `315`.

## Relacionados

`310` por qué el cliente sabe lo que la biblioteca no · `311` la encuesta post-compra · `313` entrevistar compradores · `315` del hallazgo al ángulo · `95` leer los comentarios de un anuncio · `250` ángulos de venta · `212`/`213` dolor y mapa de dolores · `185` prueba social · `284` reseñas y reputación · `98` guion de anuncio · `99` swipe file · `mercadolibre_lushows` preguntas y reseñas en ML
