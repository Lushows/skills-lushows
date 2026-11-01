# Atribución de dato cero: "¿cómo nos conociste?"

> Vigencia: 15-sep-2026. Esto **no** sustituye al píxel ni a la atribución de plataforma
> (`facebook_ads_lushows`, `200`, `201`). Es la otra mitad del cuadro.

## El problema que resuelve

El píxel y la API de conversiones ven **el último toque rastreable dentro de un navegador**. Todo lo
que pasó antes o fuera del navegador es invisible para ellos:

| Lo que pasó de verdad | Lo que registra el píxel |
|---|---|
| Vio un TikTok orgánico, lo pensó una semana, buscó la marca en Google y compró | "Google / directo" |
| Su prima le dijo "yo lo compré" y le pasó el link por WhatsApp | "Directo" o "referido desconocido" |
| Vio tu anuncio en el celular, compró en la laptop del trabajo | "Directo" |
| Vio 6 anuncios tuyos y uno de retargeting, compró tras el último | "Retargeting" (que se lleva todo el crédito) |

El resultado típico es el mismo en todas las tiendas: **la parte alta del embudo se subestima y el
retargeting se sobrevalora**. Preguntarle al cliente corrige la dirección de ese error.

## Qué te da y qué no

| Sí te da | No te da |
|---|---|
| Qué canales generan demanda que el píxel no ve | Un número exacto de ventas por canal |
| Si un canal que no estás pagando ya te trae gente | Base para auditar la factura de Meta |
| Nombres de canales que no sabías que existían (una influencer, un grupo, una tienda física) | Sustituto de la optimización dentro de la plataforma |
| Cruzado con el pedido: qué canal trae clientes de mayor valor | Causalidad |
| Un dato que sobrevive a bloqueadores, iOS y cookies | Precisión persona a persona |

La frase que debes memorizar: **al agregar cientos de respuestas la distribución es direccionalmente
correcta y muy accionable**, sobre todo para identificar **canales de la parte alta del embudo que
generan demanda real y que el píxel no puede ver**. Direccional. No contable.

## Los sesgos (el cliente miente sin querer)

Ninguno de estos sesgos es mala fe. Son cómo funciona la memoria.

| Sesgo | Qué pasa | Cómo se compensa |
|---|---|---|
| **Confusión de plataformas** | Vio un Reel de Instagram y contesta "TikTok". Para mucha gente todo video vertical es TikTok | No tomes decisiones de presupuesto entre dos plataformas de video basándote solo en esto |
| **Sesgo del último toque humano** | Recuerda a la amiga que le confirmó, no el anuncio que lo sembró | Cruza "Me lo recomendó alguien" con el volumen de tu gasto: si no pagas nada y sube, es real |
| **Sesgo de la primera opción** | La primera opción de la lista se lleva respuestas de más | Rota el orden si la herramienta lo permite |
| **Deseo de agradar** | Contesta lo que cree que quieres oír | Preguntas neutras, sin marcas de ánimo |
| **"Google" como cajón de sastre** | "Google" suele significar "busqué el nombre que ya conocía" | Si Google crece a la par de tu gasto en video, el video es la causa y Google el atajo |
| **Auto-selección** | Solo contesta el que tiene ganas | No compares tasas por segmento como si fueran poblaciones iguales |

## Cómo se agrega

Una hoja, una fila por pedido. Mínimo:

| Campo | De dónde sale |
|---|---|
| ID de pedido | Plataforma |
| Fecha | Plataforma |
| Valor del pedido | Plataforma |
| Canal declarado | Encuesta M1 (`311`) |
| Texto de "Otro" | Encuesta M1 |
| Canal según plataforma (UTM / píxel) | Meta / analytics |

Con eso calculas tres cosas, y solo tres:

| Métrica | Fórmula | Qué decide |
|---|---|---|
| **Participación declarada** | pedidos de canal X ÷ pedidos con respuesta | Dónde nace la demanda |
| **Valor medio por canal declarado** | ingresos de canal X ÷ pedidos de canal X | Qué canal trae mejor cliente |
| **Brecha de atribución** | participación declarada − participación según plataforma | Dónde el píxel está ciego |

La tercera es la que vale oro. Ejemplo de lectura (cifras ilustrativas, no benchmark):

| Canal | Declarado | Plataforma dice | Brecha | Lectura |
|---|---|---|---|---|
| TikTok orgánico | 22% | 3% | **+19 pts** | Está generando demanda y no lo estás alimentando |
| Retargeting Meta | 8% | 27% | **−19 pts** | Se está llevando crédito de otros. No lo mates, pero no escales por su ROAS |
| Recomendación | 15% | 0% | +15 pts | Boca a boca real → refuerza post-venta y programa de referidos |
| Google | 12% | 12% | 0 | Coherente |

**Nunca cierres una campaña solo por la brecha.** La brecha te dice dónde mirar, no qué apagar. La
decisión de apagar vive en la plataforma y en tu techo de CAC (`11`).

## Cuánto volumen hace falta

| Respuestas acumuladas | Qué puedes hacer |
|---|---|
| < 30 | Leer frases literales. **Nada** de porcentajes |
| 30–100 | Detectar canales sorpresa (algo que aparece 8 veces y no estaba en tu mapa) |
| 100–300 | Distribución direccional útil. Primeras decisiones de dónde invertir tiempo orgánico |
| > 300 | Valor por canal y brecha con confianza razonable |

Si necesitas saber si una diferencia entre dos canales es real o ruido, **eso se calcula, no se
opina**: rutear a `Matematicas_lushows`.

## Cómo se cruza con lo que reporta la plataforma

El error clásico es intentar reconciliarlas. No se reconcilian: miden cosas distintas. El
procedimiento correcto es de **decisión por capas**:

| Decisión | Fuente que manda | Fuente de apoyo |
|---|---|---|
| ¿Escalo o bajo este conjunto de anuncios? | Plataforma (CPA, ROAS) | — |
| ¿Cuál creativo gana? | Plataforma | Frases de la encuesta para el siguiente |
| ¿En qué canal nuevo invierto tiempo/dinero? | Encuesta declarada | Plataforma |
| ¿Mi marca ya tiene boca a boca? | Encuesta declarada | Reseñas (`284`) |
| ¿Qué ángulo pruebo en la siguiente tanda? | Encuesta abierta + entrevistas | Biblioteca (`81`) |
| ¿Mi evento de compra está llegando bien? | Plataforma (`200`, `201`) | — |

Herramientas que hacen este cruce por ti: **KnoCommerce** trae modelos de atribución de primer
clic, último clic y personalizado sobre las respuestas; **Fairing** liga cada respuesta al pedido y
al valor de vida del cliente; **Cometly** y **AdsX** cruzan encuesta con datos de campaña. Coste y
funciones cambian seguido: **verificar antes de contratar** (`311`).

## Aplicado al proyecto (México, diciembre 2026)

Contexto: CPM mexicano de Q4 alrededor de **USD 6,75** y CAC objetivo **USD 10,54**, con capital
<USD 500 y ~**5 tests** disponibles. Ahí la atribución declarada tiene un uso muy concreto y uno
falso:

| Uso | Veredicto |
|---|---|
| Decidir si el conjunto de anuncios se apaga | **Falso.** Con ese volumen no vas a tener respuestas suficientes. Manda la plataforma y el techo de CAC (`11`) |
| Detectar que 6 de tus primeros 40 pedidos dicen "me lo recomendó una amiga" | **Real y accionable.** Con bundle de ~999–1.099 MXN y prepago, el boca a boca es tu única palanca gratis |
| Ver que la gente escribe en "Otro" el nombre de una creadora que no conoces | **Oro.** Es un canal de colaboración que no te cuesta CPM |
| Descubrir que dicen "TikTok" y tú solo corres Meta | Señal de que tu creativo vertical funciona fuera de la plataforma donde lo pagas |

En Q4 con CPM alto, cada peso que no gastas descubriendo lo que un cliente te habría dicho gratis es
un peso que le quitas a los 5 tests. Esa es toda la justificación económica de este módulo.

## Errores fatales

| Error | Consecuencia |
|---|---|
| Presentar la distribución declarada como "las ventas reales por canal" | Decisiones de presupuesto sobre un número que no es contable |
| Sumar declarado + plataforma | Doble conteo. Nunca se suman |
| Cambiar las opciones de la encuesta cada mes | Pierdes la serie histórica. Congela la lista al menos un trimestre |
| Ignorar el campo "Otro" porque es texto | Ahí vive el 100% de los hallazgos nuevos |
| Usar esto en vez de arreglar el CAPI | Son cosas distintas. Arregla el evento (`201`) **y** pregunta |

## Relacionados

`310` por qué el cliente sabe lo que la biblioteca no · `311` la encuesta post-compra · `313` entrevistar compradores · `315` del hallazgo al ángulo · `11` el techo de CAC · `200`/`201` píxel y calidad del evento · `81` biblioteca de anuncios · `284` reseñas y reputación · `Matematicas_lushows` significancia · `facebook_ads_lushows` atribución de plataforma
