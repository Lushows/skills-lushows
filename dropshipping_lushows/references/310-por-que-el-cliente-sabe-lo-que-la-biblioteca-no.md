# Por qué el cliente sabe lo que la biblioteca no

> Vigencia: 15-sep-2026. Tesis del bloque 11.

## El agujero que este bloque tapa

Esta skill te enseñó a espiar: biblioteca de anuncios (`81`), antigüedad de creativos (`83`),
landings de competencia (`102`), comentarios de anuncios ajenos (`95`). Todo eso es **inteligencia de
oferta**: lo que YA está dicho en el mercado.

Lo que faltaba es la otra mitad: **inteligencia de demanda**. Lo que el comprador piensa, con sus
palabras, antes de que nadie lo haya convertido en anuncio. Ahí viven los ángulos que nadie corre.

La diferencia práctica, sin romanticismo:

| | Biblioteca de anuncios | Voz del cliente |
|---|---|---|
| Qué te da | Lo que la competencia **ya dice** | Lo que el comprador **siente y todavía nadie dice** |
| Origen del dato | Terceros (anunciantes) | Primera persona (el que pagó) |
| Sesgo dominante | Supervivencia: solo ves lo que sobrevivió | Memoria y cortesía: el cliente te quiere bien |
| Coste de obtenerlo | Tiempo (gratis) | Tiempo + una app (USD 0–50/mes típico, verificar) |
| Velocidad | Inmediata, hoy mismo | Necesitas ventas primero |
| Riesgo si te quedas solo con esto | Clonas y compites por CPM | Te enamoras de 3 anécdotas |

## La regla: la biblioteca acota, el cliente diferencia

Traducido a decisiones:

- **Antes de la primera venta** → biblioteca. No tienes clientes; no inventes que los tienes.
- **Desde la primera venta** → empiezas a capturar voz del cliente. Cada pedido sin encuesta es un
  dato que se pierde para siempre.
- **A partir de ~30–50 respuestas** → ya puedes leer patrones de vocabulario (no de atribución;
  eso pide más volumen, ver `312`).

Con **~5 tests creativos disponibles** en el arranque de este proyecto (capital <USD 500), la
matemática es brutal: si de esos 5 ángulos 2 salen de "lo que se me ocurrió", quemaste el 40% del
presupuesto de aprendizaje en corazonadas. Un ángulo que salió de la boca de un comprador entra al
test con probabilidad de acierto más alta porque **ya le funcionó a alguien real**.

## Los dos tipos de información

| Eje | Dato de terceros (espionaje) | Dato de parte cero (zero-party) |
|---|---|---|
| Definición | Lo que observas sin permiso ni intención del otro | Lo que el cliente te entrega **a propósito** |
| Ejemplos | Anuncios activos, landings, reseñas de Amazon | Encuesta post-compra, entrevista, respuesta de WhatsApp |
| Fiabilidad | Alta en lo que dice, nula en por qué funcionó | Alta en el porqué, imperfecta en los hechos |
| Uso correcto | Definir el campo de juego y el precio | Definir el ángulo, el hook y las objeciones |
| Uso incorrecto | Copiar el creativo | Tratarlo como métrica exacta de atribución |

Hay un tercer tipo que la gente confunde con este bloque: el **dato de la plataforma** (píxel, CAPI,
atribución dentro de Meta). Eso no es tuyo, es de Meta, y vive en `facebook_ads_lushows`, más
`200`/`201` para calidad de evento. Aquí no se toca. Ver la frontera abajo.

## Por qué el píxel no ve lo que el cliente sí ve

El píxel registra **el último toque rastreable dentro de un navegador**. No registra:

- El TikTok orgánico que la clienta vio hace tres semanas en el celular de su hermana.
- El grupo de Facebook donde alguien dijo "yo compré esto y sí me sirvió".
- La recomendación de la estilista del barrio.
- El anuncio que vio en el feed y buscó en Google dos días después.

Esos canales de la **parte alta del embudo generan demanda real que el píxel no puede ver**. Cuando
agregas cientos de respuestas de "¿cómo nos conociste?", la distribución resultante es
**direccionalmente correcta y muy accionable** — no sirve para auditar centavos, sirve para saber
dónde está naciendo la demanda. Todo el detalle operativo en `312`.

## Qué produce cada fuente, en concreto

| Necesito… | Fuente correcta | Módulo |
|---|---|---|
| Saber qué precio soporta el mercado mexicano | Landings de competencia | `103` |
| Saber cuánto tiempo lleva vivo un ángulo | Biblioteca, antigüedad | `83` |
| Saber **con qué palabra** el cliente nombra su problema | Encuesta abierta + entrevista | `311`, `313` |
| Saber por qué casi no compra | Reseñas de 3 estrellas + entrevista | `314`, `313` |
| Saber qué canal me está trayendo gente sin que yo lo sepa | "¿Cómo nos conociste?" | `312` |
| Convertir un hallazgo en hook | El puente | `315` |
| Saber qué dolor mueve al nicho | Mapa de dolores | `212`, `213` |

## Aplicado al proyecto (suplementos y belleza, México, diciembre 2026)

Kit capilar anticaída y gomitas de vitalidad tienen un problema específico: **no puedes hacer claims
terapéuticos** (COFEPRIS y política de Meta). Eso significa que no puedes vender el efecto
fisiológico, así que tienes que vender **identidad, hábito y percepción**. Y la identidad no la
inventas tú: la dice el cliente.

Las marcas mexicanas que llevan ~552 días activas usan vocabulario de identidad: "complementa tu
dieta", "boost", "actitud", "complemento para tu estilo de vida". Eso lo sacaste de la biblioteca —
es el **piso legal y el tono aceptado**. Lo que la biblioteca no te da es la frase que tu clienta usa
cuando le cuenta a su amiga por qué lo compró. Esa frase es tu diferencia.

Ejemplo de la brecha:

| Lo que la biblioteca te muestra | Lo que una compradora podría decirte |
|---|---|
| "Complementa tu dieta con biotina" | "Me daba pena juntar el pelo del cepillo" |
| "Boost diario de vitalidad" | "Llego a las 4 de la tarde y ya no le sirvo a nadie" |

La segunda columna no es más "bonita": es más **específica y no está corriendo en ningún anuncio**.
Ahí está el ángulo. Verificar siempre que la frase elegida no cruce a claim terapéutico antes de
ponerla en un creativo (`07`).

## Errores que vas a cometer (y el antídoto)

| Error | Por qué duele | Antídoto |
|---|---|---|
| Esperar a "tener volumen" para preguntar | Los primeros 50 clientes son los que más te enseñan y los que más recuerdan | Encuesta activa desde el pedido #1 |
| Preguntar y no leer | La app acumula respuestas que nadie abre | Revisión fija: viernes, 20 min |
| Cambiar la oferta por 2 comentarios | n=2 no es un patrón | Mínimo de 5 menciones independientes antes de mover algo |
| Poner 6 preguntas en el checkout | Se desploma la tasa de respuesta | 1 pregunta en la gracias, el resto por correo (`311`) |
| Usar la encuesta para auditar el ROAS | No es contabilidad | Dirección, no decimales (`312`) |
| Editar la frase del cliente para que "suene profesional" | Matas lo único valioso: su naturalidad | Copiar literal, corregir solo ortografía |

## Cadencia mínima del bloque

| Frecuencia | Qué haces | Módulo |
|---|---|---|
| Siempre activo | Encuesta post-compra de 1 pregunta | `311` |
| Semanal (20 min) | Leer respuestas nuevas, pegar frases literales al swipe file (`99`) | `311`, `314` |
| Cada 30–50 pedidos | Leer la distribución de "¿cómo nos conociste?" | `312` |
| Una vez al mes | 2–3 entrevistas de 15 min con compradores recientes | `313` |
| Antes de cada tanda de creativos | Convertir hallazgos en ángulos | `315`, `250` |

## Frontera

- **`facebook_ads_lushows`** → píxel, CAPI, atribución dentro de la plataforma. Aquí solo se cubre
  la atribución que viene **de la boca del cliente**.
- **`ventas_lushows`** → la conversación de venta en sí.
- **`economist_lushows`** → investigación de mercado macro, tamaño, TAM.
- **`Matematicas_lushows`** → si necesitas saber si una diferencia es significativa, ahí se resuelve.
- **`mercadolibre_lushows`** → preguntas y reseñas dentro de Mercado Libre.

## Relacionados

`311` encuesta post-compra · `312` atribución de dato cero · `313` entrevistar compradores · `314` minería de reseñas · `315` del hallazgo al ángulo · `95` comentarios de un anuncio · `250` ángulos de venta · `212`/`213` dolor y mapa de dolores · `185` prueba social · `99` swipe file · `284` reseñas y reputación
