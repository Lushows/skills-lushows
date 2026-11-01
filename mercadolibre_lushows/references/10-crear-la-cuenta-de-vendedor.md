# Crear la cuenta de vendedor

Abrir la cuenta toma quince minutos, pero tres de las decisiones que tomas ahí te acompañan
durante toda la vida del negocio y algunas no se pueden deshacer. Este módulo separa lo que
puedes cambiar después de lo que te queda amarrado.

## Lo que decides ese día y ya no sueltas

| Decisión | ¿Se puede cambiar después? | Qué se rompe si te equivocas |
|---|---|---|
| Tipo de cuenta (natural / empresa) | Sí, con soportes | Sin empresa no hay Tienda Oficial (`157`) |
| Nombre de vendedor (nickname) | Muy restringido, ver `18` | Es tu marca en cada publicación |
| Correo y celular de la cuenta | Sí | Canal de recuperación: si los pierdes, pierdes acceso |
| Documento e identidad del titular | No, sin trámite | Queda a nombre de quien verificó (`16`) |
| Datos fiscales / RUT | Sí | Afecta facturación y lo que ML te retiene (`12`, `13`) |
| Cuenta de Mercado Pago asociada | Sí | Ahí cae y se libera la plata (`15`) |

**El nombre de vendedor y el tipo de cuenta son las dos piezas caras de cambiar: decídelas
antes de tocar el formulario, no mientras lo llenas.**

## El orden correcto

No abras la cuenta como primer paso. Primero define el negocio, después abre.

```
□ Decide si vendes como persona natural o como empresa → módulo `11`
□ Ten el RUT actualizado con la actividad de comercio al por menor → módulo `12`
□ Ten el nombre de vendedor decidido y libre → módulo `18`
□ Ten el correo corporativo (no el personal de toda la vida) y un celular estable
□ Ten la cédula o el documento del representante legal a la mano → módulo `16`
□ Ten una cuenta bancaria a nombre del MISMO titular de la cuenta ML
□ Solo entonces: registrarte
```

Si la cuenta bancaria está a nombre de otra persona o de otro NIT, el retiro se traba. Es uno
de los bloqueos más frecuentes y más tontos.

## Qué te pide Mercado Libre

El registro es el mismo formulario del comprador: correo, contraseña, nombre, documento,
celular. El "modo vendedor" se activa desde **Mi cuenta → Vender** o al crear tu primera
publicación. No hay una cuenta distinta de vendedor: es la misma cuenta habilitada para vender.

Después, a medida que vendes, ML te va pidiendo capas:

| Momento | Qué te exige | Módulo |
|---|---|---|
| Al registrarte | Correo + celular verificados | — |
| Al publicar | Datos de facturación y dirección | `12` |
| Al vender / al retirar | Verificación de identidad | `16` |
| Al crecer en volumen | Datos fiscales completos, a veces cámara de comercio | `12` |
| Al querer Tienda Oficial | Cuenta empresa + certificado de marca | `18` |

## Correo y celular: no uses los tuyos de siempre

Usa un correo que sea del negocio y al que puedan entrar dos personas si mañana contratas a
alguien. Usa un celular que no vayas a cambiar de plan. Estos dos datos son la llave maestra:
con ellos se recupera la cuenta y con ellos se pierde.

Si algún día vendes el negocio o metes un socio, una cuenta atada a tu Gmail personal de hace
diez años es un problema legal y operativo.

## Una cuenta, una identidad

No abras una segunda cuenta "para probar otra categoría" ni "para el nicho nuevo". La regla de
una sola cuenta por persona o empresa es real y su sanción es dura — ver `17`.

Para probar la API sí existe un mecanismo legítimo y aparte: los **usuarios de test**
(`POST /users/test_user` con `{"site_id":"MCO"}`, hasta 10 por cuenta de desarrollador,
oficial). Eso no viola la regla porque son cuentas de prueba aisladas que solo transaccionan
entre sí. Ver `176` y siguientes.

## El error clásico

Registrarse como persona natural "por ahora, después lo cambio" y descubrir un año después,
con reputación construida y 300 reseñas, que la Tienda Oficial exige cuenta empresa y que
migrar implica soportes, tiempos y riesgo de perder historial. Si ya sabes que vas a formalizar,
**formaliza antes de vender la primera unidad**: la reputación se construye sobre la cuenta,
no sobre ti.

## Datos que no puedes poner en ningún lado

Desde el primer día: nada de teléfono, WhatsApp, correo, Instagram o enlaces externos en la
descripción, en las imágenes ni en las respuestas a preguntas. Las excepciones son Autos y
Motos, Inmuebles, Servicios y MercadoProveedores. El resto de categorías: prohibido, con
eliminación de la publicación y riesgo de sanción si es reiterado. Ver `132` y `138`.

Esto sorprende a todo el que viene de vender por WhatsApp o Instagram: aquí el cliente no es
tuyo hasta que la venta se cierra dentro de la plataforma.

## Antes de publicar el primer producto

```
□ Cuenta creada y correo/celular verificados
□ Identidad verificada (no esperes a que te trabe un retiro)
□ Datos fiscales cargados y coherentes con tu RUT
□ Cuenta bancaria del mismo titular, validada con un retiro de prueba pequeño
□ Nombre de vendedor definitivo
□ Leído el módulo `19` (productos prohibidos) para tu categoría
□ Leído el módulo `20` si vendes alimentos, cosméticos o suplementos
```

El retiro de prueba pequeño vale oro: te dice si el circuito banco↔Mercado Pago funciona antes
de que tengas $3.000.000 represados.

## Cuánto tarda en estar "viva"

La cuenta queda operativa de inmediato, pero el sistema de reputación no te mide hasta que
tengas ventas: mientras tanto apareces en **gris** — "aún no alcanzaste el mínimo de ventas"
(oficial ML Colombia). El gris no es malo, es "sin datos". Ver `125`.

Para MercadoLíder, el requisito de antigüedad es de **más de 4 meses registrado** (oficial ML
Colombia), así que el reloj de la cuenta empieza a correr el día que te registras aunque no
vendas nada. Registrarte temprano tiene ese único beneficio real.

## Relacionados

`11` persona natural vs empresa · `12` datos fiscales y RUT · `16` verificación de identidad ·
`17` una sola cuenta · `18` nombre de vendedor y marca · `19` productos prohibidos ·
`125` reputación · `176` usuarios de test de la API
