# El plan de defensa de la cuenta

Módulo de cierre y de emergencia. Está escrito para funcionar solo: si algo ya pasó —el color cayó,
llegó una denuncia, te suspendieron— este es el primero que se carga. Todo lo demás del bloque
125-143 es el detalle de lo que aquí se resume.

## Por qué esto es un tema de plata, no de orgullo

El descuento en costos de envío depende de tu color (oficial ML Colombia, verificado sep-2026):

| Reputación | Descuento | Envío 0,5-1 kg, producto >$60.000 |
|---|---|---|
| Verde / MercadoLíder / sin reputación | 50% | **$8.200** |
| Amarilla | 40% | ~$10.200 |
| Naranja o roja | Ninguno | **$16.400** |

**Perder el verde cuesta $8.200 en cada venta.** Con 200 ventas al mes son $1.640.000 mensuales que
desaparecen sin que cambie una sola cosa en tu operación. Súmale la pérdida del catálogo (`63`) y la
caída de posición orgánica (`55`), y la reputación deja de ser una métrica blanda.

## Los límites que nunca se cruzan

### Para conservar el verde

Oficial ML Colombia, verificado sep-2026:

| Variable | A 60 días | A 365 días |
|---|---|---|
| Ventas con reclamos | ≤ **3,5%** | ≤ **3,5%** |
| Envíos incorrectos | ≤ **12%** | ≤ **15,5%** |
| Canceladas por ti | ≤ **2,5%** | ≤ **4%** |

La columna de 60 días aplica con 60 o más ventas concretadas; la de 365, con menos (`127`).

### Los cuatro límites de MercadoLíder

Oficial ML Colombia, verificado sep-2026:

| Métrica | Límite |
|---|---|
| Reclamos | menos del **2,5%** |
| Mediaciones | menos del **0,5%** |
| Ventas canceladas | menos del **1,5%** |
| Envíos incorrectos | menos del **10%** |

### El límite que cierra cuentas

**Superar el 2,5% de ventas canceladas por ti pone la cuenta en riesgo de suspensión para vender.**
Es el único umbral del bloque que no solo te baja de color (`139`, `143`).

### Lo que no está publicado

> ⚠️ **Sin verificar (sep-2026).** Solo está publicado el **corte a verde**. Los cortes exactos de
> **amarillo, naranja y rojo** no aparecen en ninguna página oficial de Mercado Libre, ni la escala
> exacta de sanciones por infracción. Los blogs que dan esas tablas se las inventan o las copian de
> otro país.

## Tus números de alarma

No pongas la alarma en el límite: ponla antes. Cuando tocas el límite ya es tarde, porque la ventana
tarda 60 o 365 días en limpiarse.

| Variable | Límite oficial (60 d) | **Tu alarma** | Acción al sonar |
|---|---|---|---|
| Reclamos | 3,5% | **2,0%** | Auditar SKU y empaque |
| Envíos incorrectos | 12% | **7%** | Revisar cortes de despacho |
| Canceladas | 2,5% | **1,2%** | **Parar de escalar.** Auditar stock hoy |
| Mediaciones (si MercadoLíder) | 0,5% | **0,3%** | Ceder más rápido en reclamos |

## Las señales tempranas

Antes de que se mueva un porcentaje, se mueven estas cosas. Si ves dos o más, ya vas en caída:

```
□ La bandeja de mensajes tiene casos de hace más de un día
□ Empezaste a despachar el pedido del viernes el lunes
□ Un SKU nuevo está vendiendo mucho y no sabes cuánto stock queda de verdad
□ Encendiste pauta sobre un producto con inventario justo
□ Llegaron dos reclamos con la misma frase
□ Estás cancelando "una que otra" por stock
□ Una publicación apareció pausada y no averiguaste por qué
□ Dejaste de mirar el panel de reputación hace más de dos semanas
```

**La última es la peor de todas**, porque desactiva la detección de las otras siete.

## La rutina semanal de chequeo

Veinte minutos cada lunes. No es negociable si vendes en serio.

```
□ 1. Mi cuenta → Reputación: anota los TRES porcentajes en tu hoja. No el color: los números
□ 2. Compáralos con la semana pasada. ¿Suben? ¿Cuál?
□ 3. Revisa reclamos abiertos: ¿alguno sin responder? (reloj de 24 h hábiles, `133`)
□ 4. Revisa reclamos cerrados de la semana: ¿alguno era excluible y no lo pediste? (`136`)
□ 5. Inventario: los 10 SKU de más rotación contra el físico. ¿Colchón aplicado? (`140`)
□ 6. Publicaciones pausadas: ¿hay alguna? ¿por qué?
□ 7. Opiniones nuevas: ¿alguna negativa sin responder? ¿patrón repetido? (`142`)
□ 8. Si eres MercadoLíder: ¿mediaciones en cero?
```

El paso 1 importa más de lo que parece. **ML te muestra la foto de hoy; la película la tienes que
llevar tú.** Una hoja con doce filas —una por semana— te dice si vas subiendo o bajando, que es la
información que el panel no te da.

## Lectura por API

Si quieres automatizar la rutina:

| Qué | Cómo |
|---|---|
| Reputación completa | `GET /users/$USER_ID` → `seller_reputation` |
| Los tres porcentajes | `seller_reputation.metrics.claims` / `delayed_handling_time` / `cancellations` |
| Nivel | `seller_reputation.power_seller_status` |
| Color | `seller_reputation.level_id` (`1_red` … `5_green`) |
| Alarma de reclamo nuevo | Webhook topic `claims` (`186`) |
| Alarma de cancelación | Webhook topic `orders_v2` |
| Alarma de mensaje entrante | Webhook topic `messages` |

Guarda la lectura diaria en una tabla y grafica la tendencia. Detalle en `195`, `186`.

## Modo emergencia: el color cayó

```
□ 1. Identifica CUÁL de las tres variables rompió el umbral. Solo una, casi siempre
□ 2. Encuentra la causa raíz de esa variable (tabla abajo)
□ 3. CORTA: pausa el SKU, el lote o el proveedor responsable. Hoy
□ 4. Revisa reclamos de los últimos 60 días y pide las exclusiones que falten (`136`)
□ 5. Sigue vendiendo solo lo que sale perfecto: necesitas denominador (`127`)
□ 6. Evalúa el Programa de Despegue solo DESPUÉS de cortar la causa (`128`)
□ 7. Mide semanalmente. No vuelvas a escalar hasta 3-4 semanas limpias
```

| Rompió | Causa raíz más probable | Módulo |
|---|---|---|
| Canceladas | Quiebre de stock | `140` |
| Reclamos | Ficha que promete de más, o empaque | `30`, `110` |
| Envíos incorrectos | Cortes de despacho irreales; Flex después de las 21:00 | `115` |
| Mediaciones | Respuesta lenta o tono defensivo | `133`, `135` |

## Modo emergencia: primeras 24 horas de una suspensión

```
□ 1. Lee el mensaje de ML completo y ubica la causal exacta. No adivines
□ 2. NO abras otra cuenta. Es lo único que hace el daño irreversible (`143`)
□ 3. Reúne evidencia: facturas de compra, guías con fecha, capturas, autorizaciones de marca
□ 4. Responde por el canal que ML indica, dentro del plazo que indique
□ 5. Cumple las ventas en curso. Cancelarlas ahora suma cancelaciones al expediente
□ 6. Avisa a los compradores activos por el canal de mensajes (`134`)
□ 7. Arregla la causa raíz ANTES de apelar: el plan concreto es lo que hace creíble la apelación
```

En la apelación, **plan concreto, no disculpas**. "Voy a tener más cuidado" no vale. "Implementé
colchón de 3 unidades y sincronización por webhook, adjunto capturas" sí.

## Las reglas que nunca se rompen

| Regla | Módulo |
|---|---|
| Una sola cuenta. Siempre | `143` |
| Cero datos de contacto en descripción, imágenes y preguntas | `132` |
| Responder todo mensaje el mismo día hábil | `133` |
| Nunca cancelar por error de precio: cumplir a pérdida | `139` |
| Publicar menos stock del que tienes | `140` |
| Nunca "tipo", "símil" ni "igual a" para marcas ajenas | `27` |
| Ceder antes que llegar a mediación, si el producto vale menos que el nivel | `135` |
| Guardar factura de compra de todo lo que vendes de marca | `143` |
| Foto del paquete en la báscula antes de despachar producto caro | `141` |

## Lo que juega a tu favor y casi nadie usa

Excepciones oficiales (oficial ML Colombia, verificado sep-2026):

```
□ Los reclamos por ARREPENTIMIENTO del comprador no cuentan
□ Las ventas canceladas POR EL COMPRADOR no cuentan como cancelación tuya
□ En la categoría INMUEBLES, las ventas no afectan la reputación
□ Un reclamo con solicitud de cancelación reembolsado en 2 DÍAS HÁBILES deja la reputación intacta
□ Hay siete causales de exclusión de reclamos, y se piden (`136`)
□ Un vendedor SIN reputación tiene el mismo 50% de descuento en envíos que un verde
```

Ese último dato encierra la tesis de todo el bloque: **el sistema no castiga no tener reputación,
castiga perderla.** Lo que estás defendiendo no es una medalla: es el precio de tus envíos, tu lugar
en el catálogo y la existencia misma de la cuenta.

## Relacionados

`125` el termómetro · `126` las tres métricas · `127` el periodo de evaluación ·
`128` cómo se recupera una caída · `129` MercadoLíder · `133` el tiempo de respuesta ·
`135` el reclamo y la mediación · `136` reglas de exclusión · `139` la cancelación ·
`140` el quiebre de stock · `143` suspensión de cuenta · `118` costos de envío · `186` webhooks
