# El tablero semanal

Una sola página, un solo día de la semana, veinte minutos. Lo que no cabe en esa página no se mira.
Este módulo te da el formato listo para copiar, el orden exacto de lectura y las tres cifras que,
si se prenden, cancelan todo lo demás que ibas a hacer esa semana.

## Las reglas del tablero

| Regla | Por qué |
|---|---|
| **Un solo día fijo** — lunes en la mañana | Comparar semanas iguales; el lunes ya tienes el fin de semana cerrado |
| **Una sola página** | Si no cabe, no es un tablero, es un informe que nadie lee |
| **Datos de la semana cerrada**, no de hoy | La pauta tarda hasta 72 h en reflejar ventas (`151`) |
| **Siempre la semana anterior al lado** | Un número solo no dice nada; una tendencia sí |
| **Máximo tres acciones al final** | El tablero termina en decisiones o no sirvió (`165`) |

## Orden de lectura (no lo cambies)

```
1. ALARMAS      ¿hay algo que me pueda cerrar la cuenta?     → si sí, para todo
2. PLATA        ¿gané o solo facturé?
3. PRODUCTO     ¿qué SKU carga el mes y cuál está muerto?
4. TRÁFICO      ¿por qué entró o no entró gente?
5. PAUTA        ¿la publicidad paga o me la estoy comiendo?
6. STOCK        ¿qué se me acaba y qué se me quedó?
7. LAS 3 ACCIONES
```

Se lee de arriba abajo y **no se salta**. El vendedor que arranca por "cuánto vendí" termina
celebrando un mes récord con la tasa de cancelaciones en rojo.

## Bloque 1 · Alarmas (las tres cifras que cancelan la semana)

| Cifra | Límite | Si se pasa |
|---|---|---|
| **Ventas canceladas** | más de **2,5%** → suspensión de la cuenta | Para todo, corrige stock, no hagas nada más esa semana (`139`) |
| **Reclamos** | **2,5%** es el corte de MercadoLíder | Revisa ficha y empaque antes de tocar precio o pauta (`126`) |
| **Días con stock en cero** | cualquier valor mayor que 0 | Repón ya: el cero te saca del catálogo y de la competencia (`140`) |

(los dos primeros, oficial ML Colombia, verificado sep-2026). Los límites para **conservar el verde**
son otros y dependen de si te evalúan a 60 o a 365 días: copia la tabla de `126` al lado de esta.

## El formato — copia esta tabla

```
SEMANA DEL ___ AL ___                                    Leído el lunes ___

── ALARMAS ─────────────────────────────────────────────────────────────
Canceladas %          ____   (límite 2,5%)      sem. ant. ____
Reclamos %            ____   (límite 2,5%)      sem. ant. ____
Envíos con problema % ____   (límite 10%)       sem. ant. ____
Mediaciones %         ____   (límite 0,5%)      sem. ant. ____
Días con stock en 0   ____                      SKUs afectados: ________

── PLATA ───────────────────────────────────────────────────────────────
Ventas (unidades)     ____                      sem. ant. ____
Facturación COP       ____                      sem. ant. ____
Utilidad COP          ____                      sem. ant. ____
Margen % promedio     ____                      sem. ant. ____
Ticket promedio COP   ____                      sem. ant. ____

── PRODUCTO (top 5 por utilidad, no por unidades) ──────────────────────
SKU            Unid.   Facturación   Utilidad   Margen%   Conversión%
1. ________    ____    __________    ________   ______    __________
2. ________    ____    __________    ________   ______    __________
3. ________    ____    __________    ________   ______    __________
4. ________    ____    __________    ________   ______    __________
5. ________    ____    __________    ________   ______    __________
% del top-1 sobre la utilidad total: ____   (alarma si > 50%, ver `172`)
SKUs sin una sola venta en 30 días: ____

── TRÁFICO ─────────────────────────────────────────────────────────────
Visitas totales       ____      sem. ant. ____
Conversión general %  ____      sem. ant. ____
Preguntas recibidas   ____      Respondidas < 24 h: ____

── PAUTA (dato con hasta 72 h de rezago) ───────────────────────────────
Inversión COP         ____
Ventas atribuidas COP ____
ACOS %                ____      objetivo declarado: ____  (`150`)
TACOS %               ____

── STOCK ───────────────────────────────────────────────────────────────
SKUs con menos de 15 días de inventario: ______________  → reponer
SKUs con más de 90 días de inventario:   ______________  → liquidar (`168`)

── LAS 3 ACCIONES DE ESTA SEMANA ───────────────────────────────────────
1. ______________________________________________  responsable: ______
2. ______________________________________________  responsable: ______
3. ______________________________________________  responsable: ______
```

## De dónde sale cada número

| Bloque | Fuente |
|---|---|
| Alarmas | Mi cuenta → Reputación, o `GET /users/$USER_ID` → `seller_reputation.metrics` |
| Plata | Tus órdenes cruzadas con tus costos. **ML no conoce tu costo: la utilidad la calculas tú** |
| Producto | `GET /orders/search?seller=$SELLER_ID` + métricas de visitas por ítem |
| Tráfico | Panel de métricas de cada publicación |
| Pauta | Marketing → Publicidad → Reportes (descarga Excel) |
| Stock | Tu inventario, no el de ML |

Si ya automatizaste la descarga, el bloque de API está en `180`; si aún no, una hoja de cálculo
llena a mano en veinte minutos es suficiente hasta unas 200 ventas al mes.

## El error clásico

Construir un tablero precioso con quince pestañas, llenarlo tres semanas y abandonarlo. Pasa
siempre por lo mismo: pedía datos que hay que sacar a mano de cinco pantallas distintas. **Un
tablero que no se llena en veinte minutos está muerto antes de nacer.** Arranca con la página de
arriba; si en dos meses te quedó corta, agregas una fila — nunca una pestaña.

## Qué hacer con la página vieja

Guárdalas todas en la misma hoja, una fila por semana. A los tres meses tienes lo que ML nunca te
va a dar: **la película**. El panel te muestra la foto de hoy; la tendencia de tu conversión, de tu
margen y de tus reclamos solo existe si tú la escribes (`144`).

## Relacionados

`126` las tres métricas · `127` el periodo de evaluación · `139` la cancelación y su castigo ·
`140` el quiebre de stock · `144` plan de defensa de la reputación · `150` ACOS sano ·
`151` leer los reportes de Ads · `165` las métricas que de verdad miras ·
`167` estacionalidad en Colombia · `168` planear el inventario · `172` el SKU estrella ·
`180` bajar tus datos por API
