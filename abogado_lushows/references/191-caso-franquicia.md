# 191 — Caso: convertir un restaurante exitoso en franquicia

**El caso.** Un restaurante de comida rápida en Bogotá, con dos locales propios y buen flujo, recibe propuestas de amigos y conocidos para "abrir uno igual" en Medellín y Cali. El dueño quiere crecer con franquicias sin perder el control de la marca ni del concepto. En Colombia no hay una ley especial de franquicias: todo depende de **los contratos, la marca registrada y el manual de operaciones**. Cifras ilustrativas.

## 1. Diagnóstico
- ¿La **marca** está registrada a nombre de la sociedad, en las clases correctas (servicios de restaurante y, si aplica, productos)? Si no, se detiene todo hasta registrarla (`60`).
- ¿El **concepto** está documentado (recetas, proveedores, procesos, diseño del local) o vive en la cabeza del dueño?
- ¿La **rentabilidad** del modelo resiste pagar regalías? (**economist_lushows**).
- ¿Hay capacidad de **soporte** (capacitación, auditoría, compras)?

## 2. Arquitectura legal
1. **Sociedad franquiciante** (idealmente separada de la operadora de los locales propios, `160`).
2. **Marca registrada** y vigilada (`61`).
3. **Manual de operaciones** confidencial (anexo del contrato).
4. **Documento de información previa** al franquiciado (buena práctica y protección por buena fe precontractual; `140`).
5. **Contrato de franquicia** + licencia de marca + acuerdos de confidencialidad con el personal clave del franquiciado.
6. **Contratos de suministro** con proveedores homologados (`100`).

## 3. Cláusulas clave del contrato (extractos)
**Licencia.** "EL FRANQUICIANTE otorga a EL FRANQUICIADO licencia no exclusiva de uso de la marca [X] y del saber hacer del sistema, solo para operar un establecimiento en [DIRECCIÓN], durante [5] años."

**Pagos.** "Derecho de entrada: $[X]. Regalía mensual: [5]% de las ventas netas (ilustrativo). Fondo de publicidad: [2]% de las ventas netas, administrado por EL FRANQUICIANTE con rendición anual de cuentas."
> *Por qué:* transparencia en el fondo de publicidad evita la pelea más común.

**Territorio.** "EL FRANQUICIANTE no abrirá ni autorizará otro establecimiento de la marca en un radio de [1,5] km, mientras EL FRANQUICIADO cumpla ventas mínimas de $[Y] mensuales en promedio trimestral."

**Estándares y auditoría.** "EL FRANQUICIADO cumplirá el manual de operaciones y permitirá auditorías sin previo aviso. Tres incumplimientos graves en un año facultan la terminación."

**Proveedores.** "EL FRANQUICIADO comprará los insumos críticos de calidad (salsas, mezclas, empaques con marca) a proveedores homologados; los demás podrá adquirirlos libremente cumpliendo las especificaciones."
> *Por qué:* imponer todos los proveedores sin justificación de calidad puede generar riesgo de libre competencia (`82`).

**Terminación y post-contrato.** "Al terminar, EL FRANQUICIADO cesará el uso de la marca, retirará los signos distintivos del local en [15] días, devolverá el manual y no operará un negocio similar en el mismo local ni en un radio de [1,5] km por [12] meses."

## 4. Cumplimiento del franquiciado (lo que debes exigirle)
Concepto sanitario, uso del suelo, bomberos, música con licencia, SG-SST, contratos laborales propios (los empleados son del franquiciado, no tuyos), facturación electrónica (`114`).

## 5. Riesgos y errores comunes
- **Alto:** franquiciar sin marca registrada.
- **Alto:** que el franquiciante "maneje" al personal del franquiciado (riesgo de solidaridad laboral o contrato realidad).
- **Medio:** fondo de publicidad sin rendición de cuentas.
- **Medio:** no prever qué pasa con el local y los clientes al terminar.
- **Bajo:** manual de operaciones incompleto.

## Conexión con otros módulos
`34` franquicia · `114` restaurantes · `60`–`61` marcas · `66` secretos · `82` competencia · `142` no competencia · **economist_lushows** (modelo de regalías) · **ventas_lushows** (venta de franquicias) · **contador_lushows** (facturación de regalías).

## Siguiente paso típico
Registrar y vigilar la marca, escribir el manual de operaciones y validar con **economist_lushows** que un franquiciado gana dinero pagando la regalía propuesta.
