# 09 · Producto "general": investigar todo el contenido desde cero

> Vigencia: 16-sep-2026. Cuando Luis dice un producto sin link ("quiero vender un masajeador de
> cuello", "freidora de aire"), no hay referencia: hay que armar el expediente completo.

## El expediente (una carpeta por producto)

```
Desktop\dropshipping-productos\<producto>\
  expediente.md        ← specs verificadas, afirmación→prueba, fuentes, permisos
  radiografia\         ← referencias analizadas (espiar_tienda.py)
  img\  video\         ← medios con origen anotado
  landing.html         ← la página
```

## 1. Identificar el producto exacto

- **Número de modelo** (sin modelo no hay specs confiables). Buscarlo en Alibaba/1688/made-in-china
  por palabras clave + foto; cruzar 3 proveedores que usen el mismo modelo.
- **FCC ID** si es electrónico → fccid.io (manual, fotos internas, pruebas).
- **App compañera** si la tiene → ficha en App Store/Google Play (desarrollador, reseñas de fallas).

## 2. Specs: tabla afirmación → prueba

| Afirmación | Fuente | Prueba | ¿Publicable? |
|---|---|---|---|
| Sensor 8 MP | Ficha proveedor + fotos internas FCC | PDF + captura | Sí |
| "32 MP" | Anuncio del vendedor | Interpolado | **No** |
| 7 h música | Proveedor | Pendiente medir con muestra | Con "hasta", medir |

Regla: lo que no tenga prueba no entra a la página. Lo pendiente de medir va con "hasta" y se
confirma con la muestra antes de pautar.

## 3. Dolor, objeciones y lenguaje

- **Mercado Libre** del país: las 5 publicaciones más vendidas → preguntas + reseñas 1-3★ y 5★.
- **Amazon** (México/EE.UU.): reseñas "críticas más útiles".
- **AliExpress**: reseñas con fotos (defectos reales, tamaño real).
- **TikTok/YouTube**: comentarios en reviews del producto ("¿sirve para…?").
- **Reddit** (en inglés): hilos de comparación y quejas de durabilidad.
Salida: lista de 10 dolores + 10 objeciones + 20 frases literales → `06-copy-dolor-beneficio-costo.md`.

## 4. Precio y competencia

- Rango de precio local (Mercado Libre, Amazon MX, tiendas de marca).
- La mejor tienda del mundo en esa categoría para dirección de arte (`04-tiendas-referencia.md`).
- Margen con `dropshipping_lushows` antes de diseñar.

## 5. Medios: de dónde sale cada cosa (en orden de preferencia)

1. **Propios con la muestra** (foto a escala, en uso, macro, contenido de caja; video demo y POV).
2. **Proveedor con permiso escrito** (plantilla A en `07`).
3. **Creadores con licencia** web+ads (plantilla B en `07`).
4. **IA etiquetada** solo para ambiente, nunca para el producto o sus resultados.
5. **Placeholder honesto** en la página ("video grabado con el producto — pendiente") mientras llega lo real.

Anotar el origen y el permiso de cada archivo en `expediente.md`.

## 6. Contenido educativo que vende (cuando el producto lo pide)

- "Cómo funciona" en 3 pasos con íconos o frames del video.
- "Qué incluye la caja" con foto real.
- Guía de uso/cuidado corta (reduce devoluciones y soporte).
- Tabla "¿es para ti?" (para quién sí / para quién no) — la honestidad sube la confianza y baja devoluciones.
