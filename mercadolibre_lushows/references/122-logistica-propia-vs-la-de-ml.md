# Logística propia vs la de Mercado Libre

La pregunta suena razonable: "yo consigo el flete más barato, ¿por qué usar Mercado Envíos?". La
respuesta corta es que ahorras en el flete y pagas en posición, en cobertura de reclamos y en
descuento de reputación. La cuenta casi nunca da.

## La tabla de decisión

| Variable | Mercado Envíos | Logística propia |
|---|---|---|
| Costo del flete | Tabla oficial de `100`, con hasta 50% de descuento | El que negocies |
| Descuento por reputación | **50% si eres verde, ML o sin reputación** | Ninguno: no aplica |
| Posición en búsqueda | La logística es pilar del ranking | Pierdes esa señal |
| Desempate de catálogo | Full/Flex es variable del ganador (`63`) | Quedas en desventaja |
| Filtros de "llega gratis / llega mañana" | Entras | **Desapareces cuando filtran** |
| Envío gratis del marketplace | Aplica desde $60.000 (oficial) | No aplica |
| Agrupación de carrito entre vendedores | Solo con Full | No |
| Compra Protegida si se pierde | Cubre al comprador (`118`) | **Respondes tú, completo** |
| Rastreo dentro de la plataforma | Sí | No: más preguntas en tu bandeja |
| Gestión de guías | ML la genera | Tuya |

Nueve de diez filas favorecen a Mercado Envíos, y la única que puede favorecer a la logística
propia —el costo— tiene que competir contra un descuento del 50%.

**La logística propia gana el flete y pierde el embudo.**

## El cálculo honesto

```
AHORRO REAL DE LA LOGÍSTICA PROPIA =
    (costo de Mercado Envíos con TU descuento de reputación)
  − (tu flete negociado + tu tiempo de gestión de guías + tus pérdidas no cubiertas)

COSTO OCULTO =
    ventas perdidas por caer en el ranking
  + ventas perdidas por no aparecer en los filtros de entrega
  + ventas de catálogo perdidas en el desempate
  + paquetes perdidos que ahora pagas tú
```

Para que la logística propia gane, tu flete tiene que ser más barato que la tabla oficial **ya
descontada al 50%**. Para un paquete de 1 kg y producto de más de $60.000, eso significa competir
contra **$8.200** (oficial ML Colombia, verificado sep-2026). Y aun ganando esa comparación,
tienes que compensar el costo oculto, que casi nadie mide.

Para correr los números exactos, rutea a `Matematicas_lushows`.

## El error de razonamiento más común

"Como no tengo reputación todavía, no tengo el descuento, así que me sale mejor por fuera."

Es falso, y este es uno de los datos más útiles de toda la skill: **un vendedor sin reputación
tiene el mismo 50% de descuento que un verde** (oficial ML Colombia, verificado sep-2026). El
descuento es 50% para MercadoLíder, verde **y sin reputación**; 40% para amarilla; ninguno para
naranja o roja.

| Reputación | Descuento |
|---|---|
| MercadoLíder, verde, **o sin reputación** | 50% |
| Amarilla | 40% |
| Naranja o roja | Ninguno |

El castigo no es no tener reputación: **es perderla.** Arrancas con el mejor descuento disponible.

## Cuándo la logística propia sí tiene sentido

No es nunca, pero es poco:

| Caso | Por qué |
|---|---|
| Producto fuera de las dimensiones de Mercado Envíos | No hay alternativa |
| Categorías con logística especial (inmuebles, vehículos, servicios) | El envío no aplica |
| Producto que requiere instalación o montaje | El servicio es parte de la venta |
| Producto perecedero con cadena de frío | Mercado Envíos no lo maneja |
| Entrega local propia donde Flex no está habilitado | Sustituto de Flex, no de todo |

Fíjate que ninguno de esos casos es "porque conseguí flete más barato". Son casos donde Mercado
Envíos **no puede** hacerlo.

## Lo que pierdes en reputación

Con logística propia sigues teniendo las mismas variables del termómetro —**reclamos**,
**canceladas por ti**, **envíos incorrectos**— pero sin las defensas:

| Defensa | Con Mercado Envíos | Con logística propia |
|---|---|---|
| Evidencia de despacho a tiempo | La genera el sistema | Tuya, y tienes que probarla |
| Rastreo verificable por ML | Sí | Depende de tu transportadora |
| Exclusión por demora ajena | Se pide con el registro de ML | Más difícil de sustentar |
| Compra Protegida en paquete perdido | Cubre al comprador | La pérdida es tuya |

Y los techos oficiales no cambian: 3,5% de reclamos, 12% de envíos incorrectos a 60 días, 2,5% de
canceladas a 60 días para conservar el verde (oficial ML Colombia, verificado sep-2026). Ver
`126`.

## La comparación completa contra Full

Si lo que evalúas es "todo propio vs todo Full", la tabla se decide por rotación, no por flete:

| | Todo propio | Todo Full |
|---|---|---|
| Flete | Tabla oficial, 50% si eres verde | Tabla oficial, 50% garantizado |
| Bodegaje | Tu bodega, tu costo | Almacenamiento + cargos de antigüedad (`107`, `108`) |
| Velocidad | La que logres | Entrega al día siguiente (oficial) |
| Control del inventario | Total | Ninguno |
| Riesgo de rotación lenta | Bajo | **Muy alto**: $64.100/mes por unidad grande a los 6 meses |

Decisión completa en `105`. La respuesta sana casi siempre es mixta: Full para los de alta
rotación, bodega propia para el resto.

## El error clásico

Salirse de Mercado Envíos para ahorrar flete y no medir la caída de ventas. El vendedor ve el
ahorro —que es visible, está en la factura— y no ve la pérdida —que es invisible, son ventas que
nunca ocurrieron. Tres meses después vende la mitad, con mejor margen unitario y peor utilidad
total.

**En Mercado Libre no compras tráfico: ganas posición. Y la logística es una de las palancas de
posición que puedes mover sin pagar un peso de publicidad.**

## Relacionados

`100` tarifas oficiales de envío · `101` modalidades · `102` Flex · `103` Full · `105` cuándo
conviene Full · `104` colecta y puntos · `118` el paquete perdido · `124` auditoría mensual ·
`126` las tres métricas · `63` ganar el catálogo · `55` algoritmo · `75` el cálculo del margen
