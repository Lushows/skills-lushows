# 145 — Niveles de servicio (SLA) y penalidades

Las empresas grandes miden a sus proveedores con indicadores: entregas a tiempo, pedidos completos, lotes conformes, tiempo de respuesta. Esos indicadores, cuando se escriben en el contrato con consecuencias, son un **acuerdo de niveles de servicio** (SLA). Bien diseñado, ordena la relación; mal diseñado, se convierte en una máquina de descuentos que se come tu margen. La clave está en **qué se mide, cómo se mide y cuánto cuesta fallar**.

## Conceptos clave
- **Indicador (KPI):** métrica concreta, por ejemplo OTIF (*on time in full*: a tiempo y completo).
- **Nivel objetivo:** el umbral exigido (por ejemplo, 95% de entregas OTIF al mes).
- **Crédito de servicio:** descuento en la factura cuando no se cumple el nivel (típico en tecnología).
- **Multa:** suma pactada para presionar el cumplimiento durante la ejecución.
- **Cláusula penal:** estimación anticipada de perjuicios o sanción por incumplimiento.
- **Tope de penalidades:** máximo acumulado en un periodo.

## Qué dice la norma
- Cláusula penal: Código Civil, arts. 1592 y ss. No se puede pedir a la vez la pena y la indemnización de perjuicios, salvo que se haya pactado expresamente (Código Civil, art. 1600).
- En materia mercantil, el juez puede reducir la pena cuando sea manifiestamente excesiva o cuando hubo cumplimiento parcial (C.Co. art. 867).
- Multas entre particulares: válidas si se pactan expresamente; su cobro unilateral (descuento directo) debe estar pactado con un procedimiento que respete el derecho de defensa (la jurisprudencia ha sido exigente con esto; verificar).

## Paso a paso para negociar un SLA (como proveedor)
1. **Indicadores que controlas:** que no te midan por demoras causadas por el cliente (órdenes tardías, recepción cerrada).
2. **Medición objetiva y compartida:** quién mide, con qué sistema, y tu derecho a objetar el reporte.
3. **Periodo de gracia** al inicio (por ejemplo, los primeros [2] meses sin penalidades).
4. **Escalonamiento:** primero plan de mejora, después descuento.
5. **Tope:** el total de penalidades no puede superar un porcentaje de la facturación del periodo.
6. **Exclusividad del remedio:** que la penalidad sea el remedio único por ese incumplimiento (sin perjuicios adicionales), salvo dolo o culpa grave.
7. **Simetría:** si te penalizan por entregar tarde, que haya consecuencia si el cliente paga tarde (`144`).

## Cláusula modelo
> "**Nivel de servicio.** EL PROVEEDOR mantendrá un nivel OTIF mensual igual o superior al [95]%, medido sobre órdenes de compra emitidas con la anticipación pactada. No se computarán los incumplimientos causados por EL COMPRADOR, terceros bajo su control o fuerza mayor.
> **Procedimiento.** EL COMPRADOR enviará el reporte mensual dentro de los [5] días hábiles siguientes al cierre del mes; EL PROVEEDOR podrá objetarlo dentro de los [5] días hábiles siguientes, con soporte.
> **Consecuencias.** Si el OTIF es inferior al nivel objetivo durante [dos] meses consecutivos, EL PROVEEDOR presentará un plan de mejora. Si el incumplimiento persiste el mes siguiente, EL COMPRADOR podrá aplicar un descuento del [1]% del valor facturado ese mes por cada punto porcentual por debajo del objetivo, con un tope del [5]% de la facturación mensual. Estos descuentos constituyen el único remedio económico por incumplimiento del nivel de servicio, salvo dolo o culpa grave."

*Por qué:* mide solo lo que controlas, da derecho a objetar, escalona y pone tope.

## Riesgos y errores comunes
- **Alto:** penalidades sin tope y acumulables con indemnización de perjuicios.
- **Alto:** descuentos automáticos sin derecho a objetar el reporte.
- **Medio:** indicadores afectados por actos del propio cliente.
- **Bajo:** no pedir periodo de gracia en el arranque.

## Conexión con otros módulos
`26` cláusula penal · `25` remedios · `113` SaaS (SLA de disponibilidad) · `117` logística · `146` limitación de responsabilidad · `190` caso · **Matematicas_lushows** (impacto de las penalidades en el margen).

## Siguiente paso típico
Simular con **Matematicas_lushows** el peor mes posible bajo la cláusula propuesta por el cliente y negociar tope y escalonamiento con ese número.
