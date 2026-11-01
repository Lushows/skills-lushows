# 190 — Caso: microempresa que provee materia prima de hongos a un gran productor de café

**El caso.** Una microempresa colombiana (llamémosla HONGOS SAS, parecida a BIO-SETA) produce **extracto y polvo de hongos funcionales** (melena de león, cordyceps, ganoderma). Un **gran productor de café** quiere lanzar un "café funcional" con su marca y el ingrediente de HONGOS SAS, y propone un contrato de **suministro por 12 meses**. Para la microempresa es el negocio del año... y también el mayor riesgo: invertir en capacidad para un cliente que puede comprar poco, pagar tarde, copiar el proceso o usar la marca de forma que traiga problemas con el INVIMA. Este caso integra los módulos `100`–`149` en una sola negociación. **Todas las cifras son ilustrativas.**

## 1. Diagnóstico (módulo `02`)
- **Tamaños:** proveedor micro/pequeña; cliente gran empresa (Decreto 957 de 2019) → aplica el tope de **45 días** de la Ley 2024 de 2020 (`144`).
- **Poder de negociación:** el cliente es grande, pero el ingrediente es diferencial y difícil de sustituir rápido (calidad verificada por lote, trazabilidad). Esa es la palanca.
- **Regulatorio:** el producto terminado (café con hongos) lo pone en el mercado la cafetera: **ella tramita su registro, permiso o notificación sanitaria** como alimento. HONGOS SAS entrega ficha técnica y COA por lote y debe confirmar que su actividad cumple las condiciones sanitarias que le apliquen. **Verificar con el INVIMA** si el ingrediente requiere evaluación de su sala especializada para usarse en un alimento (`110`, `111`).
- **Riesgo principal:** dependencia de un solo cliente + inversión anticipada.

## 2. Etapa precontractual
1. **NDA mutuo** antes de mostrar el proceso (`102`), con prohibición de ingeniería inversa de muestras.
2. **Carta de intención** con hitos: pruebas de muestras, auditoría documental, borrador de contrato; muestras sobre [X] unidades pagadas por el cliente (`106`).
3. **Revelar por capas:** COA y ficha técnica sí; parámetros del proceso de extracción no (`140`).

## 3. Las cláusulas clave del contrato (extractos modelo)

**Objeto y plazo.** "Suministro de extracto en polvo de [ESPECIE] conforme al Anexo 1, durante doce (12) meses desde [FECHA], prorrogable por periodos iguales salvo aviso escrito con noventa (90) días de antelación."

**Calidad por lote (COA).** "Cada lote se entregará con certificado de análisis emitido por laboratorio [propio validado o tercero acreditado bajo ISO/IEC 17025], que incluirá como mínimo: (a) **contenido de beta-glucanos** por el método enzimático Megazyme para beta-glucanos de hongos y levaduras, con valor mínimo de [X]% (ilustrativo); (b) **identidad de especie** por secuenciación de la región ITS del ADN (por lote de materia prima o según frecuencia del Anexo 1); (c) **metales pesados** (plomo, cadmio, arsénico y mercurio) bajo los límites del Anexo 1; (d) **microbiología** (aerobios mesófilos, mohos y levaduras, coliformes o *E. coli*, *Salmonella*) bajo los límites del Anexo 1. EL PROVEEDOR conservará muestra de retención de cada lote por [24] meses. Si EL COMPRADOR objeta un resultado dentro de los [10] días hábiles siguientes a la recepción, se analizará la muestra de retención en un laboratorio acreditado elegido de común acuerdo, cuyo resultado será definitivo; el costo lo asumirá la parte cuyo resultado resulte equivocado."
> *Por qué:* criterios medibles y un mecanismo para dirimir diferencias sin pleito. Los límites concretos y métodos los define **Bio_lushows** / **Quimico_lushows**.

**Volumen mínimo y take-or-pay.** "Volumen mínimo de [300] kg por trimestre (ilustrativo). Si al cierre del trimestre EL COMPRADOR adquirió menos, pagará como precio de la capacidad reservada el [50]% del valor del déficit, recuperable el trimestre siguiente si cumple el mínimo." (`143`)

**Precio por tramos y ajuste.** "Precio por kg: hasta [300] kg/trimestre $[A]; de [301] a [600] $[B]; más de [600] $[C]. El precio se ajustará si el costo de la materia prima [sustrato/cuerpo fructífero] varía más del [10]%, en proporción a su peso en el costo ([55]%)." (`141`)

**Anticipo y póliza.** "Anticipo del [30]% del valor del primer trimestre, destinado a materia prima, amortizable con el [30]% de cada factura, garantizado con póliza de buen manejo del anticipo por el 100%." (`129`)

**Pago (Ley 2024 de 2020).** "Pago dentro de los cuarenta y cinco (45) días calendario siguientes a la recepción según remisión firmada. Descuento del [2]% por pago dentro de los [8] días (ilustrativo). EL COMPRADOR registrará en RADIAN los eventos de acuse y recibo dentro de los [2] días hábiles. La mora causará intereses a la tasa máxima legal y permitirá suspender despachos con facturas vencidas a más de [15] días." (`144`, `126`)
> *Por qué:* así se "cobra el tiempo": el precio base es a 45 días y el pronto pago se premia; no se ofrecen plazos mayores al legal.

**Co-branding.** "EL PROVEEDOR otorga licencia no exclusiva, intransferible y gratuita para usar la marca [MARCA DEL PROVEEDOR] en el empaque y la publicidad del producto, exclusivamente en la frase '[con extracto de ESPECIE de MARCA]', conforme al manual de marca. Toda pieza que mencione a EL PROVEEDOR o al ingrediente requerirá su aprobación escrita previa. EL COMPRADOR no hará, respecto del ingrediente, declaraciones de prevención, tratamiento o cura de enfermedades ni otras no permitidas por la normativa sanitaria, y será responsable de las declaraciones de su producto. EL COMPRADOR no registrará marcas que contengan o se asemejen a la de EL PROVEEDOR. Al terminar el contrato, cesará el uso, salvo el agotamiento de empaques ya producidos por [90] días." (`68`, `111`)
> *Por qué:* el co-branding da visibilidad, pero un claim de la cafetera puede contaminar la marca del proveedor ante el INVIMA y la SIC.

**Exclusividad condicionada.** "EL PROVEEDOR no suministrará el ingrediente a [competidores del Anexo 4] para bebidas a base de café en Colombia, mientras EL COMPRADOR cumpla el volumen mínimo. No limita las marcas propias de EL PROVEEDOR ni otras categorías." (`142`)

**Propiedad del know-how.** "Los procesos de cultivo, extracción y estandarización, las especificaciones internas y sus mejoras son secreto empresarial de EL PROVEEDOR. Nada en este contrato transfiere licencia sobre ellos. EL COMPRADOR no analizará el ingrediente para replicar el proceso ni contratará su fabricación con terceros usando información de EL PROVEEDOR. La formulación del café es propiedad de EL COMPRADOR." (`66`, `102`)

**Responsabilidad y seguros.** "Tope: valor pagado en los últimos 12 meses, salvo dolo o culpa grave. Indemnidad del proveedor solo por defectos del ingrediente frente a la especificación. Póliza de RC con productos por $[X]." (`146`, `152`)

**Terminación.** "Sin causa, con [90] días de preaviso, pagando el inventario terminado y la materia prima adquirida específicamente para EL COMPRADOR, hasta por [un] trimestre de volumen mínimo. Por incumplimiento grave no subsanado en [15] días tras requerimiento escrito." (`27`)

**Disputas.** "Arreglo directo [30] días; luego conciliación; luego arbitraje en [Centro de Arbitraje de la Cámara de Comercio de X], un árbitro, procedimiento [abreviado si el reglamento lo prevé]." (`92`)

## 4. Mapa de concesiones (qué dar y qué pedir)
| Si la cafetera pide… | Pide a cambio… |
|---|---|
| Exclusividad | Volumen mínimo con take-or-pay |
| Precio fijo 12 meses | Tramos de volumen o ajuste por materia prima |
| 60–90 días de pago | Recordar la Ley 2024; ofrecer pronto pago con descuento |
| Responsabilidad ilimitada | Tope + póliza RC con productos |
| Acceso al proceso | NDA + auditoría documental, no técnica |

## 5. Riesgos y errores comunes
- **Alto:** invertir en capacidad con solo una carta de intención.
- **Alto:** aceptar claims de la cafetera sobre el ingrediente sin control.
- **Alto:** firmar exclusividad sin volumen mínimo.
- **Medio:** COA sin métodos ni laboratorio definidos → peleas sobre calidad.
- **Medio:** pagos "desde la radicación de la factura" en lugar de la recepción.

## Conexión con otros módulos
`100` plantilla · `102` NDA · `106` LOI · `111` suplementos · `126` RADIAN · `129` anticipo · `141`–`149` negociación · `151` producto · **Bio_lushows** (especies, COA, límites) · **Quimico_lushows** (métodos analíticos) · **economist_lushows** (punto de equilibrio y precio) · **Matematicas_lushows** (tramos, take-or-pay, descuento por pronto pago) · **ventas_lushows** (conducción de la negociación) · **contador_lushows** (IVA, factura, anticipo).

## Siguiente paso típico
Con **economist_lushows** y **Matematicas_lushows**, calcular costo por kg, volumen de equilibrio y precios por tramo; con **Bio_lushows**, fijar el Anexo 1 de especificaciones; luego redactar el contrato completo sobre `100` y hacerlo revisar por abogado antes de firmar.
