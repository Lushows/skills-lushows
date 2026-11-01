# Variaciones

Una publicación con variaciones es un solo aviso donde el comprador elige color, talla o medida.
Es la forma correcta de vender el mismo producto en versiones distintas, y Mercado Libre Colombia
lo pide de manera explícita: "si vendes el mismo producto con distintos colores, **no pongas el
color en el título. Crea variantes**" (oficial ML Colombia, verificado sep-2026).

## Por qué importan tanto

| Razón | Detalle |
|---|---|
| Concentran el historial | Todas las ventas, visitas y opiniones suman a **una** publicación |
| Indicador de calidad | "Usar variaciones en vez de publicaciones separadas" es uno de los cuatro objetivos para llegar a Profesional (MEDIA, `47`) |
| Conversión | El comprador no se va a buscar el otro color: lo elige ahí mismo |
| Filtros | Cada variante aporta su valor al filtro de color/talla (`31`) |
| Stock | Se gestiona por variante, con su propio inventario |

**El historial de ventas es la moneda del algoritmo, y las variaciones evitan que la repartas en
cinco publicaciones débiles.** Una publicación con 60 ventas pesa mucho más que cinco con 12.

## Qué puede ser una variación

| Atributo | Ejemplo | ¿Sirve como variación? |
|---|---|---|
| Color | Rojo / Azul / Negro | Sí, el caso clásico |
| Talla | S / M / L / XL | Sí |
| Medida | 30 cm / 40 cm / 50 cm | Sí |
| Capacidad | 500 ml / 1 L | Generalmente sí |
| Sabor | Vainilla / Chocolate | Según categoría |
| Marca | Oster / Samsung | **No.** Son productos distintos |
| Modelo | Dos modelos diferentes | **No** |
| Kit vs unidad | 1 unidad / pack de 3 | Depende: ver `41` y `48` |

Los atributos que sirven como variación los define la categoría. Míralos en
`GET /categories/$CATEGORY_ID/attributes`: los que traen el tag de variación son los válidos.

## Cada variante tiene lo suyo

| Elemento | ¿Es por variante? |
|---|---|
| Foto | Sí — y debe ser la de **esa** variante |
| Stock | Sí |
| Precio | Sí, puede diferir |
| SKU propio | Sí |
| Título | No, es uno solo para toda la publicación |
| Descripción | No, es una sola |
| Categoría | No |
| Opiniones y ventas | No: son de la publicación entera |

Regla dura de fotos: si el comprador elige "azul" y ve la foto roja, desconfía y se va. Cada
variante con su foto correcta (`36`).

## Cómo se arma bien

```
□ 1. Confirma que el atributo de variación existe en tu categoría
□ 2. Escribe UN título sin color, talla ni medida (`28`)
□ 3. Crea cada variante con su valor exacto, elegido de la lista, no escrito a mano
□ 4. Súbele a cada variante su foto propia
□ 5. Carga stock real por variante, con colchón de seguridad (`45`)
□ 6. Asigna SKU a cada una para no perderte en el despacho
□ 7. Revisa el indicador de calidad después de guardar (`46`)
```

## Cuándo una variante hunde a la publicación

Todas las variantes comparten la conversión de la publicación. Una variante sin stock o con precio
disparado ensucia el conjunto:

| Situación | Efecto | Qué hacer |
|---|---|---|
| Una variante agotada y visible | El que la quiere se va sin comprar nada | Repón o quítala |
| Precios muy dispares entre variantes | Confunde y baja la conversión | Normaliza o separa (`41`) |
| Una variante que nadie compra | Diluye pero no mata | Déjala si no cuesta |
| Todas agotadas | `available_quantity: 0` pasa el ítem a pausado (ALTA) y sales de la competencia (`61`) | Nunca llegues ahí |

Cuidado con el stock cero: saca la publicación de la competencia y de la puja de catálogo, y al
reponer "revive como más nueva o menos confiable", teniendo que reconstruir señales (MEDIA, `61`).

## Variaciones y catálogo

Si la publicación compite en catálogo, recuerda que **el título ya no se puede editar** (oficial ML
Colombia, verificado sep-2026; ver `28` y `63`). Deja la estructura de variaciones resuelta antes
de entrar.

## El error clásico

Crear una publicación por color porque "así aparezco más veces". Terminas con cinco publicaciones
que compiten entre sí, ninguna acumula historial, ninguna llega a calidad Profesional, y el
comprador que quería otro color ya se fue donde el competidor que sí tenía el selector. **Cinco
publicaciones débiles no suman una fuerte: se restan.**

## Chequeo

```
□ El título no menciona color, talla ni medida
□ Cada variante usa un valor de la lista oficial, no texto libre
□ Cada variante tiene su propia foto correcta
□ Ninguna variante está en cero visible
□ Los precios entre variantes son coherentes
□ Cada variante tiene SKU
□ No tengo publicaciones separadas del mismo producto compitiendo con esta
```

## Relacionados

`41` única vs variaciones vs múltiples · `28` el título · `29` prohibiciones · `31` atributos ·
`36` la secuencia de fotos · `45` cuánto stock declarar · `46` indicador de calidad · `47` llegar a
Profesional · `48` kits · `61` stock cero y ranking · `63` ganar el catálogo · `196` stock por API
