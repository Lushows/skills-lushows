# La segunda compra: cómo se provoca

> La primera compra la compraste con dinero de Meta. La segunda dice si tienes un negocio o solo una
> máquina de convertir presupuesto publicitario en pedidos. **Es la única métrica de este bloque que
> vale la pena perseguir con obsesión**, porque después de la segunda todo se vuelve más fácil.

## Por qué la segunda vale tanto

| | 1ª compra | 2ª compra |
|---|---|---|
| Costo de adquisición | USD 10,54 | **0** |
| Margen que deja | 15,93 | **26,47** |
| Margen acumulado del cliente | 15,93 | **42,39 (2,66x)** |
| Probabilidad de una tercera | baja | **mucho más alta** |

El salto de 1 a 2 compras sube el valor del cliente 166%. Ningún cambio de creativo, de página o de
precio te da eso. Ver `300`.

Y el efecto compuesto: quien compra dos veces tiene una probabilidad sustancialmente mayor de
comprar una tercera que quien compró una de comprar una segunda. **La segunda compra no es un pedido
más: es el filtro que separa a los clientes de los compradores.**

## La ventana crítica

| Tipo de producto | Ventana donde ocurre la 2ª compra | Cuándo escribir |
|---|---|---|
| Consumible de 30 días | días 21-40 | **día 18-22** |
| Consumible de 60 días | días 45-80 | día 40-48 |
| Consumible de 90 días | días 70-120 | día 65-75 |
| Complementario (otro SKU del catálogo) | días 7-30 | día 10 y día 25 |
| Sin consumible | no hay ventana natural | forzarla con oferta rara vez funciona |

**Escribe ANTES de que se le acabe, nunca después.** Si escribes el día 35 de un producto de 30
días, el cliente ya lleva 5 días sin producto, ya rompió el hábito y probablemente ya buscó otra
marca. El cálculo fino de la fecha está en `308`.

Dato de contexto: la curva de retención cae más entre el mes 1 y el mes 2 que en cualquier otro
tramo (`301`). Todo lo que hagas concentrado en esa ventana rinde más que lo mismo hecho en el mes 5.

## El canal, en orden de efectividad real

| Canal | Cuándo usarlo | Nota |
|---|---|---|
| **WhatsApp** | el disparo principal en LatAm | lee casi todo el mundo; ojo con la ventana de 24 h de la API oficial y con las plantillas aprobadas |
| **Email** | secuencia completa, con contenido | barato, escalable, no depende de plantilla aprobada |
| SMS | respaldo en México | caro por mensaje, alto alcance |
| Retargeting pago | solo para los que no abren nada | vuelves a pagarle a Meta por un cliente que ya es tuyo |
| Inserto en la caja | QR con descuento para la reposición | costo casi cero, funciona sorprendentemente bien |

Orden de prioridad: **canal propio primero, pago último.** Si terminas retargeteando a tus propios
clientes, estás pagando dos veces por la misma persona. Ver `272` y `286`.

## La secuencia, para un consumible de 30 días

| Día | Canal | Contenido | Objetivo |
|---|---|---|---|
| 0 | email | confirmación + qué esperar | expectativa |
| 2-4 | WhatsApp | "ya salió tu pedido" + guía de uso | reducir devoluciones |
| 7 | email | **cómo usarlo bien** (no vende nada) | que el producto funcione de verdad |
| 14 | WhatsApp | "¿cómo te está yendo?" — pregunta abierta | detectar problemas + reseña (`285`) |
| **20** | email | **la oferta de reposición** | la venta |
| 25 | WhatsApp | recordatorio corto con link directo | la venta |
| 32 | email | "¿se te acabó?" + última oferta | rescate |
| 45 | — | pasa a dormidos (`306`) | — |

La pieza del día 7 es la que la mayoría se salta y la que más afecta el resultado: **un cliente que
usó mal el producto no va a recomprarlo**, por buena que sea tu oferta del día 20. La recompra se
gana en la experiencia, se cobra en el mensaje.

## Qué oferta poner (en orden de preferencia)

| Oferta | Cuándo | Riesgo |
|---|---|---|
| **Pack doble / triple con ahorro** | siempre primero | ninguno; sube ticket y te compra 2-3 meses de tranquilidad |
| Envío gratis en la reposición | segunda opción | come margen pero no toca el precio percibido |
| Producto complementario del catálogo | si tienes catálogo coherente | sube el ticket y ancla al cliente a la marca |
| Descuento 10-15% por reposición | tercera opción | acostumbra al cliente a esperar descuento |
| Descuento 25%+ | casi nunca | te vuelves su precio de referencia para siempre |

El modelo de `eleveitmx.shop` vale como referencia: núcleo 549 MXN, pack doble 727, pack triple
1.000. El pack triple contra tres unidades sueltas (1.647) es −39%, pero cobra 1.000 hoy. **Prefiere
siempre vender más cantidad antes que bajar el precio unitario**: el descuento sobre una unidad
regala margen; el pack multiplica el pedido.

## Qué hacer para que la segunda compra sea fácil

| Acción | Impacto |
|---|---|
| Link de recompra en 1 clic, con el producto ya en el carrito | el mayor de todos |
| Guardar dirección y datos del cliente | quita 6 campos de fricción |
| No obligar a crear cuenta | la cuenta es tu comodidad, no la suya |
| Mencionar el nombre del producto exacto, no "tu pedido" | especificidad vende |
| Fecha concreta: "se te acaba alrededor del 12 de octubre" | convierte mucho más que "ya es hora de reponer" |

## Qué NO hacer

| Error | Consecuencia |
|---|---|
| Mandar la oferta de recompra el día 2 | todavía no probó el producto; quema la confianza |
| Vender otro producto antes de que el primero funcione | parece que solo quieres su tarjeta |
| Descuento agresivo desde el primer recordatorio | el cliente aprende a esperar y nunca paga precio lleno |
| Usar el mismo copy del anuncio de adquisición | ya te compró; hablarle como a un desconocido lo insulta |
| No medir por cohorte | no vas a saber si funcionó (`302`) |
| Claims terapéuticos en los mensajes de recompra | en MX, COFEPRIS; **el riesgo no baja porque sea un correo privado** |

## Cómo medir si funciona

| Métrica | Cómo | Meta inicial |
|---|---|---|
| Tasa de 2ª compra a 90 días, por cohorte | `302` | **≥20%** antes de escalar |
| Mediana de días entre compra 1 y 2 | export de pedidos | calibra `308` |
| Contribución del canal propio a los ingresos | pedidos con origen email/WhatsApp ÷ total | ≥15% a los 6 meses |
| Ticket de la 2ª vs la 1ª | | si la 2ª es menor, tu oferta de recompra está descontando de más |

Prueba una cosa a la vez: cambia el día del disparo, o la oferta, o el canal — nunca los tres.
Con volúmenes chicos (30-80 clientes por cohorte) no vas a tener significancia; usa el resultado como
señal, no como prueba, y consulta `Matematicas_lushows` si vas a declarar un ganador.

## Aplicación al proyecto México

| Qué | Decisión |
|---|---|
| Captura de WhatsApp y correo | obligatoria en el checkout desde el primer pedido de octubre |
| Disparo principal | WhatsApp día 20-22, email día 20 |
| Oferta | **pack doble**, nunca descuento de entrada |
| Inserto en caja | QR de reposición, costo ~0 |
| Meta para decidir suscripción (2027) | 2ª compra ≥20% a 90 días (`303`) |

## Relacionados
`272` · `285` · `286` · `300` · `301` · `302` · `303` · `306` · `307` · `308` · `309`
