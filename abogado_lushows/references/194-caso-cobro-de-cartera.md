# 194 — Caso: cliente que no paga facturas vencidas

**El caso.** Una pyme le vendió durante seis meses a un cliente mediano (una cadena de cafeterías). Hoy tiene **$48.000.000 en facturas vencidas** (cifra ilustrativa), algunas con más de 90 días. El cliente responde "la próxima semana pagamos" y sigue pidiendo mercancía. La pyme no quiere perder al cliente, pero tampoco puede seguir financiándolo. Este caso muestra la ruta escalonada: de la conversación al proceso ejecutivo, sin quemar etapas ni dejar prescribir el derecho.

## 1. Diagnóstico
- **Documentos:** ¿hay contrato?, ¿órdenes de compra?, ¿remisiones firmadas?, ¿facturas electrónicas con eventos en RADIAN (acuse, recibo, aceptación)? (`126`, `163`).
- **¿Título ejecutivo?** Facturas aceptadas (expresa o tácitamente) que cumplan requisitos pueden cobrarse por proceso ejecutivo (CGP art. 422; C.Co. arts. 772 y ss.) (`94`, `96`).
- **Plazos:** acción cambiaria directa de la factura: tres años desde el vencimiento (C.Co. art. 789; verificar aplicación a factura) (`09`).
- **Solvencia del cliente:** ¿tiene bienes, cuentas, locales? ¿Está en proceso de insolvencia? (Si está en reorganización, las reglas cambian: Ley 1116 de 2006, `97`.)
- **Intereses:** mora mercantil a la tasa máxima legal (C.Co. art. 884), calculados con **Matematicas_lushows**.

## 2. Ruta escalonada
**Etapa 1 — Contención (semana 1)**
- **Suspender despachos** a crédito si el contrato lo permite (o pasar a contado/anticipado).
- Conciliar cartera con el cliente: lista de facturas, fechas, valores, abonos.

**Etapa 2 — Cobro prejurídico (semanas 1–4)** (`95`)
- Reunión y **acuerdo de pago** por escrito.
- Si el cliente acepta un plan de pagos, respaldarlo con **pagaré con carta de instrucciones** y, si es posible, aval del socio (`128`).

**Etapa 3 — Requerimiento formal (semana 4)**
- Carta de cobro con plazo final (abajo).

**Etapa 4 — Cobro jurídico (desde la semana 6)**
- Demanda ejecutiva con **medidas cautelares** (embargo de cuentas, bienes, establecimientos) presentadas por abogado (`96`).
- Evaluar costo/beneficio (honorarios, tiempo) con **Matematicas_lushows**.

## 3. Documentos modelo
**Acuerdo de pago (extracto)**
> "EL DEUDOR reconoce adeudar a EL ACREEDOR $[48.000.000] por las facturas del Anexo 1, más intereses moratorios causados a la fecha por $[X]. Pagará en [6] cuotas mensuales de $[Y], los días [5] de cada mes, desde [FECHA]. El incumplimiento de una cuota hará exigible la totalidad del saldo (cláusula aceleratoria). Para respaldar esta obligación, EL DEUDOR suscribe pagaré en blanco con carta de instrucciones."
> *Por qué:* el reconocimiento expreso interrumpe la prescripción (según reglas legales) y el pagaré facilita el cobro ejecutivo.

**Carta de requerimiento final (extracto)**
> "A la fecha, [CLIENTE] adeuda $[X] por las facturas relacionadas, vencidas desde [FECHAS], aceptadas conforme a la ley. Le solicitamos el pago total, o la firma de un acuerdo de pago, dentro de los [5] días hábiles siguientes. Vencido este plazo, iniciaremos sin más aviso las acciones judiciales de cobro, incluidas medidas cautelares, con los intereses moratorios y costas a que haya lugar."

## 4. Reglas de oro
- No seguir despachando a crédito a quien ya está en mora.
- No amenazar con lo que no vas a hacer.
- No publicar ni exponer al deudor (riesgo de habeas data y de difamación); reportes a centrales de riesgo solo con autorización y siguiendo la ley de habeas data financiero (`56`).
- Todo acuerdo, por escrito.

## 5. Riesgos y errores comunes
- **Alto:** dejar pasar el plazo de prescripción esperando "la próxima semana".
- **Alto:** facturas sin eventos de aceptación ni remisiones firmadas → difícil probar la entrega.
- **Medio:** acuerdo de pago verbal.
- **Medio:** seguir vendiendo a crédito durante la mora.
- **Bajo:** no calcular intereses (pierdes dinero) o calcularlos sobre la usura (riesgo penal).

## Conexión con otros módulos
`94` títulos valores · `95` cobro · `96` ejecutivo y cautelares · `97` insolvencia · `126` RADIAN · `128` pagarés · `144` Ley 2024 · `56` habeas data financiero · **Matematicas_lushows** (intereses exactos) · **contador_lushows** (provisión de cartera) · **ventas_lushows** (conversación de cobro sin romper la relación).

## Siguiente paso típico
Conciliar la cartera factura por factura, verificar qué facturas están aceptadas en RADIAN y proponer el acuerdo de pago con pagaré esta misma semana.
