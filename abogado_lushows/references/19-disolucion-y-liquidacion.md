# 19 — Disolución y liquidación

Cerrar una empresa no es "dejar de usarla". Una sociedad abandonada sigue teniendo obligaciones (renovar matrícula, declarar impuestos, responder demandas) y sus administradores pueden responder por no cerrarla bien. El cierre legal tiene dos etapas: **disolución** (se decide o se produce la causa del fin) y **liquidación** (se venden activos, se pagan deudas, se reparte el remanente y se cancela la matrícula).

## Conceptos clave (en simple)
- **Disolución:** el hecho o la decisión que pone fin a la vida activa de la sociedad. Desde ahí solo puede hacer actos para liquidarse.
- **Liquidación:** el proceso de convertir activos en dinero, pagar pasivos y repartir lo que quede.
- **Liquidador:** quien dirige la liquidación (puede ser el mismo RL si así se decide).
- **Enervar la causal:** corregir la causa de disolución dentro del plazo legal para que la sociedad siga.
- **Prelación de créditos:** orden legal en que se pagan las deudas (primero las laborales y fiscales, entre otras, antes que los proveedores comunes).
- **Cuenta final de liquidación:** el informe de lo vendido, pagado y repartido; al aprobarse e inscribirse, la sociedad se extingue.
- **Liquidación judicial:** cuando la sociedad está insolvente; se tramita ante Supersociedades bajo la Ley 1116 de 2006 (`97`).

## Qué dice la norma (Colombia — verificar vigencia)
- **Ley 1258 de 2008:** causales de disolución de la SAS (vencimiento del término si lo hubiere, imposibilidad de desarrollar el objeto, iniciación de liquidación judicial, causales estatutarias, voluntad de los accionistas, orden de autoridad, y la relacionada con pérdidas o con la hipótesis de negocio en marcha según la reforma introducida por la **Ley 2069 de 2020**) y posibilidad de enervar ciertas causales dentro de los 18 meses siguientes (verificar texto vigente de los arts. 34 y 35).
- **Código de Comercio:** procedimiento de liquidación del patrimonio social (avisos a acreedores, inventario, pago de pasivos, cuenta final).
- **Ley 1727 de 2014:** sociedades que no renuevan la matrícula durante 5 años pueden quedar disueltas y en estado de liquidación por depuración del registro (verificar).
- **Ley 1116 de 2006:** liquidación judicial por insolvencia.

## Paso a paso: liquidación voluntaria privada (sociedad solvente)
1. **Asamblea** decide disolver (con la mayoría estatutaria) y nombra liquidador; acta inscrita en la cámara. Desde ahí el nombre se usa con la expresión «en liquidación».
2. **Aviso a acreedores** en los términos legales (publicación y comunicación), para que se presenten.
3. **Inventario** de activos y pasivos (con **contador_lushows**).
4. **Terminar contratos** pendientes: laborales (liquidaciones completas, `74`), arrendamientos, proveedores, con los preavisos pactados.
5. **Cobrar cartera** y vender activos.
6. **Pagar pasivos** respetando la prelación legal.
7. **Cuenta final de liquidación** y reparto del remanente a los accionistas.
8. **Aprobación** de la cuenta final por la asamblea, inscripción en la cámara y **cancelación** de la matrícula y del RUT.
9. **Conservar** los libros y documentos por el tiempo legal (`159`).

## Checklist antes de liquidar
- [ ] ¿Hay deudas que no se alcanzan a pagar? → **No** es liquidación privada: es insolvencia (`97`).
- [ ] ¿Hay trabajadores con fuero? (`77`): se requiere autorización para despedir.
- [ ] ¿Hay procesos judiciales en curso?
- [ ] ¿La marca y el software están a nombre de la SAS? Transferirlos antes (`60`, `63`).
- [ ] Declaraciones tributarias pendientes y cierre ante la DIAN (**contador_lushows**).

## Riesgos y errores comunes
- **Alto:** repartir dinero a los socios antes de pagar a todos los acreedores: el liquidador y los socios pueden responder.
- **Alto:** abandonar la sociedad sin liquidarla: siguen corriendo obligaciones y sanciones.
- **Medio:** no transferir activos intangibles (marca, dominio, software) antes de cancelar la matrícula: quedan "huérfanos".
- **Medio:** no dar el aviso a acreedores.

## Conexión con otros módulos
- `11` SAS · `16` actas · `74` terminación laboral · `97` insolvencia · `159` conservación documental.
- **contador_lushows** (balance de liquidación, impuestos de cierre) · **Matematicas_lushows** (reparto del remanente).

## Siguiente paso típico
Hacer un diagnóstico de solvencia con el contador: si los activos alcanzan para pagar todo, liquidación privada con este paso a paso; si no, ir al módulo `97` y a un abogado titulado.
