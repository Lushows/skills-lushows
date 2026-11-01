# 108 — Plantilla comentada: política de tratamiento de datos personales

Si tu negocio guarda nombres, celulares, correos o direcciones de clientes (y un bot de WhatsApp lo hace todo el día), estás **tratando datos personales**. La Ley 1581 de 2012 te obliga a tener una **política de tratamiento** escrita, pedir **autorización** al titular y atender sus consultas y reclamos. La SIC sanciona con multas importantes a empresas pequeñas también. Esta plantilla da el esqueleto; ajústala a lo que realmente haces con los datos.

## Conceptos clave
- **Titular:** la persona dueña de los datos.
- **Responsable:** quien decide para qué y cómo se usan (tu empresa).
- **Encargado:** quien trata los datos por cuenta del responsable (tu proveedor de CRM, hosting, bot).
- **Dato sensible:** el que puede generar discriminación, incluido el de salud (ojo con suplementos: "tomo esto por ansiedad").
- **RNBD:** Registro Nacional de Bases de Datos ante la SIC, obligatorio para ciertos responsables (verificar umbrales vigentes).

## Qué dice la norma
- Ley 1581 de 2012: principios (art. 4); datos sensibles (arts. 5 y 6); derechos del titular (art. 8); autorización (art. 9); consultas (art. 14: 10 días hábiles, prorrogables) y reclamos (art. 15: 15 días hábiles, prorrogables); deberes del responsable (art. 17); RNBD (art. 25); transferencia internacional (art. 26).
- Decreto 1377 de 2013, compilado en el Decreto 1074 de 2015: contenido mínimo de la política y del aviso de privacidad (verificar).

## Texto modelo comentado

**1. Responsable.** [RAZÓN SOCIAL], NIT [X], domicilio [X], correo para datos: [datos@empresa.com].

**2. Datos que recolectamos.** Identificación y contacto (nombre, celular, correo, ciudad, dirección de entrega); datos de compra; conversaciones por WhatsApp y redes; [datos de navegación]. No recolectamos datos sensibles salvo que el titular los entregue voluntariamente; en ese caso, su entrega es facultativa.
> *Por qué:* lista solo lo que de verdad recoges. Si tu bot pregunta "¿para qué lo necesitas?", puede recibir datos de salud: trátalos como sensibles.

**3. Finalidades.** (a) Procesar y entregar pedidos; (b) atender por WhatsApp, incluido con asistentes automáticos de inteligencia artificial; (c) facturación electrónica; (d) enviar información comercial, ofertas y novedades, si el titular lo autoriza; (e) análisis estadístico y de campañas publicitarias; (f) cumplir obligaciones legales.
> *Por qué:* no puedes usar datos para finalidades que no informaste. El marketing debe poder rechazarse por separado.

**4. Encargados y transferencias.** Compartimos datos con proveedores de mensajería, alojamiento en la nube, pasarelas de pago, transportadoras y plataformas publicitarias, algunos ubicados fuera de Colombia, bajo contratos que exigen confidencialidad y seguridad.
> *Por qué:* casi todo hoy está en servidores en el exterior; informarlo y tener contrato con el encargado es tu deber.

**5. Derechos del titular.** Conocer, actualizar, rectificar y suprimir sus datos; revocar la autorización; pedir prueba de la autorización; ser informado del uso; quejarse ante la SIC tras agotar el trámite con nosotros.

**6. Procedimiento.** Consultas: respondemos en máximo diez (10) días hábiles. Reclamos: quince (15) días hábiles. Canal: [correo / formulario]. [Detallar prórrogas según la ley.]

**7. Seguridad y vigencia.** Medidas técnicas y administrativas razonables. Los datos se conservan mientras dure la relación y los plazos legales. Política vigente desde [FECHA], versión [X].

**Aviso corto para el bot o formulario:** "Al escribirnos autorizas a [EMPRESA] a tratar tus datos para atender tu compra y, si marcas sí, enviarte ofertas. Política completa: [link]. Puedes consultar, corregir o pedir que borremos tus datos en [correo]."

## Riesgos y errores comunes
- **Alto:** enviar publicidad masiva por WhatsApp sin autorización ni opción de salida (ver `57`).
- **Alto:** no poder probar la autorización (guarda fecha, canal y texto aceptado).
- **Medio:** no tener contrato de encargo con proveedores de nube o bot.
- **Bajo:** política publicada pero desactualizada.

## Conexión con otros módulos
`54` Ley 1581 · `55` política y RNBD · `57` marketing directo · `58` cookies · `59` incidentes · `173` GDPR · **engineer** de producto para guardar la prueba de autorización.

## Siguiente paso típico
Publicar la política, integrar el aviso corto en el primer mensaje del bot y guardar el registro de consentimiento por contacto.
