# 172 — Estados Unidos: LLC, C-Corp y Delaware (panorama)

Abrir una sociedad en Estados Unidos es rápido y barato; **operarla bien** desde Colombia es otra historia: impuestos federales y estatales, formularios informativos con multas altas, bancos, y además las obligaciones colombianas sobre esa inversión. Este módulo explica las dos figuras más usadas y sus trampas. Es **panorámico**: confirma con un abogado y un contador (CPA) en EE.UU.

## Conceptos clave
- **LLC (*limited liability company*):** sociedad de responsabilidad limitada, flexible. Por defecto, una LLC de un solo dueño es "transparente" para el impuesto federal (*disregarded entity*): sus resultados se atribuyen al dueño.
- **C-Corp:** sociedad por acciones que tributa por sí misma; es la preferida por fondos de capital de riesgo (VC).
- **Delaware:** estado con derecho societario muy desarrollado y tribunal especializado; estándar para startups que buscan inversión. Wyoming y otros estados son alternativas más baratas para LLC sin inversión institucional.
- **Registered agent:** agente registrado con dirección en el estado, obligatorio.
- **EIN:** número de identificación tributaria federal de la sociedad.
- **Sales tax:** impuesto a las ventas estatal; puede aplicar incluso sin presencia física si superas umbrales de ventas en un estado (*economic nexus*).

## Qué dice la norma (panorámico; verificar)
- Derecho societario: ley del estado de constitución (por ejemplo, Delaware General Corporation Law para C-Corp y Delaware Limited Liability Company Act para LLC).
- Impuesto anual del estado: Delaware cobra un impuesto anual a las LLC y un *franchise tax* a las corporaciones calculado por métodos que conviene revisar (el método por defecto puede arrojar cifras alarmantes; verificar).
- Federal (IRS): las LLC de un solo dueño extranjero tienen obligaciones informativas (Form 5472 con un Form 1120 pro forma), con multas significativas por no presentarlas (verificar).
- Beneficiarios finales (Corporate Transparency Act): en 2025 FinCEN eximió a las sociedades constituidas en EE.UU. del reporte; las extranjeras registradas para operar en EE.UU. siguen obligadas (verificar estado actual).
- Suplementos dietarios: Dietary Supplement Health and Education Act de 1994 (DSHEA); las declaraciones de estructura/función requieren la leyenda de que no han sido evaluadas por la FDA y notificación a la FDA; registro de instalaciones de alimentos ante la FDA para fabricantes extranjeros; el importador tiene obligaciones de verificación de proveedores extranjeros (FSVP). Verificar.
- Colombia y EE.UU. **no** tienen convenio para evitar la doble imposición (verificar).

## C-Corp vs. LLC (resumen)
| Criterio | LLC | C-Corp (Delaware) |
|---|---|---|
| Inversión de VC | Poco usada | Estándar |
| Impuesto | Transparente (un dueño) o elegible | Tributa la sociedad + dividendos |
| Costos y formalidades | Menores | Mayores |
| Uso típico | Vender servicios o productos en EE.UU., tener cuenta en dólares | Startup que levantará capital |

## Checklist
1. Definir el **para qué** (cuenta en dólares, Amazon US, inversionistas, contratos con clientes de EE.UU.).
2. Elegir estado y figura; contratar *registered agent*.
3. EIN, cuenta bancaria, contabilidad separada.
4. Calendario de obligaciones (impuesto anual del estado, formularios federales).
5. Obligaciones en Colombia: canalización cambiaria de la inversión (`139`), activos en el exterior y régimen de entidades controladas del exterior (**contador_lushows**).
6. Si vendes suplementos: cumplimiento FDA y claims de estructura/función.

## Riesgos y errores comunes
- **Alto:** no presentar los formularios informativos del IRS (multas muy altas).
- **Alto:** vender suplementos en EE.UU. con claims de enfermedad (la FDA y la FTC actúan).
- **Medio:** creer que la LLC "no paga impuestos en ningún lado" (en Colombia puedes tener obligaciones).
- **Bajo:** dejar vencer el agente registrado (la sociedad pierde su buen estado).

## Conexión con otros módulos
`139` inversión en el exterior · `165` precios de transferencia · `120`–`121` rondas y SAFE · `177`–`179` transfronterizo · `111` suplementos · **contador_lushows** · **economist_lushows**.

## Siguiente paso típico
Escribir en una frase para qué quieres la sociedad en EE.UU. y validar con un CPA el costo anual real de mantenerla antes de constituirla.
