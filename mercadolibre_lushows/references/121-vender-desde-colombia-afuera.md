# Vender desde Colombia hacia afuera: la operación real

Si después de leer `120` sigues queriendo exportar por Mercado Libre, este módulo es el checklist
honesto de lo que la operación exige. Advertencia previa: la mitad de las casillas no las puede
responder esta skill, y decirlo es parte del trabajo.

## Lo que no puedo verificar

> ⚠️ **Sin verificar para Colombia (sep-2026).** No pude confirmar: qué programa de exportación de
> ML está abierto a cuentas colombianas, sus requisitos, sus costos, los países destino admitidos,
> si existe apoyo logístico de ML para el cross-border desde Colombia, ni cómo se liquidan los pagos
> internacionales en Mercado Pago Colombia.
>
> Tampoco están verificadas las **retenciones tributarias que Mercado Pago Colombia aplica** por
> normativa DIAN — eso hay que resolverlo con `contador_lushows`, no con esta skill.
>
> Verificación: tu propio panel, y `mercadolibre.com.co/ayuda/search?q=` (las URLs viejas del centro
> de ayuda **no dan 404: redirigen a una página equivocada**).

## Las cinco preguntas que deciden antes de empezar

```
□ 1. ¿Mi producto es competitivo en el país destino, o solo en Colombia?
□ 2. ¿Puedo poner producto físicamente en ese país, o voy a enviar desde acá cada unidad?
□ 3. ¿El flete internacional cabe dentro de mi margen?
□ 4. ¿Tengo la estructura legal y tributaria para exportar?
□ 5. ¿Ya domino mi operación en Colombia?
```

Si la 5 es "no", detente ahí. Todo lo demás es prematuro.

La 2 es la bifurcación estructural:

| Modelo | Qué implica | Viabilidad típica |
|---|---|---|
| Stock local en el destino | Sociedad o socio allá, bodega, capital | Alta si el producto pide |
| Envío unitario desde Colombia | Flete internacional por venta | Baja salvo caro y liviano |

**El envío unitario internacional casi nunca sobrevive al flete.** La exportación por marketplace
que funciona es la que pone stock del otro lado.

## El cálculo que decide

```
PRECIO VIABLE EN DESTINO =
    costo del producto
  + exportación (documentos, agente, transporte internacional)
  + arancel e impuestos de importación del país destino
  + logística local en destino
  + comisión del marketplace de ese país
  + margen

Si ese número queda por encima de lo que ya cobra un vendedor local allá,
el producto no es viable. Punto.
```

La última línea es la prueba de realidad y se hace **antes** de cualquier trámite: abre el site
del país destino, busca tu producto, mira el precio de los tres primeros resultados. Si tu costo
landed supera ese precio, no hay estrategia que lo salve.

Para que estos números sean exactos, rutea a `Matematicas_lushows`. Para la estructura aduanera y
tributaria, `contador_lushows`. Para la viabilidad del negocio completo, `economist_lushows`.

## Lo que viaja contigo y lo que no

| Activo | ¿Viaja al otro site? |
|---|---|
| Tu reputación | **No.** Empiezas en gris, sin reputación |
| Tu historial de ventas | No |
| Tus opiniones | No |
| Tus fichas de catálogo | No: el catálogo es por país |
| Tu conocimiento operativo | **Sí**, y es lo único que viaja |
| Tus proveedores y tu producto | Sí |

Ojo con el primero: empezar sin reputación no es tan malo como suena. En Colombia, **un vendedor
sin reputación tiene el mismo 50% de descuento en envíos que un verde** (oficial ML Colombia,
verificado sep-2026); el castigo es perder el color, no no tenerlo. Si el país destino usa una
lógica parecida, el arranque no te penaliza en costo — pero sí en posición y en desempate de
catálogo.

## Qué producto aguanta la exportación

| Característica | Por qué |
|---|---|
| Alto valor por kilo | El flete internacional pesa poco en porcentaje |
| Pequeño y liviano | Ver `109` y `116` |
| Diferenciado o de marca propia | No compites contra el mismo producto genérico |
| Sin restricciones sanitarias o de registro | Menos trámite, menos riesgo |
| Rotación predecible | Reponer desde otro país tarda semanas |
| Margen bruto amplio | Hay muchas capas de costo entre tú y el comprador |

Si tu producto no marca al menos cuatro de las seis, la exportación es una distracción cara.

## La alternativa que casi nadie considera

Antes de exportar, mira si el mismo esfuerzo rinde más en Colombia:

| Palanca local | Costo de intentarlo |
|---|---|
| Subir de amarillo a verde | Gratis, y te ahorra hasta el 50% del flete (`126`) |
| Ganar el catálogo en tus SKUs principales | Gratis, es trabajo de ficha y precio (`63`) |
| Pautar con ACOS sano | Controlado, y medible en semanas (`150`) |
| Full en los SKUs de alta rotación | Medible, reversible (`105`) |
| Aprovechar Hot Sale (19-23 oct 2026) | Calendario, no capital |

Todas se pagan solas en semanas. La exportación se paga en trimestres, en el mejor caso.

## El error clásico

Confundir "quiero crecer" con "quiero exportar". La exportación es una estrategia de escala para
quien ya saturó su mercado, no una salida para quien no encuentra tracción. Colombia tiene ~8
millones de usuarios de ML y +80 millones de visitas mensuales (verificado): ese mercado no se
agota con 200 ventas al mes.

**Exportar no es el siguiente nivel: es otro negocio. Empiézalo cuando el primero ya funcione
solo.**

## Relacionados

`120` Global Selling · `116` productos grandes · `109` peso volumétrico · `122` logística propia ·
`105` cuándo conviene Full · `124` auditoría mensual · `126` las tres métricas · `63` ganar el
catálogo · `150` ACOS sano · `75` el cálculo del margen · `05` los sitios de LatAm
