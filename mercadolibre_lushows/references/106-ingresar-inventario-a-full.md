# Ingresar inventario a Full

El envío a bodega es el momento de mayor riesgo de la operación Full, y además **el traslado corre
por tu cuenta** (oficial ML Colombia, verificado sep-2026). Si algo sale mal ahí, no te enteras
hasta que el stock no aparece disponible y ya perdiste una semana.

## Los requisitos, oficiales

> "Tener reputación como vendedor. Se activa al completar tus **primeras 10 ventas**."
> "Vender productos **aptos para Full** y dentro de las **dimensiones permitidas**."
> "La activación de Full para nuevos vendedores está sujeta a la **disponibilidad de espacio** en
> nuestros centros de distribución."
> "El **traslado corre por tu cuenta**."
> (oficial ML Colombia, verificado sep-2026)

Los dos que sorprenden: sin 10 ventas no tienes reputación y por lo tanto no entras; y aunque
cumplas todo, **puede no haber espacio**. Eso no es un error tuyo ni algo que puedas apelar.

## Lo que no está publicado

> ⚠️ **Sin verificar para Colombia (sep-2026).** El detalle operativo del ingreso —formato exacto
> de etiqueta o código, cantidades mínimas por SKU, medidas de caja master, cómo se agenda la cita
> de recepción, plazos de recepción, transportadora designada— **no está publicado**.
>
> Léelo en: Panel → Ventas → Full → Enviar stock. La pantalla del envío muestra las reglas vigentes
> para tu cuenta y tu categoría, que es lo único que importa.
>
> Ojo con las guías de internet: las URLs viejas del centro de ayuda **no dan 404, redirigen a una
> página equivocada**. Para buscar un artículo usa `mercadolibre.com.co/ayuda/search?q=`

## El flujo, en orden

```
□ 1. Decidir QUÉ y CUÁNTO: solo SKUs de rotación probada, 30-45 días de venta (`105`)
□ 2. Verificar que el producto sea apto y esté dentro de las dimensiones permitidas
□ 3. Crear el envío a bodega desde el panel de Full
□ 4. Dejar que el sistema te diga cómo rotular: NO inventes etiquetas
□ 5. Imprimir las etiquetas que el panel genera, en la calidad que pide
□ 6. Rotular como indique el panel (por unidad o por caja)
□ 7. Empacar en caja master según las medidas que muestre la pantalla
□ 8. Contratar y pagar el traslado (es tuyo) y guardar la guía
□ 9. Verificar la recepción: unidades recibidas vs unidades enviadas
□ 10. Reclamar la diferencia el mismo día que la detectas
□ 11. Anotar en el calendario la fecha del MES 4 de este envío (`108`)
```

Los pasos 9 y 11 son los que nadie hace y los que más plata recuperan. **Lo que no cuadra el día
de la recepción no se cuadra nunca, y el cargo del mes 4 llega puntual aunque tú lo hayas
olvidado.**

## Lo que no puedes improvisar

| Punto | Por qué es crítico |
|---|---|
| La etiqueta la genera ML, no tú | Un código propio o mal impreso = unidad no ingresada |
| Impresión legible | Térmica corrida o tóner bajo = escaneo fallido |
| Un SKU por caja, salvo indicación contraria | Las cajas mixtas generan faltantes |
| Producto en condición de venta | Full no revisa calidad por ti: lo que mandas, se vende |
| Dimensiones dentro de lo permitido | Requisito oficial; fuera de rango, no es apto |

## El riesgo que no ves venir: el lote defectuoso

Los únicos reclamos que cuentan contra tu reputación son los de **producto incompleto/faltante** y
de **calidad** (oficial). Full no te protege: ML despacha lo que tú mandaste, sin abrirlo.

Con inventario propio detectas un lote malo al tercer pedido. Con Full lo detecta el comprador,
quince veces, y las quince cuentan. Para conservar el verde no puedes superar **3,5% de ventas con
reclamos** (oficial ML Colombia, verificado sep-2026) — con 100 ventas al mes, son tres reclamos y
medio de margen. Un lote malo te lo come en dos días.

```
□ Revisa una muestra real del lote ANTES de empacarlo para bodega
□ Con producto o proveedor nuevo, revisa unidad por unidad la primera vez
□ Proveedor con historial de fallas: no lo metas a Full hasta estabilizarlo
□ Ante la primera racha de reclamos de calidad, pausa el SKU
□ Responde los mensajes en menos de 24 horas hábiles o pierdes la exclusión (`136`)
```

## Cuánto mandar: el cálculo

| Error | Costo |
|---|---|
| Mandaste de más | Bodegaje + cargo de stock antiguo desde el mes 4 (`108`) + plata quieta |
| Mandaste de menos | Quiebre: publicación pausada, catálogo perdido, algoritmo reiniciado |

Fórmula de trabajo:

```
UNIDADES A ENVIAR = venta diaria promedio × (días de cobertura + lead time) + colchón

lead time = días de preparar + días de traslado + días de recepción en bodega
```

El `lead time` es el número que casi nadie mide y el que decide todo. Cronométralo en tu primer
envío y anótalo: con Full, reponer nunca es "mañana".

Regla de tope: **nunca mandes más de 120 días de venta.** Ese es el día en que empieza a correr el
cargo por stock antiguo (4 meses, oficial; 2 meses en Supermercado).

## El calendario de reposición

| Señal | Acción |
|---|---|
| Stock equivalente a lead time + 7 días | Prepara el siguiente envío HOY |
| Se acerca fecha de alta demanda | Adelanta la reposición varias semanas |
| Un SKU no se mueve hace 60 días | Deja de reponerlo y planea el retiro (`108`) |

Hot Sale Colombia 2026 tiene edición del **19 al 23 de octubre de 2026** (verificado). Si vendes
ahí con Full, el inventario debe estar **recibido** con semanas de anticipación — y calcula la
fecha de retiro de lo que sobre antes de mandarlo, no después.

## El error clásico

Hacer el primer envío sin cronometrar nada: sin saber cuánto costó el traslado, cuántos días tardó
la recepción, ni comparar unidades enviadas contra recibidas. Ese primer envío es tu única
oportunidad barata de medir el `lead time` y el costo real por unidad.

**El primer envío a Full no es logística: es un experimento. Anota todo.**

## Relacionados

`103` Full · `105` cuándo conviene Full · `107` costo de almacenamiento · `108` inventario viejo ·
`110` empacar sin perder plata · `111` embalaje que evita reclamos · `117` frágiles · `123`
inventario en dos canales · `124` auditoría mensual · `126` las tres métricas · `136` reclamos
excluibles · `196` la sobreventa multicanal
