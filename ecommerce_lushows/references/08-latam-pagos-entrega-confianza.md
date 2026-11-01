# 08 · México y LatAm: precio total, MSI, OXXO, entrega y confianza

> Vigencia: 16-sep-2026. Pasarelas a fondo y comisiones → `dropshipping_lushows` 192-195.
> Aquí: **cómo se muestra** en la página para que convierta y cumpla la ley.

## Obligatorio en México

- **LFPC art. 7 Bis:** mostrar "de forma notoria y visible el monto total" con impuestos, comisiones
  y cargos. → Precio **con IVA incluido** y envío claro **antes** del checkout. [V]
- **LFPC art. 76 Bis (comercio electrónico):** términos, costos, cargos adicionales y formas de pago
  visibles; datos del proveedor (razón social, contacto). [V]
  diputados.gob.mx/LeyesBiblio/pdf/LFPC.pdf

## Meses sin intereses (MSI)

- Mostrar bajo el precio: *"o 6 × $566.33 sin intereses con tarjetas participantes"* + link a bancos.
- Datos citados: 40-50% de compras online con MSI, +15% conversión, +30% ticket **[S: blogs de
  proveedores, no auditado]**.
- **La comisión la paga el comercio y sube con el plazo** → calcular margen antes de ofrecer 12 MSI
  (`dropshipping_lushows` 195 + `Matematicas_lushows`).
- Calcular la cuota en código y redondear a centavos; no mostrar "desde" engañoso.

## Efectivo, OXXO, SPEI

- Banxico: ~80% usa efectivo como medio principal; 20-25% prefiere efectivo o no tiene tarjeta [S].
- Íconos **monocromos** junto al botón: tarjeta · MSI · OXXO Pay · SPEI · Mercado Pago.
- Explicar el voucher en una línea: *"Pagas en OXXO con tu referencia; tienes 48 h."*

## Contra entrega (COD)

- 20-40% de rechazo en dropshipping mal gestionado; confirmación por WhatsApp antes de despachar lo
  reduce [S]. **No usar** la cifra "50-55% del ecommerce MX es COD" (sin fuente primaria).
- Recomendación: **prepago con incentivo honesto** (envío gratis / regalo) + COD opcional con
  confirmación obligatoria por WhatsApp. Señales: "Pagas al recibir" + guía rastreable + foto real del empaque.
- Proyecto activo de Luis: prepago, stock local (ver `dropshipping_lushows` SKILL.md).

## Fecha de entrega

- "Llega entre el **mié 23** y el **vie 25**" calculado en JavaScript desde hoy, saltando domingos,
  con corte horario ("pide antes de las 14:00"). En provincia, rango más amplio.
- Es la regla 10 de Baymard aplicada (`03`). Nunca prometer una fecha que la paquetería no cumple.

## WhatsApp

- Botón "¿Dudas? Escríbenos" con mensaje prellenado que incluye **producto, paquete y precio**
  (sirve de atribución). Va **debajo** del botón de compra, nunca en su lugar.

## Formato

- México: `$1,899` (coma de miles, punto decimal), "MXN" una vez cerca del precio.
- Colombia: `$189.900` (punto de miles), "cuotas" en vez de MSI, "contraentrega".
- `Intl.NumberFormat('es-MX', {style:'currency', currency:'MXN'})` — nunca formatear a mano.
- Sin centavos cuando terminan en ,00.

## Garantía en términos locales

- *"30/60 días para cambio o devolución; te mandamos la guía."* Enlace a condiciones completas.
- Mencionar PROFECO en la página de condiciones como derecho del consumidor, **sin logos oficiales**.
