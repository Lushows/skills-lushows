# Espiar al líder

El vendedor mejor posicionado de tu categoría es la mejor documentación que existe sobre el
algoritmo en tu nicho. No te va a decir los pesos, pero te muestra qué combinación funciona **hoy,
en Colombia, en tu categoría**. Este módulo es para competir contra él, no para copiarlo.

`dropshipping_lushows` módulo `57` cubre el espionaje desde la óptica de **investigación de
producto** ("¿qué vendo?"). Aquí el producto ya está decidido y la pregunta es otra: **"¿qué tiene
él que yo no?"**

## La ficha de espionaje

Llena esto para los 3 primeros resultados orgánicos de tu término principal.

| Campo | Qué anotar | Por qué |
|---|---|---|
| Título completo | Palabra por palabra | Te muestra qué términos usa el comprador real |
| Categoría | La ruta completa del breadcrumb | Puede que tú estés en la equivocada (`41`) |
| Atributos visibles | Los de la ficha técnica | Los que él llenó y tú no, son filtros que pierdes |
| Precio de lista | El número grande | Punto de partida |
| **Precio final con envío** | Simula la compra hasta ver el total | Es lo que compara el algoritmo (`68`) |
| Cuotas | Cuántas y con 0% interés o no | Si ofrece extra, paga 3 pp más (`78`) |
| Logística | Full / Flex / normal, y días de entrega | La barrera más difícil de igualar (`67`) |
| Reputación | Color y si es MercadoLíder/Gold/Platinum | El filtro de entrada (`66`) |
| Ventas de la publicación | "X vendidos" si está visible | Volumen real, no promesas |
| Cantidad de fotos | Y si tiene video | Estándar de ficha de tu categoría (`42`) |
| **Preguntas** | Las últimas 20, completas | Oro puro, ver abajo |
| **Opiniones negativas** | Las de 1 y 2 estrellas | Oro puro, ver abajo |
| Si está en catálogo | Y si es el ganador | Cambia toda tu estrategia (`62`, `64`) |

**El líder no te enseña qué escribir: te enseña qué combinación de precio, entrega y confianza es
suficiente en tu categoría.**

## Las preguntas son el activo más subestimado

Las preguntas públicas de tu competidor son una lista gratis de las objeciones reales de tus
clientes, escritas con sus palabras.

```
□ Lee las últimas 20 preguntas de cada uno de los 3 líderes
□ Agrupa por tema: medidas, compatibilidad, garantía, entrega, contenido de la caja
□ El tema que más se repite = la duda que está frenando la venta en tu categoría
□ Responde esa duda en tu DESCRIPCIÓN y en tus FOTOS, no esperes a que te pregunten
□ Si tres personas preguntan lo mismo, es un atributo que falta en la ficha
□ Con buscador semántico (`56`), las palabras de las preguntas son las palabras de la intención
```

Una ficha que resuelve de entrada las cinco dudas que el líder responde una por una tiene mejor
conversión que la del líder. Y la conversión es la señal más pesada (`58`).

## Las opiniones negativas son tu propuesta de valor

Lee las reseñas de 1 y 2 estrellas del líder. Ahí está escrito lo que el mercado quiere y nadie
está dando.

| Queja repetida | Tu jugada |
|---|---|
| "Llegó tarde" | Full o tiempo de manejo corto, y dilo en la ficha |
| "No es del tamaño que decía" | Foto con escala y medidas en la descripción |
| "Vino sin el cable / sin el manual" | Foto del contenido completo de la caja |
| "El color no es el de la foto" | Foto real en luz neutra, no render |
| "No respondieron" | Responde preguntas en menos de una hora (`128`) |
| "Mala calidad" | Si es el mismo producto que vendes tú, cambia de proveedor |

La última fila es la más importante y la que la gente ignora: **si las quejas son del producto y
tú vendes exactamente ese producto, no tienes ventaja competitiva, tienes el mismo problema
esperándote.** Rutea a `dropshipping_lushows` para buscar otro proveedor.

## Qué NO copiar

| No copies | Por qué |
|---|---|
| Su título literal | No tienes su conversión ni su historial; y duplicar es riesgoso |
| Sus fotos | Infracción de propiedad intelectual: te pausan y te denuncian (`73`) |
| Su descripción | Igual |
| Su precio exacto | Su costo no es tu costo. Corre tu propio margen (`83`) |
| Su estrategia de Ads | No la ves; lo que ves son sus anuncios, no su ACOS |

Lo que sí copias es el **estándar**: cuántas fotos, qué atributos, qué tiempo de entrega, qué
rango de precio es aceptable en tu categoría.

## El análisis de brecha

Con la ficha llena, haz la tabla de diferencias:

```
┌─ Variable ──────────┬─ Líder ─────┬─ Tú ────────┬─ Brecha ─┬─ Cuánto cuesta cerrarla ─┐
│ Precio final        │ $52.000     │ $58.000     │ -$6.000  │ 6 pts de margen          │
│ Cuotas              │ 12 s/interés│ No          │ Grande   │ 3 pts de comisión        │
│ Entrega             │ Full, 2 días│ 5 días      │ Grande   │ Costo Full + logística   │
│ Reputación          │ Verde Gold  │ Verde claro │ Media    │ 60 días de operación     │
│ Fotos               │ 8 + video   │ 3           │ Chica    │ Una tarde                │
│ Atributos           │ 24 llenos   │ 11          │ Chica    │ Una hora                 │
└─────────────────────┴─────────────┴─────────────┴──────────┴──────────────────────────┘
```

Ataca **siempre primero las brechas baratas**: fotos y atributos cuestan una tarde y no tocan tu
margen. El precio va de último (`68`).

## Cómo espiar sin romper nada

```
□ Ventana de incógnito, sin sesión (`69`)
□ A mano, no con scraper: ML bloquea el acceso automatizado y devuelve 403
□ Las buenas prácticas oficiales dicen usar la API en vez de scraping
□ Por API sí puedes: GET /sites/MCO/search?q=... y GET /items/$ITEM_ID (datos públicos)
□ Webhook item_competition para enterarte de cambios en tu competencia (`185`)
□ Repite el ejercicio cada mes: el líder de hoy no es el de enero
```

## El error clásico

Espiar una sola vez, copiar el título y quedarse tranquilo. El líder no es líder por su título:
es líder por la suma de Full + reputación verde + precio competitivo + ficha completa, construida
en meses. Copiar la parte visible y no la estructura es por qué el vendedor promedio "hace todo
igual que el primero" y sigue en la página tres.

## Relacionados

`31` título · `40` atributos · `41` criterios de categoría · `42` fotos · `45` descripción ·
`57` factores del ranking · `58` la conversión manda · `62` qué es el catálogo ·
`63` cómo se gana el catálogo · `64` cuándo no competir en catálogo · `66` reputación como filtro ·
`67` envío y posición · `68` precio como factor · `69` medir tu posición real ·
`71` tendencias de ML · `73` pausas e infracciones · `83` precio con margen · `128` preguntas ·
`185` webhooks · `dropshipping_lushows` `57` investigación de producto
