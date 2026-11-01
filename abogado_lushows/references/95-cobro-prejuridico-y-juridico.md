# 95 — Cobro prejurídico y jurídico

La cartera vencida es **plata de la empresa en el bolsillo de otro**. Cobrar bien es un proceso ordenado y escalonado: primero recordar, luego requerir, luego negociar, y solo al final demandar. Hacerlo dentro de la ley (sin acoso, sin escrache en redes, respetando horarios) protege a la empresa de reclamos y mantiene abierta la puerta del acuerdo.

## Conceptos clave (en simple)
- **Cartera:** cuentas por cobrar a clientes.
- **Edad de la cartera:** días de mora (0–30, 31–60, 61–90, más de 90).
- **Cobro prejurídico:** gestiones antes de demandar (recordatorios, cartas, llamadas, acuerdos de pago).
- **Cobro jurídico:** acciones judiciales (ejecutivo, monitorio, declarativo) o arbitrales.
- **Intereses moratorios:** los que se causan por el retraso; en Colombia tienen un **tope** (usura), ligado al interés bancario corriente que certifica la Superintendencia Financiera.
- **Gastos de cobranza:** costos que se trasladan al deudor solo si se pactaron y son razonables (con consumidores, con mayores restricciones).
- **Castigo de cartera:** reconocimiento contable de que una deuda es incobrable (→ **contador_lushows**).

## Qué dice la norma (Colombia — verificar vigencia)
- **Código de Comercio, art. 884:** si no se pactan intereses moratorios en negocios mercantiles, se aplica una y media veces el interés bancario corriente; no se puede superar el límite de usura.
- **Código Penal, art. 305:** delito de usura (cobrar intereses por encima del límite).
- **Ley 2300 de 2023:** horarios, canales y frecuencia en la cobranza a consumidores; prohibición de contactar a terceros o referencias en ciertos casos (`57`).
- **Ley 1266 de 2008 (mod. Ley 2157 de 2021):** reporte a centrales de riesgo con autorización y comunicación previa (`56`).
- **Ley 1480 de 2011:** protección del consumidor en operaciones de crédito (información de intereses y gastos).
- **Ley 2024 de 2020:** plazos máximos de pago a ciertos proveedores (`144`).
- **CGP (Ley 1564 de 2012):** procesos ejecutivo (arts. 422 y ss.) y monitorio (arts. 419 a 421).

## Ruta de cobro escalonada (ejemplo de política)
| Día de mora | Acción | Canal | Responsable |
|---|---|---|---|
| 1–5 | Recordatorio amable con factura adjunta | Correo / WhatsApp (en horario legal) | Comercial |
| 15 | Segundo recordatorio y llamada | Teléfono / correo | Cartera |
| 30 | **Requerimiento formal** escrito con plazo y anuncio de consecuencias | Correo certificado o con acuse | Gerencia |
| 30–45 | **Negociación** de acuerdo de pago con reconocimiento de deuda (`90`) | Reunión | Gerencia |
| 45 | Comunicación previa de reporte a centrales (si hay autorización) | Correo / físico | Cartera |
| 60–90 | **Cobro jurídico**: ejecutivo (si hay título) o conciliación + declarativo / monitorio | Abogado | Abogado titulado |

## Modelo de requerimiento formal (resumen)
> «[Ciudad, fecha]. Señores [CLIENTE]. Asunto: Requerimiento de pago. A la fecha registran saldo vencido a favor de [EMPRESA] por $[__], correspondiente a las facturas electrónicas No. [__], con vencimientos entre el [__] y el [__]. Les solicitamos efectuar el pago o comunicarse para acordar una forma de pago dentro de los [diez (10)] días hábiles siguientes. Vencido ese plazo, [EMPRESA] iniciará las acciones judiciales de cobro, con los intereses moratorios a la tasa máxima legal y las costas que correspondan. Si ya realizaron el pago, por favor envíen el soporte y omitan este mensaje.»

## Herramientas según el documento disponible
| Tienes… | Vía de cobro |
|---|---|
| Pagaré, letra, cheque, factura aceptada | **Ejecutivo** directo con medidas cautelares (`96`) |
| Contrato con obligación clara, expresa y exigible firmado por el deudor | Ejecutivo (si cumple requisitos de título ejecutivo) |
| Acta de conciliación o transacción incumplida | Ejecutivo |
| Solo factura no aceptada, chats y entregas, deuda de mínima cuantía | **Monitorio** |
| Deuda discutida o con perjuicios | Conciliación + **verbal** |

## Riesgos y errores comunes
- **Alto:** publicar deudores en redes o grupos, llamar a familiares o empleadores: viola derechos y puede ser delito.
- **Alto:** cobrar intereses por encima de la usura.
- **Medio:** dejar pasar meses sin requerimiento ni acuerdo escrito: se acerca la prescripción.
- **Medio:** seguir despachando a quien está en mora sin garantías.

## Conexión con otros módulos
- `09` prescripción · `56` habeas data financiero · `57` Ley 2300 · `90` negociación · `91` conciliación · `94` títulos valores · `96` ejecutivo · `126` factoring · `194` caso cobro de cartera.
- **Matematicas_lushows** (intereses moratorios por periodo con la tasa certificada) · **contador_lushows** (provisión y castigo de cartera) · **ventas_lushows** (tono del cobro).

## Siguiente paso típico
Adoptar la política de cobro escalonada, clasificar la cartera por edad y enviar requerimientos formales a todo lo que supere 30 días.
