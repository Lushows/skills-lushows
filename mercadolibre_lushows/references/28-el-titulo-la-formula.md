# El título: la fórmula

El título es el campo más estructurado de la publicación: hace que te encuentren y que te entiendan.
Mercado Libre Colombia publica una fórmula y una lista de prohibiciones, y son literales. No es un
espacio publicitario y no admite creatividad.

## La fórmula oficial

> El título debe llevar "**producto, marca, modelo y algunas características principales**"
> (oficial ML Colombia, verificado sep-2026).

Ejemplo oficial de ML Colombia:

> **Crema Gel Hidratante Corporal Skala Hidro Bob 500 ml**

| Bloque | En el ejemplo oficial |
|---|---|
| Producto | Crema Gel Hidratante Corporal |
| Marca | Skala |
| Modelo | Hidro Bob |
| Característica principal | 500 ml |

La "característica principal" cambia por rubro: capacidad en cosmética y electrodomésticos, talla
en calzado, potencia en herramientas, medida en textiles, cantidad en consumibles.

## Cuántos caracteres caben

> ⚠️ **Ojo con el dato de los 60 caracteres.** Ninguna página de ayuda de Mercado Libre Colombia
> publica un límite de caracteres para el título. **Los 60 caracteres son el límite de la API**
> (`POST /items`), no una regla publicada del centro de ayuda. Trabaja con 60 como techo práctico
> —es lo que el sistema acepta—, pero no lo cites como norma oficial ni bases una estrategia en
> que "ML exige 60".

Consecuencia práctica: apunta a 60 y verifica en el formulario del panel, que te muestra el contador
real de tu categoría al escribir.

## Buenos y malos, lado a lado

| ❌ Malo | Por qué | ✅ Bueno |
|---|---|---|
| `¡¡OFERTA!! Zapatillas Deportivas` | Descuentos y símbolos prohibidos (`29`) | `Zapatillas Adidas Superstar Talla 42` |
| `Licuadora Oster Oster Licuadora` | Repetición | `Licuadora Oster 3 Velocidades Vaso Vidrio 1.25 L` |
| `Audifonos` | Sin marca, modelo ni característica | `Audífonos Inalámbricos JBL Tune 510bt Bluetooth` |
| `Tenis tipo Nike Air Force` | "tipo" está prohibido literalmente | `Tenis Deportivos Blancos Unisex Talla 40` |
| `Cafetera + ENVIO GRATIS 12 CUOTAS` | Envío y cuotas los muestra ML | `Cafetera Oster Bvstdc4401 12 Tazas Programable` |
| `Camiseta Algodón Roja` (hay 5 colores) | El color no va en el título: se crean variantes | `Camiseta Algodón Cuello Redondo Unisex Manga Corta` |
| `Nevera Samsung NUEVA original` | "nuevo/usado" no va en el título | `Nevera Samsung Rt38k5930 No Frost 384 L` |
| `Set Vasos y Jarra y Bandeja` | No se menciona más de un producto | Publicación de kit bien armada (`48`) |

## Las reglas literales que afectan la fórmula

Cuatro citas oficiales que cambian cómo se escribe (texto completo en `29`):

| Regla oficial | Qué implica |
|---|---|
| "Si tu producto es nuevo, usado o reacondicionado, **no lo incluyas en el título**" | Eso va en características (`44`) |
| "Si vendes el mismo producto con distintos colores, **no pongas el color en el título**. Crea variantes" | Va a variaciones (`40`) |
| "**No mencionar más de un producto ni sus variantes**" | Un título = un producto |
| "**Separa las palabras con espacios**, no uses signos de puntuación ni símbolos" | Nada de `/ - | *` |

## Editar el título después de publicar

> "Puedes modificarlo incluso si ya tienes ventas. **Excepto si la publicación compite en catálogo**:
> en ese caso no podrás editar el título" (oficial ML Colombia, verificado sep-2026).

Eso es enorme y casi nadie lo sabe antes de entrar a catálogo:

| Situación | ¿Puedes editar el título? |
|---|---|
| Publicación libre, sin ventas | Sí |
| Publicación libre, con ventas | Sí |
| Publicación que compite en catálogo | **No** |

Además, en los títulos de catálogo —que son **compartidos** entre vendedores— ML pide "no sumar
datos de contacto ni mensajes sobre precio, tipo de envío o stock".

**Antes de entrar a catálogo, deja el título como lo quieres para siempre** (ver `62` y `63`).

## Cómo rendir los caracteres

| Técnica | Antes | Después |
|---|---|---|
| Quita conectores | `Licuadora de vaso con 3 velocidades` | `Licuadora Vaso 3 Velocidades` |
| Cifras, no palabras | `doce tazas` | `12 Tazas` |
| Unidades cortas | `1 litro y medio` | `1.5 L` |
| Fuera "nuevo", "original", "calidad" | ocupan y el primero está prohibido | quítalos |
| El color, a variaciones | `Rojo Azul Verde` | variantes (`40`) |

Regla práctica: si una palabra no la escribiría un comprador en el buscador, no merece estar.
**Cada palabra del título debe ser una palabra por la que alguien busca.**

## Cuando no hay marca

Los genéricos igual necesitan el atributo de marca lleno (`32`). En el título, reemplaza la marca
por la característica que más diferencia:

| Producto genérico | Título |
|---|---|
| Delantal de cocina | `Delantal Chef Impermeable Ajustable Bolsillo Unisex` |
| Organizador de cubiertos | `Organizador Cubiertos Cajón Cocina 5 Divisiones Plástico` |
| Set de tazas | `Set 6 Tazas Cerámica 300 Ml Blancas Aptas Microondas` |

## El error clásico

Apilar palabras clave sueltas creyendo que se aparece en más búsquedas:
`Licuadora Batidora Procesador Mixer Cocina Hogar Barata`. Se ve que es basura, el comprador
desconfía, y con el buscador semántico de 2026 pierde todavía más sentido (`30`). **Un título que
se lee como frase real le gana a uno que se lee como lista.**

## Lista de chequeo

```
□ Producto + marca + modelo + característica principal, en ese orden
□ Cabe en 60 caracteres (límite de la API)
□ Ninguna palabra repetida
□ No dice nuevo, usado ni reacondicionado
□ No lleva el color si hay varios colores (van a variantes)
□ Menciona un solo producto
□ Solo espacios: sin signos de puntuación ni símbolos
□ Sin descuentos, promociones, envío, cuotas ni devoluciones
□ Si menciona marca ajena, es con "para" (`29`)
□ Si va a competir en catálogo, este título es el definitivo: ya no se edita
```

## Relacionados

`29` prohibiciones literales · `30` búsqueda semántica · `26` elegir categoría · `27` el predictor ·
`31` atributos · `40` variaciones · `44` condición del producto · `48` kits · `53` estudiar al
líder · `62` `63` catálogo · `54` auditoría en 15 minutos
