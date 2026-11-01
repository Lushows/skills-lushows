# 181 — Firma electrónica y firma digital en la práctica

Hoy la mayoría de contratos comerciales se pueden firmar sin papel. La ley colombiana reconoce la **firma electrónica** (cualquier método confiable que identifique al firmante y su aceptación) y la **firma digital** (basada en un certificado emitido por una entidad de certificación acreditada, con más fuerza probatoria). La pregunta práctica no es "¿es válida?", sino "**¿podré probarla si la otra parte la niega?**". Este módulo complementa `29` con la operación diaria.

## Conceptos clave
- **Mensaje de datos:** información generada, enviada o archivada por medios electrónicos.
- **Firma electrónica:** métodos como códigos, contraseñas, datos biométricos o clics que identifican a una persona en relación con un mensaje de datos, siempre que sean confiables y apropiados.
- **Firma digital:** valor numérico asociado a un mensaje de datos mediante un certificado digital emitido por una **entidad de certificación** acreditada ante el **ONAC** (Organismo Nacional de Acreditación).
- **Evidencia (rastro de auditoría):** registro de quién firmó, cuándo, desde qué correo/IP, con qué método.
- **Equivalente funcional:** el mensaje de datos cumple las funciones del papel (escrito, firma, original) si reúne ciertos requisitos.

## Qué dice la norma
- Ley 527 de 1999: equivalencia funcional del mensaje de datos; firma (art. 7); original (art. 8); conservación (art. 12); firma digital con presunción de autenticidad cuando cumple los requisitos (art. 28).
- Decreto 2364 de 2012 (firma electrónica), compilado en el Decreto 1074 de 2015: la firma electrónica tiene la misma validez que la manuscrita si es confiable y apropiada (verificar).
- Código General del Proceso: valor probatorio de los documentos electrónicos y mensajes de datos.
- **Excepciones:** actos que exigen solemnidad especial (escritura pública de inmuebles, ciertos actos societarios o de familia) no se perfeccionan solo con firma electrónica simple; títulos valores tienen reglas propias (pagarés desmaterializados).

## Paso a paso: elegir el método según el riesgo
| Riesgo del documento | Método sugerido |
|---|---|
| Bajo (cotizaciones, NDA estándar, términos de compra en web) | Aceptación electrónica con registro (clic, correo, plataforma) |
| Medio (contratos comerciales, laborales, de servicios) | Plataforma de firma electrónica con autenticación por correo + celular y rastro de auditoría |
| Alto (contratos de alto valor, poderes, actas importantes) | Firma digital con certificado de entidad acreditada |
| Solemne (inmuebles, garantías que exigen escritura) | Notaría (o el medio especial que la ley permita) |

## Checklist operativo
1. **Acuerdo previo** en el contrato sobre el uso de firma electrónica (cláusula abajo).
2. **Verificar la identidad** del firmante y sus facultades (certificado de existencia de la contraparte).
3. **Descargar y archivar** el PDF firmado **y** el certificado o rastro de auditoría de la plataforma.
4. **No firmar con imágenes pegadas** de la firma manuscrita para contratos de riesgo medio o alto (prueba débil).
5. **Actas de asamblea virtuales:** dejar constancia del medio usado y la identidad de los participantes.

## Cláusula modelo
> "Las partes acuerdan que este contrato, sus anexos y modificaciones podrán suscribirse mediante firma electrónica a través de [PLATAFORMA] o mediante firma digital, conforme a la Ley 527 de 1999 y sus decretos reglamentarios, y reconocen que dichos métodos son confiables y apropiados para identificar a los firmantes y su aprobación. Cada parte conservará copia del documento firmado y de su registro de auditoría."

## Riesgos y errores comunes
- **Alto:** firma escaneada pegada en un PDF, sin evidencia de quién la puso.
- **Medio:** no descargar el rastro de auditoría (la plataforma puede cerrar o borrar).
- **Medio:** firmar electrónicamente actos que exigen solemnidad especial.
- **Bajo:** no verificar que el correo del firmante sea corporativo.

## Conexión con otros módulos
`29` firma electrónica (teoría) · `128` pagarés · `159` conservación · `180` CLM · `183` libros y actas · `177` contratos internacionales · **engineer_visualopen_lushows** (integración de firma en tus apps).

## Siguiente paso típico
Elegir una plataforma de firma con rastro de auditoría para contratos de riesgo medio y definir qué documentos irán con firma digital certificada.
