# El ciclo de vida del vendedor nuevo

De cuenta recién abierta a MercadoLíder hay cuatro etapas con hitos numéricos concretos. Saber en
cuál estás define qué se trabaja y qué se aplaza. La trampa de cada etapa es distinta y casi nunca
es la que el vendedor cree.

## El mapa completo

| Etapa | Señal | Hito que la cierra | Trampa |
|---|---|---|---|
| **1. Gris** | Termómetro sin color | Las **primeras 10 ventas** | Creer que hay reputación que arreglar |
| **2. Primeras ventas** | Color, pero evaluado a 365 días | Llegar a 60 ventas | Un error queda pesando un año |
| **3. Volumen** | Evaluación a 60 días | 120 ventas + $10.000.000 COP | Crecer y romper la logística |
| **4. MercadoLíder** | Insignia y prioridad | Gold (300 / $30M), Platinum (600 / $80M) | Caer de nivel por un mes malo |

Todas las cifras de esta tabla son oficiales de ML Colombia, verificadas sep-2026.

---

## Etapa 1 — Gris: aún no tienes reputación

El termómetro gris significa literalmente que aún no alcanzas el mínimo: **"no tendrás reputación
hasta completar tus primeras 10 ventas"** (oficial ML Colombia, verificado sep-2026). No es un
castigo ni un color malo: es ausencia de datos.

Y aquí está la buena noticia que casi nadie sabe: **sin reputación pagas el mismo envío que un
vendedor verde**. El descuento de envíos es del 50% para MercadoLíder, verde **y sin reputación**;
40% para amarilla; **0% para naranja o roja** (oficial ML Colombia, sep-2026). Arrancas con la
tarifa buena. Lo único que puedes hacer es perderla.

Qué hacer:

```
□ Publica solo cuando la ficha esté completa — el algoritmo mide las primeras 48-72 h  (59)
□ Categoría correcta con el predictor                                                   (27)
□ Todos los atributos con tags.required llenos                                          (31, 32)
□ Foto principal con fondo blanco puro #FFFFFF, 1200×1200 px                            (35)
□ Precio ya calculado con comisión, envío e IVA — no lo vas a poder bajar después       (82)
□ Stock real y suficiente: quedarte sin stock aquí te borra del mapa                    (61)
□ Tiempo de despacho que puedas cumplir el peor día, no el mejor                        (112)
```

La trampa: **publicar rápido para "empezar a aprender"**. El algoritmo no te da segundas
oportunidades baratas. Evalúa la publicación nueva en sus primeras 48-72 horas y las primeras ~100
visitas le cuelgan una etiqueta de conversión difícil de revertir (fuente especializada, sep-2026).
Es más barato demorarte un día que quemar la publicación y tener que relanzarla (`60`).

Si quieres acelerar el arranque existe el **Programa de Despegue**: dejas dinero en Mercado Pago
Financiera y obtienes el color **verde claro** mientras te evalúan (oficial ML Colombia, sep-2026).
El monto que circula es de **$90.360 COP**, pero viene de fuente secundaria: verifícalo en tu panel
antes de usarlo. Si mantienes buen desempeño recuperas el dinero; si no, lo pierdes y vuelves al
color original.

---

## Etapa 2 — Primeras ventas: el año que te persigue

Apenas concretas ventas aparece el color. Y aparece la regla que más duele para el vendedor chico:

| Ventas concretadas | Periodo de evaluación |
|---|---|
| **Menos de 60** | Últimos **365 días** |
| **60 o más** | Últimos **60 días** |

Oficial ML Colombia, verificado sep-2026. El recálculo es **dinámico y diario**.

Traducción: con pocas ventas, **un despacho tarde de hace ocho meses te sigue pesando hoy**. Y como
tienes pocas transacciones, cada error individual pesa porcentualmente muchísimo: con 20 ventas, un
solo reclamo es el 5%.

Los límites oficiales para **mantenerte en verde** cambian con el periodo, y son más duros cuando
llevas volumen (oficial ML Colombia, sep-2026):

| Variable | A 60 días | A 365 días | MercadoLíder |
|---|---|---|---|
| Ventas con reclamos | 3,5% | 3,5% | 2,5% |
| Envíos incorrectos | 12% | 15,5% | 10% |
| Canceladas por ti | 2,5% | 4% | 1,5% |

Qué se trabaja en esta etapa:

- **No cancelar nunca por falta de stock.** El límite para seguir verde es **2,5% a 60 días** (4% a
  365 días), y más del 2,5% de canceladas puede además suspender la cuenta para vender. Con 20
  ventas, media cancelación ya te acerca al borde. Ver `139`, `140`.
- **Responder en menos de 24 horas hábiles.** Si no respondes mensajes en ese plazo, **pierdes el
  derecho a pedir la exclusión del reclamo** de tu reputación (oficial ML Colombia, sep-2026).
  Ver `136`.
- **Aprender qué reclamos no cuentan.** Solo pesan en el termómetro los de producto
  incompleto/faltante y los de calidad (oficial, sep-2026). El arrepentimiento con producto en
  perfecto estado es excluible si respondiste a tiempo. Ver `136`.
- Conseguir opiniones: son el primer activo de conversión que tienes (`52`).

**La meta de esta etapa no es facturar: es llegar a 60 ventas para que el pasado caduque.**

---

## Etapa 3 — Volumen: el pasado empieza a caducar

Al cruzar las **60 ventas concretadas**, el periodo de evaluación baja a **60 días**. Es el mejor
regalo que da la plataforma: **sesenta días limpios te limpian**. Un vendedor golpeado con volumen
se recupera en dos meses; uno sin volumen tarda un año.

Aquí se rompen dos cosas al mismo tiempo:

| Lo que crece | Lo que se quiebra |
|---|---|
| Pedidos por día | El empaque artesanal y el despacho a mano (`114`) |
| SKUs publicados | El control de stock, y aparece la sobreventa (`123`, `196`) |
| Preguntas diarias | El tiempo de respuesta (`133`) |
| Ingresos | El margen, si nunca lo calculaste por SKU (`97`) |

La trampa de esta etapa: **crecer y romper la logística**. Los "envíos incorrectos" (despacho con
demora o desde depósito incorrecto) son una de las tres variables base del termómetro, junto con
reclamos y canceladas (oficial ML Colombia, sep-2026). Es el momento natural de evaluar Full
(`103`, `105`).

---

## Etapa 4 — MercadoLíder

Los tres niveles, oficiales de ML Colombia (verificados sep-2026):

| Nivel | Ventas concretadas (60 días) | Facturación |
|---|---|---|
| MercadoLíder | 120 o más | $10.000.000 COP o más |
| MercadoLíder Gold | 300 o más | $30.000.000 COP o más |
| MercadoLíder Platinum | 600 o más | $80.000.000 COP o más |

⚠️ Si ves en un blog "180 ventas y $300.000" o "415 ventas y $3,82 millones", **es de otro país o
está viejo**. Las cifras de arriba son las de la ayuda oficial colombiana.

Dos definiciones oficiales que cambian la cuenta: **ventas concretadas son las que ya recibió el
comprador** (en un carrito, cada producto distinto cuenta como una venta), y **no se tienen en
cuenta las ventas con publicación Gratuita**. Si estás vendiendo gratis para ahorrar comisión, no
estás avanzando hacia MercadoLíder.

Requisitos generales para todos los niveles:

```
□ Más de 4 meses registrado como vendedor
□ Reputación VERDE
□ Medición sobre los últimos 60 días
```

Y los cuatro límites de calidad, que aplican a todos los niveles (oficial, sep-2026):

| Métrica | Límite |
|---|---|
| Reclamos | menos del **2,5%** de las ventas |
| Mediaciones | menos del **0,5%** |
| Ventas canceladas | menos del **1,5%** |
| Envíos incorrectos | menos del **10%** |

Ojo con las **mediaciones**: para MercadoLíder se suma como cuarta variable, además de las tres
base. Es la métrica más fácil de descuidar porque el límite es bajísimo — 0,5% son 3 mediaciones
en 600 ventas.

Beneficios: **mayor prioridad y exposición en los resultados** (confirmado oficialmente) y, según
fuentes secundarias, atención personalizada por chat y acceso a capacitaciones. Detalle en `130`.

## La línea de tiempo honesta

> ⚠️ **Sin verificar (sep-2026):** cuánto tarda en promedio un vendedor colombiano en llegar a
> MercadoLíder. No hay dato público. Lo que sí es un piso duro es el requisito oficial de **más de
> 4 meses registrado**, así que antes de 4 meses es imposible por definición, sin importar cuánto
> vendas.

Lo que sí puedes calcular tú: para MercadoLíder necesitas **120 ventas en 60 días**, o sea 2 ventas
diarias sostenidas, con un ticket promedio que llegue a $10.000.000 en esos dos meses (≈ $83.000 por
venta si vendes exactamente 120). Si tu ticket es menor, necesitas más ventas, no menos. Eso conecta
directo con `85` (el ticket que aguanta ML) y `86`.

## El error clásico

Perseguir la insignia de MercadoLíder como objetivo. La insignia es **consecuencia** de vender bien
120 veces, no la causa de vender. Los vendedores que la persiguen suelen forzar volumen bajando el
precio hasta perder plata, o aceptando pedidos que no pueden despachar — y terminan con más ventas
y el termómetro en naranja, que es exactamente el peor lugar posible: ahí **no puedes ganar el
catálogo** y la pauta no compensa la penalización (`66`, `154`).

## Relacionados

`04` diagnóstico inicial · `52` las opiniones · `59` las primeras 72 horas · `60` relanzar una
publicación quemada · `61` stock cero · `82` la calculadora de margen · `85` el ticket que aguanta
ML · `103` Full · `112` el tiempo de despacho que prometes · `125` el termómetro ·
`127` el periodo de evaluación · `128` cómo se recupera una caída · `129` MercadoLíder ·
`136` reglas de exclusión de reclamos · `139` la cancelación y su castigo · `174` hoja de ruta de
90 días
