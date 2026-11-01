# El bot de preguntas con IA

Un bot que responde las preguntas de tus publicaciones con un modelo de lenguaje. Es la
automatización de mayor retorno visible: quien pregunta está a un paso de comprar y a las pocas
horas ya compró en otra parte. También es la que más rápido te mete en problemas si le dejas
hacer lo que no debe.

## La arquitectura

```
  COMPRADOR pregunta en tu publicacion
         |
         v
  ML dispara webhook  topic: questions
         |
         v
  TU RECEPTOR  --> encola --> responde HTTP 200   (menos de 500 ms) (`191`)
         |
         v
  WORKER
    1. GET /questions/search?item_id=$ITEM_ID&api_version=4   (o el resource del aviso)
    2. GET /items/$ITEM_ID  -> titulo, atributos, precio, stock
    3. Arma el contexto: ficha + politicas + tono
    4. Llama al LLM
    5. CLASIFICA: responder o escalar
    6. Si responde: POST /answers { question_id, text }
    7. Si escala: avisa a un humano y NO responde
    8. Marca procesada por question_id (`192`)
```

El `GET` del ítem en el paso 2 no es opcional: **el bot no puede inventar el dato, tiene que
leerlo.** Un bot que responde de memoria sobre el stock es un bot que promete lo que no hay.

## Qué le das al modelo como contexto

| Pieza | De dónde sale |
|---|---|
| Título, atributos y descripción del producto | `GET /items/$ITEM_ID` (`181`, `182`) |
| Precio y stock actuales | El mismo ítem (`183`) |
| Tiempo y modalidad de envío | La publicación y `186` |
| Preguntas ya respondidas de ese ítem | `GET /questions/search` — tu mejor material |
| Tus políticas: garantía, devoluciones, plazos | Un texto tuyo, fijo |
| Las reglas prohibidas | Un texto tuyo, fijo, no negociable |

Las preguntas ya respondidas del mismo producto son oro: son el lenguaje real de tus compradores.

## Las reglas que el bot NUNCA puede romper

Esto no es estilo, es riesgo de cuenta. Va en el prompt **y además como filtro en el código**,
porque un prompt se puede desobedecer y un filtro no.

| Prohibido | Por qué |
|---|---|
| Dar teléfono, WhatsApp, correo o redes | Prohibido en preguntas y respuestas (`132`, `187`) |
| Invitar a comprar fuera de Mercado Libre | Sacar al comprador de la plataforma |
| Prometer stock, plazo o precio que no leyó de la API | Termina en cancelación o reclamo (`139`) |
| Decir "tipo", "símil", "igual a" sobre una marca ajena | Riesgo de denuncia y suspensión (`29`) |
| Afirmar compatibilidad que no está en los atributos | Reclamo no excluible (`135`) |
| Negociar precio o dar descuentos | Decisión de negocio, no de bot |
| Responder dos veces la misma pregunta | Solo se responde una vez y no hay edición (`187`) |

Las excepciones de contacto (**Autos y Motos, Inmuebles, Servicios, MercadoProveedores**) no
aplican si no vendes ahí. Asume prohibido.

**Un bot que suelta un número de teléfono no comete un error: comete la misma infracción en
cincuenta publicaciones al mismo tiempo.**

## El filtro de salida obligatorio

Antes de que el texto llegue a `POST /answers`:

```
□ Ningun patron de telefono, correo, @usuario ni URL externa
□ Ninguna de las palabras vetadas de marca ("tipo", "simil", "igual a")
□ Longitud razonable, sin listas largas ni formato raro
□ Si el texto afirma stock o plazo, que coincida con lo que leyo la API
□ Si no pasa el filtro -> NO se envia: se escala
```

Si el filtro bloquea, el default es escalar, nunca "mandar algo parecido".

## Qué responde y qué escala

| Tipo de pregunta | Bot | Por qué |
|---|---|---|
| ¿Tienen disponible? ¿Qué tallas/colores? | Sí | Dato leído de la API |
| Medidas, material, peso, contenido de la caja | Sí | Está en los atributos |
| ¿Cuánto tarda a mi ciudad? ¿Envío gratis? | Sí | Dato del sistema |
| ¿Es original? ¿Tiene garantía? | Sí, con texto fijo | Respuesta de política, no improvisada |
| Compatibilidad simple listada en atributos | Sí | Verificable |
| "¿Me lo dejas en...?", descuentos, combos | **Escala** | Es negocio |
| Compatibilidad técnica no listada | **Escala** | Afirmar de más produce reclamos |
| Problema con una compra ya hecha | **Escala** | Va por posventa (`188`) |
| Pide contacto o quiere comprar por fuera | Respuesta fija que no da contacto | Riesgo de cuenta |
| Pregunta ambigua, larga o con varias cosas | **Escala** | El modelo adivina y se equivoca |
| Tono agresivo o insulto | **Escala** | Un humano decide, o se bloquea (`187`) |

**El bot contesta lo verificable. Todo lo que implique una promesa nueva, lo decide una persona.**

## Los tres modos de operación

| Modo | Cómo funciona | Cuándo |
|---|---|---|
| **Sugerencia** | El bot redacta, tú das enviar | Las primeras semanas. Siempre |
| **Automático con lista blanca** | Envía solo los tipos ya validados | Tras semanas de acierto |
| Automático total | Envía todo | No |

Empieza en sugerencia. Mide cuántas habrías enviado tal cual. Cuando pase del 90% en un tipo de
pregunta, pasa ese tipo a automático — y solo ese.

## El tono

Que el bot sea correcto no lo hace vendedor. Una respuesta que vende responde, agrega el dato que
faltaba y cierra, porque **la lee todo el que entra a la publicación después**, no solo quien
preguntó. Cómo se escribe eso es de `ventas_lushows`: pídele los guiones y mételos como ejemplos
en el prompt.

## La frontera

La construcción del software —cola, workers, dónde corre el modelo, cómo guardas los tokens, cómo
proteges el endpoint, qué proveedor de IA usas— es de `engineer_visualopen_lushows`. Este módulo
define qué endpoints llamar, qué contexto darle y qué tiene prohibido decir.

## Qué medir

```
□ Preguntas respondidas por el bot vs escaladas
□ Tiempo desde que entra la pregunta hasta que sale la respuesta
□ Cuantas respuestas del bot tuviste que corregir despues
□ Conversion de las publicaciones con bot vs sin bot
□ Cuantas veces se activo el filtro de salida (si es cero, sospecha del filtro)
```

## El error clásico

Soltar el bot en automático desde el día uno porque en las pruebas contestó bien diez preguntas.
Las diez fáciles. La número once es "¿sirve para mi Renault 2014?", el modelo dice que sí para ser
amable, el comprador compra, no le sirve, y eso es **producto distinto al anunciado**: reclamo **no
excluible** que sí pega en el termómetro (`135`).

**Cada respuesta del bot es una promesa contractual de tu negocio. Trátala así.**

## Relacionados

`29` lo prohibido en el título · `132` prohibido dar contacto · `135` reclamos excluibles ·
`139` riesgo de cuenta · `181` publicar por API · `187` las preguntas · `188` posventa ·
`190` topics y payload · `191` responder en 500 ms · `192` duplicados · `194` usuarios de prueba
