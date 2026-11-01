# 53 — Comercio electrónico, retracto y reversión del pago

Vender por internet, WhatsApp o redes es **venta a distancia**: el cliente no ve ni toca el producto antes de pagar. Por eso la ley le da dos protecciones extra: el **derecho de retracto** (deshacer la compra en un plazo corto) y la **reversión del pago** (pedir al banco que devuelva el dinero en ciertos casos). Además, el vendedor en línea tiene obligaciones de información específicas.

## Conceptos clave (en simple)
- **Venta a distancia / no tradicional:** la que se hace sin presencia física simultánea (internet, teléfono, catálogo, WhatsApp).
- **Comercio electrónico:** realización de actos de comercio por medios electrónicos.
- **Derecho de retracto:** facultad del consumidor de **devolver** el producto y recibir su dinero, **sin necesidad de que tenga defecto**, dentro de un plazo corto.
- **Reversión del pago:** mecanismo para que el emisor del medio de pago (banco, tarjeta) devuelva el dinero al consumidor en casos específicos.
- **Participantes del proceso de pago:** emisor, adquirente, pasarela, proveedor.

## Qué dice la norma (Ley 1480 de 2011 — verificar vigencia)
- **Art. 47 — Retracto:** en ventas que utilizan métodos no tradicionales o a distancia (y en las financiadas por el proveedor), el consumidor puede retractarse dentro de los **cinco (5) días hábiles** siguientes a la entrega del bien o a la celebración del contrato de servicios. El proveedor debe devolver el dinero sin descuentos ni retenciones en un plazo **máximo de treinta (30) días calendario** desde el retracto. El consumidor devuelve el producto en las mismas condiciones y asume los costos de transporte y demás que conlleve la devolución.
  - **Excepciones** (no hay retracto): servicios cuya prestación comenzó con acuerdo del consumidor; productos con precio sujeto a fluctuaciones del mercado financiero; bienes confeccionados según especificaciones del consumidor o claramente personalizados; bienes que por su naturaleza no puedan ser devueltos o puedan deteriorarse o caducar con rapidez; servicios de apuestas y loterías; bienes perecederos; bienes de uso personal.
- **Art. 50 — Comercio electrónico:** obligaciones del proveedor: informar identidad (razón social, NIT, dirección, teléfono, correo), características del producto, precio total con impuestos y costos de envío, medios de pago, plazo de entrega (máximo 30 días calendario salvo pacto), derecho de retracto, resumen del pedido antes de pagar, acuse de recibo, mecanismos de PQR, conservación de la prueba, seguridad de las transacciones, entre otras.
- **Art. 51 — Reversión del pago:** procede cuando hay fraude, operación no solicitada, producto no recibido, o producto que no corresponde a lo solicitado o es defectuoso. El consumidor debe presentar queja al proveedor y solicitar la reversión al emisor dentro de los **cinco (5) días hábiles** siguientes a cuando tuvo noticia de la operación o recibió el producto, y devolver el producto cuando corresponda.
- **Decreto 587 de 2016** (compilado en el Decreto 1074 de 2015): reglamenta la reversión del pago (verificar).

## Retracto en productos de las marcas de Luis (análisis ilustrativo)
| Producto | ¿Aplica retracto? | Razonamiento |
|---|---|---|
| Frasco BIO-SETA sellado | **Probablemente sí** mientras esté sellado | Se puede devolver intacto; si se abrió, se puede discutir la excepción de uso personal o deterioro; definir en la política |
| Calculadora GastroLatam (archivo descargado) | **Discutible** | Un contenido digital ya descargado no "se devuelve" en el mismo estado; se puede alegar la excepción de bienes que por su naturaleza no pueden ser devueltos. Informar claramente **antes** del pago y pedir aceptación expresa. Tema a verificar con doctrina de la SIC |
| Suscripción AVISPA'O ya iniciada | **No**, si la prestación comenzó con acuerdo del consumidor | Informarlo antes de iniciar |

## Checklist de la tienda en línea o el bot de ventas
- [ ] Datos completos del vendedor visibles.
- [ ] Precio total, costos de envío y plazo de entrega antes de pagar.
- [ ] Resumen del pedido y aceptación de T&C (`29`, `107`).
- [ ] Información del retracto (o de por qué no aplica) antes del pago.
- [ ] Acuse de recibo del pedido.
- [ ] Canal de PQR.
- [ ] Procedimiento interno de retracto y reversión con tiempos.

## Modelo de aviso previo al pago (producto digital)
> «Antes de pagar: este producto es un archivo digital que recibirás de inmediato después del pago. Al tratarse de un bien que, una vez entregado, no puede ser devuelto en su estado original, no aplica el derecho de retracto del artículo 47 de la Ley 1480 de 2011. Si el archivo presenta fallas o no corresponde a lo ofrecido, tienes garantía y te lo corregimos, reemplazamos o te devolvemos el dinero. ¿Confirmas que entiendes y aceptas estas condiciones? (Sí/No)»

## Riesgos y errores comunes
- **Alto:** negar el retracto en productos donde sí aplica.
- **Medio:** no informar antes de la compra las excepciones al retracto.
- **Medio:** demorar la devolución más de 30 días calendario.
- **Medio:** ignorar una solicitud de reversión notificada por el banco: se pierde la posibilidad de controvertirla.

## Conexión con otros módulos
- `29` firma y aceptación electrónica · `50` consumidor · `51` garantía · `58` términos web · `107` plantilla T&C ecommerce · `112` ecommerce y marketplaces.
- **mercadolibre_lushows** y **ecommerce_lushows** (reglas de cada plataforma).

## Siguiente paso típico
Insertar en el flujo de pago del bot y de la web el aviso de retracto (o de su excepción) con aceptación expresa y guardar la evidencia.
