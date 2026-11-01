# Medir tu posición real

Buscar tu producto desde tu propia sesión y verte primero no significa nada. El buscador
personaliza por usuario: historial, ciudad, si es Meli+, si ya te compró. Este módulo te da el
método para saber en qué puesto estás **de verdad**, que es la información sin la cual todo lo
demás de este bloque es adivinanza.

## Por qué tu propia búsqueda te miente

| Sesgo | Qué hace |
|---|---|
| **Historial de navegación** | Ya visitaste tu publicación cien veces: ML te la muestra |
| **Cuenta logueada** | Eres el vendedor; el sistema te conoce |
| **Ubicación** | El tiempo de entrega cambia por ciudad y con él la posición |
| **Personalización de catálogo** | El ganador alterna según el comprador (`65`) |
| **Cookies y sesión** | Búsquedas previas condicionan lo que sale |
| **Dispositivo** | Móvil y escritorio ordenan distinto y muestran distinta cantidad |

**Tu posición no es un número: es una distribución. Si la mides una vez, no la mediste.**

## El método de medición

```
PREPARACIÓN
□ Cierra sesión de Mercado Libre
□ Abre ventana de incógnito (Ctrl+Shift+N en Chrome)
□ No inicies sesión con nada

MEDICIÓN
□ Busca el término EXACTO que usaría un comprador, no el nombre técnico
□ Cuenta desde arriba hasta encontrarte; anota el puesto
□ Anota cuántos de los que están arriba son anuncios (llevan la etiqueta de publicidad)
□ Anota cuántos son publicaciones de catálogo (`62`)
□ Repite con 3-5 términos distintos, no solo con uno
□ Repite en móvil, con datos móviles (otra IP)
□ Pide a alguien de otra ciudad que haga la misma búsqueda

REGISTRO
□ Fecha, término, puesto, dispositivo, ciudad
□ Guarda captura: la memoria inventa
□ Repite la medición el mismo día de cada semana, a la misma hora
```

Mínimo 5 mediciones por término para que el promedio signifique algo. Una sola medición es una
anécdota.

## Los términos que debes medir

No midas solo el nombre de tu producto. Mide como busca la gente:

| Tipo de término | Ejemplo | Para qué sirve |
|---|---|---|
| Genérico | "organizador de cables" | Volumen alto, competencia alta |
| Con marca | "organizador de cables Baseus" | Intención más definida |
| Con modelo | "Baseus CW-01" | Aquí suele haber catálogo |
| Descriptivo largo | "organizar cables del escritorio sin taladrar" | Prueba el motor semántico (`56`) |
| Con atributo | "organizador de cables negro adhesivo" | Prueba si tus atributos están llenos |

El descriptivo largo es el más informativo en 2026: si apareces ahí, el motor semántico ya rige y
tu ficha está bien declarada. Si devuelve basura, el buscador de tu categoría sigue siendo literal.

## Qué mirar además del puesto

```
□ ¿Cuántos resultados hay en total para ese término? (competencia real)
□ ¿Los primeros son anuncios o orgánicos? (si son anuncios, hay pista de Mercado Ads)
□ ¿Los primeros son catálogo? (si sí, tu publicación libre pelea cuesta arriba, `62`)
□ ¿Cuántos de los 5 primeros tienen Full? (te dice si la logística es la barrera, `67`)
□ ¿Cuál es el rango de precios de los 5 primeros? (tu precio final vs. el de ellos, `68`)
□ ¿Qué reputación tienen? (si todos son verdes, es el filtro de entrada, `66`)
```

Ese conjunto vale más que el puesto solo. El puesto te dice dónde estás; esto te dice **por qué**.

## Las métricas del panel: úsalas como termómetro, no como posición

ML te muestra visitas por publicación. Eso no es tu posición, pero se mueve con ella:

| Patrón en el panel | Lectura |
|---|---|
| Visitas caen de golpe un día concreto | Perdiste posición o catálogo ese día (`72`) |
| Visitas estables, ventas caen | Problema de precio o competencia, no de posición |
| Visitas suben y ventas no | Apareces en búsquedas equivocadas (`58`) |
| Todo cae a cero | Pausa, infracción o stock cero (`61`, `73`) |

Los reportes de Mercado Ads tienen su propia demora: las ventas pueden tardar **hasta 72 horas** en
reflejarse (oficial ML Colombia, verificado sep-2026). No saques conclusiones el mismo día.

## Lo que no puedes medir (y quién te va a decir que sí)

No existe un "rank tracker" oficial de Mercado Libre. Las herramientas de terceros que prometen
seguimiento de posición scrapean, se rompen seguido y pueden violar los términos: las buenas
prácticas oficiales dicen explícitamente **usar la API en vez de scraping**.

Y hay un matiz que confunde a medio mundo: **el bloqueo no es al humano, es al robot**. ML devuelve
**403** a `fetch` automatizado y a `curl` sobre `mercadolibre.com.co/ayuda/*` y
`vendedores.mercadolibre.com.co`, pero **con navegador real esas páginas abren sin problema**. Si
alguien te dice "no se puede consultar, da 403", estaba usando la herramienta equivocada
(verificado sep-2026).

Lo que sí puedes automatizar legítimamente: el webhook `item_competition` avisa de cambios en tu
competencia, e `items_prices` de cambios de precio. Ver `185`. Lo que ya **no** puedes: la API
`GET /sites/MCO/listing_prices` dejó de ser pública y hoy responde
`403 PA_UNAUTHORIZED_RESULT_FROM_POLICIES` exigiendo token.

## La trampa de los enlaces del centro de ayuda

Esta te va a pasar y conviene saberla antes: **las URLs viejas del centro de ayuda ya no existen y
no dan 404 — redirigen en silencio a una página equivocada** (`/ayuda/1064`, que es sobre hackeo de
dispositivos). Terminas leyendo un artículo que no tiene nada que ver y creyendo que ML cambió la
política (verificado sep-2026).

Slugs muertos confirmados, que aún circulan en blogs y en respuestas de foros:

```
costos-de-vender_1265 · reputacion-vendedor_1622 · mercadolider_1302
calidad-publicaciones_4132 · tipos-de-publicacion_1285 · mercado-envios-full_13790
```

La forma correcta de llegar a un artículo oficial:

```
□ Usa el buscador interno: mercadolibre.com.co/ayuda/search?q=TU+TEMA
□ Nunca confíes en un enlace de ayuda copiado de un blog: verifica que el título de
  la página que abre corresponda al tema que buscabas
□ Si el artículo habla de algo distinto a lo que pediste, te redirigieron: vuelve al buscador
□ Guarda tú el enlace bueno el día que lo encuentres, con la fecha de consulta
```

**Un enlace de ayuda que abre no significa que abriera el correcto.** Revisa siempre el título de
la página antes de creerle al contenido.

## Frecuencia recomendada

| Situación | Cada cuánto medir |
|---|---|
| Publicación nueva | Días 1, 3 y 7 (protocolo de `59`) |
| Publicación estable | Una vez por semana, mismo día y hora |
| Peleando catálogo | 5 pruebas en incógnito, dos veces por semana (`65`) |
| Después de cambiar precio o ficha | A los 7 y a los 21 días, no al día siguiente |
| Temporada alta (Hot Sale 19-23 oct 2026) | Diario |

## El error clásico

Medir desde el celular, logueado, con la publicación abierta en otra pestaña, y concluir "estoy de
primero". Después pasar tres semanas sin entender por qué no entran ventas. La medición mal hecha
es peor que no medir: te da confianza falsa y te hace optimizar lo que no está roto.

## Relacionados

`55` cómo funciona el buscador · `56` buscador con IA · `57` factores del ranking ·
`58` la conversión manda · `59` primeras 72 horas · `61` stock cero · `62` qué es el catálogo ·
`65` compartir el primer lugar · `66` reputación como filtro · `67` envío y posición ·
`68` precio como factor · `70` espiar al líder · `71` tendencias de ML ·
`72` por qué cayó mi publicación · `73` pausas e infracciones · `185` webhooks
