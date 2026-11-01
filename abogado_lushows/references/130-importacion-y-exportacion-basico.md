# 130 — Importación y exportación: lo básico

Importar o exportar no es solo "mandar una caja": es una operación vigilada por la **DIAN** (aduanas), el **Banco de la República** (divisas), y según el producto, el **INVIMA** o el **ICA**. Un error de clasificación, un permiso faltante o un pago mal canalizado puede dejar la mercancía retenida en puerto, generar multas o hasta su decomiso. Este módulo da el mapa general; los detalles van en `131`–`139`.

## Conceptos clave
- **Declaración de importación / de exportación:** el documento aduanero que declara la mercancía, su valor y su clasificación.
- **Subpartida arancelaria:** el código que clasifica la mercancía y define arancel, IVA y requisitos.
- **Arancel:** impuesto a la importación; puede ser cero por un tratado de libre comercio (`136`).
- **Vistos buenos / registros previos:** autorizaciones de otras entidades (INVIMA, ICA, etc.) que se tramitan en la **VUCE** (Ventanilla Única de Comercio Exterior).
- **Agencia de aduanas:** intermediario autorizado que hace los trámites aduaneros; en ciertos casos su uso es obligatorio (verificar cuantías).
- **Courier / tráfico postal:** régimen simplificado para envíos pequeños, con límites de valor y peso (verificar).

## Qué dice la norma
- Ley 1609 de 2013 (ley marco de aduanas) y Decreto 1165 de 2019 (régimen aduanero), con sus modificaciones (verificar vigencia).
- Régimen cambiario: Resolución Externa 1 de 2018 de la Junta Directiva del Banco de la República (verificar actualizaciones) — los pagos de importaciones y exportaciones de bienes deben canalizarse por el mercado cambiario (`134`).
- Requisitos sanitarios: Decreto 3249 de 2006 para suplementos importados, Resolución 2674 de 2013 para alimentos (`110`, `111`).
- Estatuto Tributario: IVA en importaciones y exenciones en exportación de bienes (verificar requisitos con **contador_lushows**).

## Paso a paso: importar
1. **Clasificar** la mercancía (subpartida) — si hay duda, pedir clasificación oficial anticipada a la DIAN.
2. Verificar **requisitos previos** en la VUCE (registro sanitario, visto bueno, licencia).
3. Negociar con el proveedor el **Incoterm** (`131`) y el contrato (`132`).
4. Pagar al proveedor por el **mercado cambiario** con la declaración de cambio correspondiente.
5. Transporte, llegada, **declaración de importación**, pago de arancel e IVA, levante (autorización de retiro).
6. Guardar todos los documentos (factura comercial, documento de transporte, certificado de origen, declaraciones).

## Paso a paso: exportar
1. RUT con la responsabilidad de exportador (verificar con **contador_lushows**).
2. Confirmar requisitos del **país de destino** (sanitarios, etiquetado, registro del producto allá).
3. Certificado de origen si se quiere preferencia arancelaria (`136`).
4. Solicitud de autorización de embarque y declaración de exportación.
5. Reintegro de divisas por el mercado cambiario.
6. Factura electrónica de exportación.

## Ejemplo (cláusula en contrato con proveedor extranjero)
> "EL VENDEDOR entregará con cada embarque: factura comercial, lista de empaque, documento de transporte, certificado de análisis por lote y certificado de origen en el formato del acuerdo comercial aplicable. Cualquier costo derivado de la falta o error de estos documentos será de cargo de EL VENDEDOR."

*Por qué:* sin documentos correctos, la mercancía se queda en puerto pagando bodegaje.

## Riesgos y errores comunes
- **Alto:** importar suplementos o alimentos sin registro sanitario de importación → retención o rechazo.
- **Alto:** subvalorar o mal clasificar la mercancía → multas y posible decomiso.
- **Medio:** pagar al proveedor por canales informales → infracción cambiaria.
- **Bajo:** no pedir el certificado de origen → pagar arancel que podía ser cero.

## Conexión con otros módulos
`131` Incoterms · `132` CISG · `134` cambiario · `136` origen · `137` aduanas · `111` suplementos · **contador_lushows** (IVA, exportación) · **dropshipping_lushows** (courier) · **economist_lushows** (costo puesto en destino).

## Siguiente paso típico
Clasificar el producto y revisar en la VUCE los requisitos previos antes de negociar precio con el proveedor o el comprador extranjero.
