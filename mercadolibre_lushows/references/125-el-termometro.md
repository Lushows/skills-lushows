# El termómetro de reputación

El termómetro es el semáforo público de tu cuenta: lo ve el comprador antes de pagarte, lo lee el
algoritmo antes de decidir dónde te muestra, y —esto es lo que casi nadie sabe— **decide cuánto
pagas de envío en cada venta**. No es un adorno de perfil: es una línea de tu estado de resultados.

## Los colores

Son 5 colores más un estado gris (oficial ML Colombia, verificado sep-2026).

| Color | Qué significa | Qué te pasa en la práctica |
|---|---|---|
| ⬜ Gris | **No tienes reputación hasta completar tus primeras 10 ventas** | Sin color visible — pero con el 50% de descuento en envíos igual |
| 🟥 Rojo | La más baja de la escala | Penalización fuerte de posicionamiento · **0% de descuento en envíos** |
| 🟧 Naranja | Desempeño malo | Penalización · no puedes ganar catálogo · **0% de descuento en envíos** |
| 🟨 Amarillo | Desempeño regular | Zona de alerta · **40% de descuento en envíos** en vez de 50% |
| 🟩 Verde claro | Buen desempeño | Es el color que otorga el Programa de Despegue (`128`) |
| 🟩 Verde | La más alta de la escala | Todo habilitado · **50% de descuento en envíos** · puerta a MercadoLíder (`129`) |

## Los umbrales oficiales para ser verde

Publicados en `vendedores.mercadolibre.com.co` (oficial ML Colombia, verificado sep-2026):

| Variable | Medido a 60 días | Medido a 365 días | Si eres MercadoLíder |
|---|---|---|---|
| **Ventas con reclamos** | no superar **3,5%** | no superar **3,5%** | no superar **2,5%** |
| **Envíos incorrectos** | no superar **12%** | no superar **15,5%** | no superar **10%** |
| **Canceladas por ti** | no más del **2,5%** | no más del **4%** | no más del **1,5%** |

Esa es la vara. Cumples las tres → verde. Cuál de las dos columnas te aplica depende de tu volumen
de ventas, no de tu antigüedad (`127`).

Excepciones oficiales que **no cuentan** contra ti:

```
□ Reclamos por arrepentimiento del comprador
□ Ventas canceladas POR LA PERSONA QUE TE COMPRÓ (solo pesan las que cancelas tú)
□ La categoría Inmuebles: las ventas que recibas ahí no afectan tu reputación
```

## ⚠️ Lo único que ML sigue sin publicar

> ⚠️ **Sin verificar (sep-2026).** Solo está publicado el **corte a verde**. Los cortes exactos de
> **amarillo, naranja y rojo** no aparecen en ninguna página oficial. Los blogs que te dan tablas
> completas de los cinco colores se las inventan o las copian de otro país. Si incumples los
> umbrales de arriba sabes que **no eres verde**; a qué color exacto caes, solo lo dice tu panel.

## El argumento que convierte esto en un tema de plata

Mercado Libre aplica un descuento sobre el costo de envío según tu reputación, en productos nuevos
desde $60.000 (oficial ML Colombia, verificado sep-2026):

| Reputación | Descuento en envíos |
|---|---|
| MercadoLíder, verde, **o sin reputación** | **50%** |
| Amarilla | **40%** |
| Naranja o roja | **Ninguno** |
| Con Envíos Full | 50% |

Y en pesos, para un paquete de 0,5 a 1 kg de un producto de más de $60.000:

| Reputación | Costo del envío | Diferencia contra el verde |
|---|---|---|
| Verde / MercadoLíder / sin reputación | **$8.200** | — |
| Amarilla (1 a 2 kg, muestra oficial) | $10.200 | +$2.000 |
| Naranja o roja | **$16.400** | **+$8.200 por venta** |

**Perder el verde no es perder una medallita: es pagar $8.200 más de envío en cada venta.** Con 200
ventas al mes son $1.640.000 mensuales que se evaporan sin que cambie nada en tu operación.

Fíjate en el detalle más raro de la tabla: un vendedor **sin reputación** tiene el mismo 50% que un
verde. El sistema no castiga no tenerla — castiga **perderla**.

## Qué mide el termómetro

Tres variables base (oficial ML Colombia, verificado sep-2026), más una cuarta que entra solo cuando
aspiras a MercadoLíder:

```
□ Reclamos
□ Ventas canceladas por ti
□ Envíos incorrectos    — despacho con demora o desde el depósito incorrecto
□ Mediaciones           — solo para MercadoLíder (`129`)
```

El detalle de cada una está en `126`. La ventana de tiempo está en `127`.

## Por qué importa más que cualquier otra cosa

| Consecuencia | Detalle |
|---|---|
| Costo de envío | Duplica con naranja o roja (tabla de arriba) |
| Posicionamiento orgánico | La reputación es uno de los pilares del ranking (`55`) |
| Catálogo | Naranja o roja puede participar pero **no puede ganar** la oferta principal (`63`) |
| Publicidad | La penalización no se compensa gastando en Ads (`145`) |
| Conversión | El comprador ve el color antes de pagar |
| Full | Requiere tener reputación: se activa a las 10 primeras ventas (`105`) |
| Continuidad | Pasado cierto punto, la cuenta se suspende (`139`, `143`) |

## El error clásico

Mirar el color en vez de mirar los porcentajes. El color es un resultado retrasado: cuando cambia,
el daño lleva semanas acumulándose. Los tres porcentajes sí se mueven en tiempo real y los tienes en
el panel. Rutina semanal en `144`.

## Qué hacer según tu color

| Estás en | Prioridad número uno |
|---|---|
| Gris | Llegar a 10 ventas. Ahí nace el termómetro y se habilita Full |
| Verde | Defender: cada punto perdido cuesta plata en envíos (`144`) |
| Verde claro | Identificar cuál de las tres variables te frena y cerrarla |
| Amarillo | Ya estás pagando 10 puntos más de envío. Para de escalar y arregla la causa |
| Naranja / Rojo | Emergencia: sin descuento de envío y sin catálogo. Protocolo de `144` |

## Dónde se lee

| Vía | Cómo |
|---|---|
| Panel | Mi cuenta → Reputación |
| API | `GET /users/$USER_ID` → `seller_reputation`: `level_id`, `power_seller_status`, `transactions`, `metrics.claims` / `delayed_handling_time` / `cancellations` |

El `level_id` viene con forma `1_red`, `2_orange`, `3_yellow`, `4_light_green`, `5_green`. Si
automatizas una alarma de reputación, esa es la llave (`195`).

## Relacionados

`126` las tres métricas · `127` el periodo de evaluación · `128` cómo se recupera una caída ·
`129` MercadoLíder · `130` beneficios reales · `139` la cancelación y su castigo ·
`143` suspensión de cuenta · `144` plan de defensa de la cuenta · `118` costos de envío ·
`55` el algoritmo · `63` ganar el catálogo
