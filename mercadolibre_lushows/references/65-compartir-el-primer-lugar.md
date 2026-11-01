# Compartir el primer lugar

El catálogo no siempre tiene un único ganador. Cuando dos o más vendedores quedan empatados en las
variables que deciden, ML **comparte el primer lugar**: las visitas se dividen y el ganador alterna
según quién esté buscando. Entender esto evita dos errores caros: creer que perdiste cuando estás
empatado, y creer que ganaste cuando solo te toca la mitad.

## Qué significa "compartido"

| Escenario | Qué ve el comprador | Qué recibes tú |
|---|---|---|
| Ganador único | Siempre el mismo vendedor con "Comprar ahora" | Todo o nada |
| **Primer lugar compartido** | A veces tú, a veces el otro | Una fracción del tráfico |
| Perdiste | Siempre el otro | Solo "Otras opciones de compra" |

El reparto no es aleatorio del todo: **hay personalización por usuario**. El comprador con
historial en tu tienda, el de tu ciudad, el que es Meli+ — todos pueden inclinar la balanza hacia
un vendedor u otro en la misma ficha y al mismo tiempo.

**Ver "Comprar ahora" con tu nombre en tu pantalla no prueba que estés ganando: prueba que estás
ganando para ti.**

## Por qué te confunde tanto

```
Tú abres la ficha        → apareces tú        → "gané el catálogo"
Tu cliente abre la ficha → aparece el otro    → "¿por qué no vendo?"
```

Es el mismo fenómeno que hace inútil medir tu posición desde tu propia sesión. Método correcto de
medición: `69`.

## Cómo confirmar que estás compartiendo

```
□ Abre la ficha en ventana de incógnito, 5 veces seguidas
□ Anota qué vendedor aparece con el botón "Comprar ahora" cada vez
□ Repite desde el celular con datos móviles (otra IP)
□ Pide a alguien en otra ciudad que abra la misma ficha y te diga qué ve
□ Si el resultado alterna → primer lugar compartido
□ Si siempre sale el mismo y no eres tú → perdiste (ataca `63`)
□ Si siempre sales tú en todas las pruebas → ganador único
```

Cinco pruebas es el mínimo. Con dos o tres, el azar te engaña.

## Qué hacer cuando compartes

Compartir es una posición buena pero inestable. Estás a un movimiento del competidor de perderla
entera. Las palancas, en orden de retorno:

| Palanca | Efecto sobre el empate | Cuidado |
|---|---|---|
| Activar Full | Suele romper el empate a tu favor (`103`) | Toma días y tiene costos |
| Subir de nivel MercadoLíder | Rompe empates persistentes (`131`) | Se gana con volumen, no se fuerza |
| Ofrecer cuotas extra | Se ve directo en la tabla comparativa | Cuestan exactamente 3 pp (`78`) |
| Envío gratis | Cambia el precio final percibido (`86`) | Sale de tu margen |
| Bajar el precio | Rompe el empate hoy | El otro lo copia mañana |
| Mejorar reputación | Rompe empates y es la más difícil de copiar | Toma 60 días de medición |

Fíjate en el orden: el precio es la última. En un empate, bajar precio inicia una guerra que los
dos pierden — el competidor está viendo exactamente la misma ficha que tú.

## La cuenta que hay que hacer antes de romper el empate

Compartir el 50% del tráfico con margen sano puede ser mejor que ganar el 100% con margen
destruido. Haz el número:

```
Escenario A (compartido): visitas × 50% × conversión × margen actual
Escenario B (gano bajando precio): visitas × 100% × conversión × margen reducido
```

Si B no supera a A, **no bajes el precio**. Para que el cálculo salga exacto, rutea a
`Matematicas_lushows`. La comisión real sale del simulador oficial estando logueado —
la API `listing_prices` ya no es pública (403, exige token desde 2026).

> ⚠️ **Sin verificar para Colombia (sep-2026).** No hay cifra oficial de cómo se reparte el tráfico
> en un primer lugar compartido (¿mitad y mitad? ¿según personalización?). Trata el 50% como
> supuesto de trabajo, no como dato, y mídelo en tus propias visitas.

## Cuando compartes y aun así no vendes

Si estás compartiendo el primer lugar pero tus ventas no suben, el problema no es la posición:

| Síntoma | Causa probable | Módulo |
|---|---|---|
| Recibes visitas y no vendes | Tu precio final con envío es peor que el del otro | `68`, `83` |
| Recibes pocas visitas aun compartiendo | La ficha de catálogo entera tiene poco tráfico | `71` |
| Vendías y de pronto paraste | Perdiste el empate: vuelve a medir | `69` |
| Vendes menos de la mitad | La personalización favorece al otro (más historial) | `125` |

## El caso especial: el empate con la marca oficial

Si compartes primer lugar con la Tienda Oficial de la marca, el empate rara vez dura. La marca
tiene mejor costo, suele tener Full y suele ser MercadoLíder. Si tu producto es exactamente el
mismo, tu salida no es pelear: es diferenciar el producto o cambiarlo. Ver `64`.

## El error clásico

Tratar el catálogo como un estado ("gané" / "perdí") en vez de una medición continua. El primer
lugar se mueve todos los días, se comparte, se pierde por un quiebre de stock de dos horas y se
recupera solo. **Mide cada semana con el método de 5 pruebas en incógnito**, no cuando te acuerdes
y desde tu propia sesión.

## Relacionados

`61` stock cero · `62` qué es el catálogo · `63` cómo se gana el catálogo ·
`64` cuándo no competir en catálogo · `66` reputación como filtro · `67` envío y posición ·
`68` precio como factor · `69` medir tu posición real · `70` espiar al líder ·
`71` tendencias de ML · `78` tipos de publicación · `83` precio con margen · `86` envío gratis ·
`103` Full · `125` reputación · `131` MercadoLíder
