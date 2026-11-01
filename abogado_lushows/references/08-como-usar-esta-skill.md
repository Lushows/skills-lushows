# 08 — Cómo usar esta skill (qué módulo cargar)

La biblioteca tiene 200 módulos. **No se cargan todos**: se cargan los 1 a 4 que la pregunta necesita. Esta es la tabla de navegación. Primero siempre va el diagnóstico (`02`); después, el módulo del tema; al final, si hace falta, la plantilla.

## Conceptos clave
- **Núcleo (00–99):** el oficio completo, con Colombia dentro.
- **Expansión (100–199):** plantillas, sectores, financiación, comercio exterior, negociación avanzada, riesgo, tributario-legal, otros países, gestión legal y casos.
- **Módulo base + módulo específico + plantilla:** la combinación típica.

## Tabla de carga según la pregunta
| Pregunta de Luis | Carga |
|---|---|
| «Revísame este contrato» | `22` elementos, `23` redacción, el típico (`30`–`49`), `146` limitación de responsabilidad |
| «Redáctame un contrato de…» | El típico (`30`–`49`) + plantilla (`100`–`109`) |
| «Un proveedor/cliente no cumple» | `25` incumplimiento, `26` cláusula penal, `27` terminación, `90` negociación |
| «No me pagan» | `95` cobro, `94` títulos valores, `96` ejecutivo, `09` prescripción |
| «Voy a negociar con una gran empresa» | `149`, `144` plazos de pago, `143` volúmenes, `142` exclusividad |
| «Quiero crear / reformar la empresa» | `10`, `11`, `12`, `13` |
| «Entra un socio / inversionista» | `14`, `15`, `18`, `120`, `121` |
| «Pelea entre socios» | `15`, `16`, `87`, `195` |
| «¿Puedo vender esto así por internet?» | `50`, `53`, `58`, `107`, `112` |
| «¿Cómo manejo los datos de mis clientes / el bot?» | `54`, `55`, `57`, `58`, `59` |
| «Quiero registrar la marca / me copiaron» | `60`, `61`, `69`, `196` |
| «Contrato a alguien / despido a alguien» | `70`, `71`, `74`, `77` |
| «¿Necesito registro INVIMA?» | `83`, `110`, `111` (+ Bio_lushows) |
| «¿Qué permisos necesito para el local?» | `84`, `46`, `114` |
| «Voy a importar / exportar» | `130`, `131`, `137`, `134` |
| «Me llegó un requerimiento / una demanda» | `05`, `93`, `98`, `188` |
| «La empresa no puede pagar sus deudas» | `97` (alto riesgo: abogado titulado) |
| «¿Qué obligaciones legales tengo?» | `89` matriz legal, `184` calendario legal, `80` cumplimiento |
| «Entrégame esto en PDF» | `99` |

## Cómo responder (siempre)
1. Diagnóstico corto (`02`) si falta información.
2. Concepto con el formato: **(a)** respuesta simple, **(b)** riesgo alto/medio/bajo, **(c)** norma o cláusula, **(d)** siguiente paso.
3. Cláusulas y contratos **redactados**.
4. Ruteo explícito a otras skills (`07`).
5. Documentos presentables en **PDF** (`99`), nunca Markdown crudo.

## Cómo verificar una norma antes de citarla
1. Buscarla en SUIN-Juriscol o en la Secretaría del Senado.
2. Revisar notas de modificación y sentencias (`04`).
3. Si hay duda sobre un número de artículo, citar solo ley y año y describir la regla.
4. Agregar «(verificar vigencia)» en normas que cambian seguido (laboral, tributario, consumidor, datos, sanitario).
5. Si la norma cambió, registrarlo en `199-changelog-normativo-2026.md`.

## Cómo mantener viva la skill
- Cuando aparezca un error legal real o un caso valioso, se agrega al módulo correspondiente.
- Los cambios de normas van al changelog (`199`).
- Las plantillas se ajustan con lo aprendido de cada negociación.

## Riesgos y errores comunes
- **Medio:** cargar demasiados módulos y responder con teoría en vez de con la cláusula.
- **Medio:** saltarse el diagnóstico porque "la pregunta parece simple".
- **Bajo:** olvidar el ruteo a la skill de números o impuestos.

## Conexión con otros módulos
- `00` método · `02` diagnóstico · `07` ruteo · `99` entregables.

## Siguiente paso típico
Identificar la fila de la tabla que corresponde a la pregunta y cargar esos módulos, empezando por `02` si faltan hechos.
