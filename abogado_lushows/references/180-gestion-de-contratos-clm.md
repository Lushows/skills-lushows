# 180 — Gestión de contratos (CLM)

Firmar un buen contrato es la mitad del trabajo; la otra mitad es **gestionarlo**: saber dónde está, cuándo vence, qué te obliga a hacer (pólizas, reportes, preavisos) y qué te debe la otra parte. El **CLM** (*contract lifecycle management*, gestión del ciclo de vida de los contratos) es ese orden. En una pyme no hace falta un software caro: basta una carpeta bien organizada y una tabla maestra. El error típico es descubrir que el contrato se renovó solo por no enviar el preaviso a tiempo.

## Conceptos clave
- **Repositorio:** lugar único donde están todos los contratos firmados (versión final, no borradores).
- **Tabla maestra (registro de contratos):** una fila por contrato con sus datos clave.
- **Hitos y alertas:** fechas que exigen acción (preaviso, renovación, entrega de póliza, ajuste de precio).
- **Obligaciones recurrentes:** reportes, auditorías, certificados de calidad, pagos.
- **Plantillas aprobadas:** modelos de la casa para no empezar de cero (`100`–`109`).
- **Flujo de aprobación:** quién revisa y quién firma según el monto o el riesgo.

## Qué dice la norma
- No hay una ley que obligue a tener un CLM, pero sí deberes que dependen de él: conservación de documentos (C.Co. art. 60, `159`), deberes de diligencia de los administradores (Ley 222 de 1995, art. 23) y la validez de contratos y archivos electrónicos (Ley 527 de 1999).
- Los preavisos y plazos contractuales son vinculantes: perderlos tiene consecuencias jurídicas (renovación automática, pérdida de derechos).

## Paso a paso (versión pyme)
1. **Reunir** todos los contratos vigentes (clientes, proveedores, arriendos, laborales clave, licencias, seguros).
2. **Escanear o guardar el PDF firmado** con nombre estándar: `AAAA-MM-DD_TIPO_CONTRAPARTE_vFINAL.pdf`.
3. **Crear la tabla maestra** con estas columnas:

| Campo | Ejemplo |
|---|---|
| Contraparte | Cafetera X S.A. |
| Tipo | Suministro |
| Fecha firma / inicio / vencimiento | 2026-03-01 / 2026-03-15 / 2027-03-14 |
| Renovación automática / preaviso | Sí / 60 días |
| Fecha límite del preaviso | 2027-01-13 |
| Valor / moneda | $[X] COP anual |
| Pago | 45 días desde recepción |
| Pólizas exigidas y vencimiento | Cumplimiento, hasta 2027-06-14 |
| Exclusividad / no competencia | Sí, categoría café, Colombia |
| Cambio de control / cesión | Requiere autorización |
| Ley y foro | Colombia / arbitraje CCB |
| Responsable interno | Luis |
| Ubicación del archivo | /Legal/Contratos/Clientes/… |

4. **Llevar las fechas al calendario legal** con alertas a 90, 60 y 30 días (`184`).
5. **Revisión mensual** de 15 minutos: qué vence, qué preaviso hay que enviar, qué póliza renovar.
6. **Flujo de aprobación:** contratos sobre $[monto] o con cláusulas fuera de la plantilla pasan por revisión legal.

## Ejemplo de regla interna
> "Ningún contrato se firma sin: (1) verificar el certificado de existencia y facultades del firmante de la contraparte; (2) revisar las cláusulas de pago, responsabilidad, terminación y exclusividad; (3) registrarlo en la tabla maestra dentro de las 48 horas siguientes a la firma."

## Riesgos y errores comunes
- **Alto:** renovaciones automáticas no deseadas por no enviar el preaviso.
- **Alto:** no encontrar la versión firmada cuando hay un conflicto.
- **Medio:** pólizas vencidas que el contrato exigía vigentes.
- **Bajo:** contratos guardados en el correo de un empleado que se fue.

## Conexión con otros módulos
`109` otrosí y terminación · `159` conservación · `183` archivo legal · `184` calendario · `186` métricas · `187` auditoría anual · **engineer_visualopen_lushows** (si se automatiza con software) · **Matematicas_lushows** (cálculo de fechas límite).

## Siguiente paso típico
Construir la tabla maestra con los 10 contratos más importantes esta semana y cargar sus fechas al calendario.
