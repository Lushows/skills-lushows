# Qué es el catálogo

En categorías estandarizadas Mercado Libre no muestra 40 publicaciones del mismo producto: crea
una **ficha única compartida** y elige un ganador que aparece como "la mejor oferta". Los demás
van a "Otras opciones de compra". Es la buy box de Mercado Libre, y cambia por completo cómo
compites.

## La mecánica

```
Producto estandarizado (ej.: iPhone 15 128GB Negro)
        │
        └── UNA ficha de catálogo (fotos, título y descripción los pone ML)
                │
                ├── GANADOR → botón "Comprar ahora", se lleva casi todo el tráfico
                └── "Otras opciones de compra" → el resto, en una tabla comparativa
```

Tú no creas la ficha: te **sumas** a una que ya existe. Tus fotos y tu descripción dejan de
mostrarse. Lo que se compara del vendedor es un puñado de variables: precio final, cuotas,
reputación, tiempo de entrega, envío gratis, Full (ver `63`).

**En catálogo no vendes tu publicación: vendes tus condiciones.**

## Publicación propia vs catálogo

| | Publicación propia | Catálogo |
|---|---|---|
| Quién controla fotos y texto | Tú | Mercado Libre |
| Cómo te diferencias | Contenido, fotos, descripción, bundle | Precio, logística, reputación |
| Con quién compites | Con todos, en la grilla | Con 3-20, en la misma ficha |
| Exposición | La que te dé el ranking | Las de catálogo aparecen **más arriba** que las libres equivalentes |
| Si pierdes | Bajas de posición | Caes a "Otras opciones": casi invisible |
| Opiniones | Son de tu publicación | Son de la ficha, compartidas |
| Sirve para | Producto propio, bundle, artesanal, marca propia | Producto estandarizado con marca y modelo |

## Cómo saber si tu producto tiene catálogo

```
□ Busca tu producto exacto en ML Colombia
□ Si ves una ficha con "Otras opciones de compra" o "X opciones desde $Y" → hay catálogo
□ Al crear la publicación, ML te ofrecerá asociarla a un producto existente
□ Por API: los atributos con tags.catalog_required: true son los obligatorios
  para entrar a catálogo (distintos de los tags.required normales)
□ Si tu producto no aparece, puedes proponerlo; no siempre lo aceptan
```

> ⚠️ **Sin verificar para Colombia (sep-2026).** No está confirmado qué categorías tienen catálogo
> habilitado en MCO en 2026. Los listados que circulan son de Argentina, México y Brasil.
> Compruébalo producto por producto con el método de arriba.

## Dónde suele haber catálogo y dónde no

| Suele haber | Casi nunca hay |
|---|---|
| Celulares y accesorios con modelo definido | Ropa hecha a mano o sin marca |
| Computación y componentes | Artesanías |
| Electrodomésticos con referencia de fábrica | Combos y bundles armados por ti |
| Consolas y videojuegos | Servicios |
| Libros | Productos de marca propia recién creada |
| Perfumería y cosmética de marca | Repuestos genéricos sin referencia |

La regla mental: **si el producto tiene un número de modelo del fabricante, probablemente haya
catálogo.**

## Qué pasa con tus opiniones y tu reputación

- Las **opiniones del producto** son de la ficha compartida: las ves aunque no sean tuyas, y las
  malas de otro vendedor también afectan la percepción.
- Las **calificaciones de vendedor** siguen siendo tuyas y te acompañan. Tu reputación es de la
  cuenta, no de la publicación (ver `125`).
- Si pierdes el catálogo, tu publicación sigue existiendo en "Otras opciones": no desaparece, se
  vuelve casi invisible.

## El empate existe

No siempre hay un solo ganador. Se puede **compartir el primer lugar**: las visitas se dividen y
el ganador alterna según el comprador, porque hay personalización por usuario. Tiene módulo
propio: `65`.

## Lo que el catálogo te quita

Esto es lo que las guías optimistas no dicen: al entrar a catálogo, todo tu trabajo de contenido
se vuelve invisible. Tus fotos mejores, tu descripción que resolvía dudas, tu video de 60
segundos: nada de eso se muestra. Quedas reducido a una fila en una tabla comparativa. Si tu
ventaja competitiva era el contenido, el catálogo te la borra. Cuándo conviene igual y cuándo no:
`64`.

## Checklist de entrada a catálogo

```
□ Confirma que el producto exacto (marca + modelo + variante) existe en el catálogo
□ Revisa que la ficha de catálogo describa TU producto, no uno parecido
□ Llena los atributos con tags.catalog_required: true
□ Calcula tu precio final contra el del ganador actual, incluyendo envío (`83`)
□ Verifica tu reputación: naranja o rojo puede participar pero NO puede ganar (`63`)
□ Decide las cuotas: la publicación Gratuita no ofrece cuotas con 0% interés y
  queda en desventaja visible en la tabla comparativa
□ Asegura stock: en cero sales de la puja (`61`)
```

## El error clásico

Entrar a catálogo por defecto porque "así aparece más arriba", sin mirar el precio del ganador.
Resultado: tu publicación queda escondida en "Otras opciones de compra", con menos visitas de las
que tenía como publicación libre, y encima perdiste el control de las fotos. Entrar a catálogo sin
poder ganarlo es regalarle tráfico al competidor.

## Relacionados

`40` atributos · `41` criterios de categoría · `57` factores del ranking ·
`61` stock cero · `63` cómo se gana el catálogo · `64` cuándo no competir en catálogo ·
`65` compartir el primer lugar · `66` reputación como filtro · `67` envío y posición ·
`68` precio como factor · `70` espiar al líder · `78` tipos de publicación · `125` reputación
