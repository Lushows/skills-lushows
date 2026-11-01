# 99 — Entregables legales y PDF

Un concepto, un contrato o una cláusula valen lo que **se entienden y se pueden firmar**. Por eso esta skill entrega documentos presentables en **PDF**, nunca Markdown crudo: con título, fecha, versión, numeración de cláusulas, espacio de firmas y, cuando el riesgo es alto, la marca **«BORRADOR — para revisión de abogado titulado»**. Luis prefiere PDF directo; aquí está el método técnico con Chrome sin interfaz (headless).

## Tipos de entregable
| Entregable | Contenido mínimo |
|---|---|
| **Concepto jurídico** | Pregunta, hechos, respuesta en simple, riesgo (alto/medio/bajo), norma, recomendación y siguiente paso |
| **Contrato o cláusula** | Partes, cláusulas numeradas, anexos, firmas, versión y fecha |
| **Carta** (requerimiento, cese, petición) | Lugar y fecha, destinatario, asunto, cuerpo, firma, anexos |
| **Checklist / matriz** | Tabla con obligación, norma, responsable, fecha, evidencia |
| **Memorando para el abogado externo** | Resumen del caso, cronología, documentos, preguntas concretas |

## Reglas de forma (checklist)
- [ ] Título claro y nombre de archivo descriptivo: `AAAA-MM-DD_tipo_contraparte_vN.pdf`.
- [ ] **Versión y fecha** en el encabezado o pie.
- [ ] Cláusulas numeradas; términos definidos en mayúscula inicial.
- [ ] Normas citadas con número, año y «(verificar vigencia)» donde aplique.
- [ ] Marca de **BORRADOR** cuando el documento requiera revisión profesional.
- [ ] Bloque de firmas con nombre, cargo, identificación y empresa.
- [ ] Tipografía legible (serif para cuerpo, 11–12 pt), márgenes amplios, numeración de páginas.
- [ ] En español, sin latín sin traducir.

## Plantilla HTML base (para imprimir a PDF)
```html
<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<title>Contrato de distribución — BIO-SETA — v1</title>
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:wght@400;600&family=Inter:wght@500;700&display=swap" rel="stylesheet">
<style>
  @page { size: Letter; margin: 22mm 20mm 24mm 20mm; }
  body { font-family: "Source Serif 4", Georgia, serif; font-size: 11.5pt; line-height: 1.55; color: #111; }
  h1, h2 { font-family: Inter, Arial, sans-serif; } h1 { font-size: 18pt; margin: 0 0 4mm; }
  h2 { font-size: 12pt; margin: 7mm 0 2mm; } .meta { font: 9pt Inter, Arial, sans-serif; color: #555; }
  .borrador { position: fixed; top: 40%; left: 5%; transform: rotate(-30deg); font: 700 48pt Inter, Arial;
              color: rgba(200,0,0,.08); white-space: nowrap; }
  .firmas { display: flex; gap: 20mm; margin-top: 18mm; } .firma { flex: 1; border-top: 1px solid #000; padding-top: 2mm; }
  table { width: 100%; border-collapse: collapse; } td, th { border: 1px solid #bbb; padding: 2mm; font-size: 10pt; }
  h2, .firmas { break-inside: avoid; }
</style></head><body>
<div class="borrador">BORRADOR — REVISIÓN DE ABOGADO</div>
<h1>Contrato de distribución</h1>
<p class="meta">Versión 1 · 26 de octubre de 2026 · Preparado con abogado_lushows</p>
<h2>Primera. Objeto</h2><p>…</p>
<div class="firmas"><div class="firma">[Nombre]<br>Representante legal, [EMPRESA]</div>
<div class="firma">[Nombre]<br>Representante legal, [CONTRAPARTE]</div></div>
</body></html>
```

## Comando para generar el PDF (Windows)
**PowerShell:**
```powershell
$perfil = Join-Path $env:TEMP ("chrome-pdf-" + [guid]::NewGuid())
& "C:\Program Files\Google\Chrome\Application\chrome.exe" --headless=new --disable-gpu `
  --no-pdf-header-footer --virtual-time-budget=10000 --user-data-dir="$perfil" `
  --print-to-pdf="C:\ruta\salida.pdf" "file:///C:/ruta/documento.html"
```
**Bash (Git Bash):**
```bash
"/c/Program Files/Google/Chrome/Application/chrome.exe" --headless=new --disable-gpu \
  --no-pdf-header-footer --virtual-time-budget=10000 \
  --user-data-dir="$(mktemp -d)" \
  --print-to-pdf="C:/ruta/salida.pdf" "file:///C:/ruta/documento.html"
```
- `--user-data-dir` con un **perfil temporal** evita que el comando se cuelgue o se pegue a un Chrome ya abierto.
- `--no-pdf-header-footer` quita la fecha y la URL que Chrome pone por defecto (en versiones antiguas: `--print-to-pdf-no-header`).
- `--virtual-time-budget` da tiempo a que carguen las fuentes web; si no hay internet, el CSS cae a Georgia/Arial.
- Rutas con espacios siempre entre comillas; la URL `file:///` usa barras normales.

## Verificación después de generar
1. Confirmar que el archivo existe y pesa más de unos pocos KB.
2. Abrirlo (o leerlo con la herramienta de lectura de PDF) y revisar: saltos de página, tablas cortadas, firmas en la misma página, acentos y «ñ» correctos.
3. Si las fuentes no cargaron, aumentar `--virtual-time-budget` o usar fuentes locales.
4. Borrar el perfil temporal si quedó en disco.

## Riesgos y errores comunes
- **Medio:** entregar un borrador de alto riesgo sin la marca de BORRADOR: alguien lo firma como definitivo.
- **Medio:** PDF sin versión ni fecha: se firman versiones equivocadas.
- **Bajo:** Chrome colgado por usar el perfil normal: siempre `--user-data-dir` temporal.

## Conexión con otros módulos
- `00` método (formato de entrega) · `08` cómo usar la skill · `100`–`109` plantillas · `180` gestión de contratos · `183` archivo legal.
- **contador_lushows** y **economist_lushows** usan el mismo método de PDF.

## Siguiente paso típico
Generar el HTML del entregable con la plantilla, imprimirlo a PDF con el comando y verificar visualmente antes de enviarlo a Luis.
