# Importar para vender en ML

Traer producto de afuera cambia tu costo de una forma que el precio FOB no muestra. Entre lo
que pagas en China y lo que te queda en bodega en Bogotá hay una cadena de cargos donde **el
arancel decide si tu margen existe**. Este módulo es sobre cómo eso aterriza en una publicación
de Mercado Libre. El sourcing y los regímenes aduaneros son de `dropshipping_lushows`.

## La frontera entre skills, primero

| Tema | Dueño |
|---|---|
| Qué producto traer, validar demanda, espiar anuncios | `dropshipping_lushows` |
| Proveedores en China, 1688, Alibaba, agentes de sourcing | `dropshipping_lushows` |
| Regímenes aduaneros, de minimis, tráfico postal vs carga | `dropshipping_lushows` |
| Cómo se contabiliza y declara la importación | `contador_lushows` |
| Cuánto puedo cobrar en ML con ese costo | **Esta skill**, módulos `76`-`99` |
| Qué me exige ML por vender importado | **Esta skill**, este módulo |

No desarrolles aquí lo de la izquierda. Nombra y rutea.

## Por qué el arancel decide el margen

En Mercado Libre el precio publicado incluye IVA y sobre él se cobra la comisión. Eso significa
que un punto de arancel no se traduce en un punto de precio: se amplifica.

La cadena completa hasta tu bodega:

```
Precio FOB del producto
  + flete internacional
  + seguro
  = valor en aduana (base gravable)
      + ARANCEL (% sobre el valor en aduana)
      = base para IVA
          + IVA de importación (19%)
      + agenciamiento aduanero
      + almacenaje y manejo en puerto
      + transporte interno hasta tu bodega
  = COSTO REAL EN BODEGA
```

Y recién ahí empieza la aritmética de Mercado Libre: comisión sobre el precio con IVA, cargo
fijo si aplica, envío que asumes, empaque. Ver `12` y `82`.

**El error es cotizar contra el precio FOB. El número que va en la calculadora de margen es el
costo en bodega, no lo que le pagaste al chino.**

Si necesitas el cálculo exacto, ejecútalo — no lo estimes:
`python scripts/margen_ml.py margen --precio X --costo Y --comision Z --iva 19`
y para la cadena de importación, `Matematicas_lushows`.

## Los tres números que tienes que conocer antes de comprar

```
□ 1. La partida arancelaria de tu producto (y su % de arancel)
     Dos productos parecidos pueden tener aranceles muy distintos.
□ 2. Si tu producto tiene arancel preferencial por acuerdo comercial
     Cambia todo. Depende del país de origen y del certificado.
□ 3. Si necesita registro o permiso para importar
     INVIMA para alimentos/cosméticos/suplementos → `20`. Otros productos tienen
     vistos buenos de otras entidades.
```

El punto 3 mata contenedores enteros: producto que llega y se queda en puerto porque no tenía
el permiso. Y en Mercado Libre, mientras eso pasa, tu publicación está sin stock — lo que saca
la publicación de la competencia y de la puja de catálogo, y al reponer "revive como más nueva
o menos confiable" (`61`).

## La presión sobre Shein y Temu: por qué te afecta

Datos verificados (MEDIA-ALTA):

| Dato | Valor |
|---|---|
| Pedidos de Shein + Temu en Colombia | **+700.000 al mes** (ago-2026) |
| Paquetes que entraron en 2025 | **77 millones** |
| Estado | Presión gremial para que la DIAN actúe |

Eso significa dos cosas para ti, y van en direcciones opuestas:

1. **Competencia directa**: tu comprador puede pedir lo mismo directo de China más barato,
   aceptando esperar semanas. Tu ventaja es la entrega en días y la Compra Protegida.
2. **Riesgo regulatorio a tu favor**: si la DIAN endurece el tratamiento de esos envíos, el
   diferencial de precio se cierra y el importador formal gana. Pero **no construyas el negocio
   apostando a que eso pase**.

El movimiento correcto: **no compitas por precio contra Shein en producto genérico**. Compite
donde ellos no pueden — entrega rápida, garantía real (`23`), factura (`14`), producto que se
necesita ya.

## Qué te exige Mercado Libre por vender importado

| Exigencia | Módulo |
|---|---|
| Factura de importación que trace el origen de la marca | `21` |
| Registro sanitario si es alimento, cosmético o suplemento | `20` |
| Ficha honesta: origen, voltaje, certificaciones, compatibilidad | `33` |
| Garantía real, con quién responde en Colombia | `23` |
| No usar "tipo", "símil", "réplica" en el título | `21`, `28` |

La primera es la crítica. **Si importas producto de marca, la documentación de importación es
tu defensa ante una denuncia del titular.** Sin ella, una denuncia te tumba la publicación
aunque el producto sea auténtico. Ver `21`.

## El voltaje y los detalles que generan devoluciones

Los productos importados generan devoluciones por causas que los nacionales no tienen:

```
□ Voltaje 110V vs 220V → declararlo en la ficha y en un atributo
□ Enchufe de otro país → decir si incluye adaptador
□ Manual solo en inglés o chino → decirlo, o incluir uno en español
□ Tallas asiáticas → tabla de equivalencias en las fotos secundarias
□ Certificación eléctrica o de seguridad → si no la tiene, no la insinúes
□ Repuestos y servicio técnico → si no existen en Colombia, no prometas garantía
  del fabricante (`23`)
```

Cada punto omitido es una devolución. Y con plazos de **30 días corridos para productos
nuevos** (oficial, `138`), esa devolución llega bien después de que creíste que la venta estaba
cerrada.

**La ficha de un importado tiene que decir lo incómodo. Lo que no digas, lo devuelve el
comprador.**

## Costos que la gente olvida meter en el cálculo

| Costo olvidado | Efecto |
|---|---|
| Unidades defectuosas del lote | Sube el costo unitario real de las buenas |
| Producto que no se vende (sobrestock) | Capital muerto; y en Full, cargo por inventario viejo |
| Tiempo de reposición (45-90 días) | Necesitas más inventario flotante |
| Capital de trabajo inmovilizado | Se suma al ciclo de caja de `15` |
| Variación del dólar entre pedido y llegada | Puede borrar el margen entero |

El último es real: si compras a una TRM y vendes al precio que calculaste con esa TRM, una
devaluación entre el pedido y la venta te come el margen sin que hagas nada mal.

Sobre el cargo por inventario viejo en Full: el patrón regional es un cargo extra tras ~120 días
sin venderse, pero **no está verificado para Colombia** y las cifras que circulan sobre costos
de almacenamiento son **de México** (`107`). Ver `103`.

## El orden correcto de una primera importación

```
□ 1. Valida que el producto vende, comprando local o en volumen chico → `dropshipping_lushows`
□ 2. Averigua la partida arancelaria y el % real de arancel
□ 3. Averigua si necesita permiso o registro → `20`
□ 4. Calcula el costo en bodega COMPLETO, no el FOB
□ 5. Mete ese costo en la calculadora de margen contra el precio de mercado en ML
□ 6. Si el margen no aguanta la comisión + envío + devoluciones, NO importes
□ 7. Trae una muestra. Pruébala. Fotografíala tú → `35`
□ 8. Primera importación pequeña. Mide la tasa de falla real
□ 9. Solo entonces, volumen
```

El paso 6 es el que se salta el 80%. Importan primero y calculan después.

## El error clásico

Traer un contenedor de un producto genérico barato porque "el margen es del 300%" calculado
sobre el FOB, y descubrir en bodega que entre arancel, IVA, agenciamiento y flete interno el
costo real casi duplicó. Después la comisión de Mercado Libre, el envío asumido y un 8% de
devoluciones convierten ese 300% en algo cercano a cero — con el capital inmovilizado en 3.000
unidades que hay que vender a como sea.

**Ninguna promoción de Mercado Libre arregla un producto que se importó mal. El margen se gana
en la compra, no en la publicación.**

## Relacionados

`12` datos fiscales e IVA · `13` retenciones · `15` ciclo de caja · `20` registros sanitarios ·
`21` propiedad intelectual · `23` garantías · `28` el título · `35` fotos · `33` la ficha ·
`61` stock cero · `82` margen real · `103` Full · `138` devoluciones · `107` costos de Full ·
`dropshipping_lushows` para sourcing y aduana · `contador_lushows` para la contabilización ·
`Matematicas_lushows` para el cálculo exacto
