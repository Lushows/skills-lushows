# Cuándo abrir otro país

Mercado Libre se ve igual en Bogotá y en Ciudad de México, y por eso el error es tan común: el
vendedor asume que abrir MLM o MLA es duplicar lo que ya funciona. No lo es. Cada sitio es un
marketplace distinto, con reglas, comisiones, logística, competencia y reputación propias. **Lo
único que viaja contigo es lo que aprendiste.**

## Los sitios y sus códigos

| País | Site ID | Nota |
|---|---|---|
| Colombia | `MCO` | Tu casa |
| Argentina | `MLA` | El mercado más maduro y donde nació la empresa |
| México | `MLM` | El de mayor crecimiento de la región |
| Chile | `MLC` | Ticket alto, mercado pequeño |
| Perú | `MPE` | El más cercano en tamaño y hábitos a Colombia |
| Brasil | `MLB` | Otro idioma, otra escala, otro régimen tributario |

(ALTA, verificado sep-2026). El `site_id` no es un detalle técnico: todas las llamadas de la API,
los precios de publicación y las categorías cuelgan de él (`178`).

## Lo que NO se copia y pega

| Cosa | Por qué no viaja |
|---|---|
| **La reputación** | Es por cuenta y por sitio. Arrancas en gris, con periodo de evaluación de **365 días** hasta llegar a 60 ventas (oficial, verificado sep-2026) |
| **Las comisiones** | Cambian por país y categoría. La de Colombia ni siquiera está publicada de forma confiable (`76`) |
| **Categorías y atributos** | El árbol es distinto por sitio: `GET /sites/$SITE/categories` devuelve otra cosa |
| **Los títulos** | Cambia el vocabulario: "tenis" en Colombia y México, "zapatillas" en Argentina y Chile. El buscador es literal (`55`) |
| **Los precios** | Otra moneda, otro poder adquisitivo, otro competidor local |
| **La logística** | Full existe con reglas, tarifas y centros propios por país |
| **Las devoluciones** | México eliminó la devolución gratis por arrepentimiento en electrónica y cómputo, con cargo de ~150-300 MXN. **Colombia no** (MEDIA, sep-2026) |
| **Lo fiscal** | Régimen, retenciones, factura, aduana. Nada se parece |
| **La competencia** | El SKU que en Colombia tiene 4 competidores en México puede tener 300 con Full |

## Las siete condiciones antes de abrir

No es una lista de deseos: si falla una sola, no abras.

```
□ 1. Reputación VERDE estable en MCO durante 3 meses seguidos (`125`)
□ 2. Margen positivo por SKU SIN pauta, conocido y medido (`165`)
□ 3. El negocio en Colombia camina sin ti operando a diario (`169`)
□ 4. Caja para financiar 6 meses del país nuevo sin tocar la caja de Colombia
□ 5. Una solución logística real en destino: bodega, importador o Full local
□ 6. Alguien (tú o una persona) que responda EN HORARIO de ese país (`133`)
□ 7. Un producto que gana por algo más que precio — si ganas solo por precio, el local te gana
```

La condición 3 es la que más se salta y la que más cuesta: abrir un segundo país mientras aún
empacas tus propias cajas garantiza que se dañen los dos.

## El orden correcto de expansión

**Antes de otro país, agota el tuyo.** La secuencia con mejor retorno por peso invertido:

| Paso | Qué es | Por qué antes que otro país |
|---|---|---|
| 1 | Más SKUs en la categoría que ya dominas | Cero costo de aprendizaje |
| 2 | Full y velocidad de entrega (`105`) | Sube posición y catálogo en el mercado que ya conoces |
| 3 | Mercado Ads con ACOS controlado (`150`) | Compra tráfico dentro del canal que ya convierte |
| 4 | Tienda Oficial y marca (`157`) | Exige marca registrada, y esa marca después te sirve afuera |
| 5 | Segundo canal propio (`170`) | Mismo país, mismo cliente, mismo inventario |
| 6 | **Otro país** | Último, porque reinicia reputación, logística y aprendizaje |

Un peso invertido en subir la conversión de tus 10 SKUs actuales en MCO rinde más que el mismo peso
puesto en abrir MPE desde cero. Casi siempre.

## Si aun así vas a abrir: por dónde

| Candidato | A favor | En contra |
|---|---|---|
| **Perú (MPE)** | Idioma, hábitos y tamaño más parecidos; cercanía; menos saturado | Mercado pequeño: el techo llega rápido |
| **Chile (MLC)** | Ticket alto, comprador con poder adquisitivo | Mercado chico, logística de importación cara |
| **México (MLM)** | El mercado grande de la región | Competencia brutal, muchos con Full; el más caro para entrar |
| **Argentina (MLA)** | Mercado maduro, comprador acostumbrado | Volatilidad cambiaria y restricciones: riesgo macro que no controlas |
| **Brasil (MLB)** | El más grande | Portugués, régimen tributario propio, otra liga operativa |

> ⚠️ **Sin verificar para Colombia (sep-2026).** No hay datos oficiales de ML sobre facilidad de
> entrada de un vendedor colombiano a cada sitio. Esta tabla es criterio de mercado, no política de
> Mercado Libre. Antes de decidir, confirma en el panel de cada sitio si tu tipo de cuenta puede
> vender desde el exterior y con qué logística.

## El programa de exportación

Mercado Libre tiene esquemas para que un vendedor publique en otro sitio sin constituir empresa
allá, con la logística resuelta por ellos.

> ⚠️ **Sin verificar para Colombia (sep-2026).** No se pudo confirmar qué programa de exportación
> está abierto a vendedores colombianos en 2026, ni sus requisitos, comisiones ni países destino.
> Las páginas `vendedores.mercadolibre.com.co` devuelven 403 a lectura automatizada. Míralo estando
> logueado en tu panel, en la sección de exportación o "vender en otros países", antes de planear
> nada sobre este supuesto.

## La cuenta: una por país

Lo que sí es seguro es cómo se estructura. Cada sitio es una cuenta con su propia reputación, su
propio Mercado Pago y su propia evaluación. Y aquí hay un riesgo de cuenta que casi nadie ve venir:
en el Programa de Protección de Marcas, las infracciones reiteradas deshabilitan la cuenta **y las
cuentas asociadas** de forma permanente (MEDIA-ALTA, verificado sep-2026).

**Traducción: un problema serio en el país nuevo puede arrastrarte la cuenta de Colombia.** No es
diversificación de riesgo; en ese frente es concentración. Léelo junto con `143` y `17` antes de
abrir nada.

## Lo técnico, si automatizas

| Detalle | Qué cambia |
|---|---|
| `site_id` | Cada llamada: categorías, `listing_prices`, predictor de categoría |
| Categorías y atributos | Hay que volver a correr `domain_discovery/search` → `categories/$ID/attributes` |
| Moneda | `currency_id` distinto por sitio |
| Mensajería | Migración anunciada desde el 2-feb-2026 en MLB y MLC: `to.user_id` apunta al "Agente" del país. **No verificado para MCO** |
| Tokens | Un OAuth por cuenta. No comparten `access_token` (`176`) |

Si el plan es multi-país por API, diseña desde el día uno con el `site_id` como parámetro, nunca
quemado en el código (`195`).

## El error clásico

Abrir México porque "es diez veces más grande". Sí lo es —y también tiene diez veces más
competidores, muchos con Full, con reputación de años y con costo de última milla local que tú no
tienes. El vendedor colombiano entra, publica a precio de Colombia más flete, no vende, y
abandona la cuenta con inventario en una bodega ajena. **El tamaño del mercado no es tuyo: lo que
es tuyo es la porción que puedes servir mejor que el vendedor local.**

## Relacionados

`05` los sitios de Mercado Libre en LatAm · `17` cuentas múltiples y cuentas asociadas ·
`55` cómo funciona el buscador · `76` las comisiones y cómo verificarlas · `105` Full ·
`120` logística internacional y exportación · `125` el termómetro · `127` el periodo de evaluación ·
`133` el tiempo de respuesta · `143` suspensión de cuenta · `150` ACOS sano ·
`157` Brand Ads y Tienda Oficial · `165` las métricas que de verdad miras ·
`169` de vendedor solo a equipo · `170` ML y tienda propia · `176` OAuth ·
`178` el site_id y la API · `195` diseñar la integración
