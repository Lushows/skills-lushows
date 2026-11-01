# Cupones propios

Un cupón es un descuento que el comprador activa, no uno que todos ven en la vitrina. Sirve para
rescatar carritos, premiar recompra y hacer promociones que no queman tu precio de lista. El
problema es que **el mecanismo exacto de cupones de vendedor en Mercado Libre Colombia no se pudo
verificar en 2026**, así que este módulo enseña el concepto y te manda a comprobarlo en el panel.

## El estado del dato

> ⚠️ **Sin verificar para Colombia (sep-2026).** El **mecanismo de cupones propios del vendedor**
> —si existe, cómo se crea, qué límites tiene, si se puede segmentar— **no se pudo confirmar en
> fuente oficial**. Las descripciones que circulan son de otros países o de versiones viejas de la
> plataforma.
> Compruébalo en tu panel: **Mi cuenta → Marketing → Promociones / Descuentos**. Si existe, la
> propia herramienta te dirá sus reglas; si no aparece, no existe para tu cuenta.

No inventes la mecánica ni la copies de un tutorial mexicano. Si vas a construir una promoción
alrededor de cupones, el primer paso es ver la pantalla.

**Un cupón que crees que existe y no existe es una promoción que anunciaste y no puedes cumplir —
y eso sí tiene consecuencias legales (`92`).**

## Qué averiguar cuando entres al panel

```
□ ¿Existe la opción de crear cupones propios en mi cuenta?
□ ¿Es para toda la tienda o por publicación?
□ ¿El descuento es monto fijo o porcentaje?
□ ¿Hay monto mínimo de compra?
□ ¿Tiene fecha de inicio y fin, o corre indefinido?
□ ¿Se puede limitar la cantidad de usos, total y por comprador?
□ ¿Se puede segmentar (nuevos compradores, recompra, Meli+)?
□ ¿El cupón afecta el precio que ve el algoritmo para el catálogo?
□ ¿Se acumula con campañas de ML o son excluyentes?
□ ¿Quién asume el descuento: yo, ML, o compartido?
```

Las dos últimas son las caras. Un cupón que se acumula con un descuento de campaña puede dejarte
vendiendo 40% abajo sin que lo hayas decidido.

## Para qué sirve el concepto (si existe en tu panel)

| Uso | Por qué el cupón es mejor que bajar el precio |
|---|---|
| **Rescatar carrito abandonado** | El descuento llega solo a quien no compró; los demás pagan precio completo |
| **Premiar recompra** | Sube el LTV sin tocar tu precio de vitrina |
| **Probar elasticidad** | Mides cuánto descuento necesitas sin quemar el precio de referencia |
| **Liquidar sin señal de mercado** | El competidor no ve tu precio real bajar (`89`) |
| **Empujar el ticket** | Cupón con mínimo de compra: te ayuda a cruzar $60.000 (`79`) |

El último es el uso más rentable en Colombia. Un cupón de $5.000 con mínimo de $70.000 empuja al
comprador por encima del umbral, donde el envío gratis ya está incluido en el precio y tu margen
por pedido sube aunque des el descuento.

## La regla de cálculo, que sí puedo darte

Exista o no la herramienta, el cálculo de si un cupón conviene es el mismo de cualquier descuento:

```
python scripts/margen_ml.py margen --precio 74900 --costo 38000 --comision 15 \
    --envio 8200 --otros 900 --iva 19

# Con cupón de $6.000 aplicado
python scripts/margen_ml.py margen --precio 68900 --costo 38000 --comision 15 \
    --envio 8200 --otros 900 --iva 19
```

Cargo **15% — ejemplo dentro del rango oficial 8%-22%, verifica el tuyo** (`76`).

Dos detalles que hay que verificar en el panel antes de fiarte del cálculo:

1. **¿Sobre qué precio cobra ML su cargo, el de lista o el que pagó el comprador?** Cambia el
   resultado. Míralo en el desglose de una venta real con cupón.
2. **¿El cupón puede bajar el precio efectivo por debajo de $60.000?** Si sí, el envío cambia de
   columna y el cupón se paga solo (`79`). Si no, el envío sigue siendo el caro.

## El riesgo de anunciar un cupón

Si publicas un cupón, ese descuento es una promesa comercial. La SIC vigila que el precio final
corresponda al anunciado y que no haya costos ocultos (`92`). Un cupón que no se aplica al pagar,
que tiene condiciones no visibles, o que caducó antes de lo anunciado, es exactamente el tipo de
cosa que genera reclamos y denuncias.

```
□ Las condiciones del cupón son visibles ANTES de comprar
□ La fecha de fin es real y se respeta
□ El monto mínimo está escrito, no implícito
□ Si se agotan los usos, el anuncio deja de mostrarse
□ El descuento se aplica de verdad en el checkout
```

## Las alternativas verificadas

Mientras confirmas si los cupones existen para tu cuenta, estas sí están confirmadas:

| Alternativa | Estado | Módulo |
|---|---|---|
| Descuento propio en la publicación | Disponible | `91` |
| Campañas de Mercado Libre (Hot Sale 19-23 oct 2026) | Confirmado | `91` |
| Kits que suben el ticket | Disponible | `87` |
| Precio por cantidad | **Limitado a cuentas con perfil B2B** | `94` |
| Segmentar campañas de Ads a la audiencia Meli+ | Disponible | `150`-`164` |

Esa última es interesante: **Meli+** llegó a Colombia el **26-ago-2025** con planes desde **$9.900
COP/mes** para el comprador, y sus miembros son más recurrentes. La membresía no la pagas tú, pero
sí puedes segmentar campañas hacia esa audiencia.

## El error clásico

Diseñar toda una estrategia de retención con cupones a partir de un tutorial, descubrir que la
herramienta no está en tu panel, y salir a improvisar descuentos manuales por mensaje — que además
viola las reglas de comunicación con el comprador. Primero mira la pantalla, después diseña.

## Relacionados

`87` subir el ticket con kits · `88` precio psicológico · `89` la guerra de precios · `91`
descuentos y campañas · `92` el precio tachado y la SIC · `94` precio por cantidad y B2B · `79` el
umbral de los $60.000 · `82` la calculadora de margen · `150`-`164` Mercado Ads y crecimiento
