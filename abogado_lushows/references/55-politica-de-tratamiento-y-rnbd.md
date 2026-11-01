# 55 — Política de tratamiento de datos y RNBD

La **política de tratamiento** es el documento público donde la empresa cuenta qué datos recoge, para qué, cómo los protege y cómo la gente puede ejercer sus derechos. Es obligatoria para todo responsable del tratamiento. El **RNBD** (Registro Nacional de Bases de Datos) es un registro ante la SIC que solo deben hacer algunas empresas. Confundir las dos cosas es común: **la política la necesitan todos; el RNBD, no todos**.

## Conceptos clave (en simple)
- **Política de tratamiento de la información:** documento interno y público con las reglas de manejo de datos personales.
- **Aviso de privacidad:** comunicación corta (verbal, escrita o electrónica) que informa al titular, en el momento de recolectar, que existe la política, las finalidades y cómo acceder a ella.
- **RNBD:** directorio público de las bases de datos sujetas a tratamiento, administrado por la SIC.
- **Oficial de protección de datos:** persona o área que vela por el cumplimiento (recomendado; en empresas grandes, esperado por la SIC).
- **Responsabilidad demostrada (accountability):** poder **probar** a la SIC que se adoptaron medidas apropiadas y efectivas.

## Qué dice la norma (Colombia — verificar vigencia)
- **Ley 1581 de 2012:** deber de adoptar un manual interno de políticas y procedimientos (art. 17); el RNBD (art. 25).
- **Decreto 1377 de 2013** (compilado en el Decreto 1074 de 2015): contenido mínimo de la política de tratamiento (nombre y datos del responsable; tratamiento y finalidades; derechos de los titulares; área responsable de atender peticiones; procedimiento para ejercer derechos; fecha de entrada en vigencia y periodo de vigencia de la base de datos) y del aviso de privacidad; responsabilidad demostrada.
- **Decreto 886 de 2014 y Decreto 090 de 2018** (compilados en el Decreto 1074 de 2015): reglas del RNBD. Según el Decreto 090 de 2018, están obligadas a inscribir sus bases en el RNBD las **sociedades y entidades sin ánimo de lucro con activos totales superiores a 100.000 UVT** y las personas jurídicas de naturaleza pública (verificar umbral vigente).
- **Circular Única de la SIC, Título V:** instrucciones sobre el RNBD, su actualización y el reporte de incidentes de seguridad (verificar plazos de actualización y reporte).

## Contenido mínimo de la política (checklist)
- [ ] Identificación del responsable (razón social, NIT, domicilio, correo, teléfono).
- [ ] Bases de datos que maneja y **finalidades** de cada una (ventas, atención, marketing, facturación, empleados, proveedores).
- [ ] Tipos de datos (incluidos sensibles y de menores, si aplica, con reglas especiales).
- [ ] Derechos de los titulares.
- [ ] Área o persona responsable de atender consultas y reclamos.
- [ ] Procedimiento y plazos para consultas (10 días hábiles) y reclamos (15 días hábiles).
- [ ] Transmisiones y transferencias (proveedores de nube, encargados en el exterior).
- [ ] Medidas de seguridad (en términos generales).
- [ ] Uso de cookies y tecnologías similares (si aplica, `58`).
- [ ] Fecha de vigencia y de última actualización.

## Modelo de aviso de privacidad (formulario web)
> «[RAZÓN SOCIAL], NIT [__], como responsable, tratará tus datos personales para [atender tu solicitud, gestionar tu compra, enviarte información comercial si lo autorizas]. Tienes derecho a conocer, actualizar, rectificar y suprimir tus datos y a revocar la autorización. Consulta nuestra Política de Tratamiento en [enlace] o escríbenos a [correo].»

## Paso a paso: inscripción en el RNBD (si la empresa está obligada)
1. Verificar si se supera el umbral de activos del año anterior (con **contador_lushows**).
2. Inventariar bases de datos y su información (finalidad, cantidad de titulares, encargados, transferencias internacionales, medidas de seguridad).
3. Crear usuario en la plataforma del RNBD de la SIC.
4. Inscribir cada base de datos.
5. Actualizar cuando haya cambios sustanciales y en los plazos que fije la SIC; reportar incidentes de seguridad por la misma plataforma (`59`).

## Ejemplo (ilustrativo)
GastroLatam, como persona natural o SAS pequeña, probablemente **no** supera el umbral del RNBD, pero **sí** debe tener política de tratamiento, autorizaciones y aviso de privacidad en el bot y en la web. AVISPA'O, que trata datos de muchas pymes como encargado, necesita además contratos de transmisión con cada cliente y medidas de seguridad documentadas.

## Riesgos y errores comunes
- **Alto:** no tener política publicada mientras se hacen campañas masivas.
- **Medio:** copiar la política de otra empresa con finalidades que no corresponden.
- **Medio:** creer que inscribirse en el RNBD reemplaza la política o las autorizaciones.
- **Bajo:** política sin fecha de actualización.

## Conexión con otros módulos
- `54` Ley 1581 · `57` marketing directo · `58` privacidad web · `59` incidentes · `108` plantilla de política de datos · `184` calendario legal.
- **contador_lushows** (valor de activos para el umbral).

## Siguiente paso típico
Redactar la política con la plantilla `108`, publicarla en cada web y enlazarla desde el primer mensaje del bot.
