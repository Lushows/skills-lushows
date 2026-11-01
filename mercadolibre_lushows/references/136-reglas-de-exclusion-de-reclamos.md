# Reglas de exclusión de reclamos

Módulo de oro. No todos los reclamos golpean tu reputación: hay una lista oficial de casos
excluibles y un procedimiento para pedirlo. Casi ningún vendedor colombiano lo usa, y por eso carga
en el termómetro casos que ML mismo dice que no deberían contar.

## Los reclamos que SÍ se pueden excluir

Lista oficial (oficial ML Colombia, verificado sep-2026):

| Caso | Por qué se excluye |
|---|---|
| **Error del comprador** | Compró lo que no era, se equivocó de talla, de modelo, de cantidad |
| **Arrepentimiento con producto en perfecto estado** | Cambió de opinión; el producto está bien |
| **Demora si despachaste a tiempo** | El transportador se demoró, tú cumpliste |
| **"Entregado" no reconocido** | El sistema marca entregado y el comprador dice que no lo recibió |
| **Fallas de la plataforma** | El problema fue de Mercado Libre, no tuyo |
| **Reclamo abierto antes de 24 h desde tu último mensaje** | El comprador no te dio tiempo de responder |
| **Uso del reclamo como medio de contacto** | Abrió el reclamo solo para preguntar algo |

Además, dos excepciones que operan **por regla general, sin que tengas que pedir nada** (oficial ML
Colombia, verificado sep-2026):

```
□ Los reclamos por ARREPENTIMIENTO del comprador no cuentan contra tu reputación
□ Las ventas canceladas POR LA PERSONA QUE TE COMPRÓ no cuentan como cancelación tuya
□ En la categoría INMUEBLES, las ventas no afectan la reputación en absoluto
```

## Los que NO se pueden excluir

| Caso | Por qué |
|---|---|
| Producto defectuoso o distinto al anunciado | Es tuyo |
| Faltaron unidades o partes | Es tuyo |
| No despachaste a tiempo | Es tuyo |
| Falta de stock | Es tuyo |
| El comprador alega que el producto es falso | Es tuyo, y además abre otro frente (`143`) |

Estos cinco son exactamente las dos familias que ML cuenta como reclamo real: **producto
incompleto/faltante y problemas de calidad** (`126`). No hay negociación posible con ellos: se
previenen en la ficha y en el empaque, no en el trámite.

## El corte que te quita el derecho

> **Si no respondes los mensajes en 24 horas hábiles, pierdes el derecho a pedir la exclusión.**
> (oficial ML Colombia, verificado sep-2026)

Este es el punto donde se pierde la mayoría de las exclusiones. No las pierdes porque el caso no
fuera excluible: las pierdes porque contestaste el martes lo que llegó el viernes. Ver `133`.

Y nota la simetría de la lista de arriba: **si el comprador abre el reclamo antes de que pasen 24
horas desde tu último mensaje, el reclamo es excluible**. Los dos relojes corren al mismo tiempo,
uno a tu favor y otro en tu contra. Responder rápido gana los dos.

## Cómo se pide

```
□ 1. Responde al comprador dentro de las 24 horas hábiles. Esto es lo que habilita todo
□ 2. Resuelve el caso: repone, reembolsa o aclara. La exclusión no reemplaza la solución
□ 3. Documenta en el canal de ML por qué el caso encaja en una de las causales
□ 4. Pide la exclusión desde el detalle del reclamo en tu panel
□ 5. Guarda la evidencia: guía con fecha de despacho, foto del paquete, hilo de mensajes
□ 6. Verifica una semana después que la métrica efectivamente no lo contó (`126`)
```

> ⚠️ **Sin verificar para Colombia (sep-2026).** La ubicación exacta del botón de solicitud de
> exclusión y el plazo que ML tarda en responderla no están publicados. Se gestiona desde el detalle
> del reclamo en Mi cuenta → Ventas. Si no lo encuentras, pídelo por el canal de atención — siendo
> MercadoLíder tienes chat (`130`).

El paso 6 es el que nadie hace y el que revela si el sistema te está contando mal. Compara el
`seller_reputation.metrics.claims.value` de antes y de después (`126`).

## Reclamos con solicitud de cancelación: el caso especial

Es un caso aparte y muy favorable (oficial ML Colombia, verificado sep-2026):

| Regla | Detalle |
|---|---|
| Efecto inicial | **No afectan la reputación desde el inicio** |
| Tu plazo | **2 días hábiles** para reembolsar, sin haber entregado |
| Si cumples | Reputación **intacta** |
| Si no cumples | El reembolso se hace automático y **sí** te afecta |

Traducción: cuando alguien pide cancelar y aún no despachaste, **reembolsa el mismo día y no te pasa
nada**. Dudar dos días para ver si el cliente cambia de opinión es exactamente lo que convierte un
caso gratis en un caso que cuenta.

## La tabla de decisión rápida

Cuando entra un reclamo, clasifícalo en 30 segundos:

| Lo que dice el comprador | ¿Excluible? | Qué haces |
|---|---|---|
| "Ya no lo quiero" | Sí, arrepentimiento | Tramita la devolución (`138`) y pide exclusión |
| "Pedí el equivocado" | Sí, error del comprador | Devolución y exclusión |
| "Nunca llegó" y el tracking dice entregado | Sí | Evidencia de entrega + exclusión |
| "Llegó tarde" y despachaste a tiempo | Sí | Guía con fecha + exclusión |
| "Quiero saber cuándo llega" | Sí, uso como contacto | Responde y pide exclusión |
| "Llegó roto" | **No** | Repón o reembolsa. Revisa el empaque (`110`) |
| "Faltan piezas" | **No** | Envía lo faltante hoy. Revisa el checklist (`110`) |
| "No es lo que decía la publicación" | **No** | Resuelve y **corrige la ficha** (`30`) |
| "Quiero cancelar, no ha llegado" | Caso especial | **Reembolsa en 2 días hábiles** |

## El error clásico

Creer que pedir la exclusión es pelear con el cliente. No lo es: son dos cosas separadas. **Al
comprador le resuelves; a Mercado Libre le explicas por qué ese caso no era tuyo.** El vendedor que
confunde las dos termina discutiendo con el cliente y sin pedir la exclusión.

El segundo error: no pedir nada porque "igual es un solo reclamo". Con menos de 60 ventas, un solo
reclamo puede ser el 2,8% de tu ventana y perseguirte un año (`127`). **Un caso excluido es un año
de verde.**

## Qué hacer esta semana

```
□ Abre tus reclamos de los últimos 60 días y clasifícalos con la tabla de arriba
□ Cuenta cuántos eran excluibles y no pediste exclusión
□ Revisa si perdiste el derecho por responder tarde: ese es tu problema real
□ Si hay varios, arregla la bandeja antes que el producto (`133`)
```

## Relacionados

`126` las tres métricas · `127` el periodo de evaluación · `133` el tiempo de respuesta ·
`135` el reclamo y la mediación · `138` devoluciones · `139` la cancelación y su castigo ·
`141` el comprador problemático · `110` empaque · `144` plan de defensa de la cuenta
