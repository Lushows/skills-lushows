# Qué es Mercado Ads

La publicidad interna de Mercado Libre: pagas por aparecer más arriba frente a alguien que ya está
buscando y con la tarjeta a mano. No es lo mismo que pautar en Meta y no se gestiona igual.
Este módulo fija qué es, qué productos existen en Colombia y dónde termina esta skill.

## La diferencia real con pautar en Meta

No es "otro canal". Es otro momento del comprador.

| | Mercado Ads (interno) | Meta / TikTok (externo) |
|---|---|---|
| Dónde está la persona | Ya en Mercado Libre, buscando | En un feed, sin intención de comprar |
| Qué haces | **Capturas** demanda que ya existe | **Generas** demanda que no existía |
| Qué compras | Posición dentro del resultado | Atención de alguien distraído |
| Contra quién compites | Otros vendedores del mismo producto | Todo el contenido del mundo |
| Quién tiene el dato del cliente | Mercado Libre | Tú, si lo llevas a tu web |
| Tasa de conversión típica | Alta: el clic ya viene caliente | Baja: hay que convencer desde cero |
| Complejidad de arranque | Encender una campaña y elegir estrategia | Píxel, creativos, públicos, aprendizaje |

**Mercado Ads no crea compradores: te pone delante de los que ya iban a comprar de todos modos.**
Por eso funciona rápido y por eso tiene techo — no puedes pautar más demanda de la que existe en
la categoría.

## La frontera entre skills (léela una vez y no la cruces)

| Si vas a… | La skill es |
|---|---|
| Pautar **dentro** de ML: Product Ads, Brand Ads, Display de ML | **esta skill** (`145` a `164`) |
| Pautar en Facebook o Instagram | `facebook_ads_lushows` |
| Pautar en Google Ads o Shopping | `google_ads_lushows` |
| Pautar en TikTok | `tiktok_ads_lushows` |
| Decidir si conviene mandar tráfico externo a ML | `163` de esta skill, y luego las de arriba |

La regla: **retail media es de esta skill; tráfico externo no.** Ver también `163`.

## Los productos de Mercado Ads en Colombia

| Producto | ¿Disponible en CO? | Cómo cobra | Requisito | Para quién |
|---|---|---|---|---|
| **Product Ads** | **Sí** (oficial ML Colombia, verificado sep-2026) | CPC: solo pagas el clic | Ninguno especial | Todo vendedor. Es el 95% del trabajo |
| **Display Programmatic** | **Sí**, confirmado para anunciantes colombianos | Impresiones / programática | Presupuesto de marca | Marcas con inversión seria |
| **Brand Ads** | Sí | Marca / awareness | **Tienda Oficial** (`158`) | Marcas registradas |
| **Video / Streaming** (Mercado Play, Disney+) | ⚠️ ver abajo | — | — | — |

> ⚠️ **Sin verificar para Colombia (sep-2026).** El formato de video y streaming se lanzó a nivel
> regional, pero no hay confirmación de que esté abierto a anunciantes colombianos. No lo cuentes
> en tu plan de medios hasta verlo listado en tu propio panel de Mercado Ads.

Para el 99% de los que leen esto, "Mercado Ads" significa **Product Ads** (`146`). Lo demás es
para cuando ya tengas marca registrada y presupuesto de agencia.

## Por qué el retail media es distinto de todo lo demás

El comprador de ML ya pasó tres filtros antes de ver tu anuncio: decidió comprar, decidió comprar
online y decidió comprar en Mercado Libre. Lo único que le falta es elegir a quién. Eso hace que:

- El clic cueste caro pero convierta mucho más que un clic de feed.
- La competencia sea directa y visible: los mismos cinco vendedores de tu categoría.
- El anuncio no tenga que "vender" — vende tu ficha (`25`, `42`). El anuncio solo consigue la
  visita.

De ahí la consecuencia incómoda: **pautar una ficha mala es pagarle a ML por mostrar tu peor
versión más veces.** Ver `164`.

## Lo que Mercado Ads NO arregla

| Problema | ¿Lo arregla la pauta? |
|---|---|
| Reputación en naranja o rojo | **No.** La penalización de ranking no se compensa con gasto (`66`, `125`) |
| Precio fuera de mercado | No. El clic entra y se va |
| Ficha incompleta o fotos malas | No. Pagas la visita y pierdes la conversión (`40`, `42`) |
| Margen que no da | No. Lo empeora: suma un costo sobre un margen que ya no alcanzaba (`154`) |
| Stock inestable | No. Quedarte sin stock reinicia el aprendizaje de la campaña |
| No estar en el catálogo ganador | Ayuda, pero el catálogo se gana con las variables de `63` |

## El error clásico

Encender la pauta como primer movimiento, antes de calcular el margen. El vendedor promedio ve
que las visitas suben, se entusiasma, y descubre tres semanas después que cada venta pautada le
deja menos plata que una venta orgánica. La pauta amplifica lo que ya tienes: si tu unidad de
venta pierde plata, pautar te hace perder plata más rápido. Ejecuta `82` **antes** de crear la
primera campaña.

## Antes de encender la primera campaña

```
□ Calculé el margen neto real del SKU con la calculadora de `82`
□ El margen neto es mayor al ACOS objetivo que voy a fijar (`150`)
□ La reputación está en verde o verde claro (`125`)
□ La ficha está en nivel "Profesional" y con fotos en 1200 px (`48`, `42`)
□ Tengo stock real para al menos 30 días de ventas al ritmo actual
□ El precio publicado es el precio final: no lo voy a mover durante la prueba
□ Sé cuál es el producto que quiero empujar y por qué (no "todos")
```

Si falla alguna casilla, arregla eso primero. Pautar no es el paso uno, es el paso siete.

## Relacionados

`146` Product Ads · `147` la subasta y el CPC · `148` las tres estrategias · `149` ACOS y TACOS ·
`150` el ACOS sano según tu margen · `154` el error de pautar sin margen · `157` Brand Ads y
Display · `158` Tienda Oficial · `163` tráfico externo · `164` cuándo no es la respuesta ·
`57` factores del ranking · `63` ganar el catálogo · `82` la calculadora de margen ·
`125` reputación
