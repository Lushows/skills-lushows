# 163 — Factura electrónica: aspectos legales

La factura electrónica no es solo una obligación tributaria: es **prueba de la venta**, **soporte de costos** para tu cliente, y puede ser un **título valor** que se cobra en un proceso ejecutivo o se negocia en factoring. Emitirla mal (o no emitirla) trae sanciones de la DIAN, rechazo de deducciones a tus clientes y pérdida de herramientas de cobro. Lo técnico (validación previa, software, anexos) lo cubre **contador_lushows**; aquí, lo legal.

## Conceptos clave
- **Validación previa:** la DIAN valida la factura antes de que se entregue al adquirente.
- **CUFE:** código único de la factura electrónica.
- **Nota crédito / nota débito:** documentos para corregir, anular o ajustar una factura (no se "borra" una factura).
- **Documento soporte:** el que expide el comprador cuando adquiere bienes o servicios a personas no obligadas a facturar.
- **Eventos (RADIAN):** acuse de recibo, recibo del bien o servicio, aceptación o rechazo; necesarios para que la factura funcione como título valor (`126`).
- **Factura de exportación:** con requisitos propios.

## Qué dice la norma (verificar vigencia)
- Estatuto Tributario: obligación de facturar (art. 615), requisitos de la factura (art. 617), factura electrónica (art. 616-1).
- Resoluciones de la DIAN que fijan el anexo técnico y el calendario de implementación (por ejemplo, la Resolución 000165 de 2023 y las que la modifiquen; **verificar la vigente**).
- Código de Comercio, arts. 772 y ss., modificados por la Ley 1231 de 2008: factura como título valor; aceptación expresa o tácita.
- Decreto 1154 de 2020: circulación de la factura electrónica como título valor.
- Sanciones por no facturar o hacerlo sin requisitos, incluida la clausura del establecimiento en ciertos casos (Estatuto Tributario, arts. 652, 657 y relacionados; verificar).

## Checklist legal
1. **Facturar toda venta**, incluidas las de marketplace y las preventas (según instrucción de **contador_lushows**).
2. **Datos correctos del cliente** (razón social, NIT): un error impide que deduzca el costo y hace que rechace la factura.
3. **Descripción suficiente** del bien o servicio, ligada al contrato u orden de compra.
4. **Fecha de vencimiento** y forma de pago coherentes con el contrato y con la Ley 2024 de 2020 (`144`).
5. **Notas crédito** para devoluciones o descuentos, nunca facturas "anuladas" de hecho.
6. **Documento soporte** cuando compras a quien no factura (por ejemplo, un pequeño productor rural).
7. **Seguimiento de eventos** en RADIAN para cartera importante.

## Ejemplo (cláusula en contrato de suministro)
> "EL PROVEEDOR emitirá factura electrónica de venta por cada entrega, con referencia a la orden de compra y a la remisión correspondiente. EL COMPRADOR podrá rechazar la factura solo por causas objetivas (errores en datos, precio o cantidad), mediante el evento de rechazo en el sistema de la DIAN dentro de los [3] días hábiles siguientes a su recepción, indicando la causa. Las diferencias se corregirán mediante nota crédito o débito."

*Por qué:* evita rechazos arbitrarios para "ganar plazo" y alinea el contrato con el sistema de eventos.

## Riesgos y errores comunes
- **Alto:** no facturar ventas (sanción y posible clausura).
- **Alto:** facturas con datos errados del cliente que no te pagan "hasta que corrijas" → pierdes semanas.
- **Medio:** no emitir documento soporte en compras a no obligados (pierdes la deducción).
- **Bajo:** no conservar XML y representación gráfica.

## Conexión con otros módulos
`94` títulos valores · `126` factoring y RADIAN · `144` Ley 2024 · `159` conservación · `168` sanciones · **contador_lushows** (implementación técnica, nómina electrónica, notas) · **engineer_visualopen_lushows** (integración con software).

## Siguiente paso típico
Revisar con tu cliente grande el flujo de eventos (acuse y recibo) y pactarlo en el contrato; con **contador_lushows**, verificar que el software emita documento soporte.
