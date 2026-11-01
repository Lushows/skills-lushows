# 121 — Notas convertibles y SAFE

Para rondas tempranas (amigos, ángeles, aceleradoras), negociar una valoración es difícil: la empresa casi no tiene números. Por eso existen instrumentos que **posponen la valoración**: el inversionista entrega dinero hoy y recibe acciones **después**, en la siguiente ronda, con un descuento o un tope de valoración como premio por el riesgo. Los dos más conocidos son la **nota convertible** y el **SAFE**. Ambos nacieron en EE.UU.; en Colombia hay que adaptarlos.

## Conceptos clave
- **Nota convertible:** un préstamo que, en lugar de pagarse, se **convierte** en acciones cuando ocurre un evento (normalmente una ronda calificada). Tiene intereses y vencimiento.
- **SAFE** (*Simple Agreement for Future Equity*, acuerdo simple por acciones futuras): no es préstamo; es un derecho a recibir acciones futuras. Sin intereses ni vencimiento (en su versión original de Y Combinator).
- **Tope de valoración (*valuation cap*):** valoración máxima a la que se convierte el dinero.
- **Descuento:** porcentaje de rebaja sobre el precio de la ronda (por ejemplo, 20%).
- **Evento de liquidez:** venta de la empresa antes de la conversión.

## Qué dice la norma (Colombia)
- No hay una ley específica de SAFE. Se estructura como **contrato atípico** (válido por la autonomía de la voluntad) o como **contrato de suscripción de acciones con precio diferido**; su encaje contable y tributario debe revisarse (¿pasivo?, ¿patrimonio?, ¿anticipo para futuras capitalizaciones?) con **contador_lushows**.
- La nota convertible es un **mutuo** (préstamo) con opción de conversión: aplican límites de **usura** a los intereses (Código Penal, art. 305; tasas certificadas por la Superintendencia Financiera).
- La conversión implica **emitir acciones**: se requieren las aprobaciones de estatutos (derecho de preferencia, reglamento de colocación; Ley 1258 de 2008).
- Si el inversionista es extranjero, el dinero debe canalizarse y registrarse según el régimen cambiario (verificar si se registra como inversión o como endeudamiento externo, `134`).
- Captar dinero del público de forma masiva sin autorización puede ser **captación ilegal** (delito): solo con inversionistas determinados.

## Comparativo rápido
| | Nota convertible | SAFE |
|---|---|---|
| Naturaleza | Préstamo | Derecho a acciones futuras |
| Intereses / vencimiento | Sí | No (original) |
| Riesgo para el fundador | Si no hay ronda, hay que pagar | Menor |
| Encaje en Colombia | Más familiar (mutuo) | Requiere adaptación |

## Cláusula modelo (SAFE adaptado, extracto)
> "EL INVERSIONISTA entrega a LA SOCIEDAD $[X] en calidad de [anticipo para futura suscripción de acciones]. En la próxima emisión de acciones por un monto mínimo de $[Y] (Ronda Calificada), dicho valor se aplicará a suscribir acciones de la misma clase emitida, al menor entre (a) el precio por acción de la Ronda Calificada con un descuento del [20]%, o (b) el precio resultante de una valoración pre-money de $[TOPE]. Si antes ocurre una venta de LA SOCIEDAD, EL INVERSIONISTA recibirá el mayor entre su inversión y lo que le correspondería convertido al tope."

*Por qué:* el tope y el descuento definen cuánta empresa entregas; simula escenarios con **Matematicas_lushows**.

## Riesgos y errores comunes
- **Alto:** acumular muchos SAFE con topes bajos → dilución sorpresa enorme en la ronda.
- **Alto:** "inversión" recibida de muchas personas por redes sociales → riesgo de captación ilegal.
- **Medio:** no prever qué pasa si nunca hay ronda (¿se devuelve?, ¿se convierte a un precio fijo?).
- **Medio:** no canalizar por el mercado cambiario la plata del exterior.
- **Bajo:** no registrar contablemente el instrumento.

## Conexión con otros módulos
`120` term sheet · `125` crowdfunding · `134` cambiario · `14` cap table · **economist_lushows** · **Matematicas_lushows** (conversión) · **contador_lushows** (tratamiento contable y fiscal).

## Siguiente paso típico
Simular la conversión de todos los instrumentos en una ronda hipotética y, si hay inversionistas extranjeros, confirmar el canal cambiario antes de recibir el dinero.
