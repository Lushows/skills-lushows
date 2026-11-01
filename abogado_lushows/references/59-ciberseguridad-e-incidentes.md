# 59 — Ciberseguridad e incidentes

Un bot con su API abierta, un panel sin contraseña, una base de clientes filtrada o un correo de phishing que vacía la cuenta bancaria: los incidentes de seguridad son hoy un **riesgo legal**, no solo técnico. Si se exponen datos personales, la empresa debe **reportar** a la SIC y puede ser sancionada por no haber tenido medidas de seguridad adecuadas. Este módulo cubre la parte legal: deberes, reporte y respuesta.

## Conceptos clave (en simple)
- **Incidente de seguridad:** evento que compromete la confidencialidad, integridad o disponibilidad de la información (acceso no autorizado, filtración, pérdida, secuestro de datos).
- **Violación de datos personales:** incidente que afecta datos personales.
- **Medidas de seguridad:** controles técnicos (contraseñas, cifrado, autenticación, copias) y administrativos (políticas, accesos, capacitación).
- **Ransomware:** programa que secuestra los datos y pide rescate.
- **Phishing:** engaño para obtener credenciales o pagos.
- **Plan de respuesta a incidentes:** procedimiento escrito de qué hacer, quién lo hace y en qué plazos.

## Qué dice la norma (Colombia — verificar vigencia)
- **Ley 1581 de 2012:** principio de **seguridad** (art. 4); los responsables y encargados deben conservar la información con las medidas necesarias para impedir su adulteración, pérdida, consulta, uso o acceso no autorizado, e **informar a la SIC** cuando se presenten violaciones a los códigos de seguridad y existan riesgos en la administración de la información de los titulares (arts. 17 y 18).
- **Circular Única de la SIC, Título V:** el reporte de incidentes se hace a través del RNBD dentro del plazo que fija la SIC (se ha señalado **15 días hábiles** desde que se detecta el incidente, verificar).
- **Ley 1273 de 2009:** delitos informáticos (acceso abusivo a sistema informático, interceptación de datos, daño informático, uso de software malicioso, violación de datos personales, suplantación de sitios web, hurto por medios informáticos, entre otros) — base para denunciar.
- **Ley 1928 de 2018:** aprueba el Convenio de Budapest sobre ciberdelincuencia.
- Contratos con encargados deben exigir seguridad y aviso inmediato de incidentes (`54`).

## Checklist preventivo (lo mínimo)
- [ ] Inventario de sistemas y datos críticos (bot, paneles, tienda, bases de clientes, correo, banca).
- [ ] **Autenticación** en todo panel y API; doble factor en correo, banca y nube.
- [ ] Accesos por rol; retirar accesos de quien sale.
- [ ] Copias de seguridad probadas.
- [ ] Contraseñas y llaves fuera del código (gestor de secretos).
- [ ] Contratos con proveedores tecnológicos con cláusula de seguridad e incidentes.
- [ ] Plan de respuesta a incidentes escrito.
- [ ] Capacitación básica al equipo en phishing.
- [ ] Póliza cibernética si el riesgo lo justifica (`152`).

## Paso a paso ante un incidente
1. **Contener**: cerrar el acceso, cambiar credenciales, aislar el sistema.
2. **Preservar evidencia**: registros (logs), capturas, correos; no borrar.
3. **Evaluar**: qué datos, de cuántas personas, qué tan sensibles, si siguen expuestos.
4. **Reportar a la SIC** (si hay datos personales en riesgo) por el RNBD en el plazo fijado.
5. **Informar a los titulares** afectados cuando haya riesgo para ellos, con recomendaciones.
6. **Denunciar** ante la Fiscalía si hay delito (con el abogado).
7. **Corregir** la causa y documentar las lecciones.

## Cláusula modelo: seguridad e incidentes (contrato con proveedor tecnológico)
> «EL PROVEEDOR implementará medidas técnicas, humanas y administrativas adecuadas para proteger la información de EL CLIENTE, incluidas autenticación robusta, control de accesos, cifrado en tránsito y copias de seguridad. EL PROVEEDOR notificará a EL CLIENTE cualquier incidente de seguridad que afecte su información dentro de las [veinticuatro (24)] horas siguientes a su detección, con la información disponible, y colaborará en su contención, investigación y en los reportes que deban hacerse a las autoridades.»

## Ejemplo (ilustrativo)
Se descubre que un endpoint del panel de un bot no exigía contraseña y permitía ver conversaciones. Aunque no haya prueba de que alguien entró, es un riesgo para datos personales: contener (cerrar el endpoint), revisar registros de acceso, documentar, evaluar si hubo exposición y, si la hubo, reportar a la SIC y a los afectados.

## Riesgos y errores comunes
- **Alto:** ocultar un incidente con datos personales: agrava la sanción.
- **Alto:** paneles o APIs sin autenticación.
- **Medio:** no tener plan; improvisar bajo presión.
- **Medio:** pagar rescates sin asesoría (riesgo legal y sin garantía de recuperación).

## Conexión con otros módulos
- `54` datos · `55` RNBD · `152` seguros · `154` fraude interno · `155` crisis · `188` protocolo de crisis legal.
- **engineer_visualopen_lushows** (seguridad técnica: autenticación, secretos, CSP).

## Siguiente paso típico
Escribir el plan de respuesta a incidentes de una página y revisar que todo panel y API de las marcas exija autenticación.
