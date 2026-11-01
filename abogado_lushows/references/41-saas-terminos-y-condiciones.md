# 41 — SaaS: términos y condiciones

Un software como servicio (SaaS) —como AVISPA'O— no "vende" el software: **da acceso** a él mediante suscripción. Sus términos y condiciones son el contrato con miles de clientes que nunca se negocia uno por uno. Por eso deben estar bien hechos desde el día uno: definen qué se promete, qué no, cuánto puede costar un error y quién es responsable de los datos.

## Conceptos clave (en simple)
- **SaaS:** software alojado por el proveedor al que el cliente accede por internet mediante suscripción.
- **Términos y condiciones (T&C):** contrato de adhesión que el cliente acepta (`29`).
- **Licencia de uso / derecho de acceso:** permiso limitado, no exclusivo e intransferible para usar el servicio.
- **SLA (acuerdo de nivel de servicio):** compromisos medibles de disponibilidad y soporte (`145`).
- **Datos del cliente:** información que el cliente carga; normalmente es del cliente.
- **Responsable / encargado del tratamiento:** quien decide sobre los datos personales / quien los trata por cuenta de otro (`54`).
- **Cláusula abusiva:** cláusula que desequilibra injustificadamente la relación en perjuicio del consumidor; no produce efectos.

## Qué dice la norma (Colombia — verificar vigencia)
- **Ley 527 de 1999 y Decreto 2364 de 2012:** validez de la aceptación electrónica (`29`).
- **Ley 1480 de 2011:** si el cliente es **consumidor**, aplican las reglas de información, contratos de adhesión (art. 37), cláusulas abusivas (arts. 42 y 43) y comercio electrónico (art. 50). Ojo: la ley considera consumidor también a la empresa que adquiere un producto como destinatario final para una necesidad **no ligada intrínsecamente a su actividad económica** (art. 5) — una pyme que contrata AVISPA'O podría, según el caso, ser tratada como consumidora.
- **Ley 1581 de 2012 y Decreto 1377 de 2013:** cuando el SaaS trata datos personales de los clientes de su cliente, normalmente actúa como **encargado**; se necesita un contrato de transmisión de datos (`54`, `55`).
- **Ley 1266 de 2008:** si se maneja información financiera o crediticia (`56`).
- **Ley 23 de 1982 y Decreto 1360 de 1989:** el software es obra protegida (`63`).

## Contenido mínimo de unos T&C SaaS (checklist)
- [ ] Identificación del proveedor (razón social, NIT, domicilio, canales de atención).
- [ ] Descripción del servicio y planes.
- [ ] Derecho de acceso: alcance y prohibiciones (ingeniería inversa, reventa, uso ilícito).
- [ ] Precio, ciclo de facturación, **renovación automática** y cómo cancelar (claro y fácil).
- [ ] Mora: suspensión con aviso previo.
- [ ] SLA de disponibilidad y soporte, con exclusiones (mantenimientos, fuerza mayor).
- [ ] Datos del cliente: propiedad, seguridad, respaldo, **exportación** al terminar y borrado.
- [ ] Rol en datos personales (encargado) y anexo de transmisión.
- [ ] Propiedad intelectual del software y retroalimentación.
- [ ] Limitación de responsabilidad (válida entre empresas; con consumidores tiene límites imperativos).
- [ ] Cambios a los términos: aviso previo y derecho a terminar.
- [ ] Terminación y efectos.
- [ ] Ley aplicable, solución de controversias, PQR.

## Cláusula modelo: limitación de responsabilidad (clientes empresariales)
> «En la máxima medida permitida por la ley, la responsabilidad total de [PROVEEDOR] por cualquier reclamación derivada de estos términos estará limitada al valor efectivamente pagado por EL CLIENTE en los [doce (12)] meses anteriores al hecho que la origina. [PROVEEDOR] no responderá por lucro cesante, pérdida de oportunidades ni daños indirectos. Esta limitación no aplica en casos de dolo o culpa grave, ni frente a derechos irrenunciables de los consumidores.»

## Cláusula modelo: datos al terminar
> «Durante los [treinta (30)] días calendario siguientes a la terminación, EL CLIENTE podrá exportar sus datos en formato [CSV/JSON]. Vencido ese plazo, [PROVEEDOR] suprimirá los datos de EL CLIENTE de sus sistemas activos, salvo aquellos que deba conservar por obligación legal, y lo certificará a solicitud de EL CLIENTE.»

## Ejemplo (ilustrativo)
AVISPA'O cae 6 horas y una pyme no recibe una alerta de vencimiento de su matrícula. Sin T&C claros, la pyme podría reclamar la multa. Con SLA que excluya resultados de terceros, limitación de responsabilidad y la aclaración de que el servicio es de **recordatorio y apoyo** (no reemplaza al contador ni al abogado), el riesgo baja a medio.

## Riesgos y errores comunes
- **Alto:** prometer resultados ("nunca más te multan") en el marketing de un SaaS de cumplimiento.
- **Alto:** tratar datos personales de terceros sin contrato de encargado ni medidas de seguridad.
- **Medio:** renovación automática sin aviso ni cancelación fácil.
- **Medio:** cambiar los T&C sin aviso ni registro de versiones.

## Conexión con otros módulos
- `29` aceptación electrónica · `54` datos · `58` privacidad web · `59` ciberseguridad · `107` plantilla T&C · `113` tecnología y SaaS · `145` SLA · `146` responsabilidad · `192` caso SaaS.
- **AVIS_lushows** (el producto) · **engineer_visualopen_lushows** (registro técnico de aceptación).

## Siguiente paso típico
Redactar los T&C con este checklist, publicar con control de versiones y exigir aceptación expresa en el alta del cliente.
