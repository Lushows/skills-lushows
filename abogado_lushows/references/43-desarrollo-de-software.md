# 43 — Contrato de desarrollo de software

Cuando AVISPA'O, el bot de GastroLatam o la tienda de BIO-SETA los construye un tercero, el contrato debe responder tres preguntas que suelen quedar en el aire: **¿qué exactamente se va a construir?, ¿cuándo se considera terminado? y ¿de quién es el código?** Si alguna no tiene respuesta escrita, el proyecto termina en discusión.

## Conceptos clave (en simple)
- **Alcance:** lista de funciones que debe tener el software (documento de requerimientos).
- **Metodología:** cascada (todo definido al inicio) o ágil (entregas por ciclos o "sprints").
- **Hito:** entrega parcial verificable, ligada a un pago.
- **Pruebas de aceptación:** pruebas que el cliente hace para confirmar que el entregable funciona.
- **Código fuente:** el texto del programa que permite modificarlo; sin él, el cliente depende del desarrollador.
- **Componentes de terceros / open source:** librerías con licencias propias (algunas obligan a liberar el código derivado).
- **Escrow de código:** depósito del código fuente con un tercero que lo entrega al cliente si el desarrollador desaparece.
- **Garantía de funcionamiento:** periodo en que el desarrollador corrige errores sin costo.

## Qué dice la norma (Colombia — verificar vigencia)
- **Decreto 1360 de 1989:** el software se protege como obra literaria por derecho de autor.
- **Ley 23 de 1982, art. 20 (modificado por la Ley 1450 de 2011):** en obras creadas por encargo en virtud de un contrato de prestación de servicios o laboral, se presume que los derechos patrimoniales se transfieren al encargante, en la medida necesaria para sus actividades habituales, salvo pacto en contrario; el contrato debe constar por escrito. Para evitar discusiones sobre el alcance de esa presunción, **pactar la cesión total expresamente** (`62`).
- **Ley 23 de 1982 y Decisión 351 de 1993:** los derechos morales son del autor y no se ceden.
- **Ley 1581 de 2012:** si el desarrollador accede a datos personales reales, es encargado (`54`).

## Checklist del contrato
- [ ] **Alcance** en anexo (historias de usuario, pantallas, integraciones), con proceso de **control de cambios** y su costo.
- [ ] **Cronograma de hitos** y pagos contra aceptación.
- [ ] **Pruebas de aceptación**: plazo, criterios, cómo se reportan errores y en cuánto se corrigen.
- [ ] **Propiedad**: cesión de derechos patrimoniales del código, documentación y diseños; entrega del **código fuente** y accesos (repositorio, servidores, dominios a nombre del cliente).
- [ ] **Componentes de terceros**: lista y licencias; prohibición de licencias que obliguen a liberar el código sin autorización.
- [ ] **Garantía** de corrección de errores (por ejemplo, 90 días).
- [ ] **Soporte y mantenimiento** posterior (contrato aparte o anexo con SLA).
- [ ] **Confidencialidad** y datos personales.
- [ ] **Seguridad**: buenas prácticas, no dejar puertas traseras, gestión de credenciales.
- [ ] Terminación anticipada: entrega de todo lo avanzado y pagado.

## Cláusula modelo: aceptación
> «EL CONTRATISTA entregará cada HITO en el ambiente de pruebas indicado por EL CLIENTE. EL CLIENTE tendrá [diez (10)] días hábiles para probarlo conforme a los criterios del Anexo 2 y comunicar por escrito los errores encontrados, clasificados por severidad. EL CONTRATISTA los corregirá dentro de los [cinco (5)] días hábiles siguientes. Si EL CLIENTE no se pronuncia en el plazo, el HITO se entenderá aceptado. El pago de cada HITO se hará dentro de los [diez (10)] días hábiles siguientes a su aceptación.»

## Cláusula modelo: código fuente y accesos
> «Con cada HITO aceptado, EL CONTRATISTA entregará el código fuente completo, comentado, en el repositorio de propiedad de EL CLIENTE, junto con la documentación técnica y las instrucciones de despliegue. Los repositorios, cuentas de servicios en la nube, dominios y credenciales del proyecto estarán a nombre de EL CLIENTE desde su creación.»

## Ejemplo (ilustrativo)
Un desarrollador construye el bot de GastroLatam y aloja todo en su cuenta personal de la nube. Al terminar la relación, el bot queda "secuestrado". Prevención: cuentas a nombre de la empresa desde el inicio y entrega de código por hito.

## Riesgos y errores comunes
- **Alto:** código y servidores a nombre del desarrollador.
- **Alto:** no ceder expresamente los derechos patrimoniales.
- **Medio:** alcance vago: cada función "nueva" se vuelve un sobrecosto.
- **Medio:** librerías con licencias que obligan a liberar el código del producto.

## Conexión con otros módulos
- `40` prestación de servicios · `41` SaaS · `62` derechos de autor · `63` software · `145` niveles de servicio · `113` tecnología y SaaS.
- **engineer_visualopen_lushows** (revisión técnica del alcance y licencias).

## Siguiente paso típico
Verificar hoy a nombre de quién están el repositorio, la nube y los dominios de cada producto; trasladarlos a la empresa si no lo están.
