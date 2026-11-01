# 14 — Acciones, capital y cap table legal

El **cap table** (tabla de capitalización) dice quién es dueño de qué porcentaje de la empresa. Es una hoja de cálculo para el inversionista, pero **legalmente** solo vale lo que está en los estatutos, en las actas y en el **libro de registro de accionistas**. Si esos tres documentos no cuadran con la hoja, el día que entre un inversionista o se pelee con un socio, el problema aparece.

## Conceptos clave (en simple)
- **Capital autorizado:** el máximo de capital que la sociedad puede emitir sin reformar estatutos.
- **Capital suscrito:** lo que los accionistas se comprometieron a pagar.
- **Capital pagado:** lo efectivamente pagado. En la SAS el suscrito puede pagarse hasta en dos años (Ley 1258 de 2008, art. 9).
- **Acción ordinaria:** voto y dividendo normales.
- **Acción privilegiada / con dividendo preferencial / de pago:** clases especiales permitidas en la SAS (Ley 1258, art. 10).
- **Voto múltiple:** una acción puede tener más de un voto si los estatutos lo dicen (Ley 1258, art. 11, verificar).
- **Libro de registro de accionistas:** donde se inscriben las acciones y sus transferencias; frente a la sociedad, es accionista quien aparece allí.
- **Dilución:** cuando entra capital nuevo, el porcentaje de los socios antiguos baja.
- **Vesting:** adquisición gradual de acciones por cumplir tiempo o metas. En Colombia se implementa por contrato (acuerdo de accionistas, opciones, promesa) porque no es una figura legal propia.

## Qué dice la norma (Colombia)
- **Ley 1258 de 2008:** clases y series de acciones (art. 10), voto (art. 11), plazos de pago del capital (art. 9), restricciones de negociación (arts. 13 y 14).
- **Código de Comercio:** reglas sobre títulos de acciones, libro de registro y transferencia (por endoso del título e inscripción en el libro, o por carta de traspaso según el caso; verificar el procedimiento estatutario).

## Cómo se arma un cap table legalmente sólido (paso a paso)
1. **Estatutos**: fijar capital autorizado con margen para futuras emisiones.
2. **Acta de suscripción** (o documento de constitución) con número de acciones, valor nominal y precio de cada accionista.
3. **Prueba del pago**: consignaciones a la cuenta de la SAS; si es aporte en especie (por ejemplo, una marca o un software), avalúo y documento de transferencia.
4. **Inscripción** en el libro de registro de accionistas.
5. **Títulos** de acciones o constancias, según los estatutos.
6. **Hoja de cap table** que cuadre exactamente con los cuatro pasos anteriores.

## Aportes que no son dinero (ojo)
- **Aporte en industria** (trabajo): en la SAS es discutido y puede no permitirse como capital; lo usual es reconocerlo con **acciones de pago** o con un esquema de vesting (verificar con abogado).
- **Aporte de marca o software:** debe transferirse por escrito a la sociedad (`60`, `63`); si no, la SAS usa algo que no es suyo.

## Ejemplo de cap table (cifras ilustrativas)
| Accionista | Acciones | % | Clase | Pagado |
|---|---|---|---|---|
| Luis | 7.000 | 70 % | Ordinaria | Sí |
| Socio técnico | 2.000 | 20 % | Ordinaria con vesting por contrato | Parcial |
| Reserva para equipo (opciones) | 1.000 | 10 % | No emitida aún | — |
> Si entra un inversionista con 2.500 acciones nuevas, todos se diluyen. El cálculo exacto (pre-money, post-money, dilución) va a **Matematicas_lushows**; la valoración a **economist_lushows**.

## Cláusula modelo: vesting por contrato (en el acuerdo de accionistas)
> «Las acciones del ACCIONISTA FUNDADOR estarán sujetas a un derecho de readquisición a favor de la sociedad o de los demás accionistas, que se extinguirá gradualmente así: [25 %] al cumplirse [doce (12)] meses de vinculación y el saldo en cuotas mensuales iguales durante los [treinta y seis (36)] meses siguientes. Si el FUNDADOR deja de prestar sus servicios antes, las acciones no liberadas podrán ser readquiridas al [valor nominal / valor pactado].»

## Riesgos y errores comunes
- **Alto:** prometer "porcentajes" a empleados o aliados por WhatsApp sin documento: genera reclamos y bloquea rondas de inversión.
- **Alto:** cap table que no cuadra con el libro de accionistas: el inversionista lo detecta en la due diligence (`122`).
- **Medio:** capital autorizado sin margen: cada emisión obliga a reformar estatutos.
- **Medio:** aporte en especie sin transferencia formal.

## Conexión con otros módulos
- `11` SAS · `15` acuerdo de accionistas · `18` aumento de capital · `120` rondas · `121` notas convertibles y SAFE · `122` due diligence.
- **Matematicas_lushows** (dilución) · **contador_lushows** (registro contable del capital).

## Siguiente paso típico
Conciliar la hoja de cap table con estatutos, actas y libro de accionistas; corregir diferencias con un acta y una reforma si hace falta.
