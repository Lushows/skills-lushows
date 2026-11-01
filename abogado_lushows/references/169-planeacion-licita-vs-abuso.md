# 169 — Planeación tributaria lícita vs. abuso y evasión

Pagar menos impuestos **eligiendo legalmente** entre opciones que la ley ofrece es lícito: escoger el Régimen SIMPLE si conviene, ubicar una planta en una zona con beneficio real, deducir gastos legítimos. Lo ilícito es **simular** (crear apariencias sin realidad) o **abusar** de las formas legales sin propósito de negocio, solo para no pagar. La frontera importa porque del lado malo hay recálculo del impuesto, sanciones muy altas y, en casos graves, responsabilidad penal.

## Conceptos clave
- **Planeación tributaria (economía de opción):** elegir entre alternativas legales la que genera menos impuesto, con sustancia real.
- **Elusión / abuso en materia tributaria:** usar operaciones artificiosas, sin propósito económico o comercial relevante, para obtener un beneficio tributario.
- **Evasión:** ocultar ingresos, inflar costos o falsear información; es ilegal y puede ser delito.
- **Sustancia económica:** que la operación tenga una razón de negocio y efectos reales (personas, activos, riesgos).
- **Recaracterización:** la DIAN puede desconocer la forma y gravar según la realidad.

## Qué dice la norma
- Estatuto Tributario, art. 869 (abuso en materia tributaria), con desarrollo en los arts. 869-1 y 869-2 (verificar redacción vigente): permite a la DIAN recaracterizar operaciones abusivas.
- Código Penal: omisión de activos o inclusión de pasivos inexistentes (art. 434A) y defraudación o evasión tributaria (art. 434B) (verificar tipos y cuantías).
- Sanción por inexactitud agravada en casos de abuso (verificar art. 648 y relacionados).
- Ley 1258 de 2008, art. 42: desestimación de la personalidad jurídica si la sociedad se usa para defraudar a terceros.

## Prueba ácida: ¿lícito o abusivo?
| Pregunta | Si la respuesta es "no", alerta |
|---|---|
| ¿Haría esta operación aunque no ahorrara impuestos? | Falta de propósito de negocio |
| ¿Hay personas, activos y decisiones reales detrás de cada sociedad? | Falta de sustancia |
| ¿Los precios entre partes relacionadas son de mercado? | Riesgo de precios de transferencia (`165`) |
| ¿Los documentos reflejan lo que realmente pasa? | Riesgo de simulación |
| ¿Podría explicarla tranquilo ante un auditor de la DIAN? | Riesgo alto |

## Ejemplos ilustrativos
- **Lícito:** constituir una SAS separada para un negocio de riesgo distinto, con su equipo y sus clientes (`160`).
- **Lícito:** elegir SIMPLE cumpliendo todos los requisitos (`162`).
- **Riesgoso:** dividir un mismo negocio en varias sociedades idénticas para quedar bajo topes, sin razón operativa distinta del impuesto.
- **Abusivo/ilícito:** facturas de servicios inexistentes entre sociedades del grupo para trasladar utilidades; pagar salarios disfrazados de "reembolsos" para evitar aportes.

## Paso a paso antes de implementar una estrategia
1. Escribir en una página el **propósito de negocio** (además del ahorro).
2. Verificar **sustancia**: quién trabaja, dónde, con qué activos.
3. Revisar con **contador_lushows** y un tributarista la norma y la doctrina de la DIAN.
4. **Documentar**: actas, contratos, estudios.
5. Revisar cada año si la realidad sigue coincidiendo con la estructura.

## Riesgos y errores comunes
- **Alto:** "estrategias" vendidas por terceros que prometen pagar casi cero impuestos.
- **Alto:** gastos personales pasados como de la empresa.
- **Medio:** estructuras que funcionaban antes de una reforma y ya no.
- **Bajo:** no documentar el propósito de negocio de una reorganización.

## Conexión con otros módulos
`160` estructuración · `165` precios de transferencia · `166` beneficios · `168` sanciones · `153` penal · **contador_lushows** · **economist_lushows** (propósito de negocio).

## Siguiente paso típico
Aplicar la prueba ácida a cada sociedad y contrato intragrupo que tengas hoy y corregir lo que no la pase.
