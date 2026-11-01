# Pausas e infracciones

Una publicación puede desaparecer sin que hicieras nada malo a propósito: ficha incompleta, cambio
brusco de precio, o la denuncia de cualquier usuario desde un botón que está en tu propia ficha.
Este módulo separa lo temporal de lo grave, y te dice qué causa cada cosa.

## Los estados en que te puedes quedar

| Estado | Qué significa | Gravedad |
|---|---|---|
| **Inactiva para revisar** | Pausa temporal mientras ML verifica algo. Se reactiva al corregir | Baja |
| **Pausada por falta de stock** | `available_quantity: 0` → `paused` con sub-estado `out_of_stock` | Baja, pero cuesta posición (`61`) |
| **Pausada por ti** | La pausaste tú desde el panel | Ninguna |
| **Publicación eliminada** | ML la bajó por infracción | Alta |
| **Cuenta suspendida temporalmente** | 2 a 5 días sin poder vender | Alta |
| **Cuenta deshabilitada permanentemente** | Infracciones graves o reincidentes | Terminal |

**"Inactiva para revisar" no es un castigo: es una pregunta. Respóndela rápido y vuelve. Lo que te
mata es no enterarte.**

## Causas de "inactiva para revisar"

| Causa | Cómo evitarla |
|---|---|
| **Cambio brusco de precio** | Sube o baja en escalones, no de un salto (`68`) |
| Ficha incompleta | Atributos obligatorios llenos antes de publicar (`40`, `59`) |
| Sospecha sobre el producto o la categoría | Categoría confirmada con el predictor (`41`) |
| Datos de contacto en la ficha | Nunca teléfono, WhatsApp, redes o correo (`129`) |
| Denuncia de un usuario | Ver abajo |

El cambio brusco de precio es la causa citada por ML como ejemplo (confianza media, sep-2026), y
la que más sorprende al vendedor, porque él cree que solo estaba haciendo una promoción.

## El botón Denunciar

Cualquier usuario puede denunciar tu publicación desde el botón **"Denunciar"** en la **esquina
inferior derecha** de la ficha. No hace falta que sea un comprador, ni que tenga razón.

Esto tiene dos lecturas:

1. **Tu competencia puede denunciarte.** No es paranoia, es un canal abierto. Si tu ficha tiene
   algo objetable — una marca mal mencionada, una foto copiada, un dato de contacto — se lo estás
   sirviendo en bandeja.
2. **Tú también puedes denunciar.** Si alguien copió tus fotos o usa tu marca registrada, ese es
   el canal.

## La infracción número uno: falsificados

Los productos falsificados son la categoría con más publicaciones eliminadas (documentado en
México, Argentina, Brasil y Uruguay; confianza media, sep-2026). No es un tema menor ni una zona
gris: es la causa principal de cuentas cerradas.

Y "falsificado" incluye cosas que el vendedor no percibe como falsificación:

```
□ Réplica, "AAA", "calidad original"
□ Producto genérico con el logo de la marca puesto
□ Repuesto no oficial vendido como oficial
□ Usar "tipo Nike", "símil Adidas", "igual a Apple" en el título
□ Usar fotos oficiales de la marca sin autorización
□ Vender producto de marca sin poder acreditar la cadena de compra
```

La regla del lenguaje es dura y simple: con marcas ajenas solo puedes decir **"para"** o
**"compatible con"**. Nunca "tipo", "símil", "igual a", "idéntico a" (`31`).

## El Programa de Protección de Marcas

Cuando el titular de una marca denuncia, el proceso es:

```
1. El titular denuncia
2. La publicación SE PAUSA de inmediato
3. Tú puedes responder con evidencia (facturas, autorización, cadena de compra)
4. El titular evalúa tu respuesta
5. Si NO respondes → se elimina
6. Con infracciones reiteradas → se deshabilita tu cuenta Y LAS CUENTAS ASOCIADAS,
   de forma permanente
```

(Confianza media-alta, sep-2026.)

El punto 6 es el que hay que leer dos veces: **las cuentas asociadas también caen**. Abrir una
cuenta nueva "para empezar de cero" no funciona y empeora el caso.

## Otras prohibiciones que pausan

| Prohibición | Detalle |
|---|---|
| Datos de contacto | Teléfono, WhatsApp, redes, correo — en descripción, imágenes y en preguntas/respuestas. Excepciones: Autos/Motos, Inmuebles, Servicios y MercadoProveedores |
| Spam | En preguntas, respuestas y mensajes |
| Publicaciones duplicadas | El mismo producto publicado varias veces en vez de usar variaciones (`44`) |
| Texto y gráficos en la foto 1 | La principal va con el producto solo, sin superposiciones (`42`) |
| Frases promocionales en el título | "¡¡¡OFERTA!!!", emojis, signos, mayúsculas sostenidas (`31`) |

> ⚠️ **Sin verificar (sep-2026).** La **escala de sanciones** por poner datos de contacto no está
> verificada. Lo consistente en las fuentes es que se elimina la publicación o la pregunta y que
> hay riesgo de sanción si es reiterado. Nadie publica la tabla de "primera vez, segunda vez".

## Qué hacer cuando te pausan

```
INMEDIATO
□ Lee la notificación completa: ML dice qué infracción imputa
□ NO borres la publicación: si la borras pierdes el historial y no arreglas el caso
□ NO abras una cuenta nueva: las cuentas asociadas caen juntas
□ Identifica si es "revisar" (corriges y vuelve) o "infracción" (hay que apelar)

SI ES "INACTIVA PARA REVISAR"
□ Corrige lo que señala: completa atributos, quita el dato de contacto, ajusta el precio
□ Guarda captura del antes y el después
□ Reactiva y verifica que vuelva a aparecer en búsqueda (`69`)

SI ES INFRACCIÓN
□ Reúne evidencia: facturas de compra, autorización de la marca, fotos propias
□ Responde DENTRO del plazo: si no respondes, se elimina
□ Ve a `74` para armar la apelación

DESPUÉS
□ Audita el resto de tus publicaciones por la misma causa, antes de que caigan también
□ Si fue una denuncia de competencia, revisa qué le diste para denunciarte
```

## Auditoría preventiva

Haz esto una vez al trimestre sobre todo tu catálogo:

```
□ Ninguna publicación menciona una marca ajena sin "para" o "compatible con"
□ Ninguna foto es de otro vendedor ni del sitio oficial de la marca
□ Ninguna descripción, imagen o respuesta tiene teléfono, WhatsApp, correo o redes
□ Ningún producto duplicado: los mismos con variaciones (`44`)
□ Todos los atributos obligatorios llenos
□ Ninguna foto principal con texto, logos o gráficos superpuestos
□ Ningún título con signos, emojis, mayúsculas sostenidas o frases promocionales
□ Tengo factura de compra de todo lo que vendo de marca
```

La última línea es la que te salva en una denuncia de marca. Sin factura no tienes defensa.

## El error clásico

Reaccionar a la pausa borrando la publicación y republicando "limpia". Con eso pierdes el
historial, no resuelves la infracción imputada, y si el sistema detecta que republicaste lo mismo,
el caso escala de pausa a sanción. **Corrige y apela; no escondas.**

## Relacionados

`31` título · `40` atributos · `41` criterios de categoría · `42` fotos · `44` variaciones ·
`59` primeras 72 horas · `61` stock cero · `68` precio como factor ·
`69` medir tu posición real · `72` por qué cayó mi publicación · `74` cómo apelar ·
`129` datos de contacto prohibidos · `142` suspensión de cuenta · `143` protección de marcas
