# 141 — Cláusulas de precio, ajuste e indexación

En un contrato de varios meses, el precio fijo es una apuesta: si suben tus costos (materia prima, energía, dólar, salario mínimo), el margen desaparece y terminas trabajando a pérdida. Las **cláusulas de ajuste** reparten ese riesgo de forma ordenada y previsible. Una empresa grande aceptará un ajuste si es **objetivo, medible y simétrico** (que también baje cuando bajan los costos).

## Conceptos clave
- **Precio fijo:** no cambia durante el plazo.
- **Indexación:** ajuste según un índice público (IPC del DANE, salario mínimo, TRM, UVR).
- **Fórmula polinómica:** ajusta el precio por el peso de cada componente de costo (por ejemplo, 60% materia prima, 25% mano de obra, 15% otros).
- **Banda o umbral:** solo se ajusta si el índice varía más de cierto porcentaje.
- **Precio por tramos de volumen:** precio unitario menor a mayor volumen.
- **Moneda del contrato:** pesos, o dólares pagaderos en pesos a la tasa de cambio del día de pago.

## Qué dice la norma
- Libertad contractual para fijar el precio y sus reglas de ajuste (Código Civil, art. 1602; C.Co., art. 871 buena fe).
- Teoría de la imprevisión: si circunstancias extraordinarias, imprevistas e imprevisibles hacen excesivamente onerosa una prestación de cumplimiento futuro, se puede pedir al juez revisión (C.Co. art. 868). Es excepcional y lenta: **mejor pactar el ajuste**.
- Obligaciones en moneda extranjera entre residentes: por regla se pagan en pesos colombianos a la tasa de cambio aplicable (C.Co. art. 874 y régimen cambiario; verificar).
- Ley 2024 de 2020: el ajuste no puede usarse para disfrazar plazos de pago mayores al legal (`144`).

## Modelos de cláusula comentados

**A. Ajuste anual por IPC**
> "El precio se ajustará el [1 de enero] de cada año de vigencia en un porcentaje igual a la variación del IPC de los doce meses anteriores certificada por el DANE."
*Uso:* contratos de servicios estables. Es fácil de aceptar, pero no protege contra alzas fuertes de materia prima.

**B. Ajuste por costo de materia prima con banda**
> "Si el costo de [MATERIA PRIMA], acreditado con facturas de compra o índice [X], varía en más del [10]% frente al costo base del Anexo 2, cualquiera de las partes podrá solicitar el ajuste del precio en la proporción que dicha materia prima represente en el costo total ([60]%). El nuevo precio regirá para órdenes de compra emitidas [15] días después de la solicitud documentada."
*Uso:* productos con insumo volátil. Es **simétrico** (también baja) y documentado: eso lo hace aceptable.

**C. Precio por tramos de volumen**
> "Precio por kg: [1–100 kg/mes]: $[A]; [101–300]: $[B]; [más de 300]: $[C]. El tramo se determina por el volumen efectivamente recibido en el mes calendario."
*Uso:* incentiva al cliente a comprar más y protege tu margen en volúmenes bajos (ver `143`).

**D. Precio en dólares**
> "El precio se fija en USD [X] por kg y se facturará y pagará en pesos colombianos a la TRM vigente el día de [la factura / el pago]."
*Uso:* insumos importados. Ojo: elegir "día de factura" vs. "día de pago" cambia quién asume el riesgo cambiario durante el plazo.

## Riesgos y errores comunes
- **Alto:** precio fijo por 12 meses con insumo volátil y sin cláusula de ajuste.
- **Medio:** ajuste "de común acuerdo" sin criterio → el grande simplemente dice no.
- **Medio:** fórmula mal definida (índice sin fuente, base sin fecha).
- **Bajo:** no dejar constancia del costo base al firmar.

## Conexión con otros módulos
`100` plantilla · `143` volúmenes · `144` Ley 2024 · `147` hardship · `190` caso · **Matematicas_lushows** (verificar fórmulas y simular escenarios) · **economist_lushows** (estructura de costos) · **contador_lushows** (costo base documentado).

## Siguiente paso típico
Con **economist_lushows**, descomponer tu costo en componentes y porcentajes; con **Matematicas_lushows**, simular la fórmula en tres escenarios antes de proponerla.
