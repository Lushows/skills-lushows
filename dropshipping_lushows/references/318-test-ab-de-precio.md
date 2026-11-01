# Test A/B de precio

## Por qué es el método más confiable

Porque usa **clientes reales, con su dinero, en condiciones reales de compra**. No mide lo que la
gente dice que pagaría (`317`); mide lo que pagó. Todo lo demás es proxy.

Y por eso mismo es el más caro: necesita tráfico, y el tráfico cuesta.

## El procedimiento completo

| Paso | Qué haces | Error típico |
|---|---|---|
| 1. Hipótesis | escribe la frase antes de empezar: "A 1.099 el margen por visitante sube vs 999" | correr sin hipótesis y buscar cualquier número que salga bien |
| 2. Precios distintos, **tráfico comparable**, **al mismo tiempo** | mismo anuncio, mismo público, misma hora | comparar semana 1 vs semana 2 y llamarlo A/B |
| 3. Corre hasta significancia | el criterio se define ANTES, con el tamaño de muestra calculado | mirar el panel cada hora y parar cuando vas ganando |
| 4. Mide **conversión Y margen juntos** | la métrica es margen por visitante, no conversión | declarar ganador al precio bajo porque convirtió más |
| 5. Adopta el ganador | cámbialo en firme, no "a ver qué pasa" | dejar los dos precios vivos indefinidamente |
| 6. Sigue monitoreando | el ganador se vuelve viejo: cambia el CPM, el competidor, la temporada | asumir que el precio ganó para siempre |

### El paso 4 es el que separa al operador del aficionado

```
MÉTRICA CORRECTA = MARGEN POR VISITANTE
                 = tasa de conversión × margen por pedido
```

Con la economía del proyecto (USD): a 54,59 (999 MXN) el margen sin adquisición es 26,47.

| Escenario | Conversión | Margen/pedido | Margen por 1.000 visitas |
|---|---|---|---|
| Precio 999 | 2,00% | 26,47 | 529,40 |
| Precio 1.099 (≈ +10%) | 1,80% | ~31,93 | 574,74 |
| Precio 1.099 | 1,60% | ~31,93 | 510,88 |

A 1,80% el precio alto gana aunque convierta menos. A 1,60% pierde. **La conversión sola nunca te
dice quién ganó.** Verifica tu propio cálculo con `Matematicas_lushows`; el margen por precio
candidato lo genera `321`.

## Cuánto tráfico hace falta de verdad

Éste es el número que nadie te dice. Para detectar un cambio relativo en conversión con 95% de
confianza y 80% de poder, partiendo de una conversión base del 2%:

| Cambio que quieres detectar | Visitantes **por variante** (orden de magnitud) |
|---|---|
| 50% relativo (2,0% → 3,0%) | ~2.500 - 3.500 |
| 30% relativo (2,0% → 2,6%) | ~7.000 - 9.000 |
| 20% relativo (2,0% → 2,4%) | ~15.000 - 20.000 |
| 10% relativo (2,0% → 2,2%) | ~60.000 - 80.000 |

Rangos de orden de magnitud: **el número exacto depende de tu conversión base real y lo calcula
`Matematicas_lushows`**. No lo cites como cifra cerrada.

Traducción brutal: un cambio de precio del 10% suele mover la conversión menos de un 20% relativo.
Eso significa **15.000-20.000 visitantes por variante — 30.000-40.000 en total** para una sola
prueba. A un CPC de USD 0,30-0,50, eso son miles de dólares en una decisión.

## Advertencia honesta: con menos de USD 500 esto NO alcanza

El proyecto activo tiene capital < USD 500 y alcanza para **~5 tests en total**, de todo tipo. Un
solo A/B de precio bien hecho se comería el presupuesto completo y aun así **no llegaría a
significancia**.

Lo que pasa cuando igual lo intentas:

| Síntoma | Qué realmente ocurrió |
|---|---|
| "Ganó el A con 12 ventas vs 9" | ruido. Con esos números la diferencia no existe |
| "Paré cuando iba ganando" | *peeking*: inflas el falso positivo muchísimo |
| "Corrí 4 días" | día de semana ≠ fin de semana; mezclaste dos poblaciones |
| "Subí el precio y bajó la venta" | puede ser el precio, o el CPM de esa semana, o el creativo cansado |

No recomiendes A/B a ciegas a alguien que no tiene tráfico para sostenerlo. Con poco tráfico un A/B
no te da una respuesta mala: te da **una respuesta aleatoria disfrazada de dato**, que es peor,
porque la vas a obedecer.

## Qué hacer en su lugar (poco tráfico, poco capital)

### Opción 1 — Van Westendorp con pocos respondientes
30-50 respuestas te dan el **rango**, que es la decisión grande (¿999 o 1.699?). Cuesta casi cero.
Ver `317`. Es lo primero que debes hacer.

### Opción 2 — Prueba secuencial (antes y después)
Un solo precio a la vez, en bloques limpios.

| Regla | Detalle |
|---|---|
| Bloques de **7 días completos** | nunca 3 o 4: el ciclo semanal te engaña |
| Cambia **una sola cosa** | precio. Nada de creativo nuevo, público nuevo ni presupuesto nuevo |
| Presupuesto diario idéntico | si cambia el gasto, cambia la subasta |
| Registra CPM y CPC de cada bloque | si el CPM se movió >20%, el bloque no es comparable: repite |
| Evita semanas raras | Buen Fin, quincena, puentes. Ver `238` |
| Mínimo 2 bloques por precio, alternados A-B-A-B | si A gana las dos veces, empieza a ser señal |

Límite honesto: **es un método débil**. Confunde precio con tiempo. Sirve para detectar cambios
grandes (20-30%+), no para afinar 999 vs 1.049. Si el resultado es ambiguo, el resultado es "no sé",
y esa es una respuesta válida.

### Opción 3 — Probar el precio del BUNDLE, no del producto suelto
La mejor opción con poco tráfico, y casi siempre la ignorada.

| Por qué funciona mejor | Explicación |
|---|---|
| El efecto es más grande | pasar de 999 suelto a 1.599 con dos unidades mueve el ticket 60%, no 10% |
| Se necesita menos muestra | efectos grandes requieren menos datos (mira la tabla de arriba) |
| Ataca el ticket, que es la palanca real | ver `220` |
| Tienes referencia de mercado | CV Directo: 999 → 1.599 · 1.999 → 2.748. `eleveitmx.shop`: 549 núcleo, 727 doble, 1.000 triple |

Es decir: en vez de preguntar "¿999 o 1.099?", pregunta "¿el suelto a 999 o el pack a 1.599?". Esa
diferencia sí se ve con el tráfico que tienes. Ver `218`.

### Opción 4 — Por segmento / cohorte
Si ya vendes por dos canales separables (por ejemplo tienda propia y Mercado Libre, o dos países),
puedes sostener precios distintos por canal sin hacer trampa y comparar. Ojo: los públicos no son
iguales, así que es comparación sucia. Y en marketplace el precio relativo manda — rutea a
`mercadolibre_lushows`.

## Orden recomendado para el proyecto activo

```
1. Van Westendorp (30-50 resp.)   → rango             → coste ~0
2. Corre 321 con el rango          → descarta precios bajo 2,7x
3. Prueba de BUNDLE vs suelto      → 1 test de los 5   → efecto grande, medible
4. Secuencial A-B-A-B del ganador  → 2 tests           → afina ±10%
5. Reserva 2 tests                 → creativo y oferta, que rinden más que el precio
```

Nunca gastes más de 1 de tus 5 tests en afinar el precio dentro del rango. El rango vale 10 veces
más que el afinado.

## Errores que invalidan un A/B de precio

| Error | Efecto |
|---|---|
| Mismo cliente ve dos precios | destruye la prueba y te quema la reputación. Ver `320` |
| Precios distintos en anuncio y landing | mides confusión, no precio |
| Cambiar el envío junto con el precio | dos variables, cero conclusiones |
| Medir solo conversión | ver paso 4 |
| No fijar el criterio de parada antes | te auto-engañas garantizado |
| Ignorar devoluciones y cancelaciones | en prepago importa menos, en COD lo es todo |

## Frontera

| Necesitas | Skill |
|---|---|
| **Tamaño de muestra, significancia, potencia, verificación del cálculo** | **`Matematicas_lushows` — rutea siempre aquí** |
| Pruebas dentro de la plataforma de anuncios | `facebook_ads_lushows` |
| Mecánica del A/B en la página | `202` · `desingweb-lushows` |
| Precio dentro de Mercado Libre | `mercadolibre_lushows` |

## Relacionados
`202` · `216` · `218` · `220` · `221` · `226` · `228` · `238` · `316` · `317` · `319` · `320` · `321`
