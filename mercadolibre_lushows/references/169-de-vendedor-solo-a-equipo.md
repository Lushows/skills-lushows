# De vendedor solo a equipo

Llega un punto en que tu cuello de botella no es el tráfico ni el precio: eres tú. Este módulo te
da las señales de que ya pasaste ese punto, el orden correcto para soltar tareas, y la parte que
casi nadie hace bien — dar acceso a la cuenta sin entregar la contraseña.

## Las señales de que ya no puedes solo

Ninguna es "me siento cansado". Todas son medibles:

| Señal | Umbral | Qué se rompió |
|---|---|---|
| Preguntas sin responder pasadas las 24 h hábiles | 1 sola vez | Pierdes el derecho a excluir reclamos (`136`) |
| Envíos con problemas | acercándose al **10%** | Empacas de noche y despachas tarde (`126`) |
| Despachas después del corte | 2 veces por semana | La operación ya no cabe en tu día |
| Semanas sin llenar el tablero | 2 seguidas | Estás operando, no dirigiendo (`166`) |
| Ventas concretadas / mes | más de ~150-200 | Referencia de carga, no norma de ML |
| No publicaste un SKU nuevo | en 60 días | El negocio dejó de crecer y no te diste cuenta |
| Cancelaste por no tener el stock que creías tener | 1 sola vez | Nadie está cuidando el inventario (`139`) |

> ⚠️ **Sin verificar para Colombia (sep-2026).** El umbral de ventas/mes es criterio operativo, no
> un dato de Mercado Libre. Los porcentajes de reclamos, envíos y canceladas sí son oficiales.

## El orden de delegación

Se suelta de afuera hacia adentro. Lo que es mecánico y verificable primero; lo que define tu
negocio, último — o nunca.

| Orden | Qué delegas | Por qué en ese lugar | Riesgo si sale mal |
|---|---|---|---|
| **1º** | Empaque y despacho | Lo que más horas come y lo más fácil de enseñar con una lista | Un paquete mal hecho = reclamo de calidad. Daño acotado |
| **2º** | Compras de insumos | Cajas, burbuja, cinta. Nada decide el negocio | Bajo |
| **3º** | Carga de publicaciones | Con plantilla y checklist de ficha (`40`) | Ficha incompleta = publicación castigada. Revisable antes |
| **4º** | Fotografía y contenido | Tiene manual y se revisa antes de subir (`33`) | Bajo si hay aprobación previa |
| **5º** | Preguntas frecuentes | Con guion cerrado y lista de "esto se escala" | Medio: una respuesta mal dada pierde la venta |
| **6º** | Reclamos en primera etapa | Solo con reglas escritas de qué puede ofrecer | **Alto**: una mediación mal llevada pega en reputación (`135`) |
| **Último** | **Precio** | Define margen, catálogo y si la pauta es rentable (`150`) | Máximo |
| **Último** | **Respuestas que comprometen**: garantías, excepciones, devoluciones fuera de política | Compromete plata y reputación | Máximo |
| **Nunca** | Acceso de administrador a la cuenta principal | Ver abajo | Pérdida de la cuenta |

**Lo primero que sueltas es lo que te quita horas; lo último, lo que te quita el negocio.**

## Por qué el empaque va primero

No es porque sea lo menos importante: es porque es la única tarea donde una lista de chequeo
reemplaza al criterio. Si puedes escribirla, puedes delegarla.

```
□ Verifica el SKU contra la etiqueta de la orden antes de meterlo a la caja
□ Foto del producto dentro de la caja, antes de cerrar (prueba ante reclamo por faltante)
□ Todos los accesorios que dice la ficha — el faltante es reclamo NO excluible (`136`)
□ Etiqueta pegada plana, código de barras legible
□ Despacho antes del corte del transportador, desde el origen declarado
□ Si el corte ya pasó: se queda para mañana, NO se marca como despachado hoy
```

La última línea evita la métrica de envíos con problemas: marcar como despachado lo que aún está en
la mesa es la forma más común de arruinarla (`126`).

## Los accesos: la parte que casi nadie hace bien

**Nunca compartas la contraseña de la cuenta principal.** No es un consejo de higiene: es la
diferencia entre poder retirar a alguien y tener que rehacer tu negocio.

| Si compartes la contraseña | Si das un usuario con permisos |
|---|---|
| No sabes quién hizo qué cambio | Cada acción queda asociada a una persona |
| Para retirar a alguien tienes que cambiar la clave y reconfigurar todo | Revocas un usuario en un clic |
| Esa persona puede cambiar precios, correo de recuperación y datos bancarios | Solo ve lo que le asignaste |
| Si esa persona la reutiliza en otro lado y la filtran, pierdes la cuenta | El daño queda contenido |
| Un segundo dispositivo desconocido dispara verificaciones de seguridad | Acceso legítimo y reconocido |

Mercado Libre permite crear **usuarios colaboradores con permisos por área** desde la
configuración de la cuenta.

> ⚠️ **Sin verificar para Colombia (sep-2026).** El menú exacto y la lista completa de permisos
> disponibles en MCO no se pudo leer (las páginas de ayuda de ML Colombia devuelven 403 a lectura
> automatizada). Entra a Mi cuenta → Configuración y búscalo como "usuarios" o "colaboradores"
> antes de dar cualquier acceso.

## Reglas de acceso que sí puedes aplicar hoy

```
□ Un usuario por persona. Jamás un usuario compartido por "el equipo"
□ El correo de recuperación y el celular de la cuenta son TUYOS y de nadie más
□ Doble factor activo en la cuenta principal y en Mercado Pago
□ Los datos bancarios de retiro solo los toca el dueño
□ Cuando alguien se va: revocas el mismo día, no "la otra semana"
□ Revisión trimestral: ¿quién tiene acceso y sigue necesitándolo?
□ Si integras un software de terceros, va por OAuth con su propia app, no con tu clave (`176`)
```

La última línea importa: un integrador serio nunca te pide la contraseña de Mercado Libre. Te pide
que autorices su aplicación. Si alguien te pide la clave, es la señal de que no sabe lo que hace
—o de que no quieres que sepa (`183`).

## Cuándo contratar, con qué figura y a qué costo

Eso no es de esta skill. La decisión laboral —contrato, prestaciones, seguridad social, si es
nómina o servicios— es de `contador_lushows`. Si la duda es si el negocio aguanta un sueldo más, es
de `economist_lushows`. Aquí solo definimos **qué** se delega, **en qué orden** y **con qué
acceso**.

## El error clásico

Contratar a alguien "para que me ayude con todo". Sin lista de tareas, sin guion de respuestas y
sin permisos definidos, lo que pasa siempre es lo mismo: a la tercera semana esa persona está
respondiendo preguntas de clientes con criterio propio, y a la sexta te bajó la conversión sin que
puedas señalar dónde. **Se delega una tarea con su lista y su límite, nunca "el negocio".**

## El otro error: delegar el precio primero

Suena lógico —"que él maneje los precios mientras yo consigo producto"— y es la peor decisión
posible. El precio determina si ganas el catálogo (`63`), cuánta comisión pagas, qué ACOS puedes
pagar (`150`) y si la venta deja utilidad. Además, los cambios bruscos de precio disparan revisiones
de la publicación (`67`). **El precio se suelta cuando la persona lleva un año y entiende el margen
por SKU — o no se suelta.**

## Relacionados

`40` la lista de chequeo de la ficha · `63` ganar el catálogo · `67` pausas y revisiones ·
`110` empaque · `126` las tres métricas · `133` el tiempo de respuesta · `135` reclamo y mediación ·
`136` reglas de exclusión · `139` la cancelación y su castigo · `143` suspensión de cuenta ·
`150` ACOS sano · `166` el tablero semanal · `176` OAuth y aplicaciones ·
`183` integradores y terceros
