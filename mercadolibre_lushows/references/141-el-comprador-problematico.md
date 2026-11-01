# El comprador problemático

La inmensa mayoría de los compradores son normales. Pero existe una minoría que pregunta para
molestar, que extorsiona con la opinión o que reclama sin razón, y como tu reputación depende de
porcentajes chicos, esa minoría puede hacer daño real. Tienes herramientas: úsalas sin culpa.

## Los cuatro tipos y qué hacer con cada uno

| Tipo | Cómo se ve | Herramienta |
|---|---|---|
| **El preguntador tóxico** | Insulta, hace spam, publica el precio de un competidor, pregunta 15 veces | Eliminar la pregunta + bloquear |
| **El extorsionador** | "Si no me devuelves la plata te pongo una estrella" | No cedes. Documentas. Reportas |
| **El que reclama sin razón** | Reclama por algo que no es tuyo: se arrepintió, se equivocó, no leyó | Reglas de exclusión (`136`) |
| **El de mala fe** | Devuelve una caja vacía, alega faltante falso | Evidencia + mediación |

## El preguntador tóxico

Las preguntas son públicas y son tu vitrina (`131`). Una pregunta agresiva o con el precio del
competidor no la tienes que dejar ahí.

```
□ Elimina la pregunta desde tu panel: es tu publicación
□ Si insiste, bloquéalo como preguntador
□ No respondas con sarcasmo: lo leen los siguientes cien compradores
□ Nunca discutas en público, ni aunque tengas toda la razón
```

Bloqueo por API: `DELETE /users/$SELLER_ID/questions_blacklist/$USER_ID` (confianza media). El
bloqueo impide que siga preguntando en tus publicaciones.

Lo que el bloqueo **no** hace: impedirle comprar. Es un filtro de ruido, no un veto.

## El extorsionador de la opinión

Aparece con alguna variante de "dame X o te califico mal". Regla sin excepciones: **no se cede.**

Por qué:

| Si cedes | Consecuencia |
|---|---|
| Le devuelves el dinero por la amenaza | Aprendió que funciona, y probablemente lo repite |
| Le mandas producto gratis | Igual te puede calificar mal |
| Negocias la calificación | **Condicionar una opinión es sancionable** — te expones tú |

Qué sí haces:

```
□ Respondes con la solución que corresponda al problema REAL, si lo hay
□ Dejas la amenaza escrita en el canal: es tu evidencia
□ Reportas la conducta a Mercado Libre
□ Si al final te califica mal, respondes la opinión en público con la versión de los hechos (`142`)
```

Una mala opinión entre veinte buenas no te hunde. Una reputación de vendedor que cede a chantajes,
sí. **La opinión es de él; el precedente es tuyo.**

## El que reclama sin razón

Este es el más frecuente y el que más se maneja mal, porque el vendedor lo toma personal. Casi
siempre cae en una causal oficial de exclusión (oficial ML Colombia, verificado sep-2026):

| Lo que hizo | Causal |
|---|---|
| Se arrepintió | Arrepentimiento con producto en perfecto estado — **no cuenta** |
| Pidió el modelo equivocado | Error del comprador |
| Dice que no llegó y el tracking dice entregado | "Entregado" no reconocido |
| Reclama la demora y tú despachaste a tiempo | Demora del transportador |
| Abrió el reclamo para preguntar algo | Uso del reclamo como medio de contacto |
| Reclamó sin darte 24 h desde tu último mensaje | Reclamo prematuro |

La secuencia correcta, en este orden: **resuelves primero, pides la exclusión después.** El
procedimiento completo está en `136`. Y recuerda el corte: si no respondes en 24 horas hábiles,
pierdes el derecho a excluir aunque el caso fuera clarísimo (`133`).

## El de mala fe

El caso duro: la caja llega vacía, o con una piedra, o el comprador jura que faltaban tres unidades.
Aquí ganas o pierdes con evidencia recolectada **antes** de que pasara.

```
□ Foto del paquete cerrado sobre la báscula, con la guía pegada y la fecha visible
□ Registro del peso despachado (el transportador también lo pesa: coteja)
□ Video del empaque para SKU caros
□ Número de serie registrado por venta, en electrónica
□ Todo el acuerdo escrito en el canal de ML, nunca por fuera (`135`)
```

La foto del paquete en la báscula cuesta cinco segundos por despacho y es lo único que desarma el
"llegó vacío". Si vendes producto caro, hazlo siempre.

## Lo que NO puedes hacer

| Idea | Por qué no |
|---|---|
| Publicar los datos del comprador | Violación de privacidad y de términos |
| Escribirle por fuera de ML | Prohibido y borra tu evidencia (`132`) |
| Responder con grosería en público | Queda para siempre y lo leen los siguientes compradores |
| Negarte a tramitar una devolución | Compra Protegida la garantiza igual (`137`) |
| "Vetar" a un comprador de tus publicaciones | No existe esa herramienta; solo el bloqueo de preguntas |

## El cálculo de cuándo ceder

Cuando el comprador está equivocado pero insiste, la pregunta no es quién tiene razón:

| Camino | Costo |
|---|---|
| Ceder: reponer o reembolsar | El producto + el envío |
| Aguantar hasta mediación | El producto (probablemente igual) + reclamo + **mediación** |

Con 120 ventas en 60 días, **una sola mediación te saca de MercadoLíder** (`129`). Si tu producto
vale menos que eso, ceder es la decisión económica, no la débil.

Dónde no cedes nunca: chantaje explícito, y casos claramente excluibles donde la exclusión te
protege igual.

## El error clásico

Tratar al 2% problemático con la misma energía que al 98% normal. El vendedor que se obsesiona con
el cliente imposible deja de contestar a los otros cuarenta que iban a comprar. **El comprador
problemático no te quita plata por lo que reclama: te la quita por la atención que le regalas.**

Ponle un límite de tiempo a cada caso difícil: dos intercambios y decides —cedes, excluyes o dejas
que vaya a mediación con la evidencia lista— y vuelves a vender.

## Protocolo de 60 segundos

```
□ ¿Es una pregunta tóxica?        → eliminar y bloquear. Fin
□ ¿Hay un problema real?          → resolver hoy, con fecha (`135`)
□ ¿El caso es excluible?          → resolver Y pedir exclusión (`136`)
□ ¿Es chantaje?                   → no ceder, documentar, reportar
□ ¿Es mala fe con evidencia tuya? → presentar evidencia, aguantar
□ ¿Es mala fe sin evidencia tuya? → ceder y empezar a fotografiar los despachos
```

## Relacionados

`131` las preguntas como canal de venta · `133` el tiempo de respuesta · `135` reclamo y mediación ·
`136` reglas de exclusión · `137` compra protegida · `138` devoluciones · `142` opiniones negativas
`129` MercadoLíder · `144` plan de defensa de la cuenta
