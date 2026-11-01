# 94 — Títulos valores: factura, pagaré, letra y cheque

Un **título valor** es un documento que **incorpora un derecho** (normalmente, cobrar una suma de dinero) y que permite cobrarlo de forma **rápida** por proceso ejecutivo, sin tener que probar todo el contrato. Para una empresa que vende a crédito, saber emitir y recibir bien una factura o un pagaré es la diferencia entre cobrar en meses o en años.

## Conceptos clave (en simple)
- **Título valor:** documento necesario para legitimar el ejercicio del derecho literal y autónomo que en él se incorpora.
- **Literalidad:** vale lo que dice el documento, ni más ni menos.
- **Autonomía:** cada tenedor legítimo tiene un derecho propio, independiente de los anteriores.
- **Endoso:** forma de transmitir títulos a la orden (firma al respaldo o en documento adherido, o según las reglas electrónicas).
- **Girador / aceptante / beneficiario / tenedor:** quien crea, quien se obliga a pagar, a favor de quien se crea, quien lo tiene.
- **Factura electrónica como título valor:** factura de venta que cumple requisitos y fue **aceptada** (expresa o tácitamente) y registrada en el **RADIAN** de la DIAN para circular.
- **Pagaré:** promesa incondicional de pagar una suma.
- **Letra de cambio:** orden incondicional de pagar una suma dada por el girador al girado.
- **Cheque:** orden de pago contra un banco.
- **Título en blanco y carta de instrucciones:** título firmado con espacios sin llenar, que solo puede completarse según las instrucciones del firmante.

## Qué dice la norma (Colombia — verificar vigencia)
- **Código de Comercio, art. 619:** definición de títulos valores.
- **C.Co., art. 621:** requisitos comunes: la mención del derecho que en el título se incorpora y la firma de quien lo crea.
- **C.Co., art. 622:** títulos con espacios en blanco: deben llenarse estrictamente de acuerdo con las instrucciones del suscriptor.
- **C.Co., art. 671:** requisitos de la letra de cambio. **Art. 709:** requisitos del pagaré (promesa incondicional de pagar una suma determinada, nombre de la persona a quien deba hacerse el pago, indicación de ser pagadero a la orden o al portador y forma de vencimiento). **Arts. 712 y ss.:** cheque.
- **C.Co., arts. 772 a 779 (modificados por la Ley 1231 de 2008 y normas posteriores):** factura como título valor; aceptación expresa o **tácita** si el comprador no reclama dentro de los **tres días hábiles** siguientes a la recepción de la mercancía o del servicio (verificar redacción vigente); requisitos adicionales (fecha de vencimiento, fecha de recibo, estado de pago).
- **Decreto 1154 de 2020** (compilado en el DUR 1074 de 2015) y resoluciones de la DIAN: circulación de la **factura electrónica de venta como título valor** y el **RADIAN** (verificar).
- **C.Co., art. 784:** excepciones que se pueden oponer contra la acción cambiaria. **Art. 789:** la acción cambiaria directa prescribe en **3 años** desde el vencimiento.

## Checklist de un pagaré que sí se puede cobrar
- [ ] Palabra «pagaré» o mención del derecho; promesa **incondicional** de pagar.
- [ ] Suma **determinada** (en número y letras, coincidentes).
- [ ] Nombre del beneficiario y «a la orden de» o «al portador».
- [ ] **Fecha de vencimiento** clara (o cuotas con cláusula aceleratoria).
- [ ] **Firma** del deudor (y del representante legal con facultades si es empresa; codeudores si los hay).
- [ ] Si se firma en blanco: **carta de instrucciones** firmada, con los eventos en que se puede llenar y cómo calcular el monto.
- [ ] Guardar el **original** (el ejecutivo se inicia con el original o según las reglas de títulos electrónicos).

## Modelo de carta de instrucciones (resumen)
> «Yo, [DEUDOR], autorizo expresa e irrevocablemente a [ACREEDOR] para llenar el pagaré en blanco No. [__] que he suscrito a su favor, sin previo aviso, así: (1) el valor será el de todas las obligaciones exigibles a mi cargo a favor de [ACREEDOR] el día en que se llene, incluidos capital e intereses; (2) la fecha de vencimiento será la del día en que se llene; (3) el pagaré podrá llenarse cuando incurra en mora de más de [treinta (30)] días en cualquiera de mis obligaciones, sea admitido en un proceso de insolvencia o incumpla el contrato [__]. Declaro haber recibido copia de esta carta.»

## Factura electrónica: cómo asegurar el título valor (checklist)
- [ ] Emitirla con todos los requisitos y la **fecha de vencimiento**.
- [ ] Conseguir **constancia de recibo** de la mercancía o servicio (remisión firmada, acuse electrónico).
- [ ] Gestionar los **eventos** en el sistema de la DIAN (acuse de recibo, recibo del bien o servicio, aceptación) según la norma vigente, para habilitarla en el RADIAN (→ **contador_lushows** y proveedor de facturación).
- [ ] Si el cliente reclama, atender el reclamo dentro del plazo.

## Riesgos y errores comunes
- **Alto:** pagarés firmados en blanco **sin** carta de instrucciones: se discute su validez.
- **Alto:** dejar prescribir la acción cambiaria (3 años).
- **Medio:** facturas sin constancia de recibo ni eventos de aceptación: pierden la vía ejecutiva como título valor (queda el contrato).
- **Medio:** pagarés firmados por quien no tiene facultades.

## Conexión con otros módulos
- `09` prescripción · `95` cobro · `96` ejecutivo · `126` factoring y RADIAN · `128` créditos y pagarés · `163` factura electrónica (aspectos legales).
- **contador_lushows** (facturación electrónica y RADIAN).

## Siguiente paso típico
Para clientes a crédito: pedir pagaré con carta de instrucciones al abrir el cupo y asegurar los eventos de aceptación de cada factura electrónica.
