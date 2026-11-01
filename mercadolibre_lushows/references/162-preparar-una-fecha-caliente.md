# Preparar una fecha caliente

El plan operativo para llegar listo a Hot Sale, Black Friday o Navidad. Todo lo importante pasa
**antes** del evento: durante los cinco días solo se ejecuta y se vigila el stock.

## La cuenta regresiva

### Semana −6: decidir e inventariar

```
□ Elegí los SKU que van: los de mejor margen y mejor ficha, no todos
□ Verifiqué que cada SKU aguanta un CPC alto (margen neto > 25%, ver `150`)
□ Calculé cuántas unidades necesito: ventas normales × 3 como piso de partida
□ Hice el pedido al proveedor con holgura de tiempo, no justo
□ Definí el presupuesto total de pauta del evento y lo separé del mes normal
```

El sobre-stock en fecha caliente se vende después; el faltante no se recupera nunca. Pero ojo con
Full: el stock que sobra empieza a generar cargos por inventario antiguo (`107`).

### Semana −4: logística

```
□ Inventario recibido y contado físicamente, no en el sistema
□ Lo que va a Full ya está enviado (el traslado corre por tu cuenta y toma días) (`103`)
□ Verifiqué peso y dimensiones reales de cada empaque (`109`)
□ Revisé si algún SKU cruza el umbral de $60.000 y cambia su costo de envío (`79`)
□ Tengo plan B de despacho propio si la colecta se congestiona (`104`)
```

### Semana −3: fichas

El anuncio es la ficha (`146`). Esta semana se arregla lo que en el evento ya no se puede tocar.

```
□ Todos los atributos obligatorios llenos en los SKU del evento (`40`)
□ Fotos principales sobre blanco puro, 1200 px mínimo (`42`)
□ Al menos 4 fotos por publicación; video donde la categoría lo permita
□ Indicador de calidad en "Profesional" o lo más cerca posible (`48`)
□ Descripciones revisadas, sin datos de contacto
□ Títulos verificados: producto, marca, modelo, característica (`28`)
□ Variaciones bien armadas: no publicaciones separadas por color o talla
```

### Semana −2: números y reputación

```
□ Reputación en VERDE, verificada, no asumida (`125`)
□ Recalculé el margen de cada SKU con la comisión y el envío reales (`82`)
□ Fijé el ACOS objetivo de la campaña del evento (`150`)
□ Decidí el descuento de cada SKU y verifiqué que el margen sobrevive
□ Verifiqué que el precio "antes" es real: la SIC vigila los descuentos falsos
□ Confirmé que no ofrezco cuotas extra sin necesidad (son 3 puntos de comisión)
```

La reputación es la casilla que más gente da por hecha. Si estás en naranja o roja, el costo de
envío se te **duplica** — un paquete de 1 kg en producto de más de $60.000 pasa de $8.200 a
$16.400 (oficial ML Colombia, verificado sep-2026). Entrar a una fecha caliente con la reputación
caída es vender más para ganar menos.

### Semana −1: la campaña, creada y pausada

```
□ Campaña del evento creada APARTE de la general, con nombre que la identifique
□ Presupuesto propio, distinto del mes normal
□ Estrategia elegida a conciencia: Crecimiento o Visibilidad, según margen (`148`)
□ Escrita la FECHA DE APAGADO antes de encenderla
□ Solo los SKU del evento, con stock verificado hoy
□ La campaña queda pausada, lista para encender el día 0
```

### Día 0 al final del evento: ejecutar

```
□ Encender la campaña del evento la mañana del primer día
□ Revisar STOCK dos veces al día. Es lo único que se vigila
□ Responder preguntas rápido: en fecha caliente la demora mata la venta
□ Despachar el mismo día: los envíos incorrectos golpean la reputación (`125`)
□ NO mirar el ACOS. Está inflado: la atribución tarda hasta 72 horas (`151`)
□ NO tocar precios ni ficha durante el evento
```

**Durante el evento no se optimiza: se despacha.** Toda la optimización ya ocurrió en las semanas
anteriores.

### Día +1 y día +14: cerrar

```
□ Día +1: apagar la campaña del evento. Volver a la campaña general
□ Día +1: reponer stock de lo que se agotó antes de que caiga la posición (`61`)
□ Día +14: exportar el reporte con la atribución cerrada (`155`)
□ Día +14: ACOS y TACOS del evento, comparados con un mes normal (`149`)
□ Día +14: anotar en la bitácora qué SKU funcionaron y cuáles no (`156`)
□ Revisar si quedó stock muerto en Full y planear su salida (`107`)
```

## La tabla de prioridades si el tiempo no alcanza

Si llegaste tarde y solo tienes dos semanas, este es el orden por retorno:

| Prioridad | Qué | Por qué |
|---|---|---|
| 1 | Stock de tus 3 mejores SKU | Sin producto no hay nada que discutir |
| 2 | Reputación en verde | Duplica o no duplica tu costo de envío (`125`) |
| 3 | Foto principal y título de esos 3 SKU | Es lo que decide el clic en un listado saturado |
| 4 | Margen recalculado con el descuento puesto | Para no vender en negativo (`154`) |
| 5 | Campaña aparte con presupuesto cerrado | Para poder apagarla entera |

Lo que queda fuera de esa lista se hace la próxima vez. **Es mejor llegar con tres SKU impecables
que con treinta a medias.**

## El error clásico

Bajar el precio sin recalcular. El vendedor decide "30% de descuento porque es Hot Sale", vende el
triple y cierra el evento con menos plata que un martes normal — porque el 30% salía de un margen
del 25%. El descuento y el ACOS se suman sobre el mismo margen (`154`). **Antes de anunciar un
descuento, córrelo por la calculadora: `python scripts/margen_ml.py margen ...`** (`82`).

## Relacionados

`145` qué es Mercado Ads · `146` Product Ads · `148` las tres estrategias ·
`149` ACOS y TACOS · `150` el ACOS sano según tu margen · `151` la ventana de atribución ·
`154` el error de pautar sin margen · `155` leer los reportes ·
`156` optimizar semana a semana · `161` Hot Sale y el calendario comercial ·
`163` tráfico externo · `28` el título · `40` atributos · `42` fotos ·
`48` indicador de calidad · `61` stock cero · `79` umbral del envío gratis ·
`82` la calculadora de margen · `103` Full · `104` colecta y puntos ·
`107` costo de almacenamiento en Full · `109` peso volumétrico · `125` reputación
