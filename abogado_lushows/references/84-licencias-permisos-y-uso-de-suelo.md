# 84 — Licencias, permisos y uso de suelo

Abrir un establecimiento abierto al público (un café, una tienda, una bodega, un laboratorio) exige cumplir **requisitos de funcionamiento** que verifican la Policía, la alcaldía, bomberos y las autoridades sanitarias. El error más caro es firmar arriendo y adecuar un local **donde el uso de suelo no permite la actividad**. Este módulo es la lista de lo que hay que tener antes de abrir.

## Conceptos clave (en simple)
- **Uso de suelo:** lo que el Plan de Ordenamiento Territorial (POT) del municipio permite hacer en cada zona (comercio, industria, vivienda, servicios).
- **Concepto de uso de suelo:** documento de la curaduría o de la secretaría de planeación que dice si la actividad es compatible con la ubicación.
- **Certificado de seguridad / inspección de bomberos:** verificación de condiciones de seguridad humana y contra incendios.
- **Concepto sanitario:** visita de la secretaría de salud a establecimientos que manipulan alimentos o atienden público en ciertos sectores.
- **Derechos de autor por música:** pago a las sociedades de gestión colectiva si se ejecuta música en público.
- **Publicidad exterior visual:** avisos y vallas, con reglas municipales.
- **Medidas correctivas:** sanciones de policía (multas, suspensión de actividad, cierre).

## Qué dice la norma (Colombia — verificar vigencia)
- **Ley 1801 de 2016 (Código Nacional de Seguridad y Convivencia Ciudadana), art. 87:** requisitos para el ejercicio de actividades económicas abiertas al público, entre ellos: cumplir las normas de uso de suelo, destinación, horario y ubicación; las condiciones de seguridad, sanitarias y ambientales; tener la matrícula mercantil vigente; y, cuando se ejecuten públicamente obras musicales, acreditar el pago de los derechos de autor. Las autoridades pueden verificarlos en cualquier momento (verificar el texto exacto).
- **Ley 1575 de 2012:** Ley General de Bomberos; inspecciones de seguridad (verificar el certificado exigido en cada municipio).
- **Resolución 2674 de 2013:** condiciones sanitarias de establecimientos de alimentos (`83`).
- **Ley 140 de 1994:** publicidad exterior visual (más normas municipales).
- **Ley 23 de 1982:** derechos de autor por comunicación pública de música.
- **Planes de Ordenamiento Territorial** de cada municipio (Bogotá, Medellín, etc.).
- Actividades especiales: turismo (Registro Nacional de Turismo, **Ley 2068 de 2020**), bebidas alcohólicas, salud, entre otras.

## Checklist antes de firmar el local y abrir
- [ ] **Concepto de uso de suelo** favorable para la dirección exacta y la actividad (antes de firmar, `46`).
- [ ] **Matrícula mercantil** de la sociedad y del establecimiento de comercio, renovada.
- [ ] **RUT** con la actividad económica correcta (→ **contador_lushows**).
- [ ] **Bomberos**: inspección o certificado según el municipio.
- [ ] **Sanitario**: concepto sanitario y cursos de manipulación de alimentos del personal, si aplica (`83`).
- [ ] **Música**: pago de derechos de autor a las sociedades de gestión colectiva, si se pone música.
- [ ] **Avisos**: registro o permiso de publicidad exterior, si se requiere.
- [ ] **Horario** permitido para la zona y la actividad.
- [ ] **SG-SST** implementado (`76`).
- [ ] Registros especiales del sector (por ejemplo, RNT para turismo).
- [ ] **Impuesto de industria y comercio (ICA)** inscrito en el municipio (→ **contador_lushows**).

## Modelo de solicitud de concepto de uso de suelo (resumen)
> «Señores [Curaduría / Secretaría de Planeación de __]. Solicito concepto de uso de suelo para el inmueble ubicado en [dirección], con chip/matrícula inmobiliaria [__], en el que se pretende desarrollar la actividad de [descripción precisa, código CIIU __], con un área aproximada de [__] m². Agradezco indicar si la actividad está permitida y bajo qué condiciones.»

## Ejemplo (ilustrativo)
Un punto de venta de BIO-SETA con degustación de bebidas: además del uso de suelo comercial, puede requerir concepto sanitario por manipulación de alimentos, cursos del personal, y si pone música ambiental, el pago a la gestión colectiva. Sin eso, la Policía puede imponer medidas correctivas, incluida la suspensión.

## Riesgos y errores comunes
- **Alto:** firmar arriendo y adecuar sin verificar uso de suelo.
- **Medio:** abrir antes de la visita sanitaria en negocios de alimentos.
- **Medio:** música sin pago de derechos de autor.
- **Bajo:** avisos sin permiso.

## Conexión con otros módulos
- `13` registro mercantil · `46` arrendamiento · `76` SG-SST · `83` sanitario · `85` ambiental · `114` restaurantes.
- **AVIS_lushows** (obligaciones por rubro y ciudad) · **contador_lushows** (RUT e ICA).

## Siguiente paso típico
Pedir el concepto de uso de suelo de la dirección exacta antes de negociar el arriendo y armar la carpeta de funcionamiento con este checklist.
