# Cómo se gana el catálogo

Ganar la ficha de catálogo es ganar el botón "Comprar ahora" y casi todo el tráfico de ese
producto. Las variables que deciden están identificadas; los pesos, como en todo el algoritmo,
**no son públicos**. Este módulo te da las ocho variables reales y los tres cortes duros que la
mayoría ignora.

## Las ocho variables

| Variable | Qué mira | Módulo |
|---|---|---|
| **Precio final** | El total que paga el comprador, no tu precio de lista | `68`, `83` |
| **Cuotas sin interés** | No existen en publicación Gratuita; las extra cuestan +3 pp | `78` |
| **Reputación** | Color del termómetro del vendedor | `66`, `125` |
| **Stock** | Disponible; en cero sales de la puja | `61` |
| **Tiempo de entrega** | Cuántos días promete tu publicación | `67` |
| **Uso de Full / Flex** | La logística de ML pesa como señal | `103`, `105` |
| **Envío gratis** | Que el comprador no pague el envío | `86` |
| **Nivel MercadoLíder** | MercadoLíder, Gold, Platinum | `131` |

(Confianza media, sep-2026. Son las variables identificadas por fuentes especializadas; ML no
publica ni la lista completa ni los pesos.)

**Nadie puede darte la fórmula del catálogo. Lo que sí puedes es ganar en las ocho variables a la
vez, y entonces la fórmula deja de importar.**

## Los tres cortes duros

Estos no son "pesan más": son puertas cerradas.

### 1. Reputación naranja o roja no puede ganar

Con reputación naranja o roja **puedes participar en el catálogo pero NO puedes ganar la oferta
principal**. Da igual que tengas el precio más bajo del país y envío gratis con Full: no vas a
aparecer como la mejor oferta. Si estás ahí, deja de optimizar precio y ve a arreglar la
reputación: `66` y el bloque `125`-`144`.

### 2. Sin cuotas no compites de igual a igual

Ojo con la nomenclatura: **en Colombia ya no se dice "Clásica" y "Premium"**. El sitio colombiano
habla hoy de publicación **Gratuita**, publicación **con cuotas con 0% interés** y **cuotas extra**.
"Clásica/Premium" es el nombre viejo, que sigue vigente en otros países y por eso llena los blogs.

La gratuita queda descartada de entrada: "las publicaciones gratuitas duran 60 días, tienen una
exposición baja en el listado y **no ofrecen cuotas con 0% interés**" (oficial ML Colombia,
verificado sep-2026). Sin cuotas quedas en desventaja **visible** en la tabla comparativa: el
comprador ve "12 cuotas sin interés" al lado de tu fila que no las tiene.

El costo de ofrecer más cuotas es exacto y oficial: **3 puntos porcentuales**.

| Precio del producto | Cuotas con 0% interés | Cargo por venta |
|---|---|---|
| Menos de $499.999 | Hasta 3 cuotas | **8% a 19%** |
| Menos de $499.999 | Cuotas extra – hasta 6 | **11% a 22%** |
| $500.000 a $1.499.999 | Hasta 6 cuotas | **8% a 19%** |
| $500.000 a $1.499.999 | Cuotas extra – hasta 9 | **11% a 22%** |
| Más de $1.500.000 | Hasta 12 cuotas | **8% a 19%** |

(Oficial ML Colombia, verificado sep-2026: "pagarás entre 8% y 22% según la categoría de tu
producto y la cantidad de cuotas que elijas ofrecer".)

En catálogo la decisión casi nunca es libre: si el ganador ofrece cuotas extra, tú también las
necesitas. Corre esos 3 puntos contra tu margen antes de activarlas: `78` y `83`.

> ⚠️ **Sin verificar para Colombia (sep-2026).** La comisión **exacta de tu categoría** dentro del
> 8%-22% no es pública: vive detrás del login, en `/landing/costos-de-venta` y en el simulador de
> costos. La API `listing_prices` ya no sirve para esto: devuelve
> `403 PA_UNAUTHORIZED_RESULT_FROM_POLICIES` y exige token.

### 3. Si compites en catálogo, no puedes editar el título

"Puedes modificar el título incluso si ya tienes ventas. **Excepto si la publicación compite en
catálogo**: en ese caso no podrás editar el título" (oficial ML Colombia, verificado sep-2026).

No te impide ganar, pero cierra una puerta: **el título deja de ser una palanca tuya**. Tres
consecuencias operativas:

```
□ Revisa el título de la ficha de catálogo ANTES de sumarte: si describe mal tu
  producto o le falta la variante, no lo vas a poder arreglar después
□ En títulos de catálogo, que son compartidos, ML prohíbe expresamente sumar datos
  de contacto y mensajes sobre precio, tipo de envío o stock
□ Si tu estrategia dependía de trabajar el título, la salida es publicación propia (`64`)
```

## Cómo pelear cada variable

```
PRECIO FINAL
□ Compara TU precio + TU envío contra EL precio + EL envío del ganador
□ Calcula el margen con la comisión real antes de bajar un peso (`83`)
□ Si no puedes ganar en precio sin perder plata, no lo hagas: ve a `64`

CUOTAS
□ Activa cuotas extra solo si el número da: cuestan exactamente 3 puntos porcentuales
□ Verifica en la ficha cuántas cuotas ofrece el ganador y con qué banco

REPUTACIÓN
□ Verde o verde claro es requisito para ganar
□ Reclamos < 2,5%, mediaciones < 0,5%, canceladas < 1,5%, envíos incorrectos < 10%
  (son los requisitos oficiales de MercadoLíder, verificado sep-2026)

STOCK
□ Nunca cero. Define un piso y trátalo como cero (`61`)
□ Revisa el stock de tus publicaciones de catálogo TODOS los días

ENTREGA
□ Full si puedes; es la señal de entrega más fuerte (`103`)
□ Si no, Flex o tiempos de manejo cortos y cumplidos (`105`)

ENVÍO GRATIS
□ Desde $60.000 ML te pide ofrecer envío gratis o con descuento (oficial)
□ Debajo de $60.000 es opcional y el costo corre 100% por tu cuenta
□ Cruzar los $60.000 casi duplica tu costo de envío: 1 kg pasa de $4.300 a $8.200
□ Tu descuento depende del color: verde/MercadoLíder/sin reputación 50%,
  amarilla 40%, naranja o roja ninguno (oficial)

MERCADOLÍDER
□ 120 ventas y $10.000.000 en 60 días = MercadoLíder
□ 300 ventas y $30.000.000 = Gold · 600 ventas y $80.000.000 = Platinum
  (oficial ML Colombia, verificado sep-2026; requiere +4 meses registrado y reputación verde)
```

El envío es donde la reputación se vuelve dinero dentro del catálogo (oficial ML Colombia,
verificado sep-2026):

| Reputación | Descuento en envíos desde $60.000 | Costo real de 1 kg |
|---|---|---|
| MercadoLíder, verde, o **sin reputación** | 50% | **$8.200** |
| Amarilla | 40% | **$9.600** |
| Naranja o roja | Ninguno | **$16.400** |

Un competidor naranja paga el doble que tú por cada despacho. Eso significa que, aunque iguale tu
precio de lista, su margen es peor y no lo puede sostener. Y a ti te pasa lo mismo al revés si
pierdes el verde. La tabla completa por peso y rango de precio está en `86`.

## El orden correcto de ataque

No ataques las ocho a la vez. Este es el orden por retorno:

| Orden | Variable | Por qué primero |
|---|---|---|
| 1 | Reputación | Es puerta cerrada: sin verde no ganas nunca |
| 2 | Stock | Es puerta cerrada: en cero sales de la puja |
| 3 | Full / tiempo de entrega | Es la más difícil de igualar para el competidor pequeño |
| 4 | Cuotas con 0% interés | Se ve directo en la tabla comparativa |
| 5 | Envío gratis | Cambia el precio final que ve el comprador |
| 6 | Precio | El último, porque es el que te quita margen |
| 7 | MercadoLíder | Se gana con el tiempo, no se fuerza |

Bajar el precio es la palanca más fácil y la más cara. Es también la única que tu competidor puede
copiar en treinta segundos. Full, reputación y MercadoLíder tardan meses en copiarse.

## Cómo saber si estás ganando

```
□ Abre la ficha del producto en ventana de incógnito (`69`)
□ Mira quién aparece con el botón "Comprar ahora": ese es el ganador
□ Abre "Otras opciones de compra" y ubica tu fila
□ Compara columna por columna: precio, cuotas, envío, entrega, vendedor
□ Repite desde otra ciudad o con otra cuenta: hay personalización (`65`)
□ Por API, el topic de webhook `item_competition` avisa de cambios en la competencia
```

## El error clásico

Pelear el catálogo solo con precio. El vendedor baja $2.000, gana dos días, el competidor baja
$2.500, y al mes los dos venden lo mismo con la mitad del margen. Las variables que de verdad
sostienen el catálogo son las que el otro no puede copiar rápido: **Full, reputación verde y
MercadoLíder**. El precio es la última carta, no la primera.

## Relacionados

`61` stock cero · `62` qué es el catálogo · `64` cuándo no competir en catálogo ·
`65` compartir el primer lugar · `66` reputación como filtro · `67` envío y posición ·
`68` precio como factor · `69` medir tu posición real · `70` espiar al líder ·
`78` tipos de publicación · `80` comisión real · `83` precio con margen · `86` envío gratis ·
`103` Full · `105` Flex · `125` reputación · `131` MercadoLíder
