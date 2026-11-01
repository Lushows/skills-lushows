# 192 — Caso: lanzar un SaaS de WhatsApp con IA para pymes

**El caso.** Una startup colombiana (parecida a AVISPA'O o a los bots de GastroLatam) lanza un **asistente de WhatsApp con inteligencia artificial** que atiende clientes, guarda conversaciones y organiza documentos de pymes. Cobra suscripción mensual. Depende de la API de WhatsApp (Meta), de un proveedor de modelos de IA y de una nube. Los riesgos legales: propiedad del código, datos personales de los clientes de sus clientes, lo que dice el bot, caídas del servicio y dependencia de proveedores. Cifras ilustrativas.

## 1. Diagnóstico
- **Cliente:** pymes (relación mercantil, más libertad contractual) y posiblemente personas naturales comerciantes (algunas reglas de consumidor podrían aplicar; verificar).
- **Datos:** el SaaS es **encargado** del tratamiento de los datos de los clientes finales de cada pyme; la pyme es **responsable** (`54`).
- **Proveedores críticos:** Meta (WhatsApp Business), proveedor de IA, nube, pasarela de pagos.
- **PI:** código escrito por fundadores y freelancers.

## 2. Arquitectura legal
1. **Cesión de PI** de todos los que escribieron código (`103`, `43`).
2. **Términos de servicio** (contrato con la pyme) aceptados electrónicamente con registro (`181`).
3. **Acuerdo de encargo de datos** (DPA) como anexo de los términos.
4. **Política de privacidad** propia (para los datos de las pymes como clientes) (`108`).
5. **Política de uso aceptable:** qué no puede hacer la pyme con el bot (spam, contenido ilegal, claims prohibidos).
6. **Revisión de términos de proveedores** y su reflejo en tus términos.

## 3. Cláusulas clave (extractos)
**Servicio y disponibilidad.** "Disponibilidad objetivo mensual del [99]%, excluidas ventanas de mantenimiento informadas y fallas de proveedores de terceros (incluidos la plataforma de mensajería y los proveedores de modelos de IA). Si la disponibilidad es inferior, EL CLIENTE recibirá un crédito del [5]% de la tarifa mensual por cada punto por debajo, con tope del [25]%, como remedio único." (`145`)

**Respuestas de la IA.** "Las respuestas del asistente se generan automáticamente con modelos de inteligencia artificial y pueden contener errores. EL CLIENTE configurará la información de su negocio, revisará el comportamiento del asistente y es responsable de las ofertas y declaraciones que haga a sus propios clientes. EL PROVEEDOR implementará filtros razonables y la opción de escalar a un humano." (`182`)

**Datos.** "EL CLIENTE es responsable del tratamiento de los datos de sus contactos y garantiza contar con las autorizaciones necesarias. EL PROVEEDOR actúa como encargado, solo según las instrucciones del Anexo de Tratamiento, con subencargados listados [nube, IA, mensajería], y no usará los datos para entrenar modelos [salvo autorización expresa]."

**Uso aceptable.** "EL CLIENTE no usará el servicio para enviar mensajes masivos no solicitados, publicidad engañosa, declaraciones de salud prohibidas ni contenido ilícito. El incumplimiento permite suspender el servicio de inmediato."
> *Por qué:* si un cliente hace spam, Meta puede bloquear tu número o tu cuenta: protege la plataforma de todos.

**Pagos y renovación.** "Suscripción mensual prepagada, renovación automática informada, cancelación en cualquier momento con efecto al final del periodo pagado. Suspensión por mora de [10] días."

**Limitación.** "Responsabilidad total limitada a lo pagado por EL CLIENTE en los [12] meses anteriores, salvo dolo o culpa grave; sin lucro cesante." (`146`)

**Terminación y portabilidad.** "Al terminar, EL CLIENTE podrá exportar sus datos durante [30] días; luego se eliminarán, salvo obligación legal de conservarlos."

## 4. Riesgos y errores comunes
- **Alto:** código de freelancers sin cesión → problema en una ronda de inversión (`122`).
- **Alto:** usar los datos de las conversaciones para fines no autorizados.
- **Alto:** el bot de un cliente promete curas o descuentos falsos y se culpa a la plataforma (la cláusula de responsabilidad del cliente y los filtros ayudan, pero no eliminan el riesgo reputacional).
- **Medio:** términos de proveedores incompatibles con lo que prometes (SLA imposible).
- **Bajo:** no informar la renovación automática.

## Conexión con otros módulos
`41` SaaS · `113` tecnología · `108` datos · `145` SLA · `146` limitación · `182` IA · `120`–`121` inversión · **AVIS_lushows** · **engineer_visualopen_lushows** (arquitectura, seguridad) · **optimizer_tokens_lushows** (costos de IA) · **ventas_lushows**.

## Siguiente paso típico
Hacer el inventario de PI y de proveedores críticos, y redactar términos + DPA antes de cobrar al primer cliente pagador.
