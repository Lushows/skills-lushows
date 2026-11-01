# Por qué no sabes tu precio

## La tesis

Casi nadie fija precio. Casi todo el mundo **copia un precio por analogía** — miró tres anuncios de
la competencia, vio 999, puso 999 — y después nunca lo verificó. El precio es la única variable del
negocio que entra directo a la utilidad sin costo adicional, y es la única que nadie mide.

Ver `216` para *cómo* se pone un precio. Este bloque (316-321) es lo otro: **cómo se prueba** el
precio que pusiste, y qué hacer cuando no tienes tráfico para probarlo bien.

## El diagnóstico: contesta esto antes de seguir

| Pregunta | Si la respuesta es "no sé" |
|---|---|
| ¿Por qué tu producto cuesta exactamente eso y no 15% más? | copiaste un precio |
| ¿Qué pasa con tu conversión si subes 10%? | nunca lo probaste |
| ¿Cuánto margen por pedido te deja hoy ese precio? | ver `228`, córrelo hoy |
| ¿Cuál es el precio más alto que un cliente te pagó sin quejarse? | no estás mirando tus datos |
| ¿Cuántos clientes te dijeron "está caro" y cuántos compraron igual? | la queja no es el dato |

Si fallaste 3 de 5, tu precio es una suposición heredada de un competidor que probablemente también
lo copió.

## Los cuatro métodos que existen (2026)

| Método | Qué necesita | Cuándo se usa | Confianza |
|---|---|---|---|
| **A/B de precio** | tráfico alto y simultáneo | tienda con volumen estable | la más alta |
| **Antes y después** (secuencial) | histórico limpio, mercado quieto | poco tráfico, un solo canal | media |
| **Por segmento / cohorte** | segmentos separables (país, canal, dispositivo) | ya tienes varias fuentes | media-alta |
| **Encuesta (Van Westendorp)** | 30-50 respondientes del público real | producto nuevo, cero datos | baja-media, pero es rango |

La elección **no es de gusto**: depende de tu volumen de tráfico y de tu histórico disponible. Quien
te dice "haz A/B" sin preguntarte cuánto tráfico tienes está vendiendo humo. Ver `318`.

## La heurística que ordena los dos métodos grandes

> **Van Westendorp te dice si tu producto debe costar 20 o 200. El A/B te dice si debe costar 199 o
> 225.**

Uno resuelve el orden de magnitud. El otro afina el último 10%. Usarlos al revés es el error caro:
correr un A/B de 999 vs 1.099 cuando el precio correcto del mercado era 1.899 te da un ganador
perfectamente medido dentro de una zona equivocada.

## Qué cuesta equivocarse hacia abajo

Con la economía verificada del proyecto activo (USD, ticket 54,59 ≈ 999 MXN):

| Concepto | Valor |
|---|---|
| Margen sin adquisición | 26,47 |
| CAC | 10,54 |
| Utilidad por pedido | 15,93 |
| Techo de CAC | 30,73 |
| Holgura | 2,92x |
| ROAS de equilibrio | 1,95 |

Bajar el ticket 10% (a ~899 MXN) le quita ~5,46 al margen, porque **el costo no baja contigo**:
el flete de 8,74 y el costo de producto siguen iguales; solo cede la comisión del 5,5%. Utilidad
por pedido: de 15,93 a ~10,77. **Perdiste un tercio de la utilidad por un 10% de precio.**

Y hay un segundo golpe, el que nadie modela: con menos margen, el techo de CAC baja y **te sacan de
la subasta**. Ver `11` y `226`. Un precio bajo no solo te deja menos por venta; te deja menos con
qué competir por esa venta.

| Error hacia abajo | Cómo se ve | Costo real |
|---|---|---|
| "bajé para vender más" | vendes más unidades, ganas menos plata | utilidad total cae |
| "igualé al competidor" | competencia por precio contra quien tiene mejor costo | pierdes tú |
| descuento permanente | el precio tachado deja de significar algo | mata el ancla (`221`) |
| entrar por debajo del múltiplo mínimo | 2,7x México es **veto automático** | no hay negocio |

## Qué cuesta equivocarse hacia arriba

Menos de lo que crees, pero no es gratis.

| Error hacia arriba | Cómo se ve | Costo real |
|---|---|---|
| precio por encima de la promesa | CTR normal, conversión al piso | quemas presupuesto en clics muertos |
| precio alto sin prueba social | carrito abandonado alto | recuperable con contenido, no con descuento |
| precio alto en marketplace | invisible por comparación directa | ver `mercadolibre_lushows` |
| precio alto con envío caro visible | abandono en checkout | mata el ticket, no el precio |

La asimetría importa: **equivocarte hacia arriba es visible y reversible** (bajas el precio mañana).
**Equivocarte hacia abajo es invisible y pegajoso** — vendes, te felicitas, y el negocio no da. Por
eso, ante empate, el operador experimentado prueba primero hacia arriba. Ver `319`.

## La trampa de la analogía con el competidor

Copiar el precio del competidor asume tres cosas que casi nunca son verdad:

| Supuesto oculto | Por qué suele ser falso |
|---|---|
| Su costo es como el tuyo | él puede tener stock local, MOQ grande, agente propio |
| Su CAC es como el tuyo | él lleva 18 meses de píxel entrenado |
| Su oferta es como la tuya | su 999 puede traer 2 unidades + garantía + regalo |

Ese último es el más común: comparas tu precio suelto contra su **bundle**. Ver `218` y `104`.

Referencias observadas en el mercado mexicano (verificar vigencia antes de usarlas como ancla):

| Tienda / oferta | Precio (MXN) |
|---|---|
| `eleveitmx.shop` — núcleo | 549 |
| `eleveitmx.shop` — pack doble | 727 |
| `eleveitmx.shop` — pack triple | 1.000 |
| `eleveitmx.shop` — bundle "Masculinidad Total" | 999 |
| `eleveitmx.shop` — order bump | 49 |
| `eleveitmx.shop` — upsell digital | 359 |
| CV Directo — batería sola → 2 baterías + cubiertos | 999 → 1.599 |
| CV Directo — masajeador solo → con cojín | 1.999 → 2.748 |

Fíjate en el patrón: **nadie vive del precio suelto**. El precio que ves anunciado es la puerta; el
ticket real sube con bump y upsell. Si copias solo la puerta, copiaste la mitad del modelo. Ver `220`.

## El precio relativo

En Shopify y sobre todo en marketplaces, **tu precio relativo importa tanto como el absoluto**. El
cliente no evalúa "999 pesos"; evalúa "999 contra los otros 999 que ya vio esta semana", y en
marketplace el algoritmo lo evalúa por ti y te castiga. Consecuencia práctica: el mismo número puede
ser correcto en tu tienda y suicida en Mercado Libre. Rutea a `mercadolibre_lushows`.

## Qué hacer esta semana

1. Corre `228` con tu precio actual. Si el múltiplo está bajo 2,7x en México, no hay nada que
   probar: **el precio está mal y ya lo sabes**.
2. Decide el método por tu tráfico, no por moda. Ver la tabla de arriba y `318`.
3. Si no tienes datos, arranca por `317` (rango), no por A/B.
4. Antes de tocar el precio del producto suelto, pregúntate si lo que debes mover es el **bundle**
   (`218`) — casi siempre rinde más y se prueba con menos tráfico.

## Frontera

| Necesitas | Skill |
|---|---|
| Estrategia de precio del negocio completo | `economist_lushows` |
| Significancia estadística y verificación de cálculos | `Matematicas_lushows` |
| IVA y facturación del precio | `contador_lushows` |
| Cómo se muestra el precio en la página | `desingweb-lushows` |
| Pruebas dentro de la plataforma de anuncios | `facebook_ads_lushows` |

## Relacionados
`103` · `202` · `216` · `217` · `218` · `220` · `221` · `226` · `228` · `238` · `317` · `318` · `319` · `320` · `321`
