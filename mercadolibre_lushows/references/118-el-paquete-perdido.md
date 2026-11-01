# El paquete perdido

El paquete que no llega es, contra la intuición, el problema más manejable de la posventa: Compra
Protegida cubre al comprador **hasta 21 días desde la compra** (oficial ML Colombia, verificado
sep-2026), y si tú despachaste a tiempo, el reclamo por demora es **excluible** de tu reputación.

## Lo que cubre Compra Protegida

| Caso | Cobertura | Fuente |
|---|---|---|
| **No llegó** | Hasta **21 días** desde la compra (o desde que se fabrica) | Oficial |
| Arrepentimiento o problema con el producto | Hasta **30 días** desde que lo recibió | Oficial |
| Qué reembolsa | Valor del producto **+ envío** si fue con Mercado Envíos | Oficial |
| Qué NO reembolsa | Garantías o seguros adicionales | Oficial |

Los 21 días son el reloj que importa aquí. Pasados, el caso deja de estar dentro de esa cobertura
y la conversación cambia. Por eso la respuesta rápida no es cortesía: es plazo.

## Quién responde, según la modalidad

| Modalidad | Quién responde ante el comprador | Quién absorbe la pérdida |
|---|---|---|
| **Full** | ML: el paquete salió de su bodega | ML, salvo faltante del ingreso |
| **Colecta / agencias / correo** | ML, vía Compra Protegida | Se resuelve con la transportadora |
| **Flex** | **Tú**: entregaste tú | **Tú** |
| **Logística propia** | **Tú, todo** | **Tú, todo** (`122`) |

Las dos últimas filas son la razón económica de estar dentro de Mercado Envíos. En Flex y en
logística propia **el paquete perdido es tuyo, completo**.

## Qué haces tú, en orden

```
□ 1. Confirma el estado real: GET /shipments/$SHIPMENT_ID, no la memoria del comprador
□ 2. Verifica que TÚ despachaste a tiempo y guarda la evidencia
□ 3. Responde al comprador en menos de 24 HORAS HÁBILES (oficial: si no, pierdes la exclusión)
□ 4. Dale el número de rastreo y una fecha concreta de siguiente paso
□ 5. Si el rastreo está detenido, escala por el canal de ML, no por fuera
□ 6. Cuando se abra el reclamo, pide la exclusión citando el despacho en fecha
□ 7. Verifica después que la exclusión se haya aplicado (`124`)
```

El paso 3 es el corte duro: **si no respondes mensajes en 24 horas hábiles, pierdes el derecho a
pedir la exclusión del reclamo de tu reputación** (oficial ML Colombia, verificado sep-2026). Un
paquete perdido que te tumba el termómetro casi siempre es un paquete perdido que no respondiste.

## La tabla de exclusión

| Situación | ¿Cuenta contra tu reputación? |
|---|---|
| Despachaste a tiempo y se perdió en tránsito | **No**: es excluible |
| Despachaste a tiempo pero no respondiste en 24 h hábiles | **Sí**: perdiste la exclusión |
| No despachaste a tiempo | **Sí**: no es excluible |
| El comprador dice "entregado" y no lo reconoce | **No**: es excluible |
| Faltaron unidades o partes dentro del paquete | **Sí**: no es excluible (`111`) |

(Todo oficial ML Colombia, verificado sep-2026.)

La cuarta fila salva muchos casos: el "figura entregado pero no me llegó" está en la lista oficial
de reclamos excluibles. Pídela.

## La trampa de cancelar

Cuando el paquete se pierde, la tentación es cancelar para cerrar rápido. Ojo con el techo:
"canceladas por ti" no puede pasar de **2,5% a 60 días** ni de **4% a 365 días** para seguir
verde, y **1,5%** si eres MercadoLíder (oficial).

Dos matices oficiales que juegan a tu favor:

- Las ventas canceladas **por la persona que te compró** no cuentan contra ti.
- Los reclamos **con solicitud de cancelación no afectan la reputación desde el inicio**: tienes
**2 días hábiles** para reembolsar sin haber entregado y la reputación queda intacta. Si no
cumples, el reembolso es automático y **sí** te afecta.

**Si el comprador quiere cancelar, deja que lo pida él y reembolsa dentro de los 2 días hábiles.
No canceles tú.**

## El caso Flex

En Flex entregaste tú, así que no hay transportadora a quién reclamar. Tu única defensa es la
evidencia:

```
□ Confirma la entrega en la app en el momento exacto, no después
□ Foto del paquete entregado si tu operación lo permite
□ Nombre de quien recibió, cuando aplique
□ Nunca marques "entregado" antes de entregar: es la falta más grave del módulo
```

La última línea no es un consejo de eficiencia: marcar entregas falsas es riesgo de sanción de
cuenta, no solo de reputación. Ver `143`.

## Prevención

| Medida | Efecto |
|---|---|
| Etiqueta legible y bien pegada (`114`) | Menos paquetes extraviados por escaneo fallido |
| Quitar etiquetas viejas de cajas reutilizadas | Evita el destino equivocado |
| Confirmar el despacho el mismo día | Detectas el paquete que nunca salió |
| Revisar diariamente los que siguen "listo para despachar" | Atrapa el error antes del reclamo |
| Mapa propio de destinos problemáticos (`115`) | Refuerzas donde se pierde más |

## El error clásico

Discutir con el comprador sobre si el paquete llegó o no, en vez de mirar el rastreo y responder
rápido. Cada hora que pasa te acerca al vencimiento de las 24 horas hábiles y al día 21 de Compra
Protegida. El caso se gana con velocidad y evidencia, nunca con argumentos.

**El paquete perdido no se pierde en el camión: se pierde en tu bandeja de mensajes sin
responder.**

## Relacionados

`113` la demora y su costo · `114` el flujo diario · `115` zonas difíciles · `119` entrega fallida
· `102` Flex · `122` logística propia · `124` auditoría mensual · `126` las tres métricas · `136`
reclamos excluibles · `138` devoluciones · `143` suspensión de cuenta · `111` embalaje
