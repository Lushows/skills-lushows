# 120 — Rondas de inversión y term sheet

Cuando un inversionista quiere entrar a tu empresa, lo primero que llega es un **term sheet** (hoja de términos): dos o tres páginas con el precio, cuánto pone, qué porcentaje recibe y qué derechos exige. Parece un trámite, pero ahí se decide casi todo: quién controla, cuánto recibe cada uno si la empresa se vende y qué puedes hacer sin pedir permiso. Firmar un mal term sheet es difícil de corregir después.

## Conceptos clave
- **Valoración pre-money / post-money:** valor de la empresa antes / después de que entre la plata. Porcentaje del inversionista = inversión ÷ post-money.
- **Dilución:** la reducción de tu porcentaje cuando se emiten acciones nuevas.
- **Preferencia de liquidación:** el inversionista recupera primero su dinero (1x = una vez lo invertido) si la empresa se vende o liquida. *Participativa* = además participa del resto (más dura para el fundador).
- **Antidilución:** protección del inversionista si una ronda posterior es más barata (*full ratchet* = muy agresiva; *weighted average* = estándar).
- **Pool de opciones (ESOP):** acciones reservadas para empleados clave.
- **Derechos de veto (*protective provisions*):** decisiones que requieren el sí del inversionista.

## Qué dice la norma
- Ley 1258 de 2008: la SAS permite emitir **clases de acciones** (preferenciales, con dividendo preferencial, con voto múltiple, etc.), lo que facilita estas rondas (verificar requisitos de la emisión y del reglamento de colocación).
- Inversión extranjera: si el inversionista es del exterior, registro ante el Banco de la República (`134`, `139`).
- Mercado de valores: ofrecer acciones al público en general puede ser oferta pública regulada; las rondas privadas a pocos inversionistas calificados normalmente no (verificar con abogado de mercado de valores).

## Paso a paso de una ronda
1. **Preparar la casa:** estatutos y cap table limpios (`14`, `104`), PI a nombre de la empresa, contratos firmados (`122`).
2. **Negociar el term sheet** (normalmente no vinculante salvo confidencialidad y exclusividad).
3. **Due diligence** del inversionista.
4. **Documentos definitivos:** contrato de suscripción de acciones, reforma de estatutos, acuerdo de accionistas.
5. **Cierre:** desembolso, emisión de acciones, inscripción en libro de accionistas, registro cambiario si aplica.

## Cláusula modelo (term sheet, extracto comentado)
> "**Inversión:** USD [X] por acciones preferenciales Serie Semilla, sobre una valoración pre-money de USD [Y], incluyendo un pool de opciones del [10]% calculado en el pre-money.
> **Preferencia de liquidación:** 1x no participativa.
> **Antidilución:** promedio ponderado amplio (*broad-based weighted average*).
> **Junta directiva:** [2] fundadores, [1] inversionista.
> **Vetos:** emisión de acciones con derechos superiores, venta de la compañía por debajo de [Z], cambio del objeto principal."

*Por qué:* "pool en el pre-money" significa que la dilución del pool la pagan solo los fundadores. Negociable. 1x no participativa y promedio ponderado son lo más amigable para el fundador.

## Riesgos y errores comunes
- **Alto:** preferencia participativa o múltiple (2x, 3x) → en una venta mediana el fundador recibe muy poco.
- **Alto:** *full ratchet* o vetos operativos amplios (contrataciones, presupuesto).
- **Medio:** no calcular la dilución real con pool incluido (pásalo a **Matematicas_lushows**).
- **Medio:** exclusividad larga en el term sheet sin compromiso de cierre.
- **Bajo:** olvidar el registro cambiario de la inversión extranjera.

## Conexión con otros módulos
`14` cap table · `18` aumento de capital · `105` acuerdo de accionistas · `121` SAFE y notas · `122` due diligence · `139` inversión extranjera · **economist_lushows** (valoración y si conviene levantar) · **Matematicas_lushows** (tabla de dilución y cascada de liquidación).

## Siguiente paso típico
Modelar con **Matematicas_lushows** la cascada de liquidación (quién recibe cuánto en 3 escenarios de venta) antes de aceptar el term sheet.
