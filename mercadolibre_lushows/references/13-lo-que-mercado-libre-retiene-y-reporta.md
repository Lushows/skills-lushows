# Lo que Mercado Libre retiene y reporta

Entre el precio que el comprador paga y la plata que puedes retirar hay tres descuentos, no uno.
La comisión es el que todo el mundo conoce. Los otros dos —los cargos de plataforma y las
retenciones tributarias— son los que descuadran las cuentas. Este módulo te enseña **dónde
leerlos en tu propia cuenta**, porque las tarifas colombianas no están públicas.

## La advertencia que manda sobre todo este módulo

> ⚠️ **Sin verificar para Colombia (sep-2026).** No se pudo confirmar en fuente oficial qué
> retiene Mercado Pago Colombia por normativa DIAN: ni los conceptos (retefuente, ReteIVA,
> ReteICA), ni las tarifas, ni las bases, ni si se practican sobre cada venta o sobre el
> retiro. Las cifras que circulan en blogs son de Argentina, México o Brasil y **no aplican**.
> Léelo en tu propia cuenta: **Mercado Pago → Actividad → detalle del movimiento** y
> **Mercado Pago → Informes / Certificados de retención**.

No uses ningún porcentaje de retefuente ni de ICA que no hayas visto con tus ojos en tu propio
extracto. Cualquiera que te dé un número de memoria para Colombia se lo está inventando o lo
está copiando de otro país.

## Los tres descuentos, separados

| Descuento | Quién se lo queda | Dónde se ve |
|---|---|---|
| **Comisión de venta** | Mercado Libre | Detalle de la venta y liquidación mensual |
| **Cargos de plataforma** (envío, cargo fijo, publicidad) | Mercado Libre | Liquidación y reportes de Ads |
| **Retenciones tributarias** | La DIAN y el municipio, vía ML | Certificados de retención de Mercado Pago |

La diferencia práctica: **la comisión es un gasto; la retención es un anticipo de impuesto**.
La retención no la perdiste, la puedes descontar cuando declares. Pero sí te quita caja hoy. Si
tratas la retención como gasto, calculas mal el margen; si la tratas como si no existiera,
calculas mal el flujo.

**La comisión te reduce la utilidad. La retención te reduce la caja pero no la utilidad. No son
lo mismo y no van en la misma línea.**

## Los cuatro lugares donde se lee la verdad

```
□ 1. Detalle de una venta concreta
     Ventas → la orden → "Detalle de la venta" / "Ver desglose"
     Ahí aparece: precio, comisión, costo de envío asumido, cargos.
□ 2. Actividad de Mercado Pago
     Cada movimiento con su desglose. Aquí se ven descuentos que no aparecen en la venta.
□ 3. Informes / Liquidaciones
     El reporte descargable por periodo. Es el documento que le entregas al contador.
□ 4. Certificados de retención
     Mercado Pago → Informes → Certificados / Impuestos. Es el papel que soporta el
     descuento ante la DIAN.
```

Descarga el reporte del punto 3 **todos los meses** y guárdalo. No dependas de que la
plataforma conserve el histórico completo ni de que se lo puedas pedir después.

## El método para saber tu descuento real (sin adivinar)

Este es el reemplazo honesto de una tabla de porcentajes que no tenemos:

```
□ Haz una venta real de valor conocido (o tómala de tu histórico)
□ Anota el precio publicado
□ Busca en Mercado Pago el monto EXACTO que quedó acreditado por esa venta
□ Resta:  precio publicado – acreditado = descuento total en pesos
□ Abre el desglose y separa cuánto es comisión, cuánto envío, cuánto retención
□ Divide cada parte entre el precio publicado → tus porcentajes REALES
□ Repite con 3 ventas de distinto valor: el cargo fijo por venta de bajo valor,
  si existe en Colombia, se delata porque el % sube en las ventas baratas
□ Mete esos porcentajes en la calculadora de margen, no los del blog
```

Tres ventas de distinto valor te dan más verdad sobre tu negocio que veinte artículos de
internet. Y te sirven de línea base: si el mes entrante el descuento cambia, lo detectas.

## Lo que sí está verificado sobre el método

La forma oficial de conocer el **costo de publicación y la comisión** por rango de precio es el
simulador estando logueado, o la API:

```
# Ojo: este endpoint YA NO es público. Desde 2026 responde
# 403 PA_UNAUTHORIZED_RESULT_FROM_POLICIES y exige token.
GET https://api.mercadolibre.com/sites/MCO/listing_prices?price=50000
```

Mientras no tengas token, la vía es el simulador oficial estando logueado.

(método verificado, ALTA). Eso te resuelve la comisión y el costo de publicación. **No te
resuelve las retenciones tributarias**, que son otra cosa y viven en Mercado Pago.

## ML como agente retenedor y como reportante

Dos funciones distintas, y las dos te afectan:

1. **Agente retenedor**: te descuenta y le entrega a la DIAN plata a tu nombre. Tú luego la
   imputas en tu declaración con el certificado.
2. **Reportante de información**: las plataformas reportan las operaciones de sus vendedores.
   Es decir, **la DIAN sabe cuánto vendiste aunque tú no lo declares**.

El punto 2 mata la fantasía de "vendo por Mercado Libre y no declaro". Tu histórico de ventas
está registrado, con fecha, monto y contraparte, en una plataforma que reporta.

⚠️ **Sin verificar para Colombia (sep-2026).** El alcance exacto del reporte de información
exógena de las plataformas de comercio electrónico en Colombia, los umbrales y los formatos
son materia de `contador_lushows`. No inventes el número de formato ni el umbral.

## Cómo entregarle esto al contador

```
□ Liquidación mensual de Mercado Libre (comisiones y cargos)
□ Extracto de Mercado Pago del periodo
□ Certificados de retención descargados
□ Reporte de ventas con detalle de IVA
□ Facturas emitidas (si usas integración, salen de ahí → `14`)
```

Con esos cinco documentos el contador arma el mes. Sin ellos, te va a pedir que reconstruyas a
mano, y te va a cobrar por hacerlo.

Lo que él hace con eso —imputar retenciones, liquidar IVA, presentar— es de `contador_lushows`.
Tú entregas los soportes; él los convierte en declaración.

## El error clásico

Calcular el margen con "precio menos comisión" y descubrir a fin de mes que la caja no alcanza.
Entre la comisión, el envío asumido, el cargo fijo si aplica, la publicidad y las retenciones,
el descuento total sobre el precio publicado **es bastante mayor que la comisión sola**. El que
solo resta la comisión se cree rentable hasta que se queda sin plata para reponer inventario.

Y el error hermano: **no descargar los certificados de retención**. Esa plata ya la pagaste;
sin el certificado no la puedes descontar y la pagas dos veces.

## Relacionados

`12` datos fiscales y RUT · `14` facturación electrónica · `15` cuándo te liberan la plata ·
`76` las comisiones · `77` cargos fijos · `82` margen real · `166` el tablero de control ·
`contador_lushows` para declarar, liquidar e imputar
