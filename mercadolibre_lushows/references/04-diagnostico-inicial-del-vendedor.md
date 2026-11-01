# Diagnóstico inicial del vendedor

Antes de recomendar nada hay que saber siete cosas. Sin ellas cualquier consejo es adivinanza: la
misma pregunta tiene respuestas opuestas según el color del termómetro y el país. Se pregunta
**una a la vez**, en lenguaje simple, y no se avanza sin respuesta.

## Las siete preguntas, en orden

El orden no es casual: cada una puede cambiar o cancelar las siguientes.

```
1. ¿En qué país vas a vender? (o ¿en cuál ya vendes?)
2. ¿Ya tienes cuenta de vendedor? ¿Es a nombre tuyo o de una empresa?
3. ¿De qué color está tu termómetro de reputación? (si dice gris o no lo has visto, dilo)
4. ¿Cuántas ventas llevas, más o menos, en los últimos 60 días?
5. ¿Qué vendes y a qué precio lo publicas? ¿Cuánto te cuesta a ti?
6. ¿Usas Full, Flex, o despachas tú?
7. ¿Tienes marca registrada?
```

No las hagas en bloque. Una pregunta, una respuesta, y usa la respuesta para ajustar la siguiente.
Si el usuario dice "no sé" en la 3 o la 4, mándalo a mirar el panel antes de seguir: son las dos que
más cambian el plan.

## Pregunta 1 — País (sitio)

Todo cambia con el país: comisiones, tarifas, reglas, catálogo habilitado, calendario comercial.
**Un consejo con cifras de otro sitio es peor que no dar consejo** (`02`).

| Respuesta | Sitio | Qué haces |
|---|---|---|
| Colombia | `MCO` | El default de esta skill |
| Argentina, México, Chile, Perú, Brasil | `MLA`, `MLM`, `MLC`, `MPE`, `MLB` | Avisa que esta skill está calibrada a Colombia y que toda cifra hay que releerla en su sitio. `05` |
| "Quiero vender en varios" | — | Primero uno solo funcionando. `171` |

## Pregunta 2 — Tipo de cuenta

| Respuesta | A dónde va |
|---|---|
| No tengo cuenta | `10` crear la cuenta · `11` persona natural vs empresa · `12` datos fiscales y RUT |
| Persona natural | `11` para saber si ya le conviene pasar a empresa · `13` retenciones |
| Empresa | Habilitado para Tienda Oficial si tiene marca (pregunta 7) · `158` |
| Tengo dos o más cuentas | 🚨 Bandera roja. Ver `17` y `07`: las cuentas asociadas caen juntas |

## Pregunta 3 — El color del termómetro

**Esta pregunta cambia la respuesta más que ninguna otra.** Es la primera bifurcación real.

| Color | Estado | Qué se hace |
|---|---|---|
| **Gris** | Aún no alcanza el mínimo: **no hay reputación hasta las primeras 10 ventas** | No hay nada que arreglar: hay que vender. `06` |
| **Verde / verde claro** | Sano | Se puede optimizar, competir en catálogo y pautar |
| **Amarillo** | Aviso | Se corrige la causa antes de invertir un peso en pauta. `128` |
| **Naranja / rojo** | Emergencia | **No se optimiza, se rescata.** `144`, `128` |

La escala va de rojo (la más baja) a verde (la más alta), más gris. **No tienes reputación hasta
completar tus primeras 10 ventas** (oficial ML Colombia, verificado sep-2026). En la categoría
**Inmuebles** las ventas no afectan la reputación.

Los umbrales oficiales **para mantenerte en verde** (oficial ML Colombia, sep-2026):

| Variable | Medido a 60 días | Medido a 365 días | Si eres MercadoLíder |
|---|---|---|---|
| Ventas con reclamos | no superar **3,5%** | **3,5%** | **2,5%** |
| Envíos incorrectos | no superar **12%** | **15,5%** | **10%** |
| Canceladas por ti | no cancelar más del **2,5%** | **4%** | **1,5%** |

No cuentan los reclamos por arrepentimiento del comprador ni las ventas canceladas **por quien te
compró** (oficial, sep-2026).

> ⚠️ **Sin verificar (sep-2026):** los cortes exactos de **amarillo, naranja y rojo**. Solo está
> publicado el corte a verde. No cites porcentajes para esos tres colores: trabaja con el color que
> el usuario ve en su panel.

Por qué el corte es tan duro en naranja y rojo:

- **Pierdes el 50% de descuento en envíos.** Un paquete de 1 kg de un producto de más de $60.000
  pasa de **$8.200 a $16.400** (oficial, sep-2026). Son $8.200 menos de utilidad en cada venta
  (`09`).
- **Puedes participar en el catálogo pero no puedes ganar** la oferta principal (fuente
  especializada, sep-2026). Tu mejor precio no sirve de nada.
- Activa penalizaciones de posicionamiento que **ningún gasto en publicidad compensa**. Pautar ahí
  es tirar la plata (`154`).

## Pregunta 4 — Número de ventas

No es curiosidad: define el periodo con el que ML te evalúa.

| Ventas concretadas | Periodo de evaluación | Consecuencia |
|---|---|---|
| Menos de 60 | Últimos **365 días** | Un error de hace 8 meses te sigue pesando. Recuperarse es lento |
| **60 o más** | Últimos **60 días** | El pasado caduca rápido: 60 días limpios te limpian |
| 120+ y $10M COP facturados | 60 días | Puerta de MercadoLíder si además llevas +4 meses y estás verde. `129` |

Oficial ML Colombia, verificado sep-2026. Este umbral de 60 ventas es la mejor noticia que le puedes
dar a alguien con reputación golpeada y volumen: **su historial se renueva solo**. A quien vende
poco hay que decirle la verdad contraria: le va a tomar meses.

## Pregunta 5 — Qué vende, a qué precio, a qué costo

Aquí se decide si el negocio existe. Con precio y costo en la mano:

```
□ Ejecuta scripts/margen_ml.py con la comisión que el usuario lea del simulador oficial
  python scripts/margen_ml.py margen --precio X --costo Y --comision Z --iva 19
□ Si no tiene la comisión, NO la inventes. El rango oficial es 8%-22%; el dato exacto de la
  categoría está tras login en mercadolibre.com.co/landing/costos-de-venta o el simulador.
  La API listing_prices ya NO es pública: responde 403 y exige token
□ Ubica su peso y su rango de precio en la tabla oficial de envíos                       (78)
□ Revisa si está cerca de los $60.000: cruzar ese umbral casi duplica el envío           (79, 09)
□ Si el margen tras comisión + envío + IVA es negativo o mínimo → el problema NO es la publicación
```

| Señal en la respuesta | A dónde va |
|---|---|
| Ticket muy bajo | `86` por qué los productos baratos pierden · `87` subir el ticket con kits |
| "No sé cuánto me queda" | `75` estructura de costos · `82` la calculadora |
| "Lo compro en China / busco qué vender" | Eso es `dropshipping_lushows`. Aquí solo si **aguanta la comisión** |
| Producto voluminoso o pesado | `109` peso volumétrico · `116` productos grandes |
| Categoría regulada (alimentos, cosmética, salud) | `19`, `20` antes de publicar |

## Pregunta 6 — Logística

| Respuesta | Implicación |
|---|---|
| Full | 50% de descuento en envíos y entrega al día siguiente. Requiere reputación activa (10 ventas) y hay **disponibilidad de espacio**; el traslado lo pagas tú. Revisa el cargo por stock antiguo. `103`, `108` |
| Flex | Buena para ciudad propia y entrega el mismo día. `102` |
| Despacho yo / logística propia | Revisar el tiempo de despacho prometido: es de las causas frecuentes de "envíos incorrectos". `112`, `122` |
| "No sé qué es eso" | `100` cómo funciona Mercado Envíos, de cero |

## Pregunta 7 — Marca registrada

Una sola consecuencia, pero grande:

| Respuesta | Qué se abre / se cierra |
|---|---|
| Sí, registrada y vigente | Tienda Oficial (subiendo el certificado, cuenta empresa) y Brand Ads. `158`, `157` |
| No | **No hay atajo.** Sin marca registrada no hay Tienda Oficial. Se trabaja con Mi Página. `159` |
| Vendo marcas de otros | `21` propiedad intelectual · `29` cómo nombrar marcas ajenas sin que te denuncien |

## Tabla maestra: si responde X → ve a Y

| Respuesta | Módulo de entrada |
|---|---|
| "Quiero empezar, no tengo nada" | `06`, luego `10`-`12` |
| "Ya publiqué y no vendo nada" | `54` auditoría en 15 min, luego `58` |
| "Vendía y me caí de golpe" | `72` por qué cayó mi publicación |
| "Me pausaron la publicación" | `73`, luego `74` cómo apelar |
| "Me suspendieron la cuenta" | `143`, luego `144` |
| "Termómetro naranja o rojo" | `128`, `144`. **Nada de pauta ni de catálogo** |
| "Vendo pero no me queda plata" | `75`, `82`, `83` |
| "Quiero pautar" | Primero `150` (ACOS contra margen), después `146` |
| "Quiero ganar el catálogo" | `63`, y antes `66` si no está verde |
| "Quiero automatizar / conectar mi sistema" | `175`, y revisa `198` antes de programar |
| "Quiero abrir México / Argentina" | `171`, y `05` para entender que las reglas cambian |

## El error clásico

Aconsejar sin preguntar. El 80% de las respuestas que circulan sobre Mercado Libre asumen un
vendedor verde, en Argentina, con volumen. Aplicadas a una cuenta nueva colombiana en gris, o a una
naranja en rescate, hacen daño: mandan a pautar a quien no puede convertir, o a pelear catálogo a
quien tiene prohibido ganarlo.

**Con termómetro naranja o rojo no se optimiza: se rescata. Cualquier otra conversación se aplaza.**

## Relacionados

`02` los cuatro motores y la trampa de los datos · `03` glosario · `05` los sitios de LatAm ·
`06` ciclo de vida del vendedor nuevo · `07` errores que matan una cuenta nueva ·
`54` auditoría de una publicación en 15 minutos · `72` por qué cayó mi publicación ·
`82` la calculadora de margen · `125` el termómetro · `128` cómo se recupera una caída ·
`129` MercadoLíder · `144` el plan de defensa de la cuenta · `150` el ACOS sano según tu margen ·
`158` Tienda Oficial
