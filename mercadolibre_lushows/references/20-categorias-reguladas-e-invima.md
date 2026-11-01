# Categorías reguladas e INVIMA

Alimentos, cosméticos, suplementos y dispositivos médicos se pueden vender en Mercado Libre,
pero son productos que en Colombia necesitan permiso sanitario **antes** de existir en el
mercado. Mercado Libre no te lo pide con un formulario claro, así que el vendedor cree que
está bien hasta que llega la denuncia o la SIC.

## La regla de fondo

En Colombia, el INVIMA regula lo que se come, lo que se aplica en el cuerpo y lo que se usa
para diagnosticar o tratar. Cada familia de producto tiene su figura:

| Producto | Figura sanitaria típica | Quién la saca |
|---|---|---|
| Alimentos procesados | Registro / permiso / notificación sanitaria | El **fabricante o importador** |
| Bebidas | Registro sanitario | Fabricante o importador |
| Cosméticos | Notificación Sanitaria Obligatoria (NSO) | Fabricante o importador |
| Suplementos dietarios | Registro sanitario | Fabricante o importador |
| Dispositivos médicos | Registro sanitario, por clase de riesgo | Fabricante o importador |
| Productos de aseo y desinfectantes | Registro / notificación | Fabricante o importador |

**El permiso es del producto, no tuyo.** Si eres revendedor, no necesitas sacar el registro:
necesitas que **el producto que revendes lo tenga** y poder demostrarlo. Si eres tú quien
fabrica o importa, el permiso es tuyo y no hay forma de evitarlo.

Esta distinción es la que más confunde y la que más plata ahorra entenderla.

## Qué tienes que tener a la mano

```
□ Número de registro / NSO / permiso sanitario del producto
□ Nombre del titular del registro (debe coincidir con el fabricante/importador real)
□ Verificación en la consulta pública del INVIMA de que está VIGENTE
□ Factura de compra que trace el producto hasta ese titular
□ Ficha técnica del producto
□ Si importas: la documentación de importación → `24`
```

El de la vigencia es el que se salta todo el mundo. Un registro vencido es igual que no tener
registro, y el fabricante no te va a avisar cuando se le venza.

## Qué pasa si publicas sin el registro

| Frente | Qué te pasa |
|---|---|
| Mercado Libre | Pausa o eliminación de la publicación, infracción en la cuenta (`19`) |
| Denuncia de competidor | Cualquiera denuncia con el botón "Denunciar" de la ficha |
| INVIMA | Medidas sanitarias sobre el producto y el responsable |
| SIC | Si además hiciste claims engañosos, es publicidad engañosa (`22`) |
| Consumidor | Reclamo con soporte legal y garantía (`23`) |

No son excluyentes: una publicación mal hecha de un suplemento puede activar los cinco.

**El riesgo de vender un producto regulado sin registro no es que te bajen la publicación: es
que respondes personalmente por un daño a la salud de alguien.** Ver `11` sobre por qué aquí la
figura jurídica deja de ser un tema fiscal.

## El problema de los claims: dónde muere la mayoría

Aun con registro vigente, **lo que escribes en la ficha te puede hundir**. En Colombia un
alimento o suplemento no puede atribuirse propiedades de prevención, tratamiento o curación de
enfermedades. Eso convierte al producto en medicamento a los ojos de la norma, y los
medicamentos tienen otro régimen entero.

| Lo que NO puedes escribir | Por qué |
|---|---|
| "anticancerígeno", "previene el cáncer" | Claim de enfermedad → producto pasa a ser medicamento |
| "cura", "trata", "elimina la enfermedad X" | Igual |
| "previene enfermedades neurológicas" | Igual |
| "reemplaza el medicamento" | Igual, y es peligroso |
| "aprobado por el INVIMA" | El INVIMA registra, no "aprueba" ni recomienda |
| "100% seguro", "sin efectos secundarios" | Publicidad engañosa (`22`) |

Lo que sí se puede decir está limitado a lo que ampare el registro y a descripciones de
composición y uso. La frontera es fina y se cruza sin querer.

**Escribir un claim de enfermedad en la ficha no es un error de marketing: es reclasificar tu
producto en una categoría en la que no tienes permiso para vender.**

## Referencia cruzada entre skills

La skill **`Bio_lushows`** tiene el caso desarrollado en detalle: suplementos, hongos
funcionales, el régimen del Decreto 3249/2006, el vocabulario aprobado frente al prohibido, y
un análisis real de un negocio que estaba vendiendo con claims de enfermedad sin registro. Si
vas a vender suplementos o alimentos funcionales, **ese es el material de fondo**; este módulo
solo te dice cómo aterriza en la ficha de Mercado Libre.

La química y la evidencia del producto en sí —principios activos, dosis, estabilidad— es de
`Quimico_lushows`.

## Cómo se ve esto en la ficha de Mercado Libre

```
□ Categoría correcta: usa el predictor, no la elijas a ojo → `26`
□ Atributos obligatorios de la categoría: muchas categorías reguladas piden el número
  de registro como atributo. Si el campo existe, LLÉNALO → `31`
□ Registro visible en la descripción, con número y titular
□ Fecha de vencimiento del lote visible y actualizada si aplica
□ Sin claims de enfermedad en título, descripción NI en las imágenes
□ Sin claims en las respuestas a preguntas (ahí también te leen)
□ Foto de la etiqueta real, legible
```

El punto de las imágenes y las preguntas es el que se olvida: el texto prohibido cuenta igual
si está en un gráfico dentro de la foto o si se lo respondiste a un comprador en público.

## Alimentos: la regla de devolución que cambia

Dato oficial de Mercado Libre: los plazos de devolución son **30 días corridos** para productos
nuevos, **14 días** para usados y **6 días corridos para alimentos y bebidas (de personas y de
mascotas)**. Es el único plazo corto y existe justamente por la naturaleza del producto. Ver
`138`.

Si vendes alimentos, ese plazo de 6 días es a tu favor: úsalo, pero también entiende que un
reclamo por calidad en alimentos es de los que **no** se pueden excluir de tu reputación
(producto defectuoso o distinto al anunciado — oficial, ver `136`).

## Si tú fabricas

El camino es largo y no lo resuelve esta skill:

```
□ Definir la categoría sanitaria exacta del producto
□ Ficha técnica y análisis de laboratorio
□ Estudios de estabilidad (pueden ser 2 años en tiempo real)
□ Maquila: fabricar en una planta que ya tenga certificación es legítimo y más rápido
□ Trámite ante el INVIMA, con tarifa (hay exenciones para microempresa)
□ Solo después: publicar
```

No publiques "mientras sale el registro". No existe esa figura.

## El error clásico

Comprar un suplemento importado a un mayorista, publicarlo con la descripción que traía el
fabricante extranjero —llena de claims que en su país son legales y aquí no— y creer que la
responsabilidad es del fabricante. **En la ficha de Mercado Libre el que afirma eres tú.** El
titular de la publicación responde por lo que la publicación dice.

El error hermano: asumir que porque el producto se vende en cadenas grandes, ya está registrado.
Verifícalo tú, en la consulta pública del INVIMA, por número de registro.

## Relacionados

`11` persona natural vs empresa · `19` productos prohibidos · `21` propiedad intelectual ·
`22` estatuto del consumidor · `23` garantías · `24` importar · `26` categoría correcta ·
`31` atributos · `33` lo que declaras en la ficha · `136` reclamos excluibles ·
`138` devoluciones · `Bio_lushows` para suplementos e INVIMA en detalle ·
`Quimico_lushows` para la formulación
