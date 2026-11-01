# 184 — Calendario legal de la empresa

La mayoría de sanciones a pymes no vienen de hacer algo malo, sino de **olvidar una fecha**: renovar la matrícula mercantil, reunir la asamblea, renovar una marca, actualizar una base de datos, presentar una declaración, enviar un preaviso. El **calendario legal** junta en un solo lugar todas esas fechas, con alertas, y asigna un responsable a cada una. Las fechas tributarias exactas las publica la DIAN cada año y las administra **contador_lushows**; aquí va la estructura y las obligaciones legales recurrentes.

## Conceptos clave
- **Obligación periódica:** se repite (anual, mensual, bimestral).
- **Obligación por evento:** nace de un hecho (contratar un empleado, firmar un contrato con preaviso, recibir un requerimiento).
- **Alerta escalonada:** avisos a 90, 30 y 7 días.
- **Responsable:** una persona con nombre, no "la empresa".

## Qué dice la norma (obligaciones recurrentes típicas; verificar fechas de cada año)
- **Renovación de la matrícula mercantil:** dentro de los tres primeros meses de cada año, hasta el 31 de marzo (C.Co. art. 33).
- **Asamblea ordinaria de accionistas:** al menos una vez al año, dentro de los tres meses siguientes al vencimiento del ejercicio, salvo otra fecha en estatutos (C.Co. art. 422; verificar estatutos de la SAS).
- **Estados financieros:** aprobación por la asamblea y, si aplica, depósito o reporte a la Superintendencia de Sociedades (verificar obligación según tamaño).
- **Tributarias:** renta, IVA, retención en la fuente, información exógena, SIMPLE (anticipos y anual), ICA municipal, según calendario anual de la DIAN y de cada municipio (**contador_lushows**).
- **Laborales:** PILA mensual, prima de servicios (fechas legales del Código Sustantivo del Trabajo), consignación de cesantías, intereses sobre cesantías, dotación, SG-SST (autoevaluación y plan anual) (verificar fechas).
- **Datos personales:** actualización del Registro Nacional de Bases de Datos cuando aplique y reporte de reclamos e incidentes según instrucciones de la SIC (verificar periodicidad).
- **Marcas:** renovación cada 10 años; se puede pedir dentro de los seis meses anteriores al vencimiento, con un plazo de gracia de seis meses posteriores (Decisión 486, arts. 152 y 153).
- **Registros sanitarios:** renovación antes del vencimiento según su vigencia (verificar en el acto de concesión).
- **Pólizas, contratos y preavisos:** según cada contrato (`180`).
- **SAGRILAFT/PTEE:** reportes y actualizaciones si la empresa está obligada (`81`).

## Plantilla de calendario
| Mes | Obligación | Norma / fuente | Responsable | Alerta |
|---|---|---|---|---|
| Ene–Mar | Renovar matrícula mercantil (hasta 31-mar) | C.Co. art. 33 | Representante legal | 1-feb, 1-mar |
| Ene–Mar | Asamblea ordinaria y aprobación de estados financieros | C.Co. art. 422 / estatutos | Gerente + contador | 15-feb |
| Según DIAN | Declaración de renta, exógena, IVA, retención | Calendario DIAN | contador_lushows | 30 y 7 días antes |
| Mensual | PILA y nómina electrónica | Normas laborales | Nómina | Día 1 de cada mes |
| Según contrato | Preaviso de no renovación de [CONTRATO] | Contrato | Luis | 90 y 30 días antes |
| [Fecha] | Renovación marca [X] (6 meses antes del vencimiento) | Decisión 486 | Abogado PI | 9 y 6 meses antes |
| [Fecha] | Renovación registro sanitario [X] | Acto INVIMA | Calidad | 6 meses antes |
| [Fecha] | Vencimiento póliza [X] | Contrato | Administración | 45 días antes |

## Paso a paso
1. Listar todas las sociedades y, para cada una, las obligaciones periódicas.
2. Agregar las fechas de contratos, marcas, registros y pólizas desde la tabla maestra (`180`).
3. Cargar todo en un calendario compartido con alertas.
4. Asignar responsable y respaldo.
5. Revisión mensual de 15 minutos y actualización anual cuando la DIAN publique su calendario.

## Riesgos y errores comunes
- **Alto:** marca o registro sanitario vencido por olvido → pérdida del derecho o de la posibilidad de vender.
- **Alto:** no renovar la matrícula mercantil → sanciones y, con el tiempo, efectos sobre la sociedad (verificar).
- **Medio:** asamblea ordinaria no realizada → estados financieros sin aprobar.
- **Bajo:** alertas en el celular de una sola persona.

## Conexión con otros módulos
`09` plazos · `16` asamblea · `60` marcas · `83` registro sanitario · `159` conservación · `180` CLM · `187` auditoría · **contador_lushows** (calendario tributario) · **Matematicas_lushows** (cálculo de fechas y días hábiles).

## Siguiente paso típico
Crear el calendario compartido con las obligaciones de este año para cada sociedad y asignar responsables.
