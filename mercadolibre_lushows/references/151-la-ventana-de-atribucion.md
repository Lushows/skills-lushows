# La ventana de atribución

Cuándo y cómo Mercado Ads decide que una venta fue "gracias a tu anuncio". Entender esto es lo que
te impide tomar decisiones tontas mirando el reporte de ayer, que es el error operativo más común
de toda la pauta.

## Las tres reglas

| Regla | Qué dice |
|---|---|
| **14 días post-clic** | Si alguien hizo clic en tu anuncio y compra dentro de los 14 días siguientes, esa venta se atribuye a la campaña |
| **Última impresión, 24 horas** | Si no hay clic atribuible, cuenta la última vez que se le **mostró** el anuncio, dentro de las 24 horas previas a la compra |
| **Ventas indirectas** | Si hace clic en un anuncio tuyo y termina comprando **otro producto tuyo**, esa venta también se atribuye a la campaña |

## Qué implica cada una

**Los 14 días post-clic** significan que la campaña que encendiste hoy sigue sumando ventas dentro
de dos semanas. Apagarla hoy no detiene las ventas atribuidas de mañana, y encenderla hoy no
muestra su verdadero rendimiento hasta el día 15.

**La última impresión de 24 horas** significa que se te atribuyen ventas de gente que ni siquiera
te clicó. Es atribución generosa: infla el ACOS a tu favor en volumen, pero también te hace creer
que la pauta hizo más de lo que hizo.

**Las ventas indirectas** son la más traicionera. Pautas el SKU A, el comprador entra, mira tu
tienda y se lleva el SKU B. La venta del B entra al ACOS de la campaña del A. Consecuencia
práctica: **el ACOS de una campaña puede verse bien gracias a un producto que ni siquiera estás
pautando.** Cuando el reporte no cuadra con lo que ves en tus órdenes, esto es lo primero a
revisar (`155`).

## La demora de los reportes: 72 horas

Las ventas pueden tardar **hasta 72 horas** en aparecer en el reporte (oficial ML Colombia,
verificado sep-2026). No es un error del panel: es el tiempo que tarda el sistema en confirmar y
atribuir.

| Si miras… | Lo que ves |
|---|---|
| Hoy | Gasto casi completo, ventas casi ninguna → ACOS aterrador y falso |
| Ayer | Gasto completo, ventas parciales → ACOS inflado |
| Hace 3 días | Gasto y ventas casi cerrados → dato usable |
| Hace 14+ días | Atribución cerrada de verdad → dato firme |

**El ACOS de ayer siempre se ve peor de lo que fue.** Si optimizas mirándolo, vas a apagar
campañas que estaban funcionando. Esa es la trampa: el panel te muestra el gasto en tiempo real y
las ventas con retraso, así que la foto instantánea siempre miente en la misma dirección.

## La consecuencia operativa

```
□ No mires el reporte de hoy para tomar decisiones. Ninguna. Nunca
□ La ventana mínima de lectura es de 14 días corridos sin tocar nada
□ Al leer, descarta los últimos 3 días: su atribución aún no cerró
□ Al apagar una campaña, espera 14 días antes de declarar el resultado final
□ Si cambias algo, el reloj de 14 días vuelve a cero
```

Por eso la rutina de optimización es **semanal o quincenal, nunca diaria** (`156`).

## Comparación con lo que ya conoces

Si vienes de Meta o Google, la mecánica es parecida pero los plazos no:

| | Mercado Ads | Meta / Google |
|---|---|---|
| Ventana de clic | 14 días | Configurable (1, 7, 28 días) |
| Ventana de vista | 24 horas | Configurable (1 día es lo común) |
| ¿Eliges la ventana? | **No.** Viene fija | Sí |
| Demora del reporte | Hasta 72 horas | Minutos a horas |
| Ventas de otros productos | **Sí, se atribuyen** | Depende del pixel y del catálogo |

La diferencia que más duele al llegar de Meta es la demora: allá optimizas con datos de la mañana,
aquí con datos de la semana pasada. Si gestionas los dos canales, **no uses la misma rutina**
(`163`).

## Qué NO cubre la atribución

| Caso | ¿Se atribuye? |
|---|---|
| Vio el anuncio, no clicó, compró 3 días después | No (pasaron las 24 horas de la impresión) |
| Clicó, compró a los 20 días | No (pasaron los 14 días) |
| Clicó y compró otro producto tuyo a los 5 días | **Sí**, como venta indirecta |
| Clicó, no compró, pero volvió por búsqueda orgánica y compró al día 10 | Sí — y por eso el orgánico se ve peor de lo que es (`153`) |
| Compró y después canceló o devolvió | El reporte no descuenta tu costo de devolución (`95`) |

El último punto importa para el margen: el ACOS del reporte cuenta ventas brutas. Las
devoluciones te las comes tú y no aparecen en la métrica. Es una razón más para apuntar a **dos
tercios de tu margen** y no al techo (`150`).

## El error clásico

Encender la campaña un lunes, mirarla el miércoles, ver un ACOS de 80% y apagarla. La campaña
nunca estuvo en 80%: estaba en la mitad de su ventana de atribución con el gasto ya contabilizado
y las ventas todavía no. El vendedor promedio repite este ciclo tres o cuatro veces, concluye que
"Mercado Ads no sirve" y nunca llega a tener un dato real. **Dos semanas de paciencia valen más
que cualquier optimización.**

## Checklist antes de juzgar una campaña

```
□ Han pasado al menos 14 días corridos desde el encendido
□ No cambié presupuesto, estrategia, precio ni ficha durante esos 14 días
□ Estoy leyendo un rango que termina hace 3 días o más
□ Descarté que el ACOS esté inflado por ventas indirectas de otro SKU
□ Comparo contra el margen neto de ESE SKU, no contra un benchmark (`150`)
□ Anoté el resultado y la fecha para comparar con el siguiente periodo
```

## Relacionados

`146` Product Ads · `147` la subasta y el CPC · `148` las tres estrategias ·
`149` ACOS y TACOS · `150` el ACOS sano según tu margen · `152` pautar una publicación nueva ·
`153` el efecto sobre lo orgánico · `155` leer los reportes ·
`156` optimizar semana a semana · `163` tráfico externo · `95` costo oculto de la devolución ·
`97` margen por SKU
