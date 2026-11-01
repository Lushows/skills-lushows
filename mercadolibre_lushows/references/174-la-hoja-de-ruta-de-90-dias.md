# La hoja de ruta de 90 días

El plan completo para pasar de cero a vendedor que factura con reputación verde. Cada semana tiene
una tarea y un hito verificable — algo que miras en el panel y respondes sí o no. Si un hito no se
cumple, no avanzas de fase: lo arreglas primero.

## La lógica de las tres fases

| Fase | Días | Objetivo único | El hito que la cierra |
|---|---|---|---|
| **Montar** | 1-30 | Publicar bien y hacer las primeras ventas | Ficha completa vendiendo |
| **Consolidar** | 31-60 | Llegar a **60 ventas concretadas** | El periodo de evaluación pasa de 365 a 60 días |
| **Crecer** | 61-90 | Más SKUs, mejor logística, primera pauta | SKU-2 vendiendo y ACOS bajo tu margen |

**El hito que gobierna los 90 días son las 60 ventas.** Con 60 o más ventas concretadas, ML te
evalúa sobre los últimos **60 días**; con menos, sobre los últimos **365** (oficial ML Colombia,
verificado sep-2026). Es la diferencia entre corregir un error en dos meses o cargarlo un año.

## Días 1-30 · Montar

### Semana 1 — La cuenta

```
□ Decides persona natural o empresa: afecta impuestos y Tienda Oficial (`11`)
□ Creas la cuenta con TU correo y TU celular. Nadie más los toca (`10`)
□ Doble factor activo en Mercado Libre y en Mercado Pago
□ Datos fiscales, RUT y cuenta bancaria de retiro a nombre del titular (`12`)
□ Lees qué retiene y reporta Mercado Pago (`13`) — lo fiscal es de `contador_lushows`
```

**Hito:** entras a Mi cuenta y ves tu nombre, tu RUT y tu banco correctos. Sin esto no se publica.

### Semana 2 — El producto y el número

```
□ Eliges 1 SKU para arrancar. Uno. No cinco (`172`)
□ Corres el margen ANTES de publicar, con scripts/margen_ml.py (`75`)
□ Sacas la comisión real de TU categoría en el simulador oficial, logueado (`76`)
□ Decides si ofreces cuotas extra con el número en la mano: cuestan 3 puntos   (`80`)
□ Compras empaque suficiente para 30 días (`110`)
```

**Hito:** sabes cuántos pesos te quedan de una venta. Si no lo sabes, no sigues.

> **La comisión oficial en Colombia va entre 8% y 22%** según categoría y cuotas: 8-19% con hasta
> 3 cuotas sin interés, 11-22% con cuotas extra (oficial ML Colombia, sep-2026). El exacto solo se
> ve en el simulador logueado; `listing_prices` ya responde 403. Ignora los rangos de blog.

### Semana 3 — La ficha

Esta semana decide los otros 89 días. No se apura.

```
□ Categoría verificada: GET /sites/MCO/domain_discovery/search?q=tu+producto&limit=3  (`27`)
□ Título: Producto + Marca + Modelo + especificación, 60 caracteres (límite de la API).
  Sin símbolos, emojis, "OFERTA", ni mención de envío gratis o cuotas (`28`, `29`)
□ TODOS los atributos con tags.required llenos: alimentan los filtros del buscador (`31`)
□ Foto 1: fondo blanco #FFFFFF digital, 1200×1200 px (zoom), solo el producto. Las
  secundarias sí llevan contexto, detalle y escala (`33`)
□ Video de hasta 60 segundos: es gratis y también va a Mercado Play (`36`)
□ Descripción que responda las 10 preguntas que te haría el comprador (`37`)
□ Variaciones bien armadas en vez de publicaciones separadas (`38`)
```

**Hito:** el indicador de calidad marca **Profesional** y la lista de `40` está toda en ✓ (`39`).

### Semana 4 — Publicar y aguantar

```
□ Publicas lunes o martes en la mañana, nunca viernes en la noche
□ NO tocas el precio en 7 días: ML evalúa en 48-72 h y las ~100 primeras visitas fijan
  tu etiqueta de conversión (`59`)
□ Respondes toda pregunta en menos de 24 horas hábiles, siempre (`133`)
□ Empiezas el tablero semanal. Lo llenas aunque haya puros ceros (`166`)
□ Consideras el Programa Despegue: depósito de $90.360 COP para impulso inicial (`128`)
```

**Hito día 30:** tienes visitas, tienes al menos una venta y **no cancelaste ninguna**.

## Días 31-60 · Consolidar

El objetivo de estos 30 días es uno solo: **llegar a 60 ventas concretadas.**

### Semana 5 — Leer, no adivinar

```
□ Primera lectura seria del tablero (`166`) y diagnóstico honesto (`165`):
    Sin visitas          → ficha, categoría o título (`25`-`31`)
    Visitas y sin ventas → precio, foto o descripción (`58`)
    Ventas y sin plata   → costo: corre el margen otra vez (`75`)
□ Un solo cambio a la vez, y 7 días antes de tocar otra cosa
```

### Semana 6 — Logística

```
□ Mides tu despacho real contra el prometido y evalúas Full con números (`105`)
□ Revisas el umbral de envío gratis y qué te cuesta a ti (`102`)
□ Ajustas el corte de despacho: nunca marques despachado lo que sigue en la mesa (`126`)
```

### Semana 7 — Posventa blindada

```
□ Te aprendes la lista de reclamos EXCLUIBLES y NO excluibles: sin respuesta en
  24 horas hábiles pierdes el derecho a excluirlo (oficial) (`136`)
□ Guion de respuestas frecuentes escrito y listo para reusar (`133`)
□ Foto del producto dentro de la caja: tu prueba ante un reclamo por faltante
□ Política de devolución clara: nuevos 30 días corridos, usados 14, alimentos 6 (`137`)
```

### Semana 8 — Profundizar el ganador

```
□ Variaciones, packs de 2 y 3, y la versión premium del mismo producto (`38`, `172`)
□ Punto de reposición: (venta diaria × días del proveedor) + (venta diaria × 7)
```

**Hitos día 60:**

| Hito | Cómo lo verificas |
|---|---|
| **60 ventas concretadas** | El periodo de evaluación cambia a 60 días en tu panel (`127`) |
| Reputación **verde** | El termómetro, que se recalcula diariamente (`125`) |
| Canceladas por debajo de 2,5% | Más de 2,5% → la cuenta puede ser suspendida (oficial) |
| Margen real medido y cero preguntas sin responder en 24 h | Tu hoja y tu registro |

Sin 60 ventas **no avances a la fase 3**: repite la semana 5. Pautar sobre una ficha que no
convierte solo hace la pérdida más rápida.

## Días 61-90 · Crecer

### Semana 9 — El segundo SKU

```
□ Eliges el SKU-2 por complemento o vecino de categoría, no por "algo distinto" (`172`)
□ Inventario de prueba: 15-21 días, no más (`168`)
□ Ficha completa ANTES de publicar, y un SKU nuevo a la vez: la ventana de 48-72 h
  no se repite (`59`)
```

### Semana 10 — Catálogo y posición

```
□ Revisas si tu categoría tiene catálogo y quién lo gana (`62`). Corte duro: naranja
  o roja participa pero NO puede ganar la oferta principal (`63`)
□ Sin cuotas sin interés pierdes en la tabla comparativa, y ofrecerlas cuesta 3 puntos
  de comisión: haz el número antes (`80`)
```

### Semana 11 — La primera pauta

Solo si el margen lo permite. ACOS objetivo oficial: **Rentabilidad 5-15% · Crecimiento 15-30% ·
Visibilidad más de 30%** (oficial `vendedores.mercadolibre.com.co`, verificado sep-2026).

```
□ Declaras tu estrategia ANTES de encender (`148`), con el ACOS objetivo MENOR que tu
  margen neto. Con margen ~15%, aún no pautes (`150`)
□ Enciendes sobre la publicación que YA convierte, nunca sobre una recién publicada (`147`)
□ No apagas nada antes de 14 días: reportes con 72 h de rezago, atribución a 14 días (`151`)
□ Nunca dejas que se acabe el stock con pauta encendida: reinicia el aprendizaje (`140`)
```

### Semana 12 — Cerrar y planear

```
□ Lectura completa de los 90 días (`166`) y concentración del SKU-1: semáforo en `172`
□ Calendario de los próximos 90 días (`167`). Hot Sale 2ª edición: 19-23 de octubre de 2026
□ Defines qué delegar primero (empaque y despacho, en ese orden) y los tres objetivos
  de los siguientes 90 días. Tres, no diez (`169`)
```

**Hitos día 90:** verde sostenido 30 días seguidos · dos SKUs con ventas en los últimos 30 días ·
margen positivo por SKU sin depender de pauta · si hay pauta, ACOS por debajo del margen neto ·
tablero llenado 12 semanas seguidas · cero cancelaciones por falta de stock en el último mes.

## Lo que NO haces en estos 90 días

| Tentación | Por qué no |
|---|---|
| Abrir otro país | Reinicia reputación y logística. Antes, lee `171` |
| Comprar una cuenta hecha | Se evapora en 60 días y arrastra tu cuenta buena (`173`) |
| Publicar 40 SKUs | 40 fichas a medias rinden menos que 2 impecables (`172`) |
| Cambiar precio cada semana | Descalibra el algoritmo y dispara revisiones (`67`) |

## El error clásico

Saltarse la semana 3. Publicar el jueves porque "ya quiero vender" y arreglar la ficha después. No
hay después: el algoritmo evalúa en 48-72 horas y las primeras visitas le cuelgan una etiqueta de
conversión difícil de revertir. **Sale más barato demorarte una semana que quemar la publicación.**

## Relacionados

`10`-`13` cuenta, RUT y fiscal · `25`-`40` la publicación que vende · `58` la conversión manda ·
`59` la ventana de 48-72 horas · `62`-`63` catálogo · `67` pausas · `75`-`80` costos, comisiones y
cuotas · `102` envío gratis · `105` Full · `110` empaque · `125` el termómetro · `127` el periodo
de evaluación · `128` Programa Despegue · `133` tiempo de respuesta · `136` exclusión de reclamos ·
`137` devoluciones · `140` quiebre de stock · `147`-`151` Mercado Ads · `165` las métricas ·
`166` el tablero · `167` estacionalidad · `168` inventario · `169` equipo · `170` tienda propia ·
`171` otro país · `172` el SKU estrella · `173` comprar una cuenta
