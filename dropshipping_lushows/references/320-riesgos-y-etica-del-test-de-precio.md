# Riesgos y ética del test de precio

## El hecho incómodo

Un A/B de precio es, por definición, **cobrarle distinto a personas distintas por lo mismo, al mismo
tiempo**. Eso es normal en ecommerce y lo hace todo el mundo. También es lo que más rápido te
incendia la reputación si lo haces mal.

Este módulo no es moralina: es gestión de riesgo. Un test que te ahorra 5% de margen y te cuesta una
captura viral en TikTok fue un mal negocio.

## La línea: qué es legítimo y qué no

| Práctica | Veredicto | Por qué |
|---|---|---|
| Probar dos precios en periodos distintos (secuencial) | **Legítimo** | es solo "cambiamos el precio" |
| Probar dos precios simultáneos por **asignación aleatoria** | **Legítimo, con cuidado** | es experimento estándar; el riesgo es de percepción |
| Precio distinto por **país o moneda** | **Legítimo** | costos, impuestos y flete distintos, y es visible |
| Precio distinto por **canal** (tienda vs marketplace) | **Legítimo** | comisiones distintas, y el cliente lo entiende |
| Cupón de bienvenida, precio de lanzamiento, oferta por tiempo | **Legítimo** | es un descuento declarado, con condición pública (`221`) |
| Precio distinto según **fuente del anuncio** | **Zona gris** | defendible, pero difícil de explicar en público |
| Precio más alto a quien vuelve o ya compró | **NO** | castigas la lealtad; es el caso que más indigna |
| Precio según dispositivo (iPhone paga más) | **NO** | es el ejemplo de manual de discriminación de precio; te destruye |
| Precio según datos personales inferidos (edad, código postal rico, género) | **NO** | además del daño reputacional, entra en terreno legal |
| Precio tachado que nunca existió | **NO** | publicidad engañosa. En México lo mira PROFECO. Ver `07` |
| Subir el precio y llamarlo "descuento Buen Fin" | **NO** | mismo caso anterior, con testigos |

Regla práctica que resuelve el 95% de los casos:

> **Si no puedes explicar el criterio en voz alta al cliente sin que suene a trampa, no lo uses.**
>
> "Estamos probando dos precios de lanzamiento" se puede decir.
> "Te cobramos más porque entraste desde un iPhone" no se puede decir.

Y la segunda regla: **el criterio debe ser algo que el cliente controla o que es neutral** (el
momento, el país, el canal, el azar), nunca algo que el cliente *es*.

## Riesgo de que un cliente lo descubra

Siempre lo descubren. Las vías, por frecuencia:

| Vía | Frecuencia | Gravedad |
|---|---|---|
| Dos personas comparan en un grupo de WhatsApp o Facebook | alta | media-alta |
| El mismo cliente vuelve con otro dispositivo o en incógnito | alta | media |
| Captura de pantalla circulando en comentarios del anuncio | alta | **alta** — es público y arrastra |
| Página en caché / Google mostrando otro precio | media | baja |
| Confirmación de pedido con precio distinto al del anuncio | media | **alta** — es reclamo directo |
| Comparadores y extensiones de historial de precios | baja en LatAm | baja |

El que mata no es el descubrimiento: es la **respuesta**. Un "es un error del sistema" mentiroso
convierte un incidente de 1 cliente en un hilo de 200 comentarios.

## Cómo protegerte — reglas duras

| Regla | Implementación |
|---|---|
| **Un cliente, un precio, para siempre** | asigna la variante por cookie/ID persistente, no por visita |
| **El precio del anuncio = el precio de la landing = el del checkout** | si no cuadran, no es un test, es un fraude percibido |
| **Ventana corta** | 7-14 días por bloque. Un test permanente es una política de precios oculta |
| **Un solo precio vivo por canal público** | jamás dos precios visibles simultáneos en la misma URL indexada |
| **Honra el precio más bajo si hay reclamo** | siempre. Cuesta menos que discutir |
| **Guarda evidencia** | fechas, precios, variantes, criterio de asignación. Si hay reclamo, tienes el registro |
| **Precio tachado solo si existió** | y guarda la prueba de que existió, con fechas |
| **Nada de precio por atributo personal** | ver la tabla de arriba |

## El guion cuando te reclaman

Corto, sin negar, sin regalar el negocio:

> "Tienes razón, esta semana tuvimos dos precios de lanzamiento distintos mientras definíamos el
> precio final. Te ajusto al más bajo ahora mismo y te confirmo por aquí."

Qué hace bien: reconoce, explica en una línea, resuelve, cierra. Qué NO hacer: culpar al "sistema",
decir que el otro precio "ya venció", pedirle que pruebe con captura, o ignorar.

Costo de honrar el precio bajo: unos pocos dólares por caso. Costo de discutirlo en público:
incalculable, y además baja la conversión de todo el que lee los comentarios.

## Lo que sí puedes hacer sin ningún riesgo

Alternativas que consiguen el mismo aprendizaje sin cobrar distinto a la vez:

| Táctica | Qué aprendes | Riesgo |
|---|---|---|
| Prueba secuencial por bloques (`318`) | efecto grande del precio | ninguno |
| Van Westendorp (`317`) | rango aceptable | ninguno |
| Probar **bundles** distintos al mismo precio unitario | qué oferta paga más | ninguno |
| Probar **order bump** y upsell (`220`) | ticket real, sin tocar el precio de entrada | ninguno |
| Probar el **precio tachado** (ancla) manteniendo el precio de venta | efecto del ancla | bajo, si el ancla es real |
| Descuento con condición pública (primera compra, código de creador) | sensibilidad al descuento | ninguno |

La tercera y la cuarta son las mejores del cuadro: **cambias el ticket sin cambiar el precio
anunciado**, así que ni siquiera hay dos precios que comparar. Ver `218`, `220`.

## Riesgo legal y de plataforma

No es asesoría legal — verificar con abogado local antes de cualquier práctica de precios agresiva.

| Riesgo | Dónde aparece |
|---|---|
| Publicidad engañosa por precio tachado falso | México: PROFECO. Precio anunciado debe respetarse |
| Precio anunciado ≠ precio cobrado | reclamo directo, y motivo de contracargo |
| Rechazo de anuncio en Meta | discrepancia anuncio-landing es causal conocida. Ver `facebook_ads_lushows` |
| Sanción de marketplace | precio inconsistente o precio de "gancho". Ver `mercadolibre_lushows` |
| IVA y precio con impuestos incluidos | el precio mostrado debe ser el final. `contador_lushows` |
| Contracargos | suben cuando el cliente siente que pagó de más |

Verificar la normativa vigente de precios y promociones en México antes del Buen Fin: hay reglas de
temporada específicas y cambian año a año.

## Riesgos operativos, no éticos

Estos no te hunden la marca, te hunden el dato:

| Riesgo | Efecto |
|---|---|
| Precio cambiado a media prueba | los datos antes y después no son el mismo experimento |
| Carritos abandonados con precio viejo | recuperas ventas al precio equivocado y ensucias la medición |
| Email o remarketing con el precio de la otra variante | el cliente ve dos precios de tu propia mano |
| Catálogo de Meta desactualizado | el anuncio dinámico muestra el precio anterior |
| Marketplace sincronizado con la tienda | el test te cambia el precio en ML sin que lo pidas |

El del catálogo es el más común y el más silencioso: haces el test en la tienda y Meta sigue
anunciando el precio viejo durante días. Revisa el feed **antes** de arrancar.

## Checklist antes de arrancar cualquier test de precio

```
[ ] El criterio de asignación es neutral (azar, tiempo, país, canal) — nunca un atributo personal
[ ] Un cliente ve UN precio, persistente
[ ] Anuncio, landing, catálogo y checkout dicen lo mismo
[ ] Fecha de inicio y fin escritas antes de empezar
[ ] Guion de reclamo listo y guardado
[ ] Política: honramos el precio más bajo, sin discutir
[ ] Precio tachado, si existe, es real y documentado
[ ] Registro del experimento guardado (fechas, variantes, criterio)
[ ] Feed de catálogo y marketplace revisados
```

## Frontera

| Necesitas | Skill |
|---|---|
| Ética y legalidad general del negocio | `07` |
| IVA, facturación, precio con impuestos | `contador_lushows` |
| Consistencia anuncio-landing y políticas de Meta | `facebook_ads_lushows` |
| Reglas de precio en marketplace | `mercadolibre_lushows` |

## Relacionados
`07` · `103` · `202` · `216` · `217` · `218` · `220` · `221` · `238` · `316` · `317` · `318` · `319` · `321`
