# 83 — Registro sanitario y regulación de alimentos y suplementos

Para BIO-SETA este es **el módulo más crítico**. Todo producto que se ingiere (alimento, bebida, suplemento dietario) necesita la autorización sanitaria que corresponda, una etiqueta conforme y una publicidad que no le atribuya propiedades que no tiene. Vender sin la autorización correcta o con claims terapéuticos puede terminar en **decomiso, cierre, multas** y en problemas penales en casos graves. La parte técnica (qué es exactamente el producto, su composición, qué está probado) va con **Bio_lushows** y **Quimico_lushows**; aquí va el marco legal.

## Conceptos clave (en simple)
- **INVIMA:** Instituto Nacional de Vigilancia de Medicamentos y Alimentos; expide registros, permisos y notificaciones sanitarias y vigila productos.
- **Registro sanitario / permiso sanitario / notificación sanitaria:** las tres autorizaciones posibles para alimentos, según su nivel de riesgo para la salud pública (alto, medio, bajo).
- **Suplemento dietario:** producto cuyo propósito es adicionar la dieta normal, fuente concentrada de nutrientes y otras sustancias con efecto fisiológico o nutricional; tiene su propio régimen.
- **Producto fitoterapéutico:** producto medicinal a base de plantas; régimen distinto, más exigente (de medicamentos).
- **Titular del registro:** quien responde por el producto ante el INVIMA (`35`).
- **BPM:** Buenas Prácticas de Manufactura.
- **Rotulado o etiquetado:** información obligatoria en el empaque.
- **Declaraciones de propiedades (claims):** nutricionales y de salud; solo las permitidas por la norma o autorizadas.

## Qué dice la norma (Colombia — verificar vigencia)
- **Ley 9 de 1979:** Código Sanitario Nacional; base de las medidas sanitarias y sanciones.
- **Decreto 3249 de 2006** (modificado, entre otros, por el Decreto 3863 de 2008): régimen de **suplementos dietarios**: registro sanitario, fabricación, etiquetado, publicidad y vigilancia; prohíbe atribuirles propiedades terapéuticas, preventivas o curativas (verificar alcance y si la publicidad requiere aprobación previa).
- **Resolución 3096 de 2007:** reglamento técnico sobre condiciones y requisitos de los suplementos dietarios (verificar).
- **Resolución 2674 de 2013 del Ministerio de Salud:** requisitos sanitarios de **alimentos** (fabricación, BPM, manipulación, transporte, comercialización) y autorizaciones según riesgo; **Resolución 719 de 2015:** clasificación de alimentos por riesgo (verificar).
- **Resolución 5109 de 2005:** rotulado general de alimentos envasados.
- **Resolución 810 de 2021** (modificada por la **Resolución 2492 de 2022**): etiquetado nutricional y **frontal de advertencia** (sellos) para alimentos envasados (verificar aplicabilidad a suplementos).
- **Decreto 2266 de 2004:** régimen de productos fitoterapéuticos (verificar si alguna presentación cae en esta categoría).
- **Ley 2120 de 2021:** entornos alimentarios saludables y etiquetado.

## Paso a paso: lanzar un producto ingerible
1. **Clasificar el producto** con Bio_lushows / Quimico_lushows: ¿alimento (y de qué riesgo), suplemento dietario o fitoterapéutico? La clasificación decide todo lo demás.
2. **Definir el titular** de la autorización (la SAS, idealmente) y el fabricante (con BPM o condiciones sanitarias exigidas).
3. **Preparar el expediente** (fórmula cuali-cuantitativa, especificaciones, estudios de estabilidad, etiqueta, certificados del fabricante, entre otros, según el trámite).
4. **Radicar** ante el INVIMA y pagar la tarifa vigente.
5. **Diseñar la etiqueta** conforme a la norma aplicable, con el número de la autorización.
6. **Revisar la publicidad** (web, bot, redes, distribuidores, influencers) para que no exceda lo autorizado (`52`, `49`).
7. **Calendarizar** el vencimiento y renovación de la autorización (`184`).

## Checklist de etiqueta (general, verificar norma aplicable)
- [ ] Nombre del producto y denominación correcta («suplemento dietario», si aplica).
- [ ] Lista de ingredientes y contenido neto.
- [ ] Número de registro/permiso/notificación sanitaria.
- [ ] Nombre y dirección del titular y del fabricante.
- [ ] Lote y fecha de vencimiento.
- [ ] Modo de uso, dosis, advertencias y leyendas obligatorias.
- [ ] Condiciones de conservación.
- [ ] Sin afirmaciones terapéuticas ni imágenes que las sugieran.

## Frase modelo de advertencia (para validar con la norma aplicable)
> «Este producto es un suplemento dietario, no es un medicamento y no suple una alimentación equilibrada. Consérvese en lugar fresco y seco. Manténgase fuera del alcance de los niños. Consulte a su médico si está embarazada, lactando o toma medicamentos.»
> *Las leyendas obligatorias exactas dependen de la autorización y de la norma: verificar con el INVIMA y con Bio_lushows.*

## Riesgos y errores comunes
- **Alto:** vender sin autorización sanitaria vigente o con una que no corresponde al producto.
- **Alto:** claims de curar, tratar o prevenir enfermedades (en cualquier canal, incluidos distribuidores y el bot).
- **Alto:** registro a nombre de un tercero que puede retirarlo.
- **Medio:** cambiar fórmula o proveedor sin actualizar la autorización.
- **Medio:** etiqueta sin las leyendas obligatorias.

## Conexión con otros módulos
- `35` maquila · `49` influencers · `52` publicidad · `110` alimentos y bebidas · `111` suplementos · `151` producto defectuoso · `153` responsabilidad penal.
- **Bio_lushows** (estado real frente al INVIMA y claims permitidos) · **Quimico_lushows** (clasificación técnica).

## Siguiente paso típico
Con Bio_lushows, confirmar la clasificación y el estado de la autorización de cada producto BIO-SETA y auditar todos los textos publicitarios contra lo autorizado. Riesgo alto: revisión de abogado o asesor regulatorio titulado.
