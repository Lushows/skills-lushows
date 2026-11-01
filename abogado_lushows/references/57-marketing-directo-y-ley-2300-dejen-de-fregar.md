# 57 — Marketing directo y Ley 2300 de 2023 («dejen de fregar»)

Las campañas por WhatsApp, las llamadas de venta, los SMS y los correos masivos son el motor de negocios como GastroLatam y BIO-SETA. La **Ley 2300 de 2023** puso límites claros: **solo se puede contactar a consumidores por los canales que autorizaron, en ciertos horarios y con frecuencia limitada**. Sumada a la Ley 1581, define cómo hacer marketing directo sin multas.

## Conceptos clave (en simple)
- **Marketing directo:** contacto individual con potenciales clientes (WhatsApp, llamadas, SMS, correo, redes) para vender o promocionar.
- **Gestión de cobranza:** contactos para cobrar deudas; también limitados por esta ley.
- **Canal autorizado:** el medio que el consumidor aceptó expresamente para ser contactado.
- **Opt-in:** consentimiento previo para recibir mensajes. **Opt-out:** mecanismo para dejar de recibirlos.
- **Registro de Números Excluidos (RNE):** listado administrado bajo la regulación de la CRC donde los usuarios piden no recibir mensajes comerciales (verificar alcance actual).

## Qué dice la norma (Colombia — verificar vigencia)
- **Ley 2300 de 2023:** protege la intimidad de los consumidores frente a contactos de publicidad, ventas y cobranza. Puntos centrales (verificar el texto exacto de cada artículo):
  - Solo se puede contactar por los **canales** que el consumidor **autorizó**, y el consumidor puede escoger y cambiar esos canales.
  - **Horarios** permitidos: **lunes a viernes de 7:00 a.m. a 7:00 p.m.** y **sábados de 8:00 a.m. a 3:00 p.m.**; **no** domingos ni festivos.
  - **Frecuencia** limitada de contactos por semana y por canal (verificar la regla exacta, que distingue entre publicidad y cobranza).
  - Prohibición de contactar a referencias personales o terceros para cobrar, salvo reglas específicas.
  - La SIC vigila su cumplimiento (y la Superintendencia Financiera para sus vigiladas).
- **Ley 1581 de 2012:** se necesita autorización para usar datos personales con fines de marketing (`54`).
- **Ley 1480 de 2011:** información veraz en la publicidad (`52`).
- **Regulación de la CRC** (Comisión de Regulación de Comunicaciones): mensajes comerciales por SMS y el RNE (verificar resolución vigente).
- **Políticas de WhatsApp Business / Meta:** exigen opt-in y plantillas aprobadas para mensajes iniciados por la empresa fuera de la ventana de 24 horas (no es ley, pero su violación bloquea el número).

## Checklist de una campaña masiva legal
- [ ] Base de datos con **autorización** expresa para marketing por **ese canal** (prueba guardada: fecha, texto aceptado).
- [ ] Excluir a quien revocó o pidió no ser contactado (lista de exclusión interna y RNE si aplica).
- [ ] Programar envíos **solo** en los horarios permitidos (zona horaria de Colombia) y nunca domingos ni festivos.
- [ ] Respetar el límite de frecuencia por persona y canal.
- [ ] Identificar al remitente (marca) y ofrecer **salida fácil** («responde SALIR»).
- [ ] Contenido veraz, sin claims prohibidos (`52`).
- [ ] Registro de envíos (quién, cuándo, qué plantilla) para demostrar cumplimiento.

## Modelo de autorización de marketing (separada de la de servicio)
> «¿Quieres recibir promociones y novedades de [MARCA] por WhatsApp? Te escribiremos máximo [una (1)] vez por semana, de lunes a sábado en horario permitido por la ley. Puedes cancelar cuando quieras respondiendo SALIR. Responde SÍ para aceptar.»

## Regla técnica sugerida para el bot (pseudocódigo)
> Antes de cada envío: si el día es domingo o festivo → no enviar; si es lunes a viernes fuera de 7:00–19:00, o sábado fuera de 8:00–15:00 (hora Colombia) → reprogramar; si el contacto no tiene `optin_marketing = sí` o tiene `excluido = sí` → no enviar; si ya recibió el máximo semanal por ese canal → no enviar.

## Riesgos y errores comunes
- **Alto:** campañas a bases compradas o sin autorización: violación de Ley 1581 y Ley 2300 a la vez.
- **Alto:** cobrar a clientes llamando a familiares o publicando la deuda.
- **Medio:** campañas programadas que salen un domingo o a las 9 p.m.
- **Medio:** no honrar el «SALIR».

## Conexión con otros módulos
- `54` datos · `55` política · `56` habeas data financiero · `95` cobro · `112` ecommerce.
- **facebook_ads_lushows** (CTWA y plantillas) · **ventas_lushows** (secuencias de seguimiento) · skills de WhatsApp (`automate-whatsapp`).

## Siguiente paso típico
Implementar en el sistema de campañas del bot la regla de horario, frecuencia y opt-in, y separar la autorización de marketing de la de atención.
