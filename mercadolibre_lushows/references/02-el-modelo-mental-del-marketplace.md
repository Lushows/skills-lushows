# El modelo mental del marketplace

Mercado Libre tiene cuatro motores y nada más: conversión, reputación, logística y precio. Si una
acción no mueve uno de esos cuatro, sobra. La segunda mitad de este módulo es la lección más cara de
toda la skill: cómo la web te miente con cifras de Argentina, y el caso real donde tres fuentes
secundarias coincidían y **las tres estaban mal**.

## Los cuatro motores

```
CONVERSIÓN  ·  REPUTACIÓN  ·  LOGÍSTICA  ·  PRECIO
```

| Motor | Qué mide ML | Palanca concreta | Módulos |
|---|---|---|---|
| **Conversión** | De cada 100 que te ven, cuántos compran | Ficha, fotos, título, descripción | `25`-`54`, `58` |
| **Reputación** | Reclamos, cancelaciones, envíos incorrectos | Posventa y cumplimiento | `125`-`144` |
| **Logística** | Tiempo de entrega y quién despacha | Full, Flex, tiempo de despacho | `100`-`124` |
| **Precio** | Competitividad contra los demás vendedores | Margen que aguante bajar | `75`-`99` |

De los cuatro, el que más pesa es la **conversión** (fuente especializada, sep-2026; ML no publica
pesos). Es contraintuitivo: la gente pide "más visitas" cuando el problema es que las visitas que ya
tiene no compran. Conseguir más visitas con mala conversión **acelera la caída**, porque le confirma
al algoritmo que no vales la posición.

**No pidas más tráfico mientras tu ficha no convierta: en Mercado Libre el tráfico extra con mala
conversión es una condena, no un premio.**

## El orden en que se tocan

```
1. ¿SOBREVIVE?   margen tras comisión + envío + IVA                  → 75-99
2. ¿SE ENTIENDE? categoría, título, ficha técnica, fotos             → 25-54
3. ¿LLEGA?       logística y promesa de entrega                      → 100-124
4. ¿SE VE?       algoritmo, catálogo y, solo al final, Mercado Ads   → 55-74, 145-164
```

Pautar un producto que no sobrevive al paso 1 es la forma más rápida de perder plata aquí (`154`).

## Los motores se retroalimentan (y ahora se puede poner en pesos)

No son cuatro cajas separadas. El ejemplo más brutal es que **la reputación es un costo logístico**:

| Reputación | Envío de 1 kg, producto de más de $60.000 |
|---|---|
| Verde, MercadoLíder, o **sin reputación aún** | **$8.200** |
| Amarilla | ~$10.200 |
| Naranja o roja | **$16.400** |

Oficial ML Colombia, verificado sep-2026. Perder el verde **duplica** tu costo de envío: son $8.200
por cada venta. La reputación no es orgullo ni una medallita, es una línea del P&G. Y hay un detalle
que cambia la estrategia del que arranca: **un vendedor sin reputación paga lo mismo que un verde**.
El castigo no es no tenerla — es perderla (`125`, `128`).

Y al revés: la reputación naranja o roja **puede participar en el catálogo pero no puede ganar** la
oferta principal (fuente especializada, sep-2026), y activa penalizaciones de posicionamiento que
ningún gasto en publicidad compensa. Por eso `04` empieza por el color del termómetro.

---

## 🔴 LA TRAMPA DE LOS DATOS

### El caso resuelto (léelo completo, es la lección)

En septiembre de 2026 se investigaron los costos de vender en Mercado Libre Colombia. Esto fue lo
que devolvió cada capa de fuentes:

| Capa | Qué decía | Veredicto |
|---|---|---|
| **Resúmenes de buscador** | "Desde el 1-sep-2026 los ítems bajo $33.000 pagan un cargo fijo de $1.330 / $2.740 / $3.320" | ❌ Es **Argentina**, en pesos argentinos. Fuentes: Página/12, iProfesional, iProUp |
| **Blogs colombianos de agencia** | "La comisión es 12%-16% en Clásica y 16%-21% en Premium" | ❌ Sin citar fuente. Ni el rango ni los nombres corresponden |
| **Página oficial de ML Colombia** | "Pagarás **entre 8% y 22%** según la categoría y la cantidad de cuotas" | ✅ Texto oficial, leído con navegador real |

Y al leer la página oficial aparecieron dos cosas que **ninguna** fuente secundaria mencionaba:

1. **En Colombia NO existe el "cargo fijo por venta de bajo valor".** Lo que existe es un **precio
   mínimo de publicación de $2.900**: *"El precio de tu producto debe ser igual o superior a $2.900.
   Esto te permitirá cubrir las tarifas de venta. Puedes vender productos de menor valor ofreciendo
   packs o combos"* (oficial ML Colombia, verificado sep-2026).
2. **Los nombres "Clásica" y "Premium" ya no se usan en Colombia.** El sitio habla hoy de
   **Gratuita**, publicaciones **con cuotas con 0% interés**, y **cuotas extra** — y ofrecer cuotas
   extra cuesta exactamente **3 puntos porcentuales** más, no los "~4 puntos" que repiten los blogs.

**Tres fuentes secundarias coincidiendo no valen una fuente oficial.** Coincidían porque se copian
entre sí, no porque fueran verdad.

### Por qué pasa esto

1. ML **bloquea el acceso automatizado**: `mercadolibre.com.co/ayuda/*` y
   `vendedores.mercadolibre.com.co` devuelven **403** a `curl` y a cualquier fetch de máquina. Con
   navegador real sí se leen.
2. Como nadie puede leer la fuente oficial a escala, los blogs se copian entre sí.
3. Argentina y México generan mucho más contenido en español sobre ML que Colombia.
4. Los modelos de lenguaje heredamos esa mezcla si no verificamos.

### Las dos trampas nuevas del método (sep-2026)

**Trampa 1: las URLs viejas de la ayuda no dan 404, redirigen en silencio a otra cosa.** Los slugs
muertos (`costos-de-vender_1265`, `reputacion-vendedor_1622`, `mercadolider_1302`,
`calidad-publicaciones_4132`, `tipos-de-publicacion_1285`, `mercado-envios-full_13790`) llevan a
`/ayuda/1064`, que trata de **hackeo de dispositivos**. Si no te fijas, crees que leíste la página
de costos y leíste otra. Nunca uses una URL guardada: busca el artículo con el buscador interno,
`mercadolibre.com.co/ayuda/search?q=`

**Trampa 2: la API pública de precios ya no es pública.**
`GET /sites/MCO/listing_prices` hoy responde `403 PA_UNAUTHORIZED_RESULT_FROM_POLICIES` y exige
token. Cualquier guía que la presente como consulta abierta está desactualizada.

### El método de 5 pasos para verificar una cifra

```
1. SIMULADOR OFICIAL logueado — la fuente más confiable
   mercadolibre.com.co/landing/costos-de-venta  ·  /simulador-de-costos
2. Navegador real (Playwright / Chrome DevTools MCP). NUNCA fetch HTTP: da 403
3. Encuentra el artículo por el buscador interno mercadolibre.com.co/ayuda/search?q=
   NUNCA por una URL vieja: redirige en silencio a /ayuda/1064
4. Proxy de lectura sobre la página oficial (r.jina.ai) — funcionó en sep-2026.
   La API listing_prices ya NO sirve sin token
5. Si nada funciona, DILO y trabaja el número como VARIABLE, no como hecho
```

El paso 5 no es rendirse: es la forma correcta de trabajar. Por eso `scripts/margen_ml.py` recibe la
comisión **como parámetro**. El modelo de costos es estable; el porcentaje es del usuario, de su
categoría y de su país.

### Lo que hoy SÍ está verificado y lo que sigue abierto

| Dato | Estado (sep-2026) |
|---|---|
| Rango de comisión en Colombia | ✅ **8% a 22%** oficial, según categoría y cuotas |
| Sobrecosto de ofrecer cuotas extra | ✅ **+3 puntos porcentuales** oficial |
| Precio mínimo de publicación | ✅ **$2.900** oficial |
| Cargo fijo por venta de bajo valor | ✅ **No existe en Colombia.** Lo argentino era argentino |
| Tablas de costo de envío por peso y reputación | ✅ Oficiales, completas (`78`, `79`) |
| Umbral de envío gratis | ✅ **$60.000** oficial |
| Descuento de envío por reputación | ✅ 50% verde/MercadoLíder/sin reputación · 40% amarilla · 0% naranja o roja |
| Umbrales del termómetro **para ser verde** | ✅ Publicados (`125`) |
| **Comisión exacta de tu categoría** | ❌ Solo tras login. La calculadora la recibe como parámetro (`76`) |
| Cortes de amarillo, naranja y rojo | ❌ Solo está publicado el corte a verde |
| Cortes numéricos de calidad profesional/estándar/básica | ❌ No publicados |
| Tarifa de comprar espacio en Full | ❌ "Varía según la demanda", sin cifra |

### Cómo se escribe una cifra en esta skill

| Situación | Forma correcta |
|---|---|
| Dato oficial | "Pagarás entre 8% y 22% (oficial ML Colombia, verificado sep-2026)" |
| Dato no verificado | Bloque ⚠️ con la vía para leerlo (simulador logueado, buscador interno de la ayuda) |
| Dato de otro país como comparación | "en México son 150-300 MXN — no aplica a Colombia" |

**Un módulo que admite lo que no sabe vale más que uno completo e inventado.** Si das una comisión
inventada, el usuario fija un precio real con ella y pierde plata real.

## El error clásico

Buscar en Google "comisión de Mercado Libre Colombia", tomar el primer número y publicar. En el
mejor caso el número es viejo; en el peor es argentino. El costo no es teórico: es vender tres meses
por debajo del costo mientras el dinero **sí** entra a Mercado Pago y todo parece funcionar, hasta
que cuentas el inventario.

## Relacionados

`01` qué es ML · `03` glosario · `04` diagnóstico inicial · `09` cuánto se gana de verdad ·
`58` la conversión manda · `66` la reputación como filtro de entrada · `75` estructura de costos ·
`76` las comisiones y cómo verificarlas · `77` el precio mínimo de $2.900 · `78` el envío que pagas
tú · `79` el umbral de los $60.000 · `82` la calculadora de margen · `108` inventario viejo ·
`125` el termómetro · `150` el ACOS sano según tu margen · `154` el error de pautar sin margen
