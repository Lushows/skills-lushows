# Elegir categoría

La categoría es la decisión más cara de la publicación y la que más gente toma en cinco segundos.
Define en qué búsquedas y filtros puedes aparecer, qué atributos te van a exigir, si puedes entrar
a catálogo y **cuánto te cobra ML por vender**. Elegir mal es volverse invisible y pagar de más.

## Qué se te juega en esa lista desplegable

| Consecuencia | Detalle |
|---|---|
| Visibilidad | Si el comprador navega por otra rama, no existes para él |
| Filtros | Los atributos que puede filtrar dependen de la categoría (`31`) |
| Comisión | Varía por categoría; hay que leerla, no suponerla |
| Catálogo | Solo algunas categorías tienen ficha compartida (`62`) |
| Atributos obligatorios | Cambian 100% según la categoría (MEDIA-ALTA) |
| Ficha técnica exigida | Una ficha incompleta es causa citada de pausas y revisiones (MEDIA) |

Lo público sobre comisión en Colombia es el rango: **entre 8% y 22% según la categoría y la
cantidad de cuotas que ofrezcas** (oficial ML Colombia, verificado sep-2026). El detalle por
categoría no es público.

> ⚠️ **Sin verificar para Colombia (sep-2026).** Qué categorías son las más caras y las más baratas
> en MCO no está confirmado. El patrón que circula (Supermercado barata, Computación cara) es
> **de Argentina**. Para leer tu comisión real: simulador de costos del panel **estando logueado**.
> La API `GET /sites/MCO/listing_prices` **ya no es pública**: hoy responde
> `403 PA_UNAUTHORIZED_RESULT_FROM_POLICIES` y exige token.

## Cómo se elige bien

Tres pasos, en este orden:

```
□ 1. Corre el predictor de categoría con el nombre real del producto (`27`)
□ 2. Busca tu producto como comprador y mira en qué rama están los que VENDEN
□ 3. Compara comisión y atributos exigidos entre las 2-3 candidatas antes de decidir
```

El paso 2 es el que la gente se salta. Escribe en el buscador de ML exactamente lo que escribiría
tu cliente, abre las tres primeras publicaciones con más ventas y mira la **miga de pan**
(el rastro "Inicio > Hogar > Cocina > ...") arriba de la ficha. Esa es la categoría que el mercado
ya validó.

## El criterio de desempate

Cuando dos categorías son defendibles, no elijas la que "suena mejor". Elige con esta tabla:

| Criterio | Peso | Por qué |
|---|---|---|
| Dónde están los que venden | Muy alto | Es donde el comprador busca de verdad |
| Comisión más baja | Alto | Es margen permanente, venta tras venta (`75`) |
| Tener catálogo disponible | Alto | Más exposición que las libres equivalentes (`62`) |
| Menos atributos obligatorios | Bajo | Los vas a llenar todos igual (`32`) |

**Veredicto: manda dónde compra la gente, no dónde te cobran menos.** Una comisión dos puntos más
baja en una rama donde nadie busca vale cero.

## Categorías que se prestan a error

| Producto | Error frecuente | Dónde suele ir |
|---|---|---|
| Accesorio de celular | En "Celulares y Teléfonos" a secas | En la subcategoría de accesorios |
| Utensilio de cocina profesional | En "Industrias y Oficinas" | En Hogar > Cocina, salvo equipo grande |
| Plantilla o Excel descargable | En la categoría del rubro | En Servicios / digitales, con reglas propias (`49`) |
| Repuesto compatible | En la categoría de la marca original | En repuestos, con el atributo de compatibilidad |
| Kit de varios productos | En la categoría del producto más caro | En la del producto principal de uso (`48`) |

## Cambiar de categoría después

Se puede editar, pero no es gratis en señales: la publicación cambia de vecindario, pierde los
filtros donde ya estaba indexada y vuelve a competir desde otro lugar. Si la publicación ya tiene
ventas y opiniones, evalúa antes de mover.

| Situación | Qué hacer |
|---|---|
| Publicación nueva, sin ventas | Corrige la categoría ya, sin miedo |
| Con pocas ventas y mal desempeño | Corrige: probablemente el problema es ese |
| Con historial y ventas sanas | No la muevas por corazonada; mide primero (`166`) |

## El error clásico

Aceptar la primera sugerencia del formulario sin mirar. El predictor acierta mucho, pero se guía
por el texto que tú escribiste: si tu título es ambiguo ("organizador multiusos"), la sugerencia
también lo será. **La categoría no la elige el formulario: la elige el comprador, y tú solo la
descubres.**

## Señales de que estás en la categoría equivocada

```
□ Tienes visitas pero casi ninguna llega por búsqueda con filtros
□ Los atributos que te pide ML no tienen nada que ver con tu producto
□ Ningún competidor directo tuyo está en esa rama
□ Tu producto no aparece cuando navegas la categoría como comprador
□ La comisión te parece rarísima comparada con la de tus competidores
```

Dos o más marcados: revisa con el predictor (`27`) y con la miga de pan de los líderes.

## Relacionados

`27` el predictor de categoría · `31` ficha técnica y atributos · `32` obligatorios vs opcionales ·
`48` kits y combos · `49` servicios y digitales · `62` catálogo · `75` comisiones y margen ·
`54` auditoría en 15 minutos
