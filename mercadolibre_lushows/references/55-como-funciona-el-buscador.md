# Cómo funciona el buscador de Mercado Libre

El buscador de ML no es Google con productos adentro. Es un motor de **intención de compra**: cada
consulta viene de alguien con la tarjeta en la mano, y el sistema decide qué mostrar según qué es
más probable que se **venda**, no qué responde mejor la pregunta. Entender esa diferencia cambia
todo lo que escribes en la publicación.

## La diferencia de fondo con Google

| | Google | Buscador de Mercado Libre |
|---|---|---|
| Qué optimiza | Que la respuesta sea buena | Que la transacción ocurra |
| Unidad indexada | Página web | Publicación (ítem) con precio, stock y envío |
| Señal más fuerte | Enlaces y autoridad del dominio | Conversión histórica de esa publicación |
| Qué pasa si no vendes | Nada, sigues posicionado | Bajas: no vender ES la señal negativa |
| Texto largo | Ayuda | Casi no pesa; la descripción no es un blog |
| Quién juzga | Un crawler | Un comprador real que compra o se va |

En Google escribes para que te lean. En Mercado Libre escribes para que te **compren**, y el que
mide es el algoritmo mirando qué hizo la gente después de verte.

**Google te premia por ser la mejor respuesta; Mercado Libre te premia por ser la mejor compra.**

## Qué ve el buscador cuando publicas

No lee tu publicación como un texto. La descompone en campos:

| Campo | Para qué lo usa el buscador |
|---|---|
| Título | Coincidencia con lo que escribió el comprador |
| Categoría | Ubicarte en el árbol correcto; si está mal, no existes |
| Atributos | Alimentar los **filtros** de la izquierda (marca, talla, color, capacidad) |
| Precio | Comparación directa contra los de al lado |
| Envío / Full | Tiempo de entrega prometido |
| Reputación del vendedor | Filtro de confianza |
| Historial de la publicación | Visitas, preguntas, ventas, tasa de conversión |

Los atributos son el campo más subestimado. No son decoración: si no llenas "Talla", desapareces
en el momento en que el comprador toca el filtro de talla. Ver `40` atributos y `41` criterios de
categoría.

## Los tres momentos de una búsqueda

```
1. RECUPERACIÓN   → el buscador junta todas las publicaciones que "califican"
                     (categoría + coincidencia + stock disponible)
2. ORDENAMIENTO   → las ordena según las señales del ranking (ver `57`)
3. PERSONALIZACIÓN → reordena según el usuario concreto: su historial, su ciudad,
                     si es Meli+, si ya te compró
```

El paso 3 es la razón de que tú y tu cliente vean resultados distintos con la misma palabra. Por
eso medir tu posición desde tu propia sesión es engañarte: ver `69`.

## Lo que el buscador NO es

- **No es un índice de texto.** Repetir la palabra clave cinco veces en el título no te sube;
  te hace ver spam y ML prohíbe la repetición de palabras (ver `31`).
- **No premia la antigüedad.** Una publicación vieja con mala conversión pierde contra una nueva
  bien armada.
- **No mira tu descripción como contenido SEO.** No existe el "artículo de blog dentro de la
  ficha". La descripción sirve para resolver dudas y bajar reclamos, no para posicionar.
- **No ve tu web ni tus redes.** Nada de lo que hagas fuera de ML entra al ranking interno.

## El tráfico externo no reemplaza al buscador

Puedes mandar tráfico de Meta, Google o TikTok a tu publicación, y eso genera ventas reales. Pero
esas campañas viven fuera de esta skill: rutea a `facebook_ads_lushows`, `google_ads_lushows` y
`tiktok_ads_lushows`. Lo que SÍ es de esta skill es **Mercado Ads**, la subasta interna que compite
por los mismos espacios del buscador (ver `145`).

Y ojo con la trampa: mandar tráfico frío a una ficha mala **empeora** tu posición orgánica, porque
sube las visitas sin subir las ventas y hunde tu tasa de conversión. Ver `58`.

## El error clásico

Tratar la publicación como una página web: título largo lleno de palabras clave, descripción de
mil palabras, categoría "la que más se parezca". El resultado es una ficha que califica para
muchas búsquedas, convierte en ninguna, y termina con etiqueta de baja conversión.

La jugada correcta es al revés: **poca ambición de palabras, mucha precisión**. Un título exacto,
la categoría correcta, todos los atributos llenos, y que cada visita que llegue tenga motivo para
comprar.

## Checklist de lectura del buscador

```
□ Busca tu producto como lo buscaría un cliente, no como lo llamas tú
□ Anota los 3 primeros resultados y qué tienen en común (Full, precio, cuotas)
□ Mira los filtros de la izquierda: esos son los atributos que DEBES tener llenos
□ Toca cada filtro relevante y confirma que tu publicación sigue apareciendo
□ Repite la búsqueda en ventana de incógnito (ver `69`)
□ Anota si los primeros son publicaciones de catálogo (ver `62`)
```

## Qué cambió en 2026

El buscador dejó de ser solo coincidencia de palabras. En el primer trimestre de 2026 ML desplegó
una experiencia de búsqueda con IA que interpreta intención en vez de comparar cadenas de texto.
Eso reescribe buena parte del "SEO de Mercado Libre" que circula en internet, y tiene módulo
propio: `56`.

> ⚠️ **Sin verificar para Colombia (sep-2026).** No está confirmado si el buscador con IA ya rige
> en MCO o solo en algunos países. Compruébalo tú: haz una búsqueda descriptiva larga
> ("bolso que aguante para el diario y combine con todo") y mira si te devuelve productos
> coherentes o basura literal.

## Relacionados

`31` título · `40` atributos · `41` criterios de categoría · `56` buscador con IA ·
`57` factores del ranking · `58` la conversión manda · `62` qué es el catálogo ·
`69` medir tu posición real · `71` tendencias de ML · `145` Mercado Ads
