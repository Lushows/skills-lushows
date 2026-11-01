# 182 — Inteligencia artificial en lo legal y sus riesgos

La IA (incluida esta skill) puede acelerar mucho el trabajo legal: resumir contratos, comparar versiones, redactar borradores, preparar listas de verificación. Pero tiene riesgos serios: **inventa normas y sentencias** con total seguridad, puede **filtrar información confidencial** si se usa mal, y su uso en productos (como un bot que atiende clientes) genera **responsabilidades** propias. Este módulo explica cómo usarla con disciplina, tanto dentro de la empresa como en lo que vendes.

## Conceptos clave
- **Alucinación:** respuesta falsa presentada como cierta (un artículo de ley inexistente, una sentencia inventada).
- **Verificación en fuente primaria:** comprobar cada norma en el texto oficial (Secretaría del Senado, Diario Oficial, SUIN-Juriscol, sitio de la entidad).
- **Confidencialidad:** lo que pegas en una herramienta de IA puede quedar almacenado o usarse según sus términos.
- **Humano en el circuito:** una persona responsable revisa antes de enviar o firmar.
- **Transparencia:** informar al usuario que interactúa con un sistema automatizado.

## Qué dice la norma (verificar vigencia; el tema cambia rápido)
- Colombia no tiene, a la fecha, una ley general de IA aprobada (verificar proyectos en el Congreso). Hay instrumentos de política pública (por ejemplo, documentos CONPES sobre IA; verificar el vigente).
- Ley 1581 de 2012: el uso de datos personales en sistemas de IA debe respetar los principios de finalidad, transparencia y seguridad; la SIC ha emitido orientaciones sobre IA y datos personales (verificar circular vigente).
- Ley 1480 de 2011: la información que da un bot de ventas obliga al vendedor como cualquier publicidad u oferta.
- Jurisprudencia: la Corte Constitucional se ha pronunciado sobre el uso de herramientas de IA en decisiones judiciales, exigiendo transparencia y control humano (verificar sentencia y alcance).
- UE: Reglamento (UE) 2024/1689 (`173`) si atiendes usuarios europeos.

## Reglas de uso dentro de la empresa
1. **Nunca** citar una norma, artículo, plazo o sentencia sin verificarla en la fuente oficial.
2. **No pegar** información confidencial de clientes o secretos empresariales en herramientas sin acuerdo empresarial de confidencialidad y sin desactivar el uso para entrenamiento.
3. **Anonimizar** cuando sea posible (reemplazar nombres por [CLIENTE A]).
4. **Revisión humana** obligatoria de cualquier documento que salga a un tercero.
5. **Registro:** guardar qué herramienta se usó para documentos importantes.

## Reglas para productos con IA (bots como los de GastroLatam, BIO-SETA o AVISPA'O)
1. **Aviso** al usuario de que habla con un asistente automatizado.
2. **Límites de contenido:** el bot no puede hacer claims prohibidos (salud, rentabilidad), ni prometer lo que la empresa no cumple.
3. **Datos personales:** autorización, finalidad informada y contratos con el proveedor del modelo (encargado) (`108`).
4. **Escalamiento a humano** para reclamos, temas de salud y decisiones importantes.
5. **Registro de conversaciones** conforme a la política de datos, para defenderte si hay disputa.

## Texto modelo (aviso en el primer mensaje del bot)
> "Hola, soy [NOMBRE], el asistente virtual de [MARCA]. Respondo con ayuda de inteligencia artificial y una persona de nuestro equipo revisa los casos especiales. No doy consejos médicos. Al continuar aceptas nuestra política de datos: [link]."

## Riesgos y errores comunes
- **Alto:** presentar ante un juez, la DIAN o una contraparte un escrito con normas o sentencias inventadas por IA.
- **Alto:** bot que promete curas o descuentos que no existen (la empresa queda obligada o sancionada).
- **Medio:** subir contratos confidenciales a herramientas gratuitas.
- **Bajo:** no informar que se trata de un asistente automatizado.

## Conexión con otros módulos
`00` método · `01` ética y límites · `03` fuentes del derecho · `54`/`108` datos · `111` claims · `113` SaaS · `189` capacitación · **optimizer_tokens_lushows** y **engineer_visualopen_lushows** (arquitectura del bot) · **AVIS_lushows**.

## Siguiente paso típico
Revisar el prompt base de cada bot para incluir el aviso de IA, la prohibición de claims y la regla de escalamiento a humano.
