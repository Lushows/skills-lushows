# Flex: entregar tú mismo el mismo día

Flex es la modalidad donde conservas el inventario y entregas con tu propia logística el mismo
día. La regla oficial es dura y concreta: **"completa la entrega del producto antes de las 21
hs"** (oficial ML Colombia, verificado sep-2026). Esa hora es el contrato.

## Qué es y qué no es

| Es | No es |
|---|---|
| Entrega el mismo día, antes de las 21 hs | Entrega nacional |
| Tú pones el mensajero, la moto o el carro | ML no te manda un repartidor |
| Se gestiona dentro de la app de ML | No es vender por fuera y mandar por tu cuenta |
| Señal fuerte de velocidad para el algoritmo | No reemplaza a Full en cobertura |

Flex no te saca de Mercado Envíos: te mete con un compromiso más exigente. La promesa sigue siendo
de ML y el incumplimiento sigue contando en tu reputación.

## Las 21 horas

Es el número más importante del módulo. No es "el mismo día" en abstracto: es una hora de corte.

```
□ Define tu hora de corte de pedidos hacia atrás desde las 21:00, no hacia adelante
□ Calcula: tiempo de empaque + tiempo de ruta + margen de tráfico
□ En Bogotá o Medellín a las 18:00 el tráfico te puede comer una hora entera
□ Si el pedido entra a las 19:30 y tu ruta es de 90 minutos, ya vas tarde
□ Ajusta la zona de cobertura para que el punto más lejano quepa dentro de la ventana
```

**Una zona pequeña siempre cumplida vale más que media ciudad con 12% de incumplimientos** — y ese
12% no es un número inventado: es exactamente el techo de envíos incorrectos para conservar el
verde a 60 días (oficial ML Colombia, verificado sep-2026).

## Cuándo conviene

| Situación | Veredicto |
|---|---|
| Vendes en tu ciudad y tienes cómo salir | Conviene: velocidad sin ceder inventario |
| Producto voluminoso o pesado | Conviene mucho: evitas la tarifa de peso alto (`116`) |
| Rotación media que no justifica bodegaje | Conviene: evitas `107` y el cargo de `108` |
| Vendes a todo el país | No alcanza solo: Flex cubre tu zona |
| No tienes quién salga todos los días | No conviene: el incumplimiento pesa más |
| Producto que se fabrica a pedido | No conviene: Flex promete hoy |

## El costo real de Flex

La tarifa que ML te cobra es la misma tabla de `100`. Lo que cambia es que **tú también pagas la
entrega**. El cálculo honesto por entrega:

```
costo por entrega Flex =
    combustible o pasaje
  + tiempo del mensajero (o el tuyo, valorado)
  + desgaste del vehículo
  + el costo de las entregas fallidas de la semana repartido entre las exitosas (`119`)
  − lo que ML te reconozca por el envío (GET /shipments/$SHIPMENT_ID/costs)
```

Para un producto de más de $60.000 y 1 kg con reputación verde, ML te cobra **$8.200** por el
envío (oficial, ver `100`). Si tu entrega propia te cuesta $12.000 en moto y tiempo, Flex te está
saliendo $3.800 más caro que Colecta en esa venta. Lo compensas solo si la velocidad te trae
ventas extra.

Para el cálculo exacto con tus cifras, rutea a `Matematicas_lushows`.

## Su efecto en posición

La logística es pilar del ranking y el uso de Flex es variable del desempate en catálogo (`63`).
En concreto te da:

1. Promesa de entrega corta visible, que sube conversión — y la conversión es el factor de mayor
peso en el ranking.
2. Elegibilidad en los filtros de entrega rápida.
3. Señal de logística confiable para el desempate.

Lo que **no** te da: la agrupación de carrito entre vendedores distintos, exclusiva de Full. Con
Flex, tu producto de $30.000 solo cruza el umbral de envío gratis de $60.000 si el comprador arma
carrito contigo mismo (oficial: "si vendes varios productos que juntos sumen $60.000").

## Flex y el termómetro

| Falla | Consecuencia |
|---|---|
| No entregas antes de las 21 hs | Envío incorrecto: una de las 3 variables base (`126`) |
| Marcas "entregado" sin entregar | Reclamo no excluible y riesgo para la cuenta |
| El comprador no estaba y no reprogramas | Entrega fallida, ver `119` |

Y el corte que más duele: **si no despachaste a tiempo, pierdes el derecho a que el reclamo por
demora se excluya de tu reputación** (oficial ML Colombia, verificado sep-2026). La demora ajena
es excluible; la tuya no. Ver `136`.

Recuerda además el corte de **24 horas hábiles para responder mensajes**, so pena de perder el
derecho a pedir la exclusión del reclamo (oficial).

## Qué te exige de verdad

```
□ Una zona que puedas cumplir el peor día, no el mejor
□ Días y horarios declarados que respetes, incluidos los puentes festivos
□ Revisar pedidos durante el día, no en la noche
□ Empaque listo antes de vender, no salir a comprar cinta cuando entra el pedido (`110`)
□ Confirmar la entrega en la app en el momento
□ Un plan B para el día que te enfermas
```

> ⚠️ **Sin verificar para Colombia (sep-2026).** Los requisitos formales de activación de Flex en
> MCO (ciudades habilitadas, si es por invitación, reputación mínima específica) no están
> publicados. Míralos en Panel → Ventas → Envíos → Configuración de envíos.

## El error clásico

Activar Flex con zona amplia en la primera semana. Lo correcto es al revés: la zona más chica con
demanda, 30 días limpios, y recién ahí amplías. Y hay un agravante de calendario: con menos de 60
ventas, ML te evalúa sobre los **últimos 365 días** (oficial). Un mal mes al principio te persigue
un año entero.

**Flex es la jugada del vendedor que tiene ciudad y tiene piernas. Si no tienes las dos, no la
actives.**

## Relacionados

`100` tarifas oficiales de envío · `101` modalidades · `103` Full · `105` cuándo conviene Full ·
`110` empacar sin perder plata · `112` el tiempo que prometes · `113` la demora y su costo · `114`
el flujo diario · `116` productos grandes · `119` entrega fallida · `122` logística propia · `124`
auditoría mensual · `126` las tres métricas · `136` reclamos excluibles · `63` ganar el catálogo
