# La subasta y el CPC

Cada vez que alguien busca en Mercado Libre se corre una subasta para decidir qué anuncios se
muestran y en qué orden. Entender la lógica te evita la trampa de creer que ganar es cuestión de
pujar más. Este módulo también marca, con honestidad, lo que ML **no** publica.

## Lo que sí está confirmado

| Hecho | Fuente |
|---|---|
| El cobro es por clic (CPC), nunca por impresión | Oficial ML Colombia, verificado sep-2026 |
| Hay una subasta que decide posición entre anunciantes | Oficial (existe el mecanismo) |
| La estrategia elegida determina qué tan agresiva es la puja | Oficial: las tres estrategias (`148`) |
| El presupuesto diario limita el gasto, no la posición | Oficial |

## Lo que NO está publicado

> ⚠️ **Sin verificar (sep-2026).** Mercado Libre **no publica** la mecánica detallada de su
> subasta: ni la fórmula, ni los pesos de relevancia, ni si es de primer o segundo precio. Todo
> diagrama con porcentajes que encuentres en un blog está inventado o copiado de Amazon. Trabaja
> con la lógica, no con números falsos.

> ⚠️ **Sin verificar para Colombia (sep-2026).** El **presupuesto mínimo diario en COP** no está
> publicado. Las cifras que circulan son de Argentina y México. Léelo en el panel al crear la
> campaña: Mi cuenta → Marketing → Publicidad → Crear campaña. Aparece en COP antes de confirmar.

## La lógica: puja más relevancia

Ninguna subasta de retail media moderna ordena solo por dinero. Si lo hiciera, el marketplace
llenaría la primera pantalla de anuncios que nadie clica y perdería plata. El ordenamiento
responde a dos familias de señales:

| Familia | Qué incluye | Quién la controla |
|---|---|---|
| **Puja** | Cuánto estás dispuesto a pagar por el clic | Tú, vía estrategia y presupuesto |
| **Relevancia** | Qué tan probable es que ese clic termine en venta | Tu ficha, precio, reputación, envío |

Las mismas variables que deciden tu posición orgánica (`57`) empujan tu relevancia publicitaria:
conversión histórica, calidad de ficha, precio competitivo, reputación, logística. Por eso los
dos mundos no están separados.

**El que tiene la mejor ficha paga menos por el mismo lugar.** Esa es la frase que resume toda la
subasta: la relevancia es un descuento.

## Qué te encarece el clic

| Señal | Efecto en tu costo |
|---|---|
| Ficha incompleta, foto mala | Menos clics por impresión → el sistema te muestra menos → pagas más por llegar |
| Precio por encima del mercado | Te muestran, no te clican; y si te clican, no conviertes |
| Reputación naranja o roja | Penalización de ranking que la plata no compensa (`66`, `125`) |
| Quiebres de stock | Reinicia el aprendizaje sobre esa publicación y encarece la pauta futura |
| Categoría muy disputada | Competencia pura: más anunciantes, clic más caro |
| Cambiar precio y ficha a diario | El sistema nunca estabiliza qué esperar de ti |

El último punto vale doble: **la campaña necesita quietud para aprender.** Ver `156`.

## Lo que NO controlas y hay que aceptar

- No eliges "posición 1". Eliges agresividad (estrategia) y tope de gasto (presupuesto).
- No ves la puja del competidor. La subasta es ciega.
- El CPC varía por hora, por categoría y por temporada. En fechas calientes sube (`161`).
- No puedes comprar relevancia. Se construye con ventas, ficha y reputación.

## Cómo pujar sin datos: el método

No adivines el CPC. Deja que el sistema lo descubra dentro de un tope que tú controlas:

```
1. Elige estrategia Rentabilidad (ACOS objetivo 5-15%, ver `148`)
2. Fija un presupuesto diario que puedas perder 14 días seguidos
3. NO toques nada durante 14 días (la atribución tarda, ver `151`)
4. Lee el reporte: ACOS real, clics, conversión por publicación (`155`)
5. Si el ACOS quedó por debajo de tu margen, sube presupuesto un 20-30%
6. Si quedó por encima, baja la agresividad o apaga los SKU que no dan
```

Subir el presupuesto un 20-30% por vez, no doblarlo: los saltos grandes reinician el
comportamiento de la campaña y pierdes la lectura que acabas de conseguir.

## Presupuesto agotado: qué significa

Si tu campaña gasta todo el presupuesto diario temprano, no significa "éxito": significa que
dejaste de aparecer el resto del día, probablemente en las horas de más compra. Dos lecturas
posibles:

| Situación | Qué hacer |
|---|---|
| ACOS por debajo del margen y presupuesto agotado | Sube el presupuesto: estás dejando ventas rentables en la mesa |
| ACOS por encima del margen y presupuesto agotado | No subas nada. Estás comprando ventas que pierden plata (`154`) |

## El error clásico

Creer que el CPC es un precio fijo que se negocia. El vendedor promedio busca "cuánto cuesta el
clic en Mercado Libre Colombia", encuentra una cifra de un blog argentino, arma un plan con ella
y se estrella. El CPC es un resultado, no un dato de entrada: depende de tu categoría, tu ficha y
tu competencia ese día. El único número real es el que sale de tu propio reporte a los 14 días.

## Checklist antes de tocar la puja

```
□ Llevo al menos 14 días corridos sin cambiar nada en la campaña
□ Revisé el reporte con la atribución ya cerrada, no con datos de ayer (`151`)
□ Sé el ACOS real de la campaña y el margen neto del SKU (`149`, `82`)
□ Voy a mover UNA sola variable (presupuesto O estrategia, no las dos)
□ El movimiento es de 20-30%, no el doble
□ Anoté la fecha del cambio para poder comparar el siguiente periodo
```

## Relacionados

`145` qué es Mercado Ads · `146` Product Ads · `148` las tres estrategias y su ACOS ·
`149` ACOS y TACOS · `150` el ACOS sano según tu margen · `151` la ventana de atribución ·
`155` leer los reportes · `156` optimizar semana a semana · `161` fechas calientes y CPC ·
`57` factores del ranking · `61` stock cero · `66` reputación como filtro · `68` precio ·
`82` la calculadora de margen · `125` reputación
