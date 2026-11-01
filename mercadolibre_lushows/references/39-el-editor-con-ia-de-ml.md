# El editor con IA de ML

Mercado Libre tiene un editor de fotos nativo dentro del panel, con un botón "**Generar fotos con
IA**" que mejora o genera imágenes de producto (MEDIA). Resuelve justo el problema que tumba a la
mayoría: el fondo blanco #FFFFFF (`35`).

> ⚠️ **Sin verificar para Colombia (sep-2026).** No está confirmado si el editor con IA ya llegó a
> Colombia o sigue solo en países piloto. Compruébalo tú: entra a editar una publicación, ve a la
> sección de fotos y mira si aparece el botón. Si no está, no existe para tu cuenta todavía y no
> hay forma de forzarlo.

## Qué hace (cuando está disponible)

| Función | Para qué sirve |
|---|---|
| Quitar el fondo y ponerlo blanco | Cumplir el requisito de #FFFFFF sin editor externo |
| Mejorar iluminación y nitidez | Rescatar una foto tomada con poca luz |
| Generar ambientaciones | Poner el producto en un contexto para las fotos secundarias |
| Ajustar encuadre al formato | Llevar la foto a 1200 × 1200 sin deformarla |

## Cuándo usarlo

| Situación | ¿Usarlo? |
|---|---|
| Tienes buena foto pero fondo sucio | **Sí.** Es exactamente para eso |
| La foto está subexpuesta | Sí, con cuidado de no alterar el color real |
| Necesitas la foto 1 rápido para publicar hoy | Sí |
| Tienes 80 SKUs y cero presupuesto de fotografía | Sí, como piso de calidad |
| Quieres una foto de uso en contexto | Con cuidado: ver abajo |

## Cuándo NO usarlo

| Situación | Por qué no |
|---|---|
| El color generado no es el color real del producto | Reclamo de "producto distinto al anunciado", **no excluible** (`136`) |
| El ambiente generado sugiere que se incluye algo que no va | Reclamo de producto incompleto (`125`) |
| El producto tiene textura que la IA "inventa" | Estás vendiendo un acabado que no existe |
| Es tu foto principal de un producto caro | Ahí sí conviene fotografía real y buena |
| El producto tiene letras, logos o etiquetas | La IA los deforma; queda evidente y barato |

**La IA puede arreglar el fondo; no puede inventar el producto.** Todo lo que toque al producto
mismo —color, textura, forma, etiquetas— hay que revisarlo contra el objeto real antes de subirlo.

## El control de calidad obligatorio

Cada imagen generada o retocada pasa por este filtro antes de publicarse:

```
□ El color en pantalla es el color del producto que tienes en la mano
□ La forma no está deformada (bordes rectos siguen rectos)
□ Los logos y textos del producto se leen correctamente
□ No aparece ningún objeto que no venga incluido
□ El fondo es #FFFFFF de verdad, no casi blanco (verifícalo con cuentagotas)
□ No quedaron halos ni restos del fondo anterior en los bordes
□ A tamaño de miniatura sigue viéndose bien
```

Si falla una, no la subas.

## Alternativas si no lo tienes

| Herramienta | Nota |
|---|---|
| Cualquier removedor de fondo | Suficiente para el 90% de los productos |
| Editor de escritorio | Más control en bordes complicados (pelo, transparencias) |
| Fotógrafo de producto | Para el catálogo estrella; se paga solo si el producto es caro |

Todo lo que sea dirección de arte, estilo de marca y producción fotográfica de verdad sale de esta
skill: **rutea a `directorcreativo_lushows`**.

## Lo que la IA no reemplaza

| Pieza | Por qué necesita el producto real |
|---|---|
| Foto de escala (`36`) | El tamaño relativo tiene que ser verdadero |
| Foto de detalle del material | Es justo la textura que no se puede inventar |
| Foto del contenido de la caja | Es un inventario, no una ilustración |
| Video (`38`) | Muestra funcionamiento |

O sea: la IA sirve para la foto 1 y para limpiar. Las fotos 2 a 6 siguen necesitando que tomes el
producto y lo fotografíes.

## El error clásico

Generar seis imágenes con IA, todas bonitas, todas de un producto que no existe exactamente así, y
publicar. Las visitas suben, la conversión sube al principio y después llegan las devoluciones y
las opiniones de tres estrellas. Los reclamos por producto distinto al anunciado **no se pueden
excluir** de tu reputación (ALTA, `136`), y perder el verde te duplica el costo de envío (oficial
ML Colombia, verificado sep-2026; ver `126`). **La foto más rentable es la que hace que nadie
devuelva.**

## Relacionados

`35` foto principal · `36` la secuencia · `37` errores de foto · `38` el video · `125` reputación ·
`126` qué te cuesta perder el verde · `136` reclamos no excluibles · `46` indicador de calidad ·
dirección de arte y fotografía → `directorcreativo_lushows`
