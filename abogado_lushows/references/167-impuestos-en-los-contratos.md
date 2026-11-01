# 167 — Impuestos en los contratos

Muchos contratos dicen "precio: $10.000.000" y nada más. Luego aparece la pregunta: ¿ese valor incluye IVA? ¿Quién asume la retención en la fuente? ¿Y el ICA, el 4x1000, el timbre? ¿Y si cambia la ley tributaria durante el contrato? Una **cláusula de impuestos** clara evita que el margen se evapore en discusiones. Esto es especialmente importante en contratos internacionales, donde una retención inesperada puede comerse el 15% o más del pago.

## Conceptos clave
- **Precio "más IVA" vs. "IVA incluido":** define si el IVA se suma al precio o ya está adentro.
- **Retención en la fuente:** el cliente retiene parte del pago como anticipo del impuesto del proveedor; no es un descuento del precio, es un pago a cuenta (ver **contador_lushows**).
- **ICA y reteICA:** impuesto municipal de industria y comercio y su retención.
- **GMF (4x1000):** gravamen a los movimientos financieros (Estatuto Tributario, art. 871).
- **Impuesto de timbre:** grava ciertos documentos y actos; su tarifa ha cambiado en el tiempo (verificar si aplica a tu contrato).
- **Gross-up:** cláusula por la cual el pagador aumenta el pago para que el beneficiario reciba el neto pactado después de retenciones (típico en pagos al exterior).
- **Cambio en la ley (*change in law*):** cláusula sobre qué pasa si cambian los impuestos.

## Qué dice la norma
- La ley define **quién es sujeto pasivo** de cada impuesto; el contrato solo puede repartir **el costo económico** entre las partes, no cambiar quién responde ante la DIAN.
- Estatuto Tributario: IVA (arts. 420 y ss.), retención en la fuente (arts. 365 y ss.), GMF (arts. 870 y ss.), pagos al exterior y retenciones (arts. 406 y ss.); convenios para evitar la doble imposición firmados por Colombia (verificar los vigentes).
- ICA: normas de cada municipio sobre la base de la Ley 14 de 1983 (verificar).

## Checklist de la cláusula de impuestos
1. **Precio:** "más IVA" o "IVA incluido", y a qué tarifa (`164`).
2. **Retenciones:** el cliente practicará las retenciones legales y entregará certificados.
3. **Impuestos de cada parte:** cada una asume los que la ley le impone (renta, ICA propio).
4. **Pagos internacionales:** quién asume la retención del país de la fuente; si hay *gross-up*; si aplica convenio de doble imposición y qué certificados se requieren (residencia fiscal).
5. **Cambio en la ley:** si un nuevo impuesto encarece el contrato, ¿se ajusta el precio o se reparte?
6. **Timbre** y otros impuestos documentales, si aplican.

## Cláusula modelo
> "**Impuestos.** Los precios de este contrato no incluyen IVA, el cual se facturará a la tarifa legal vigente. Cada parte asumirá los impuestos, tasas y contribuciones que la ley ponga a su cargo. EL COMPRADOR practicará las retenciones en la fuente aplicables y entregará los certificados correspondientes en los plazos legales. Si durante la vigencia se crea un nuevo impuesto o se modifica una tarifa que afecte directamente el precio de los bienes suministrados, las partes negociarán de buena fe el ajuste del precio dentro de los [30] días siguientes a la entrada en vigencia de la norma."

**Variante para cobrar desde el exterior (tú exportas un servicio):**
> "Todos los pagos se harán libres de deducciones o retenciones. Si la ley exige practicar una retención, EL CLIENTE incrementará el pago de modo que EL PROVEEDOR reciba el valor neto pactado, salvo que la retención sea acreditable por EL PROVEEDOR en Colombia, caso en el cual EL CLIENTE entregará el certificado de retención."

## Riesgos y errores comunes
- **Alto:** precio pactado "IVA incluido" sin darse cuenta → pierdes el margen.
- **Alto:** cobrar servicios al exterior sin pactar quién asume la retención en el país del cliente.
- **Medio:** no exigir certificados de retención (no podrás descontarlas).
- **Bajo:** no prever cambios de ley en contratos largos.

## Conexión con otros módulos
`100` plantilla · `141` precio · `164` IVA · `177` contratos transfronterizos · `162` SIMPLE · **contador_lushows** (retenciones, ICA, convenios) · **Matematicas_lushows** (cálculo de *gross-up*).

## Siguiente paso típico
Revisar tus 5 contratos principales: ¿dicen si el precio incluye IVA y quién asume cada impuesto? Si no, corregirlo en el próximo otrosí (`109`).
