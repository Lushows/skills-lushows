# Integradores y cuándo no programar

La pregunta correcta no es "¿puedo programarlo?" sino "¿alguien ya lo resolvió mejor de lo que lo
voy a resolver yo?". Para contabilidad e inventario la respuesta es sí, y programarlo tú es tirar
meses a la basura.

## La regla

**Si lo que necesitas es contabilidad o facturación, no programes. Programa solo cuando necesites
lógica que ningún integrador te da.**

| Necesidad | Integrador o código |
|---|---|
| Sincronizar ventas con tu contabilidad | Integrador |
| Emitir la factura electrónica DIAN | Integrador |
| Descontar inventario con la venta | Integrador |
| Crear el cliente en tu sistema contable | Integrador |
| Bot que responde preguntas con IA (`195`) | **Código** |
| Reglas de precio propias del negocio | **Código** |
| Sincronizar stock con tu tienda física o tu ERP raro | **Código** |
| Alarmas y tableros a tu medida | **Código** |

## Alegra

| Dato | Valor |
|---|---|
| Integración con Mercado Libre en Colombia | **Confirmada y documentada** |
| Qué hace | Sincroniza ventas, crea el cliente, descuenta inventario |
| Factura electrónica DIAN | **La emite automáticamente** |
| Requisito | **Numeración electrónica activa** ante la DIAN |

(confianza ALTA, verificado sep-2026)

El requisito de la numeración no es un detalle: sin resolución de numeración vigente, la
integración no puede emitir nada. Ese trámite y todo lo fiscal es de `contador_lushows`, y
conviene tenerlo listo **antes** de conectar.

Lo que esto te ahorra escribir: leer órdenes, mapear compradores a terceros, calcular impuestos,
armar el XML de la factura, firmarla, enviarla a la DIAN, manejar rechazos y guardar el acuse.
Eso son meses, y son meses de un problema donde equivocarse tiene consecuencias legales.

## Los otros dos

| Integrador | Estado |
|---|---|
| **Siigo** | API robusta, pero **sin confirmación** de integración nativa con ML |
| **Bsale** | Fuerte en Chile y LatAm, **cobertura en Colombia no verificada** |

> ⚠️ **Sin verificar para Colombia (sep-2026).** Ni la integración nativa de Siigo con Mercado
> Libre ni la cobertura de Bsale en Colombia se pudieron confirmar. Si ya usas alguno de los dos
> para tu contabilidad, **pregúntale directamente al proveedor** antes de asumir que conecta.
> No compres un plan por una promesa de página web.

Cómo preguntar bien:

```
□ Existe integracion nativa con Mercado Libre COLOMBIA, no con ML de otro pais?
□ Trae las ordenes automaticamente o hay que subir un archivo?
□ Emite la factura electronica DIAN desde la venta de ML?
□ Descuenta inventario?
□ Que pasa con las devoluciones y las notas credito?
□ Cuanto cuesta al mes con mi volumen de ventas?
```

## Cómo se decide

| Tu caso | Veredicto |
|---|---|
| Pocos SKUs, poco volumen, todo en ML | **Ni integrador ni código.** El panel te sirve (`175`) |
| Necesitas facturar y llevar contabilidad | **Integrador.** Alegra es el camino confirmado |
| Integrador + una necesidad puntual que no cubre | Integrador **y** un código pequeño al lado |
| Operación rara que ningún producto contempla | Código, con los ojos abiertos |
| Quieres el bot de IA | Código: eso no lo vende nadie hecho a tu medida |

Ese tercer caso es el más común y el que la gente no considera: **no es integrador o código, es
integrador para lo aburrido y código para lo tuyo.** El integrador factura y contabiliza; tu
código responde preguntas y vigila el stock. Cada uno en lo suyo.

## Lo que un integrador te quita de encima

| Problema | Quién lo sufre si programas tú |
|---|---|
| Renovar el token cada 6 horas (`178`) | Tú, y a las 3 a.m. |
| El `invalid_grant` (`179`) | Tú |
| Responder webhooks en 500 ms (`191`) | Tú |
| Deduplicar avisos (`192`) | Tú |
| Que ML cambie un endpoint | Tú |
| Que la DIAN cambie un formato | Tú, y con multa de por medio |

Esa última fila es la que cierra la discusión. **Equivocarte en el stock cuesta una venta;
equivocarte en la factura cuesta con la DIAN.**

## El costo real de programar tu propia integración contable

No es el mes que te toma hacerlo. Es:

```
□ Mantenerla cuando ML cambia algo
□ Mantenerla cuando la DIAN cambia algo
□ Arreglarla el dia que se rompe, que sera un dia de mucha venta
□ Ser la unica persona del mundo que entiende como funciona
□ No poder irte de vacaciones sin dejar el telefono prendido
```

Un integrador cuesta una mensualidad. Tu tiempo cuesta más, y tu tiempo vale más puesto en vender.

## El error clásico

Empezar a programar la integración contable "porque el plan del integrador parece caro", y a los
tres meses tener medio sistema que ni factura bien ni se puede abandonar. La comparación honesta
no es "mensualidad contra cero": es mensualidad contra **tu tiempo más el riesgo de facturar mal**.

El segundo error, al revés: contratar el integrador y esperar que también te traiga el bot de IA,
las alarmas y las reglas de precio. No lo hace. Para eso sí hay que escribir código, y ese código
es el que de verdad te diferencia.

## Relacionados

`175` cuándo automatizar y cuándo no · `178` tokens · `179` invalid_grant · `185` las órdenes ·
`191` responder en 500 ms · `192` duplicados · `195` el bot de preguntas con IA ·
`197` el servidor MCP oficial · `199` arquitectura de referencia
