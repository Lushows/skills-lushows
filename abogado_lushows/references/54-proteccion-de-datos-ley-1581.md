# 54 — Protección de datos personales (Ley 1581 de 2012)

Cada número de WhatsApp que llega al bot, cada correo de un cliente, cada conversación guardada es un **dato personal**. Usarlos sin autorización, para fines distintos o sin seguridad puede costar multas de la SIC y la confianza del cliente. Para negocios que viven de bots y campañas (GastroLatam, AVISPA'O), este es uno de los temas legales **más importantes**.

## Conceptos clave (en simple)
- **Dato personal:** cualquier información que identifica o puede identificar a una persona natural (nombre, cédula, celular, correo, foto, voz, ubicación).
- **Dato público / semiprivado / privado:** según su naturaleza (por ejemplo, el estado civil es público; los datos financieros son semiprivados; los gustos personales son privados).
- **Dato sensible:** afecta la intimidad o puede generar discriminación: **salud**, biometría, orientación sexual, origen racial, creencias, afiliación política o sindical. Requiere protección reforzada.
- **Titular:** la persona a quien se refieren los datos.
- **Responsable del tratamiento:** quien decide sobre la base de datos y su uso (la empresa).
- **Encargado del tratamiento:** quien trata datos **por cuenta** del responsable (proveedor de CRM, el SaaS, la agencia).
- **Tratamiento:** cualquier operación con datos (recolectar, guardar, usar, enviar, suprimir).
- **Autorización:** consentimiento previo, expreso e informado del titular.
- **Transmisión vs. transferencia:** enviar datos a un encargado (transmisión) vs. a otro responsable (transferencia).

## Qué dice la norma (Colombia — verificar vigencia)
- **Ley 1581 de 2012:**
  - **Art. 4:** principios (legalidad, finalidad, libertad, veracidad, transparencia, acceso y circulación restringida, seguridad, confidencialidad).
  - **Arts. 5 y 6:** datos sensibles y su tratamiento excepcional (con autorización explícita, informando que no está obligado a darlos).
  - **Art. 7:** datos de niños, niñas y adolescentes.
  - **Art. 8:** derechos del titular (conocer, actualizar, rectificar, pedir prueba de la autorización, ser informado del uso, quejarse ante la SIC, revocar la autorización y pedir supresión, acceder gratis).
  - **Art. 9:** autorización previa e informada.
  - **Art. 12:** deber de informar al titular la finalidad y sus derechos.
  - **Art. 14:** consultas: respuesta en máximo **10 días hábiles** (prorrogables hasta 5 más).
  - **Art. 15:** reclamos: respuesta en máximo **15 días hábiles** (prorrogables hasta 8 más).
  - **Arts. 17 y 18:** deberes de responsables y encargados (incluido informar a la SIC violaciones de seguridad).
  - **Art. 23:** sanciones de la SIC: multas de hasta **2.000 SMMLV**, suspensión, cierre temporal o definitivo de la operación.
  - **Art. 26:** transferencia internacional solo a países con nivel adecuado de protección, salvo excepciones.
- **Decreto 1377 de 2013** (compilado en el Decreto 1074 de 2015): autorización, aviso de privacidad, políticas de tratamiento, transmisiones y contratos con encargados.
- **Circular Única de la SIC (Título V):** instrucciones de cumplimiento.

## Checklist de cumplimiento mínimo
- [ ] Inventario de bases de datos (clientes, leads del bot, empleados, proveedores).
- [ ] **Autorización** en cada punto de recolección (formulario, bot, web, tienda), con finalidades claras y prueba guardada.
- [ ] **Política de tratamiento** publicada (`55`, `108`).
- [ ] **Aviso de privacidad** donde se recolecten datos.
- [ ] Canal para consultas y reclamos con plazos legales.
- [ ] Contratos con **encargados** (proveedores de nube, CRM, WhatsApp API, agencias).
- [ ] Medidas de **seguridad** (accesos, contraseñas, cifrado, copias, `59`).
- [ ] Reglas especiales para **datos sensibles** (salud) y de menores.
- [ ] Registro en el RNBD si la empresa está obligada (`55`).

## Modelo de autorización corta (bot de WhatsApp)
> «Hola, soy el asistente de [MARCA]. Para atenderte y enviarte información de nuestros productos, trataremos tus datos (nombre, número y mensajes) conforme a nuestra Política de Tratamiento: [enlace]. Puedes conocer, actualizar, rectificar y suprimir tus datos o revocar esta autorización escribiendo a [correo]. ¿Autorizas el tratamiento de tus datos para estas finalidades? Responde SÍ para continuar.»

## Ojo con los datos de salud (BIO-SETA)
Si un cliente cuenta en el chat que tiene ansiedad, diabetes o que está embarazada, ese es un **dato sensible**. Reglas: no pedirlo si no es necesario; si se recibe, no usarlo para perfilar ni para publicidad sin autorización explícita; restringir acceso; y no dar recomendaciones médicas (además del riesgo sanitario, `83`).

## Riesgos y errores comunes
- **Alto:** campañas masivas a números sin autorización (además viola la Ley 2300 de 2023, `57`).
- **Alto:** guardar conversaciones con datos de salud sin protección.
- **Medio:** compartir bases con aliados sin contrato ni autorización (transferencia).
- **Medio:** no responder consultas y reclamos en los plazos.

## Conexión con otros módulos
- `55` política y RNBD · `56` habeas data financiero · `57` marketing directo · `58` privacidad web · `59` ciberseguridad · `108` plantilla de política de datos · `173` GDPR.
- **engineer_visualopen_lushows** (medidas técnicas) · **AVIS_lushows**.

## Siguiente paso típico
Hacer el inventario de bases de datos de cada marca e insertar la autorización en el primer mensaje del bot.
