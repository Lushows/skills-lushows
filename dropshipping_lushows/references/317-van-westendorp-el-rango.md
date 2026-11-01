# Van Westendorp: el rango

## Para qué sirve (y para qué no)

El **Medidor de Sensibilidad al Precio de Van Westendorp (1976)** no te da un precio. Te da un
**rango aceptable** y dos fronteras: dónde te vuelves sospechosamente barato y dónde te vuelves
imposible de comprar.

> Van Westendorp te dice si tu producto debe costar 20 o 200. El A/B te dice si debe costar 199 o
> 225. Ver `316`, `318`.

Úsalo cuando **no tienes datos**: producto nuevo, mercado nuevo, cero historial de ventas. Es el
único método de los cuatro que funciona con tráfico igual a cero.

## Las 4 preguntas exactas (español mexicano)

Se hacen **en este orden**, después de mostrar el producto exactamente como lo verá el cliente
(foto, promesa, lo que incluye). Si preguntas sin mostrar la oferta, mides fantasía.

| # | Pregunta | Nombre de la curva |
|---|---|---|
| 1 | *¿A qué precio te parecería **tan barato** que dudarías de la calidad?* | Muy barato |
| 2 | *¿A qué precio te parecería **una ganga**, buen producto por buen precio?* | Barato |
| 3 | *¿A qué precio **empezaría a parecerte caro**, pero aún lo considerarías?* | Caro |
| 4 | *¿A qué precio te parecería **demasiado caro** como para comprarlo?* | Muy caro |

Redacción que sí funciona en México, palabra por palabra:

1. "¿A qué precio este producto te parecería tan barato que pensarías que es de mala calidad?"
2. "¿A qué precio dirías que es una ganga — buena calidad por ese precio?"
3. "¿A qué precio empezarías a decir 'está caro', pero todavía lo pensarías?"
4. "¿A qué precio dirías 'no, eso ya es un robo' y no lo comprarías?"

Reglas de aplicación:

| Regla | Por qué |
|---|---|
| Campo abierto, sin opciones sugeridas | cualquier lista ancla la respuesta |
| Pesos mexicanos, sin decimales | "999" no "999.00" |
| Una sola oferta por encuesta | mezclar suelto y bundle contamina todo |
| Sin mencionar el precio que tú pensabas | es el error #1 |
| Público REAL, no amigos | tus amigos te dan precios de cortesía, siempre altos |

## Cómo se tabula

Ordena las respuestas de menor a mayor y construye **porcentajes acumulados**:

| Curva | Se acumula | Sentido |
|---|---|---|
| Muy barato | descendente (% que diría "tan barato que desconfío" a ese precio o menos) | baja |
| Barato | descendente | baja |
| Caro | ascendente (% que diría "caro" a ese precio o más) | sube |
| Muy caro | ascendente | sube |

## Cómo se leen los cuatro cruces

| Cruce | Se llama | Qué significa |
|---|---|---|
| Muy barato × Caro | **PMB** — punto de bajo costo marginal | por debajo, pierdes por verte barato |
| Barato × Muy caro | **PMC** — punto de alto costo marginal | por encima, pierdes clientes rápido |
| Barato × Caro | **PIO** — punto de indiferencia | precio "normal" percibido del mercado |
| Muy barato × Muy caro | **POP** — precio óptimo | menos rechazo total |

**Rango aceptable = entre PMB y PMC.** Ese es el entregable. Todo lo demás es adorno.

Lectura de operador, no de manual:

| Lo que ves | Qué te está diciendo |
|---|---|
| Rango angosto (PMC ÷ PMB < 1,5) | mercado con precio muy establecido; poco margen para jugar |
| Rango ancho (PMC ÷ PMB > 2,5) | no hay referencia clara; puedes posicionar alto con promesa fuerte |
| PIO cerca del PMB | el mercado te ve como commodity; necesitas bundle (`218`) |
| POP por debajo de tu costo × 2,7 | **veto**: no hay negocio en México a ese nivel. Ver `316` |

## Cuántas respuestas hacen falta

| Respondientes | Qué puedes decir |
|---|---|
| < 15 | nada. Es anécdota con gráfica |
| 15-29 | orden de magnitud, con pinzas. Sirve para descartar, no para elegir |
| **30-50** | **mínimo operativo**: define el rango, con error visible |
| 100-200 | rango confiable, permite cortar por segmento |
| > 300 | lujo; en dropshipping rara vez lo tendrás y no lo necesitas |

Con capital bajo (< USD 500, ver el proyecto activo), **30-50 es tu objetivo realista**, y se
consigue sin pagar panel: comentarios de un anuncio, grupos de Facebook del nicho, encuesta corta
por WhatsApp a lista propia, o un formulario después del landing sin compra. Verificar siempre de
dónde salió cada respuesta — una encuesta mezclada entre público real y conocidos no sirve.

## Cómo interpretar un Van Westendorp chico (20-40 respuestas)

No leas los cruces al peso. Lee **la mediana de cada pregunta**:

| Estadístico | Uso |
|---|---|
| Mediana de "demasiado caro" | techo duro. No pruebes por encima |
| Mediana de "empieza a parecer caro" | tu **candidato alto** para probar |
| Mediana de "ganga" | tu **candidato bajo** — y probablemente ya estás ahí |
| Mediana de "tan barato que desconfío" | piso absoluto. Nunca bajes de ahí |

Con muestra chica, la mediana es más estable que el cruce de curvas, porque el cruce depende de las
colas y las colas con 30 datos son basura. Para calcular intervalos de confianza de esas medianas,
rutea a `Matematicas_lushows`.

## Los límites (dilos en voz alta)

| Límite | Consecuencia práctica |
|---|---|
| Mide **intención declarada**, no compra | la gente miente hacia abajo cuando la pregunta suena a "te van a cobrar" |
| No mide volumen | te da rango, no cuántos venderías a cada precio |
| No conoce tu oferta real | sin bump ni upsell, subestima el ticket final (`220`) |
| Sesgo de muestra | si preguntas donde hay cazadores de ofertas, te da precios de cazador |
| Asume producto entendido | si el respondiente no entendió qué hace, el número es ruido |
| No sustituye margen | un rango bonito por debajo de 2,7x sigue siendo un no. Ver `216` |

El más grave es el primero: **Van Westendorp casi siempre da un rango más bajo que el precio que
realmente pagará el mercado**, porque responder es gratis y comprar no. Trátalo como suelo del
rango, no como veredicto. El veredicto lo da la venta.

## Aplicación al proyecto activo (México, diciembre 2026)

Bundle candidato 999-1.099 MXN, capital < USD 500, prepago, stock local.

| Paso | Acción |
|---|---|
| 1 | Arma el mock del **bundle completo**, no del producto suelto |
| 2 | Consigue 30-50 respuestas del público objetivo real, sin conocidos |
| 3 | Saca las 4 medianas y el rango PMB-PMC |
| 4 | Cruza con `321`: si el rango completo queda bajo el múltiplo 2,7x → mata el producto |
| 5 | Si el rango cubre 999-1.099, ya no necesitas más encuesta: pasa a prueba secuencial (`318`) |
| 6 | Si el rango sugiere 1.400+, no lo creas de inmediato: pruébalo con dinero real, no con encuesta |

Cuidado con el Buen Fin: una encuesta corrida en plena temporada de descuentos te devuelve un rango
deprimido. Corre la encuesta fuera de la semana de ofertas o descuéntalo en la lectura. Ver `238`.

## Frontera

| Necesitas | Skill |
|---|---|
| Medianas, intervalos y tamaño de muestra exacto | `Matematicas_lushows` |
| Estrategia de precio del negocio | `economist_lushows` |
| Diseño del formulario / landing de encuesta | `desingweb-lushows` |

## Relacionados
`103` · `104` · `216` · `217` · `218` · `220` · `238` · `316` · `318` · `319` · `320` · `321`
