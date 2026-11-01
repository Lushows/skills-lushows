# Usuarios de prueba

Mercado Libre **no tiene sandbox**. No existe un entorno separado donde equivocarse gratis: lo que
hay son usuarios de test que viven en la plataforma real, aislados entre sí. Entender esa
diferencia evita el accidente de probar sobre tu cuenta de verdad.

## No hay sandbox

| Lo que la gente espera | Lo que hay |
|---|---|
| Un servidor de pruebas aparte | **No existe** |
| Datos falsos que no afectan nada | Usuarios reales, marcados como de test |
| Poder resetear todo | No |
| Probar reputación y posicionamiento | **No se puede** |

(oficial ML, verificado sep-2026)

Los usuarios de test **solo transaccionan entre sí**, nunca con cuentas reales. Esa es la única
frontera. Todo lo demás corre sobre la infraestructura de producción.

## Crear uno

```
POST https://api.mercadolibre.com/users/test_user
Authorization: Bearer APP_USR-...
Content-Type: application/json
```

```json
{ "site_id": "MCO" }
```

Respuesta, en forma típica:

```json
{
  "id": 987654321,
  "nickname": "TETE1234567",
  "password": "qatest8888",
  "site_status": "active"
}
```

## 🔴 GUARDA LA CONTRASEÑA EN ESE MOMENTO

> **No hay endpoint para recuperarla.** (oficial ML, verificado sep-2026)

Si cierras la terminal sin copiarla, ese usuario queda inservible para entrar por el navegador. No
hay "olvidé mi contraseña", no hay soporte que te la devuelva: gastaste uno de tus diez cupos.

**La contraseña de un usuario de test se copia antes de hacer cualquier otra cosa. No después de
leer el JSON: antes.**

Lo mínimo que hay que guardar de cada uno:

```
□ id
□ nickname
□ password
□ site_id
□ Para que lo creaste: vendedor de prueba o comprador de prueba
□ Fecha de creacion (cuentan los 60 dias)
```

## Los límites

| Límite | Valor |
|---|---|
| Máximo por cuenta de desarrollador | **10 usuarios de test** |
| Se eliminan tras | **60 días sin actividad** |

Diez no es mucho si los quemas de a uno por olvidar la contraseña. Y los 60 días importan: si
armas un entorno de pruebas y lo dejas quieto dos meses, al volver no está.

Con 10 cupos, el reparto que funciona:

| Rol | Cuántos | Para qué |
|---|---|---|
| Vendedor de pruebas | 1-2 | Publicar, responder, despachar |
| Comprador de pruebas | 2-3 | Comprar, preguntar, reclamar |
| Reserva | El resto | Para cuando necesites un escenario limpio |

## Qué SÍ puedes probar

| Prueba | Detalle |
|---|---|
| Publicar | Con título `Item de Prueba - Por favor, NO OFERTAR` |
| Comprar y vender | Entre usuarios de test |
| Preguntas y respuestas | Todo el flujo de `187` |
| Pagos | Con tarjetas de prueba; el titular **"APRO APRO"** fuerza la aprobación |
| Webhooks | Los eventos reales llegan a tu `callback_url` (`189`) |
| OAuth completo | El flujo de `177` de punta a punta |

## Qué NO puedes probar

| No se puede | Por qué |
|---|---|
| Transaccionar con cuentas reales | Los test users están aislados |
| Publicar en `gold` / `gold_premium` | **Prohibido** para usuarios de test |
| Reputación real | No se construye termómetro de verdad |
| Posicionamiento y búsqueda | No compites en resultados reales |
| Comisiones y costos reales | Los números no representan tu caso |

Ese primer "no" de la segunda tabla limita algo importante: como no puedes publicar en Premium, no
puedes probar el comportamiento de cuotas sin interés ni el flujo de catálogo tal como te va a
tocar en producción. Cuéntalo en tu plan.

## El plan de pruebas mínimo antes de producción

```
□ OAuth completo: autorizar, canjear, refrescar y volver a refrescar (`177`, `178`)
□ Forzar un invalid_grant a proposito y ver que mi alarma suena (`179`)
□ Publicar un item con todos los atributos requeridos (`181`, `182`)
□ Cambiar stock y precio, y LEER de vuelta para confirmar (`183`)
□ Comprar con el usuario comprador y ver llegar el webhook orders_v2 (`190`)
□ Medir el tiempo de respuesta de mi receptor: debe estar bajo 500 ms (`191`)
□ Reenviar el mismo aviso a mano y confirmar que NO se procesa dos veces (`192`)
□ Hacer una pregunta con el comprador y que el bot la responda (`195`)
□ Apagar mi servidor 10 minutos y ver que el barrido de respaldo recupera (`185`)
```

Ese es el plan. Si los nueve pasan, tu integración está lista; si te saltas el séptimo y el
noveno, no lo está aunque lo parezca.

## Higiene

```
□ Usa una app aparte para pruebas, con su propia callback_url (`176`, `189`)
□ Nunca pruebes escrituras contra tu cuenta real de vendedor
□ Pon los datos de los test users en un archivo privado, no en el repo
□ Toca los test users cada mes o los pierdes a los 60 dias
□ Si ya no usas uno, no lo borres: dejalo para el proximo escenario
```

## El error clásico

Probar "rapidito" con la cuenta real porque crear usuarios de test da pereza. Publicas un ítem de
prueba, recibes visitas reales en las primeras horas —que es justo la ventana en que el algoritmo
etiqueta la conversión (`56`)— y dejas un ítem basura con historial malo colgado de tu cuenta. O
peor: tu script con un bug cambia precios en publicaciones que sí están vendiendo.

**La cuenta real no es un entorno de pruebas, y borrar el ítem no borra el historial.**

## Relacionados

`56` la ventana de 48-72 horas · `176` crear tu aplicación · `177` el flujo OAuth ·
`179` invalid_grant · `181` publicar por API · `183` precio y stock · `189` webhooks ·
`191` responder en 500 ms · `192` duplicados · `195` el bot de preguntas con IA
