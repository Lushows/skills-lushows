# 113 — Sector tecnología y SaaS

Un **SaaS** (*software as a service*, software como servicio) es software que el cliente usa por internet pagando una suscripción, sin instalarlo: como un bot de WhatsApp para pymes o un panel de facturación. Legalmente, lo que vendes no es "un programa", sino una **licencia de uso + un servicio** con niveles de disponibilidad. Los riesgos típicos: quién es dueño del código, qué pasa con los datos de los clientes, cuánto respondes si el sistema se cae y cómo se usa la inteligencia artificial.

## Conceptos clave
- **Licencia de uso:** permiso para usar el software, sin transferir la propiedad.
- **SLA** (*service level agreement*): acuerdo de niveles de servicio, como disponibilidad mensual y tiempos de respuesta (`145`).
- **Encargado del tratamiento:** el SaaS que procesa datos de los clientes de tu cliente actúa como encargado (Ley 1581).
- **Código abierto:** software con licencia pública; algunas licencias obligan a liberar tu código si lo distribuyes (*copyleft*).
- **Proveedor de IA:** el modelo de un tercero que usas (Anthropic, OpenAI, Google); sus términos te obligan.

## Qué dice la norma
- Software: protegido por derecho de autor como obra literaria (Decisión 351 de 1993 CAN; Ley 23 de 1982). No se patenta como tal en la Comunidad Andina (Decisión 486, con matices).
- Ley 1581 de 2012: datos personales; transmisión internacional a proveedores de nube requiere contrato (Decreto 1377 de 2013, compilado en el Decreto 1074 de 2015).
- Ley 527 de 1999: aceptación electrónica de términos (*clickwrap*).
- Ley 1480 de 2011 si vendes a consumidores; si vendes a empresas, el régimen es mercantil (más libertad contractual).
- Inteligencia artificial: en Colombia no hay a la fecha una ley general de IA en firme (verificar proyectos en curso); en la UE rige el Reglamento (UE) 2024/1689 (ver `173`).

## Checklist legal de un SaaS
1. **PI del código:** contratos con desarrolladores que cedan derechos (`103`, `43`); inventario de librerías de código abierto y sus licencias.
2. **Términos de servicio** con: licencia, pago y renovación automática (informada), SLA, suspensión por impago, limitación de responsabilidad, propiedad de los datos del cliente, exportación de datos al terminar.
3. **Acuerdo de tratamiento de datos (DPA)** con clientes empresariales y con tus subencargados (nube, IA, mensajería).
4. **Términos de proveedores críticos:** WhatsApp Business/Meta, proveedor de IA, nube. Si ellos te suspenden, tú incumples: trasládalo como causa ajena en tus términos.
5. **IA responsable:** informar al usuario que interactúa con un asistente automático; no prometer exactitud; revisar uso de datos para entrenamiento.
6. **Facturación** electrónica de suscripciones; IVA del servicio digital (con **contador_lushows**).

## Ejemplo de cláusula
> "Los datos que EL CLIENTE cargue en la plataforma son de su propiedad. [PROVEEDOR] los trata como encargado, solo para prestar el servicio, y los pondrá a disposición de EL CLIENTE en formato [CSV/JSON] durante los [30] días siguientes a la terminación, tras lo cual los eliminará, salvo obligación legal de conservarlos."

*Por qué:* el miedo número uno del cliente empresarial es perder sus datos; resolverlo vende.

## Riesgos y errores comunes
- **Alto:** código hecho por freelancers sin cesión de derechos → no eres dueño de tu producto (riesgo en una ronda, `122`).
- **Alto:** usar datos de clientes para entrenar o para otros fines no informados.
- **Medio:** responsabilidad ilimitada en los términos; SLA prometido que no puedes medir.
- **Medio:** licencias *copyleft* incompatibles con tu modelo.
- **Bajo:** renovación automática no informada (queja de consumidor).

## Conexión con otros módulos
`41` SaaS T&C · `43` desarrollo de software · `63` software · `145` SLA · `146` limitación · `182` IA en lo legal · `192` caso SaaS · **engineer_visualopen_lushows** (arquitectura y seguridad) · **AVIS_lushows** (producto AVISPA'O).

## Siguiente paso típico
Hacer el inventario de PI (código, marcas, dominios) y de proveedores críticos, y luego redactar términos con `41` y el caso `192`.
