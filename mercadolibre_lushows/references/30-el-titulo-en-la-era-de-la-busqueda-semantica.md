# El título en la era de la búsqueda semántica

En el **primer trimestre de 2026** Mercado Libre desplegó su primera experiencia de búsqueda con
IA: pasó de comparar palabras literales a un motor con **LLM que interpreta intención** (MEDIA).
Eso cambia el consejo de título que todo el mundo repite desde hace diez años.

> ⚠️ **Sin verificar para Colombia (sep-2026).** No está confirmado si el buscador con IA ya rige
> en `MCO` o solo en algunos países. Compruébalo tú mismo: busca en ML Colombia una frase
> conversacional ("un bolso que dure años y combine con todo"). Si devuelve resultados coherentes
> en vez de basura, ya está activo para ti.

## Qué cambia exactamente

| | Buscador viejo (coincidencia literal) | Buscador con LLM (intención) |
|---|---|---|
| Qué compara | Las palabras del título con las del comprador | El significado de la consulta con el del producto |
| Consulta típica | `licuadora oster 1.25` | `una licuadora que aguante hielo y no sea ruidosa` |
| Gana quien | Tiene las palabras exactas | Describe de verdad el producto y sus atributos |
| Efecto de apilar keywords | Ayudaba algo | Pierde sentido, y se lee como spam |
| Peso de los atributos | Filtros | Filtros **y** materia prima del entendimiento |

## El consejo viejo vs el nuevo

| Tema | Consejo viejo | Consejo 2026 |
|---|---|---|
| Título | Meter todas las variantes de la palabra | Una frase limpia y específica (`28`) |
| Sinónimos | Repetirlos en el título | Dejarlos a los atributos y a la descripción |
| Errores de ortografía a propósito | "audifonos" sin tilde para cazar búsquedas | Innecesario y feo |
| Descripción | Relleno de keywords | Texto real que responde objeciones (`33` `34`) |
| Ficha técnica | Lo mínimo obligatorio | TODO lleno: es lo que el modelo lee (`32`) |

**Un buscador que entiende premia al que describe y castiga al que apila.**

## Qué hacer hoy, con o sin IA en Colombia

Lo bueno es que no hay que apostar: las dos cosas que sirven para el buscador semántico también
servían para el viejo.

```
□ Título como frase real, con producto + marca + modelo + especificación (`28`)
□ Todos los atributos llenos, incluidos los opcionales (`32`)
□ Descripción escrita para humanos, que nombra usos y problemas resueltos (`33`)
□ Las objeciones respondidas con palabras del comprador (`34`)
□ Cero apilamiento de keywords en cualquier campo
```

No hay ninguna táctica que gane con el buscador nuevo y pierda con el viejo. Por eso este módulo no
es una apuesta: es limpieza.

## Dónde meter las palabras que ya no caben en el título

El título tiene 60 caracteres (límite de la API; la ayuda de ML Colombia no publica un
máximo). Las variantes, sinónimos y usos van en otros campos que sí los
reciben:

| Palabra | Dónde va |
|---|---|
| Sinónimo del producto ("licuadora / batidora de vaso") | Descripción (`33`) |
| Uso ("para batidos de proteína") | Descripción, primer bloque |
| Especificaciones secundarias | Atributos (`31`) |
| Compatibilidades | Atributos de compatibilidad, y "compatible con" en título si cabe |
| Público ("para restaurantes") | Descripción y atributos si la categoría lo tiene |

## Lo que NO cambia

| Sigue igual | Por qué |
|---|---|
| El límite de 60 caracteres | Es un límite de campo, no de algoritmo |
| Las prohibiciones de `29` | Son reglas de política, no de buscador |
| La conversión como factor más pesado del ranking | El buscador cambia, el ranking no (`55`) |
| Que la reputación te tape (`126`) | Ningún buscador arregla una cuenta naranja |

## El error clásico

Leer que "ahora el buscador entiende lenguaje natural" y escribir el título como una frase
publicitaria larga: `La mejor licuadora para tus batidos de la mañana`. Entender intención no es
adivinar de qué producto hablas: el modelo sigue necesitando **producto, marca, modelo,
especificación**. La diferencia es que ya no necesita que repitas.

## Cómo comprobar si te está afectando

```
□ Busca 3 frases conversacionales que describan tu producto sin nombrarlo por su nombre exacto
□ Anota si apareces en la primera página
□ Compara con la búsqueda literal del nombre del producto
□ Si apareces en la literal y no en la conversacional: te faltan atributos y descripción
□ Repite la prueba cada 2 meses: esto está cambiando
```

Guarda el resultado con fecha. Cuando ML active el cambio en Colombia, la diferencia se va a ver en
esa misma prueba.

## Relacionados

`28` la fórmula del título · `29` prohibiciones · `31` ficha técnica y atributos · `32`
obligatorios vs opcionales · `33` la descripción · `34` objeciones en la descripción · `55` cómo
rankea ML · `59` la ventana de 72 horas · `166` medir de verdad
