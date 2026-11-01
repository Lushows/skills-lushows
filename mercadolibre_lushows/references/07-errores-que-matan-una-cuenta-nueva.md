# Errores que matan una cuenta nueva

Los del primer mes no son errores de optimización: son errores que cuestan la cuenta. Una venta
perdida se recupera; una cuenta suspendida a veces no. Esta es la lista, con la consecuencia real
y el módulo que la desarrolla.

## La tabla de los fatales

| Error | Consecuencia | Módulo |
|---|---|---|
| **Publicar sin la ficha completa** | El algoritmo te etiqueta en 48-72 h como baja conversión y cuesta muchísimo revertirlo. Además la ficha incompleta es causa citada de pausas y revisiones | `31`, `59`, `60` |
| **Cancelar por falta de stock** | Cuenta como venta cancelada. El límite oficial para seguir verde es **2,5% a 60 días** (4% a 365), y superar el 2,5% puede suspender la cuenta para vender | `139`, `140` |
| **Dejar caer el termómetro a naranja** | **Pierdes el 50% de descuento en envíos**: 1 kg de un producto de más de $60.000 pasa de $8.200 a **$16.400** por venta (oficial ML Colombia, sep-2026) | `09`, `125` |
| **Dar el WhatsApp o el correo en una pregunta** | Prohibido en descripción, imágenes y preguntas. Se elimina la publicación o la pregunta, con riesgo de sanción si es reiterado | `132` |
| **Copiar fotos o usar marca ajena** | El titular denuncia, la publicación **se pausa**; con infracciones reiteradas ML deshabilita la cuenta **y las cuentas asociadas**, de forma permanente | `21`, `29` |
| **Prometer un despacho que no cumples** | "Envíos incorrectos" es una de las tres variables base del termómetro. Y arrastra reclamos NO excluibles | `112`, `113` |
| **Abrir varias cuentas** | Las cuentas asociadas caen juntas cuando una infringe. No es un plan B: es duplicar el riesgo | `17` |
| **Quedarte sin stock** | Te saca de la competencia y de la puja de catálogo. Al reponer, la publicación "revive como más nueva o menos confiable" y reconstruye señales desde cero | `61`, `140` |
| **No responder en 24 horas hábiles** | **Pierdes el derecho a pedir la exclusión del reclamo** de tu reputación (oficial ML Colombia, sep-2026) | `133`, `136` |
| **Publicar en categoría regulada sin permisos** | Retiro de la publicación y riesgo legal fuera de ML (INVIMA y otros) | `19`, `20` |
| **Poner un precio sin calcular la comisión** | La comisión oficial va de **8% a 22%**: con la de arriba, un producto barato pierde plata en cada venta. Vendes meses por debajo del costo mientras el dinero entra a Mercado Pago y parece que funciona | `09`, `75`, `82` |
| **Precio tachado inventado** | La SIC vigila los "descuentos falsos": el precio final debe corresponder al promocional, sin costos ocultos | `92` |
| **Pautar antes de convertir** | Pagas por visitas que confirman al algoritmo que no vendes. La penalización por reputación baja **ningún gasto en publicidad la compensa** | `154`, `150` |

## Los tres que más cuentan suspenden

### 1. Cancelar porque no tenías el producto

Definición oficial de venta cancelada: **"el comprador recibe su dinero de vuelta antes de que hayas
entregado el producto"**, sin importar quién la pidió. Y solo te penaliza **si cancelas tú**; si
cancela el comprador, no te afecta (oficial ML Colombia, sep-2026).

Los límites oficiales de canceladas para mantenerte en verde: **2,5% medido a 60 días**, **4% medido
a 365 días**, **1,5% si eres MercadoLíder**. Superar el 2,5% además pone la cuenta en riesgo de
suspensión para vender.

Haz la cuenta de lo que eso significa siendo nuevo:

| Ventas que llevas | Cancelaciones para cruzar el 2,5% |
|---|---|
| 40 | 1 |
| 80 | 2 |
| 200 | 5 |

Con 40 ventas, **una sola cancelación** te pone en zona de riesgo. Por eso la regla operativa es
declarar menos stock del que tienes, no más (`45`).

Hay una salida cuando el problema aparece: si el comprador abre un reclamo **pidiendo cancelación**,
ese reclamo **no afecta la reputación desde el inicio** y tienes **2 días hábiles** para reembolsar
sin haber entregado. Si cumples, la reputación queda intacta; si no, el reembolso se hace automático
y **sí** te afecta (oficial ML Colombia, sep-2026).

### 2. Marcas y fotos ajenas

El **Programa de Protección de Marcas** funciona así: el titular denuncia → la publicación se pausa
→ tú puedes responder con evidencia → el titular evalúa. Si no respondes, se elimina. Con
infracciones reiteradas se deshabilita la cuenta y **las cuentas asociadas** de forma permanente
(fuente especializada, sep-2026).

La regla del lenguaje en el título es simple y no tiene matices:

| Permitido | Prohibido |
|---|---|
| "**para** iPhone 14" | "tipo iPhone" |
| "**compatible con** Samsung Galaxy" | "símil", "igual a", "idéntico a" |

Y las fotos: si no la tomaste tú y no tienes autorización, no es tuya. Los falsificados son la
categoría con más publicaciones eliminadas en México, Argentina, Brasil y Uruguay (fuente
especializada, sep-2026).

Cualquier usuario puede denunciarte con el botón **"Denunciar"** de la esquina inferior derecha de
tu ficha. Tu competencia también.

### 3. Varias cuentas

La intuición es "abro otra por si acaso". La realidad es que ML asocia cuentas y, cuando una
infringe de forma reiterada, **caen las asociadas**. Además dividir el historial es dividir la
reputación: dos cuentas en gris valen menos que una verde, y el termómetro premia el volumen
concentrado (`127`). Ver `17`.

## El error clásico del primer mes

Publicar rápido "para ir probando". Mercado Libre no tiene modo borrador con tráfico: la publicación
empieza a ser evaluada desde la hora 0.

| Momento | Qué hace el algoritmo | Qué debes tener listo |
|---|---|---|
| Hora 0 | Te da visitas de prueba | Ficha completa, fotos, precio final |
| Hora 48 | Mide tu conversión | Nada que cambiar: ya está midiendo |
| Día 7 | Fija tu posición base | Primeras ventas y opiniones |

Ventana de 48-72 h y ~100 primeras visitas: fuente especializada, sep-2026.

**Es más barato demorarte un día que quemar la publicación.**

## Checklist antes de publicar la primera vez

```
□ Categoría verificada con el predictor, no elegida a ojo                        (27)
□ Todos los atributos con tags.required llenos                                   (32)
□ Título con producto, marca, modelo y características; sin signos de puntuación  (28, 29)
   (el límite de 60 caracteres es de la API, no una regla publicada en la ayuda)
□ Sin "tipo", "símil" ni "igual a": para marcas ajenas solo se usa "para"          (29)
□ Sin color en el título si hay variantes, sin "nuevo/usado", sin promociones      (29)
□ Foto principal: fondo blanco puro #FFFFFF creado digitalmente, 1200×1200 px     (35)
□ Foto 1 solo con el producto: sin empaque, sin texto, sin accesorios no incluidos (37)
□ Cero datos de contacto en descripción, imágenes y respuestas                    (132)
□ Precio calculado con scripts/margen_ml.py y comisión leída del simulador        (82)
□ Stock declarado por debajo del real                                             (45)
□ Tiempo de despacho que cumples el peor día                                      (112)
□ Garantía que puedas sostener                                                    (50)
□ ¿Categoría regulada? permisos en mano antes de publicar                         (19, 20)
```

## Lo que NO es un error fatal (deja de preocuparte)

| Preocupación común | La verdad |
|---|---|
| "Me devolvieron un producto" | **Las devoluciones NO son cancelaciones** y no pesan igual (oficial, sep-2026). `138` |
| "El comprador canceló" | Si cancela él, no te afecta (oficial, sep-2026) |
| "Me pausaron la publicación" | "Inactiva para revisar" suele ser temporal y se reactiva al corregir. `73` |
| "Tengo una opinión negativa" | Duele en conversión, no suspende la cuenta. `142` |
| "Mi termómetro está gris" | Es falta de ventas, no un castigo. `06` |

## Relacionados

`04` diagnóstico inicial · `06` ciclo de vida del vendedor nuevo · `17` una sola cuenta ·
`19` productos prohibidos · `21` propiedad intelectual · `29` lo que el título tiene prohibido ·
`45` cuánto stock declarar · `59` las primeras 72 horas · `61` stock cero ·
`73` pausas e infracciones · `74` cómo apelar · `92` el precio tachado y la SIC ·
`112` el tiempo de despacho · `132` lo que no puedes decir · `136` reglas de exclusión de reclamos ·
`139` la cancelación y su castigo · `143` suspensión de cuenta · `144` el plan de defensa
