# Facturación electrónica de tus ventas

Cada venta en Mercado Libre es una venta real ante la DIAN, y el comprador tiene derecho a
pedirte factura. Facturar a mano 200 órdenes al mes no es sostenible: por eso el punto central
de este módulo es **la integración que emite la factura DIAN automáticamente por cada venta**.

## Lo que sí está verificado

**Alegra tiene integración directa y documentada con Mercado Libre para Colombia.** Sincroniza
las ventas, crea el contacto del cliente, descuenta el inventario y **emite la factura
electrónica DIAN** por cada orden. Requiere tener la numeración electrónica activa
(verificado, confianza ALTA).

Eso resuelve el 90% del problema operativo: dejas de facturar a mano.

| Integrador | Estado para Colombia + ML |
|---|---|
| **Alegra** | Integración confirmada y documentada (ALTA) |
| Siigo | API robusta, **sin confirmación** de integración nativa con ML (BAJA) |
| Bsale | Fuerte en Chile/LatAm, cobertura CO no verificada (BAJA) |
| Desarrollo propio por API | Posible, pero ver el veredicto de abajo |

**Si lo que necesitas es facturar, no programes: Alegra ya lo resolvió.** Construir tu propio
puente OAuth + webhooks + deduplicación + proveedor tecnológico DIAN te cuesta semanas y
mantenimiento eterno para replicar algo que ya existe. Ver `175` (cuándo NO programar).

## Quién está obligado a facturar

Esto es de `contador_lushows`, no lo resuelvas de memoria. Lo que necesitas saber como vendedor
de marketplace:

- Si eres responsable de IVA, facturas.
- Si estás en el Régimen Simple, facturas.
- Hay casos de no obligados, pero **incluso el no obligado debe entregar un documento
  equivalente si el comprador lo exige**.
- La obligación es tuya, no de Mercado Libre. ML no factura por ti.

→ Confirma tu caso exacto con `contador_lushows` antes de publicar la primera unidad.

## Qué pide el comprador y cuándo

| Escenario | Qué espera el comprador |
|---|---|
| Compra personal, producto barato | Normalmente nada |
| Compra personal, producto caro | Factura para respaldar la garantía (`23`) |
| Compra empresarial | **Factura con su NIT, siempre.** Sin factura no te vuelve a comprar |
| Reclamo o devolución | La factura es el soporte de la operación (`22`, `138`) |

El comprador empresarial es un segmento entero que se pierde si no facturas bien y rápido. En
categorías de insumos, herramientas, tecnología y oficina, es la mitad del mercado.

## El flujo automatizado, paso a paso

```
□ Ten la numeración de facturación electrónica habilitada ante la DIAN
□ Ten el proveedor tecnológico operando (Alegra lo es)
□ Conecta la cuenta de Mercado Libre desde Alegra (OAuth, autorizas y listo)
□ Configura: qué numeración usa, qué producto/servicio mapea a cada publicación,
  qué pasa con el envío y la comisión
□ Haz UNA venta de prueba y revisa la factura emitida línea por línea
□ Verifica que el IVA, el valor y los datos del cliente salgan correctos
□ Solo entonces déjalo corriendo
```

El paso que la gente se salta es el de revisar la primera factura completa. Si el mapeo de
impuestos quedó mal, no te enteras hasta que llevas 400 facturas emitidas con IVA equivocado y
hay que emitir 400 notas crédito.

## Las tres trampas de facturar ventas de marketplace

| Trampa | Qué pasa |
|---|---|
| **Datos del comprador incompletos** | ML no siempre entrega NIT: facturas a consumidor final y el comprador empresarial reclama |
| **Devoluciones** | Cada una necesita **nota crédito**. Si facturas automático y no anulas, el IVA se infla |
| **Precio con IVA adentro** | El precio publicado incluye IVA: la factura debe desagregarlo (`12`) |

La de las devoluciones es la más cara: en categorías con 30 días de devolución para productos
nuevos (oficial, ver `138`), un porcentaje real de tus facturas hay que reversarlo. Si el
proceso de nota crédito no está automatizado o al menos calendarizado, pagas IVA sobre ventas
que no existieron.

**Facturar automático sin anular automático es peor que facturar a mano: multiplicas el error
en vez del trabajo.**

## Qué NO hace la integración por ti

- No decide tu régimen ni tu responsabilidad de IVA.
- No liquida ni presenta declaraciones.
- No emite la nómina electrónica.
- No concilia lo que Mercado Pago te acreditó contra lo que facturaste (eso lo revisas tú, con
  los reportes de `13`).
- No te exime de llevar los libros.

Todo eso es `contador_lushows`.

## La conciliación que sí tienes que hacer tú

Una vez al mes, cuadra tres números:

```
□ A = Ventas reportadas por Mercado Libre en el periodo
□ B = Facturas emitidas en el periodo
□ C = Dinero acreditado en Mercado Pago en el periodo
```

A y B deben coincidir (salvo devoluciones ya anuladas). A y C **nunca** coinciden, porque entre
medio están la comisión, los cargos, el envío y las retenciones (`13`), más el desfase de la
liberación del dinero (`15`). Si A ≠ B, hay facturas sin emitir o duplicadas y eso sí es un
problema ante la DIAN.

Si el cálculo tiene que ser exacto para una declaración, ejecútalo:
→ `Matematicas_lushows`.

## El error clásico

Arrancar a vender "y después arreglo lo de la factura". A los seis meses hay 600 ventas sin
facturar, el comprador empresarial ya se fue, y regularizar implica emitir facturas con fecha
vieja o asumir el costo. Es mucho más barato tener la facturación resuelta el día uno, cuando
son cero facturas, que el día 180.

## Checklist de arranque

```
□ Confirmado con contador si estoy obligado a facturar
□ RUT con la responsabilidad correcta → `12`
□ Numeración electrónica habilitada ante la DIAN
□ Integración conectada (Alegra) y probada con una venta real
□ Proceso definido para notas crédito por devolución
□ Reporte mensual de ML descargado y conciliado → `13`
```

## Relacionados

`12` datos fiscales y RUT · `13` retenciones y reportes · `15` liberación del dinero ·
`22` retracto · `23` garantías · `138` devoluciones · `166` operación con datos ·
`175` cuándo NO programar · `contador_lushows` para la obligación, la liquidación y los libros
