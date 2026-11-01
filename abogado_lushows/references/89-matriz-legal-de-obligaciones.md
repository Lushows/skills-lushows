# 89 — Matriz legal de obligaciones

La **matriz legal** es la herramienta que convierte todo este conocimiento en una lista práctica: **qué norma aplica a mi empresa, qué me obliga a hacer, cada cuánto, quién es responsable y dónde está la prueba de que lo hice**. Es la base del programa de cumplimiento (`80`) y del calendario legal (`184`). Este módulo trae una matriz base para una pyme colombiana que se adapta a cada marca.

## Conceptos clave (en simple)
- **Matriz legal (de requisitos legales):** tabla de normas aplicables con sus obligaciones concretas.
- **Obligación periódica:** se cumple cada cierto tiempo (anual, mensual).
- **Obligación por evento:** se activa cuando pasa algo (contratar, despedir, lanzar producto, incidente de datos).
- **Evidencia:** documento que prueba el cumplimiento.
- **Responsable:** persona encargada de cumplir y guardar la evidencia.

## Cómo construirla (paso a paso)
1. **Perfil de la empresa:** tipo societario, ciudad, actividad (CIIU), número de trabajadores, activos e ingresos, canales de venta, tipo de producto, si trata datos, si importa o exporta.
2. **Listar las áreas**: societario, tributario, laboral, SST, consumidor, datos, sanitario, PI, ambiental, funcionamiento, cumplimiento.
3. **Por cada área**, identificar normas y obligaciones concretas (usar los módulos de la skill).
4. **Asignar** periodicidad, responsable y evidencia.
5. **Pasar las fechas** al calendario legal (`184`).
6. **Revisar** cada seis meses o cuando cambie el negocio o la norma (`199`).

## Matriz base (pyme colombiana — verificar cada obligación y su vigencia)
| Área | Obligación | Norma de referencia | Periodicidad | Evidencia | Módulo |
|---|---|---|---|---|---|
| Societario | Renovar matrícula mercantil | C.Co., art. 33 | Anual (hasta 31-mar) | Certificado renovado | `13` |
| Societario | Asamblea ordinaria y aprobación de estados financieros | Ley 1258 de 2008, estatutos | Anual | Acta | `16` |
| Societario | Libros de actas y de accionistas al día | C.Co. | Por evento | Libros | `16`, `183` |
| Tributario | Declaraciones y pagos (renta, IVA, retención, ICA), facturación electrónica, exógena, RUB | Estatuto Tributario y normas municipales | Según calendario DIAN/municipal | Declaraciones | → contador_lushows |
| Laboral | Contratos escritos, afiliaciones, PILA, nómina electrónica | CST, normas de seguridad social | Mensual / por evento | Planillas | `70`, `79` |
| Laboral | Prima, cesantías (consignación), intereses, vacaciones, dotación | CST, Ley 50 de 1990 | Semestral/anual | Comprobantes | `79` |
| Laboral | Reglamento interno (si se supera el umbral) | CST, arts. 104 y ss. | Por evento | Reglamento publicado | `72` |
| SST | SG-SST y estándares mínimos | Decreto 1072 de 2015, Res. 0312 de 2019 | Anual + continuo | Plan de trabajo, matriz | `76` |
| Convivencia | Comité o mecanismo de convivencia | Ley 1010 de 2006 | Continuo | Actas | `75` |
| Consumidor | Información, garantías, retracto, PQR | Ley 1480 de 2011 | Continuo | Políticas, registro de PQR | `50`–`53` |
| Datos | Política, autorizaciones, atención de derechos, seguridad | Ley 1581 de 2012, Dec. 1377 de 2013 | Continuo | Política, bitácora | `54`, `55` |
| Datos | RNBD (si supera umbral) | Dec. 090 de 2018 | Anual / cambios | Constancia SIC | `55` |
| Marketing | Horarios, canales y frecuencia de contacto | Ley 2300 de 2023 | Continuo | Registro de envíos | `57` |
| Sanitario | Autorización sanitaria vigente, etiquetado, publicidad conforme | Dec. 3249 de 2006, Res. 2674 de 2013 | Por producto / renovación | Registros, etiquetas | `83` |
| PI | Renovación de marcas, vigilancia, cesiones | Decisión 486 de 2000 | 10 años / mensual | Certificados | `60`, `61` |
| Funcionamiento | Uso de suelo, bomberos, sanitario, música | Ley 1801 de 2016 | Por apertura / anual | Conceptos | `84` |
| Ambiental | Gestión de residuos, REP envases | Dec. 1076 de 2015, Res. 1407 de 2018 | Continuo / anual | Certificados | `85` |
| Cumplimiento | SAGRILAFT / PTEE (si aplica) | Circular Básica Jurídica Supersociedades | Anual + continuo | Manuales, reportes | `81` |
| Contratos | Vencimientos, prórrogas automáticas y preavisos | Cada contrato | Por evento | Calendario | `27`, `180` |

## Ejemplo de perfil (ilustrativo)
**BIO-SETA SAS** — Bogotá, venta en línea y a distribuidores, 3 trabajadores, producto ingerible, campañas por WhatsApp. Obligaciones prioritarias: sanitario (`83`), publicidad (`52`), consumidor y retracto (`50`, `53`), datos y Ley 2300 (`54`, `57`), laboral básico y SG-SST (`70`, `76`), marca (`60`), contratos de distribución (`32`). Probablemente **no** obligada a RNBD ni SAGRILAFT por tamaño (verificar con el contador), pero sí le pedirán información de cumplimiento los clientes grandes (`81`).

## Riesgos y errores comunes
- **Alto:** no saber qué obligaciones aplican: se descubren con la multa.
- **Medio:** matriz hecha una vez y nunca actualizada.
- **Medio:** obligaciones sin responsable ni evidencia.

## Conexión con otros módulos
- `80` programa de cumplimiento · `184` calendario legal · `187` auditoría legal anual · `199` changelog normativo.
- **contador_lushows** (bloque tributario completo) · **AVIS_lushows** (obligaciones por rubro y ciudad).

## Siguiente paso típico
Llenar el perfil de cada empresa, adaptar la matriz base y cargar sus fechas en el calendario legal (`184`).
