# Una sola cuenta

Una persona, una cuenta. Una empresa, una cuenta. La gente la rompe todo el tiempo con
justificaciones que suenan razonables, y la sanción cuando la detectan no es sobre la cuenta
nueva: es sobre **todas**.

## La regla y su consecuencia verificada

Mercado Libre vincula cuentas por documento, correo, celular, dirección, cuenta bancaria, medio
de pago, dispositivo e IP. Cuando detecta que dos cuentas son de la misma persona o empresa, las
trata como una sola historia.

Lo verificado, del Programa de Protección de Marcas: **con infracciones reiteradas se
deshabilita la cuenta y las cuentas asociadas de forma permanente** (confianza MEDIA-ALTA).

| Lo que crees que arriesgas | Lo que realmente arriesgas |
|---|---|
| La cuenta nueva | La cuenta nueva **y** la vieja |
| Unos días sin vender | Deshabilitación **permanente** |
| Tus publicaciones | Tu reputación construida en meses |
| Tu inventario en Full | Acceso a tu operación completa |

**Abrir la segunda cuenta no es apostar la cuenta nueva: es apostar la que ya funciona.**

## Por qué la gente la rompe

| Excusa | Por qué no vale |
|---|---|
| "Quiero probar otra categoría" | Publica en la misma cuenta. La categoría no ensucia nada |
| "Mi reputación está en naranja, abro otra limpia" | Es exactamente el fraude que la regla castiga |
| "Una para mayorista y otra para detal" | Se resuelve con variaciones y precio por cantidad (`40`) |
| "Una es mía y otra de mi esposa" | Si la operas tú, con tu dirección y tu banco, es tuya |
| "Quiero dos Tiendas Oficiales para dos marcas" | Una cuenta empresa puede tener varias marcas (`18`) |
| "Para hacer pruebas de la API" | Para eso existen los usuarios de test, ver abajo |
| "Para autocomprarme y subir ventas" | Fraude directo. Deshabilitación permanente |

La de la reputación es la más peligrosa porque parece la más lógica. Está en naranja, el
algoritmo la está castigando —la reputación naranja o roja activa penalizaciones de
posicionamiento que ningún gasto en publicidad puede compensar, y en catálogo **puede
participar pero no puede ganar** la oferta principal (`63`)—, así que el impulso es empezar de
cero. Es la vía más rápida a perder las dos.

## Lo que sí es legítimo

| Necesidad | Solución dentro de una sola cuenta |
|---|---|
| Vender varias marcas propias | Varias marcas registradas en una cuenta empresa (`18`) |
| Vender mayorista y detal | Variaciones, y precio por cantidad si califica (`40`) |
| Que un empleado gestione | Usuarios/operadores con permisos, no cuenta aparte |
| Probar la API sin ensuciar | **Usuarios de test**, ver abajo |
| Persona natural que formaliza a SAS | Migración de la cuenta, no cuenta nueva (`11`) |
| Separar dos negocios distintos | Dos personas jurídicas reales, cada una con cuenta, bodega y bancos |

La última tiene letra chica: si las dos "empresas" son tuyas, con la misma dirección, el mismo
inventario y el mismo computador, ML puede asociarlas igual. La separación tiene que ser real,
no de papel.

## Los usuarios de test: la única multi-cuenta bendecida

Para desarrollo hay un mecanismo oficial y no viola la regla:

```
POST https://api.mercadolibre.com/users/test_user
{ "site_id": "MCO" }
```

| Característica | Valor |
|---|---|
| Cuántos | Hasta **10 por cuenta de desarrollador** |
| Caducidad | Se eliminan tras **60 días sin actividad** |
| Con quién transaccionan | **Solo entre sí**, nunca con cuentas reales |
| Contraseña | La devuelve al crearlo. **Guárdala: no hay endpoint para recuperarla** |
| Restricción | Prohibido publicar en `gold` / `gold_premium` |
| Qué no prueban | Reputación real ni posicionamiento |

Todo lo anterior verificado (ALTA). Detalle en `176`.

## Cómo te detectan

No es magia ni es manual. Son señales cruzadas:

```
□ Mismo documento o NIT
□ Mismo correo o correo con patrón obvio (ventas1@, ventas2@)
□ Mismo celular
□ Misma dirección de despacho o de facturación
□ Misma cuenta bancaria de retiro
□ Misma tarjeta o medio de pago
□ Mismo dispositivo / navegador / IP
□ Mismas fotos de producto (se comparan las imágenes)
□ Mismo texto de descripción palabra por palabra
```

Las dos últimas sorprenden: puedes cambiar todo lo administrativo y delatarte porque subiste la
misma foto en las dos cuentas.

## Si ya tienes dos cuentas

No entres en pánico, pero tampoco lo dejes creciendo.

```
□ Decide cuál es LA cuenta: la de mayor reputación y antigüedad
□ Baja el stock de la otra a cero y pausa sus publicaciones
□ Termina las ventas en curso y la posventa pendiente — no dejes reclamos abiertos
□ NO la borres de golpe si tiene operaciones vivas: cancelar ventas te pega en reputación
  (más del 2,5% de canceladas puede suspender la cuenta — dato oficial, ver `125`)
□ Migra fotos y descripciones a la cuenta que se queda, y bórralas de la otra
□ Consolida todo en una sola cuenta y opera solo desde ahí
```

Si la cuenta que vas a cerrar tiene mejor reputación que la que te quedas, reconsidera cuál
sacrificas: la reputación es lo más caro de reconstruir.

## Qué hacer si te suspenden

Lo que se sabe con certeza es poco:

- La suspensión puede ser **temporal** (2 a 5 días sin vender) o **permanente** (infracciones
  graves o reincidentes) — confianza MEDIA.
- La recuperación **depende del motivo y no siempre es reversible** — confianza MEDIA.

⚠️ **Sin verificar para Colombia (sep-2026).** El proceso de apelación está descrito solo por
terceros, no por Mercado Libre: investigar la causa → enviar una carta con el análisis y un plan
de prevención → hacer seguimiento, con tiempos reportados de 3 a 15 días hábiles. **No lo trates
como procedimiento oficial.** Ver `74`.

## El error clásico

Abrir la segunda cuenta "solo por un mes, mientras arreglo la reputación de la primera" y
perder las dos en la semana tres, con inventario en Full que ya no puede despachar. El costo de
arreglar una reputación naranja es alto —requiere meses de desempeño limpio, y existe el
Beneficio de Reputación con depósito en garantía (`125`)— pero **existe**. El costo de perder
las dos cuentas de forma permanente no tiene arreglo.

## Relacionados

`10` crear la cuenta · `11` persona natural vs empresa · `16` verificación de identidad ·
`18` nombre y marca · `21` propiedad intelectual · `40` variaciones · `63` ganar el catálogo ·
`125` reputación · `73` riesgo de cuenta · `74` suspensiones y apelación ·
`176` usuarios de test
