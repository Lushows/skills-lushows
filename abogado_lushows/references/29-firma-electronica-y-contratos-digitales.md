# 29 — Firma electrónica y contratos digitales

Hoy la mayoría de los tratos de Luis se cierran por WhatsApp, correo, una pasarela de pago o un "acepto" en una página. **Eso es válido en Colombia**: la ley reconoce los mensajes de datos y la firma electrónica. La clave no es si vale, sino **si se puede probar** quién aceptó, qué aceptó y cuándo.

## Conceptos clave (en simple)
- **Mensaje de datos:** información generada, enviada o guardada por medios electrónicos (correo, chat, PDF, registro en una base de datos).
- **Firma electrónica:** cualquier método (contraseña, código por SMS, clic de aceptación, firma dibujada en pantalla) que identifica al firmante y muestra su aprobación, si es confiable y apropiado para el fin.
- **Firma digital:** tipo especial de firma electrónica basada en un certificado digital emitido por una **entidad de certificación** acreditada; tiene presunciones más fuertes.
- **Clickwrap:** aceptación por clic en una casilla de «acepto los términos».
- **Browsewrap:** términos que supuestamente se aceptan solo por navegar; prueba débil.
- **Trazabilidad / evidencia:** registro de quién, cuándo, desde dónde y qué versión aceptó.

## Qué dice la norma (Colombia — verificar vigencia)
- **Ley 527 de 1999:** reconoce efectos jurídicos a los mensajes de datos (art. 5); cuando la ley exige que algo conste por escrito, el mensaje de datos lo satisface si es accesible para consulta posterior (art. 6); regula la firma (art. 7) y la firma digital (art. 28).
- **Decreto 2364 de 2012** (compilado en el Decreto 1074 de 2015): reglamenta la **firma electrónica**; establece que tiene la misma validez que la firma manuscrita si cumple requisitos de confiabilidad y apropiabilidad.
- **Código General del Proceso (Ley 1564 de 2012):** valoración de documentos y de mensajes de datos como prueba (art. 247, verificar).
- **Ley 2213 de 2022:** uso de tecnologías en procesos judiciales (notificaciones y actuaciones virtuales).
- **Ley 1480 de 2011:** obligaciones de información en comercio electrónico con consumidores (`53`).

## Qué método usar según el contrato
| Contrato | Método recomendado |
|---|---|
| Términos y condiciones de una web o bot | Clickwrap con registro de versión, fecha, hora e identificador del usuario |
| Contratos entre empresas de valor medio | Plataforma de firma electrónica con certificado de evidencias (correo + OTP) |
| Contratos de alto valor, pagarés, poderes | Firma digital con certificado o firma manuscrita con reconocimiento |
| Acuerdos por WhatsApp | Válidos, pero confirmar por correo un resumen y exportar el chat |
| Inmuebles, ciertas garantías | Lo que exija la ley (p. ej. escritura pública) |

## Checklist de evidencia (para que el contrato digital aguante)
- [ ] Identificación del firmante (correo verificado, número de celular, cédula).
- [ ] Versión exacta del documento aceptado (hash o PDF guardado).
- [ ] Fecha y hora (sello de tiempo).
- [ ] Registro técnico (IP, dispositivo) cuando sea posible.
- [ ] Copia enviada al firmante.
- [ ] Conservación por el tiempo de prescripción (`09`, `159`).

## Cláusula modelo: aceptación electrónica
> «Las partes acuerdan que este contrato y sus modificaciones podrán celebrarse mediante firma electrónica en los términos de la Ley 527 de 1999 y el Decreto 2364 de 2012 (compilado en el Decreto 1074 de 2015), y reconocen que dicha firma tiene la misma validez y efectos que la firma manuscrita. Las partes aceptan como prueba los mensajes de datos y registros electrónicos generados por la plataforma de firma, así como las comunicaciones enviadas a los correos electrónicos indicados en la cláusula de notificaciones.»

## Ejemplo (ilustrativo)
El bot de GastroLatam vende la calculadora por WhatsApp y cobra por pasarela. Para que la venta tenga respaldo: (1) el bot envía el enlace a los términos y pide confirmación expresa antes del pago; (2) se guarda el chat, la versión de los términos y el comprobante; (3) se emite factura electrónica. Con eso, ante un reclamo, hay prueba de qué se ofreció y qué aceptó el cliente.

## Riesgos y errores comunes
- **Alto:** firmar pagarés o cartas de instrucciones con métodos de firma débiles: la ejecución puede caerse (`94`).
- **Medio:** términos tipo browsewrap sin aceptación expresa.
- **Medio:** cambiar los términos sin guardar versiones: no se puede probar qué aceptó cada cliente.
- **Bajo:** no exportar ni respaldar chats de negociación.

## Conexión con otros módulos
- `20` teoría · `41` SaaS · `53` comercio electrónico · `58` términos web · `107` plantilla T&C · `181` firma electrónica práctica.

## Siguiente paso típico
Elegir una plataforma de firma electrónica con certificado de evidencias para contratos entre empresas y añadir la cláusula modelo a las plantillas.
