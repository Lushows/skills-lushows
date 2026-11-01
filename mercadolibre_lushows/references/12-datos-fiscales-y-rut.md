# Datos fiscales y RUT

Lo fiscal aquí importa por una razón muy concreta: **en Mercado Libre el precio que publicas
es el precio final con IVA incluido**, así que tu condición tributaria entra directo en el
número que el comprador ve. Lo demás —declarar, liquidar, llevar libros— es de
`contador_lushows`.

## Lo que tienes que tener listo antes de vender

```
□ RUT actualizado y con la actividad económica de comercio al por menor incluida
□ Saber si eres o no responsable de IVA (casilla 53 del RUT)
□ Saber en qué régimen estás: Simple o ordinario
□ Datos de facturación cargados en Mi cuenta → Datos de facturación
□ Que el nombre/razón social del RUT coincida con el titular de la cuenta ML
□ Que la cuenta bancaria de retiro esté a nombre del mismo titular
□ Numeración de facturación electrónica habilitada si estás obligado a facturar → `14`
```

El punto que más se rompe: **incoherencia entre el titular de la cuenta, el RUT y la cuenta
bancaria**. Los tres tienen que ser la misma persona o el mismo NIT. Cuando no coinciden, el
retiro se traba y nadie te explica por qué.

## Por qué el RUT te cambia el precio publicado

| Situación | Efecto en el precio que publicas |
|---|---|
| No responsable de IVA | El precio que publicas es todo tuyo (menos comisión y costos) |
| Responsable de IVA, producto gravado 19% | De cada $119.000 publicados, $19.000 no son tuyos |
| Responsable de IVA, producto excluido | No hay IVA, pero tampoco descuentas IVA de tus compras |
| Responsable de IVA, producto exento 0% | IVA cero al vender, sí descuentas el de compras |

Esto es brutal cuando compites contra alguien que no es responsable de IVA: **con el mismo
precio publicado, él se lleva 19% más que tú**. No es que "venda más barato": es que juega otro
juego. Ver `81` y `84`.

**El competidor que "vende imposible de barato" muchas veces no tiene un mejor proveedor: tiene
otra condición tributaria o no está facturando.**

## Simple vs ordinario: solo lo que afecta al marketplace

| | Régimen Simple (RST) | Ordinario |
|---|---|---|
| Cómo se paga | Anticipos bimestrales sobre ingresos brutos | Renta anual + retenciones |
| Base | **Ingresos brutos**, no la utilidad | Utilidad |
| Efecto en ML | Vendes mucho con poco margen → duele más | El margen bajo se refleja en menos renta |
| ICA | Integrado en el Simple | Se declara aparte en cada municipio |
| Retenciones que te practican | Régimen distinto de retención | Régimen estándar |

La implicación de marketplace: **si tu modelo es alto volumen y margen delgado, el Simple
castiga**, porque te cobra sobre lo que facturas, no sobre lo que ganas. Vender $100.000.000
con 8% de margen y tributar sobre los $100.000.000 es una aritmética distinta a tributar sobre
los $8.000.000.

Cuál te conviene, con tus números reales, no lo decide esta skill:
→ **`contador_lushows`**. Y si necesitas la comparación numérica exacta, ejecútala en
`Matematicas_lushows`, no la estimes de cabeza.

## Dónde se cargan los datos en Mercado Libre

Los datos fiscales viven en **Mi cuenta → Información personal / Datos de facturación**. Ahí se
define si emites factura, con qué datos y a nombre de quién.

⚠️ **Sin verificar para Colombia (sep-2026).** La ruta exacta del menú, los campos obligatorios
y si ML valida tu RUT contra la DIAN en línea no se pudieron confirmar: las páginas de ayuda de
`mercadolibre.com.co` devuelven 403 a consulta automatizada. Ábrelo logueado en tu cuenta y
verifica el formulario real antes de asumir nada.

## Lo que Mercado Libre hace con esos datos

Tres cosas, y conviene no confundirlas:

1. **Los usa para la factura** que se genera por la venta, si tienes facturación integrada
   (`14`).
2. **Los usa para cobrarte a ti**: las comisiones y los cargos de ML también se te facturan.
3. **Los usa para practicar retenciones** sobre lo que te paga Mercado Pago (`13`).

El punto 3 es el que la gente descubre tarde: el dinero que entra a Mercado Pago **no es
exactamente el precio de venta menos la comisión**. Hay un tercer descuento de origen
tributario. Cuánto, con qué concepto y con qué tarifa → `13`, y la liquidación de eso →
`contador_lushows`.

## La aritmética honesta del precio

El orden correcto para pensar el precio en Colombia, con IVA adentro:

```
precio publicado (con IVA)
  – IVA (no es tuyo, es de la DIAN)
  = base sin IVA
      – comisión de la categoría (ojo: se cobra sobre el precio CON IVA)
      – cargo fijo por venta de bajo valor, si aplica
      – envío que asumes tú, neto del subsidio de ML
      – empaque y costos propios
      – costo del producto
  = utilidad
```

Dos trampas dentro de esa fórmula:

- **La comisión se calcula sobre el precio con IVA**, no sobre la base. Es decir, pagas
  comisión también sobre la plata de la DIAN.
- El IVA que pagaste al comprar el producto es descontable si eres responsable de IVA, y eso
  no aparece en la fórmula de arriba: aparece en tu declaración. Otra razón para no calcular
  el margen a ojo.

Ejecuta siempre el cálculo, no lo estimes:
`python scripts/margen_ml.py margen --precio X --costo Y --comision Z --iva 19`

Ver `81` (el precio con IVA adentro) y `82` (margen real).

## El error clásico

Publicar el precio "que me deja $X" sin restar el IVA, porque el vendedor viene de vender en
efectivo sin facturar. Cuando llega el momento de declarar descubre que el 19% de todo lo
facturado del año no era suyo y ya se lo gastó en inventario. Es la causa más común de que un
vendedor con ventas crecientes se quede sin caja.

**El IVA que cobras no es ingreso: es plata que estás guardando para la DIAN.**

## Qué NO desarrollamos aquí

| Pregunta | Va a |
|---|---|
| ¿Cómo declaro renta / IVA / ICA? | `contador_lushows` |
| ¿Me conviene el Simple? | `contador_lushows` |
| ¿Cómo llevo los libros? | `contador_lushows` |
| ¿Cómo emito la factura electrónica? | `14` y luego `contador_lushows` |
| ¿Qué me retiene Mercado Pago? | `13` (y es un dato no verificado) |
| ¿Cuánto me queda de cada venta? | `82`, con la calculadora |

## Relacionados

`11` persona natural vs empresa · `13` lo que ML retiene y reporta · `14` facturación
electrónica · `15` liberación del dinero · `24` importar · `81` precio con IVA ·
`82` margen real · `84` competir contra precios imposibles
