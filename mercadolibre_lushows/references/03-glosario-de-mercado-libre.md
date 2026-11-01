# Glosario de Mercado Libre

El vocabulario mínimo para que el resto de la skill se entienda. Está en orden alfabético para que
lo consultes suelto. Si un término tiene módulo propio, ahí está el número.

## Tabla alfabética

| Término | Qué es |
|---|---|
| **ACOS** | *Advertising Cost of Sale*. Inversión en publicidad ÷ ingresos generados por esa publicidad × 100. Ejemplo oficial: invierto $100, genero $1.000 → ACOS 10%. `149` |
| **Atributo** | Cada campo de la ficha técnica (marca, modelo, color, talla, material). Los obligatorios dependen de la categoría; en la API vienen con `tags.required: true`. `31`, `32` |
| **Buy box** | El nombre genérico del lugar donde cae el botón "Comprar" cuando varios venden lo mismo. En Mercado Libre se llama **ganar el catálogo**. `63` |
| **Cargo fijo** | Monto en pesos que algunos sitios cobran por vender productos de bajo valor, además de la comisión. **En Colombia NO existe** (oficial ML Colombia, verificado sep-2026): lo que hay es un **precio mínimo de publicación de $2.900**. El cargo fijo con umbral de $33.000 es de Argentina. `77`, `02` |
| **Clásica** | Nombre **viejo** del tipo de publicación de duración indefinida sin cuotas sin interés. El sitio colombiano ya no lo usa: hoy habla de **Gratuita**, publicaciones **con cuotas con 0% interés** y **cuotas extra**. Sigue vigente en otros países. `42`, `43` |
| **Cuotas extra** | Ofrecer más cuotas con 0% interés de las que trae tu rango de precio. Cuesta exactamente **+3 puntos porcentuales** de comisión (oficial ML Colombia, sep-2026). `43`, `80` |
| **Colecta** | Modalidad de Mercado Envíos en la que un transportador pasa a recoger los paquetes a tu bodega. `104` |
| **Compra Protegida** | Garantía de ML al comprador: si no llega, cubre hasta **21 días** desde la compra; si se arrepiente o hay problema, hasta **30 días** desde que lo recibió (oficial ML Colombia, sep-2026). `137` |
| **CPC** | *Costo por clic*. La forma en que cobra Product Ads: solo pagas cuando alguien hace clic, nunca por impresión (oficial ML Colombia, sep-2026). `147` |
| **Exposición** | Qué tanto muestra ML tu publicación. Depende del tipo de publicación y del ranking; no se compra directamente. `42`, `57` |
| **Ficha técnica** | El bloque de atributos estructurados de la publicación. Alimenta los filtros de búsqueda: sin el atributo lleno, desapareces cuando el comprador filtra por ese valor. `31` |
| **Flex** | Modalidad en la que **tú** entregas el mismo día en tu ciudad con tu propio mensajero, bajo la promesa de ML. `102` |
| **Full** | *Fulfillment*: guardas tu inventario en la bodega de ML y ellos empacan y despachan. En Colombia el centro citado es **Funza, Cundinamarca** (una sola fuente, sep-2026). `103` |
| **GMV** | *Gross Merchandise Value*: el valor total vendido antes de descontar comisiones, envíos y devoluciones. No es tu ingreso ni de lejos. `165` |
| **Gratuita** | Publicación sin costo: dura **60 días**, exposición baja, sin cuotas con 0% interés, máximo **10 simultáneas** con **1 unidad** cada una. Usados: hasta 20 ventas al año; nuevos: hasta 5. Si eres MercadoLíder o usuario profesional de Mercado Pago, **no puedes** vender gratis (oficial ML Colombia, sep-2026). `42` |
| **listing_type_id** | El nombre técnico del tipo de publicación en la API: `gold_special` y `gold_pro` son los que verás. Los nombres de la API conservan la nomenclatura vieja aunque el sitio colombiano ya no la muestre. `42`, `181` |
| **MCO** | El *site ID* de Colombia en Mercado Libre. Argentina es `MLA`, México `MLM`, Chile `MLC`, Perú `MPE`, Brasil `MLB`. Toda tarifa y toda regla se lee por sitio. `05` |
| **Mediación** | Segunda instancia de un problema: el reclamo no se resolvió entre las partes y **entra Mercado Libre** por un canal exclusivo, sin contacto directo. Pesa en la reputación de MercadoLíder. `135` |
| **Meli+** | Membresía del **comprador** (no la pagas tú). Llegó a Colombia el 26-ago-2025 desde $9.900 COP/mes: Esencial (envíos gratis, cashback, meses sin intereses) y Total (suma Disney+ estándar). `160` |
| **Mercado Ads** | La plataforma publicitaria interna de ML: Product Ads, Brand Ads y Display. Es subasta **dentro** del marketplace, no tráfico comprado afuera. `145` |
| **Mercado Envíos** | El sistema logístico de ML, que agrupa Full, Flex, Colecta y despacho por punto. `100` |
| **MercadoLíder** | Nivel de vendedor con prioridad y exposición extra. En Colombia arranca en **120 ventas concretadas en 60 días y $10.000.000 COP** facturados (oficial ML Colombia, sep-2026). `129` |
| **Mi Página** | La vitrina de marca dentro del marketplace que reemplazó a Mercado Shops. En Colombia: **3 meses gratis y luego $44.990 COP/mes**. Sin dominio propio ni control del checkout. `159` |
| **Premium** | Nombre **viejo** del tipo de publicación con comisión más alta y cuotas sin interés. En Colombia la ayuda oficial ya no lo usa: el sobrecosto real hoy es el de las **cuotas extra**, +3 puntos porcentuales (oficial ML Colombia, sep-2026). `42`, `43` |
| **Publicación de catálogo** | La que está enganchada a la ficha única compartida de un producto estandarizado, en vez de vivir suelta. Aparece más arriba que una publicación libre equivalente. `62` |
| **Reclamo** | El comprador abre un caso por un problema. Solo cuentan para tu termómetro los de **producto incompleto/faltante** y de **calidad** (oficial ML Colombia, sep-2026). `135`, `136` |
| **Reputación** | Tu historial de desempeño como vendedor, medido por reclamos, cancelaciones y envíos incorrectos, y mostrado en el termómetro. `125` |
| **SKU** | *Stock Keeping Unit*: el código único con el que identificas cada variante de producto en tu inventario. No es el `item_id` de ML. `97` |
| **TACOS** | *Total ACOS*: inversión en publicidad ÷ ingresos **totales** (pagados + orgánicos) × 100. Siempre menor que el ACOS. Es el que dice si la pauta te está sirviendo de verdad. `149` |
| **Termómetro** | La barra de color de tu reputación: rojo → naranja → amarillo → verde claro → verde, más **gris** cuando aún no alcanzas el mínimo de ventas (oficial ML Colombia, sep-2026). `125` |
| **Tienda Oficial** | Espacio de marca dentro de ML. Requisito duro: **marca registrada y vigente**, validada subiendo el certificado, con cuenta tipo empresa. Sin marca no hay atajo. `158` |
| **Variación** | Las opciones dentro de una misma publicación (talla, color). Usar variaciones en vez de publicaciones separadas es uno de los objetivos del indicador de calidad. `40`, `41` |

## Las palabras que ML cambió y los blogs no

El sitio colombiano renombró cosas y la web sigue usando los nombres viejos. Si buscas por el nombre
viejo, encuentras contenido viejo — casi siempre de otro país (`02`).

| Nombre viejo (lo que dicen los blogs) | Nombre vigente en Colombia (sep-2026) |
|---|---|
| Publicación Clásica | Publicación **con cuotas con 0% interés**, según el rango de precio |
| Publicación Premium | La misma, pero con **cuotas extra** (+3 puntos porcentuales) |
| "Cargo fijo por venta de bajo valor" | No existe aquí. Lo que hay es **precio mínimo de $2.900** |
| Mercado Shops | **Mi Página**, dentro del marketplace |
| Nivel 6 del comprador | **Meli+** |

Los nombres viejos sí siguen vivos en dos lugares: en los otros sitios de LatAm, y en la API, donde
`listing_type_id` conserva `gold_special` y `gold_pro`.

## Las cinco unidades de medida que decides mal si confundes

| Concepto | Qué se mide de verdad |
|---|---|
| **Peso de un envío** | El mayor entre el físico y el **volumétrico**, y se cobra **por unidad** (oficial ML Colombia, sep-2026). `109` |
| **Venta concretada** | La que **ya recibió el comprador**. En un carrito, cada producto distinto cuenta como una venta. Las de publicación **Gratuita no cuentan** para MercadoLíder (oficial, sep-2026). `129` |
| **Precio del producto** para el envío | El rango de precio define la tarifa: el salto de $59.999 a $60.000 casi duplica el costo de envío. `79`, `09` |
| **Periodo de evaluación** | 60 días si llevas 60+ ventas; **365 días** si llevas menos (oficial, sep-2026). `127` |
| **Comisión** | Se cobra sobre el precio **con IVA**, no sobre tu base gravable. `81` |

## Los cinco que más se confunden

| Par confundido | La diferencia que importa |
|---|---|
| **Reclamo** vs **mediación** | El reclamo lo negocian comprador y vendedor. La mediación la arbitra ML. La mediación es la que entra como 4ª variable para MercadoLíder |
| **Cancelación** vs **devolución** | Cancelación = el comprador recibe su dinero **antes** de que entregues. Devolución = ya lo tenía y lo regresa. **Las devoluciones NO son cancelaciones** y el castigo es distinto (oficial ML Colombia, sep-2026). `139` |
| **Catálogo** vs **publicación libre** | En catálogo compites por el **mismo** espacio con la misma ficha; libre es tu publicación propia. `62`, `64` |
| **ACOS** vs **ROAS** | ACOS es un costo (menor = mejor); ROAS es un retorno (mayor = mejor). Son inversos. En ML se habla en ACOS |
| **Mercado Ads** vs **Facebook Ads** | Ads interno = pagas por posición frente a quien ya está comprando. Meta = pagas por interrumpir a quien no estaba comprando. Meta es de `facebook_ads_lushows` |

## Términos que vas a ver en la API

| Término | Qué es |
|---|---|
| `item_id` | El identificador de tu publicación, tipo `MCO123456789`. No es tu SKU |
| `category_id` | El identificador de la categoría, tipo `MCO1234`. Define atributos y comisión |
| `seller_reputation` | El objeto de `GET /users/$USER_ID` con `level_id`, `power_seller_status` y métricas. `180` |
| `available_quantity` | El stock. Ponerlo en `0` pasa el ítem a `paused` con sub-estado `out_of_stock`. `183` |
| `pack_id` | Agrupa varios ítems de una misma compra; se usa para los mensajes de posventa. `188` |
| **Usuario de test** | Cuenta de prueba creada con `POST /users/test_user`. **No existe sandbox separado**: operan sobre la plataforma real, aisladas entre sí. `194` |

## El error clásico

Usar las palabras al revés delante de un soporte de Mercado Libre. Decir "me cancelaron" cuando fue
una devolución, o "tengo una mediación" cuando es un reclamo, te manda por el flujo equivocado y te
hace perder los plazos que sí importan — como las **24 horas hábiles** para responder antes de
perder el derecho a pedir la exclusión del reclamo de tu reputación (oficial ML Colombia, sep-2026).
Los nombres aquí son plazos disfrazados.

## Relacionados

`01` qué es ML · `02` los cuatro motores · `04` diagnóstico inicial · `42` tipos de publicación ·
`62` qué es el catálogo · `125` el termómetro · `129` MercadoLíder · `135` reclamo y mediación ·
`139` la cancelación y su castigo · `145` qué es Mercado Ads · `149` ACOS y TACOS ·
`158` Tienda Oficial · `160` Meli+ · `180` los endpoints que vas a usar
