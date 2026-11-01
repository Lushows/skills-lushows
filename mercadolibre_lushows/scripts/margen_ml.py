#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
margen_ml.py — Margen real de una venta en Mercado Libre, y precio mínimo viable.

POR QUÉ EXISTE ESTE ARCHIVO
---------------------------
El error número uno del vendedor de Mercado Libre es calcular el margen de cabeza
restando solo "la comisión". La venta real pierde plata en CINCO lugares distintos:

    comisión por venta  +  cargo fijo  +  envío que asumes  +  IVA  +  costos propios

Este script los suma todos con aritmética decimal exacta (nada de float) y responde
las dos preguntas que importan:

    1. Si vendo a este precio, ¿cuánto me queda?      → modo `margen`
    2. ¿A cuánto tengo que vender para ganar X%?      → modo `minimo`

ADVERTENCIA QUE NO SE PUEDE IGNORAR
-----------------------------------
La COMISIÓN es un parámetro que tú debes traer, no un número que este script sepa.

Mercado Libre cambia las comisiones por país, por categoría y por tipo de publicación,
y bloquea el acceso automatizado a sus páginas de ayuda. Peor: casi todo el contenido
que circula en internet sobre "comisiones de Mercado Libre" es de Argentina o México
presentado como si fuera universal. Usar la comisión de otro país te hace calcular mal
CADA venta.

    Léela del simulador oficial de TU país, logueado en tu cuenta,
    o consúltala por la API:
        GET https://api.mercadolibre.com/sites/MCO/listing_prices?price=50000
    (MCO = Colombia · MLA = Argentina · MLM = México · MLC = Chile · MPE = Perú)

USO
---
    # ¿Cuánto me queda vendiendo a $89.900 un producto que me cuesta $42.000?
    python margen_ml.py margen --precio 89900 --costo 42000 --comision 14.5 \
        --cargo-fijo 0 --envio 0 --iva 19

    # ¿A cuánto debo vender para que me quede 25% de margen?
    python margen_ml.py minimo --costo 42000 --margen-objetivo 25 --comision 14.5 \
        --cargo-fijo 0 --envio 12000 --iva 19

    # Verificar que la aritmética del script es correcta
    python margen_ml.py test
"""

from __future__ import annotations

import argparse
import sys
from decimal import Decimal, ROUND_HALF_UP, getcontext

getcontext().prec = 28

CENTAVO = Decimal("0.01")
PESO = Decimal("1")


def d(valor) -> Decimal:
    """Convierte a Decimal pasando por str, para no heredar el error binario del float."""
    return Decimal(str(valor))


def pesos(x: Decimal) -> Decimal:
    return x.quantize(PESO, rounding=ROUND_HALF_UP)


def pct(x: Decimal) -> Decimal:
    return x.quantize(CENTAVO, rounding=ROUND_HALF_UP)


def moneda(x: Decimal, simbolo: str = "$") -> str:
    """Formato colombiano: separador de miles con punto."""
    entero = int(pesos(x))
    return f"{simbolo}{entero:,}".replace(",", ".")


# ---------------------------------------------------------------------------
# El modelo
# ---------------------------------------------------------------------------

class VentaML:
    """
    Una venta en Mercado Libre, con todos sus descuentos.

    Supuestos explícitos (cámbialos con banderas si tu caso es otro):

    * El PRECIO PUBLICADO ya incluye IVA. Así se publica en Colombia: el comprador
      ve el precio final. Si eres responsable de IVA, esa porción no es tuya —
      la recaudas para la DIAN.
    * La COMISIÓN se calcula sobre el precio publicado completo (con IVA).
      Es el comportamiento estándar de ML. Si tu caso difiere, usa --comision-sin-iva.
    * El ENVÍO es lo que TÚ asumes, ya neto del subsidio de ML. Si el comprador
      paga el envío completo, va en 0.
    """

    def __init__(
        self,
        precio: Decimal,
        costo: Decimal,
        comision_pct: Decimal,
        cargo_fijo: Decimal = Decimal(0),
        envio: Decimal = Decimal(0),
        iva_pct: Decimal = Decimal(0),
        otros: Decimal = Decimal(0),
        comision_sobre_base_sin_iva: bool = False,
    ):
        self.precio = d(precio)
        self.costo = d(costo)
        self.comision_pct = d(comision_pct)
        self.cargo_fijo = d(cargo_fijo)
        self.envio = d(envio)
        self.iva_pct = d(iva_pct)
        self.otros = d(otros)
        self.comision_sobre_base_sin_iva = comision_sobre_base_sin_iva

    # -- descomposición del precio ------------------------------------------

    @property
    def base_sin_iva(self) -> Decimal:
        """Lo que queda del precio una vez sacas el IVA que le debes a la DIAN."""
        return self.precio / (PESO + self.iva_pct / Decimal(100))

    @property
    def iva(self) -> Decimal:
        return self.precio - self.base_sin_iva

    # -- lo que se lleva Mercado Libre --------------------------------------

    @property
    def comision(self) -> Decimal:
        base = self.base_sin_iva if self.comision_sobre_base_sin_iva else self.precio
        return base * self.comision_pct / Decimal(100)

    @property
    def costo_ml_total(self) -> Decimal:
        return self.comision + self.cargo_fijo + self.envio

    # -- resultado -----------------------------------------------------------

    @property
    def ingreso_neto(self) -> Decimal:
        """Lo que efectivamente entra a tu bolsillo antes de pagar el producto."""
        return self.base_sin_iva - self.costo_ml_total - self.otros

    @property
    def utilidad(self) -> Decimal:
        return self.ingreso_neto - self.costo

    @property
    def margen_pct(self) -> Decimal:
        """Margen sobre la base sin IVA (la forma honesta de medirlo)."""
        if self.base_sin_iva == 0:
            return Decimal(0)
        return self.utilidad / self.base_sin_iva * Decimal(100)

    @property
    def markup_pct(self) -> Decimal:
        """Cuánto le montaste al costo. No confundir con margen."""
        if self.costo == 0:
            return Decimal(0)
        return self.utilidad / self.costo * Decimal(100)

    def informe(self) -> str:
        L = []
        L.append("=" * 62)
        L.append("  MARGEN REAL DE UNA VENTA EN MERCADO LIBRE")
        L.append("=" * 62)
        L.append("")
        L.append(f"  Precio publicado (con IVA)      {moneda(self.precio):>18}")
        if self.iva_pct > 0:
            L.append(f"  – IVA {pct(self.iva_pct)}% (no es tuyo)      {moneda(-self.iva):>18}")
            L.append(f"  = Base sin IVA                  {moneda(self.base_sin_iva):>18}")
        L.append("")
        L.append("  LO QUE SE LLEVA MERCADO LIBRE")
        L.append(f"  – Comisión {pct(self.comision_pct)}%              {moneda(-self.comision):>18}")
        if self.cargo_fijo > 0:
            L.append(f"  – Cargo fijo por venta          {moneda(-self.cargo_fijo):>18}")
        if self.envio > 0:
            L.append(f"  – Envío que asumes              {moneda(-self.envio):>18}")
        L.append(f"  = Subtotal Mercado Libre        {moneda(-self.costo_ml_total):>18}")
        L.append("")
        L.append("  LO TUYO")
        if self.otros > 0:
            L.append(f"  – Otros costos (empaque, etc.)  {moneda(-self.otros):>18}")
        L.append(f"  – Costo del producto            {moneda(-self.costo):>18}")
        L.append("")
        L.append("-" * 62)
        signo = "GANAS" if self.utilidad > 0 else "PIERDES"
        L.append(f"  {signo:<8}                        {moneda(self.utilidad):>18}")
        L.append(f"  Margen sobre base sin IVA       {str(pct(self.margen_pct)) + ' %':>18}")
        L.append(f"  Markup sobre el costo           {str(pct(self.markup_pct)) + ' %':>18}")
        L.append("-" * 62)
        L.append("")

        # Lectura honesta del número
        m = self.margen_pct
        if self.utilidad <= 0:
            L.append("  VEREDICTO: pierdes plata en cada venta.")
            L.append("  Vender más solo te hace perder más rápido. Sube el precio,")
            L.append("  baja el costo, o este producto no es para Mercado Libre (ver 84).")
        elif m < 10:
            L.append("  VEREDICTO: margen muy delgado (<10%).")
            L.append("  Una sola devolución se come varias ventas (ver 95). NO pautes:")
            L.append("  el ACOS mínimo de la estrategia Rentabilidad ya arranca en 5-15% (ver 150).")
        elif m < 20:
            L.append("  VEREDICTO: margen justo (10-20%).")
            L.append("  Aguanta la operación pero casi no deja espacio para publicidad.")
            L.append("  Antes de pautar, sube el ticket con un kit (ver 87).")
        elif m < 35:
            L.append("  VEREDICTO: margen sano (20-35%).")
            L.append("  Hay espacio para Mercado Ads si el ACOS se mantiene debajo del margen.")
        else:
            L.append("  VEREDICTO: margen alto (>35%).")
            L.append("  Puedes competir en precio o invertir en posición. Revisa que la")
            L.append("  comisión usada sea la real de tu categoría: un margen así sorprende.")

        L.append("")
        L.append("  Recuerda: la comisión no la sabe este script. Verifica que")
        L.append(f"  el {pct(self.comision_pct)}% sea el de TU categoría, TU país y TU tipo de publicación.")
        L.append("")
        return "\n".join(L)


def precio_minimo(
    costo: Decimal,
    margen_objetivo_pct: Decimal,
    comision_pct: Decimal,
    cargo_fijo: Decimal = Decimal(0),
    envio: Decimal = Decimal(0),
    iva_pct: Decimal = Decimal(0),
    otros: Decimal = Decimal(0),
    comision_sobre_base_sin_iva: bool = False,
) -> Decimal:
    """
    Despeja el precio publicado necesario para alcanzar un margen objetivo.

    Con la comisión sobre la base sin IVA, el álgebra es directa:
        base * (1 - c - m) = costo + fijo + envio + otros
    Con la comisión sobre el precio con IVA (el caso normal de ML), la comisión
    efectiva sobre la base se multiplica por (1 + iva), y queda:
        base * (1 - c*(1+iva) - m) = costo + fijo + envio + otros
    """
    costo = d(costo)
    m = d(margen_objetivo_pct) / Decimal(100)
    c = d(comision_pct) / Decimal(100)
    iva = d(iva_pct) / Decimal(100)
    fijos = d(cargo_fijo) + d(envio) + d(otros)

    c_efectiva = c if comision_sobre_base_sin_iva else c * (PESO + iva)
    denominador = PESO - c_efectiva - m

    if denominador <= 0:
        raise ValueError(
            f"Imposible: comisión ({pct(d(comision_pct))}%) + margen objetivo "
            f"({pct(d(margen_objetivo_pct))}%) consumen el 100% del precio. "
            "Baja el margen objetivo o cambia de categoría."
        )

    base = (costo + fijos) / denominador
    return base * (PESO + iva)


# ---------------------------------------------------------------------------
# Autoverificación
# ---------------------------------------------------------------------------

def _test() -> int:
    fallos = []

    def check(nombre, obtenido, esperado, tol=Decimal("0.02")):
        if abs(d(obtenido) - d(esperado)) > tol:
            fallos.append(f"  FALLA {nombre}: obtuve {obtenido}, esperaba {esperado}")
        else:
            print(f"  ok  {nombre}")

    print("Verificando la aritmética...\n")

    # 1. Sin IVA, sin extras: 100.000 al 10% con costo 50.000 → quedan 40.000 (40%)
    v = VentaML(precio=100000, costo=50000, comision_pct=10)
    check("caso simple, utilidad", v.utilidad, 40000)
    check("caso simple, margen", v.margen_pct, 40)

    # 2. Descomposición del IVA: 119.000 con IVA 19% → base 100.000, IVA 19.000
    v = VentaML(precio=119000, costo=0, comision_pct=0, iva_pct=19)
    check("base sin IVA", v.base_sin_iva, 100000)
    check("IVA extraído", v.iva, 19000)

    # 3. La comisión se cobra sobre el precio CON IVA por defecto
    v = VentaML(precio=119000, costo=0, comision_pct=10, iva_pct=19)
    check("comisión sobre precio con IVA", v.comision, 11900)
    v2 = VentaML(precio=119000, costo=0, comision_pct=10, iva_pct=19,
                 comision_sobre_base_sin_iva=True)
    check("comisión sobre base sin IVA", v2.comision, 10000)

    # 4. Ida y vuelta: el precio mínimo debe devolver exactamente el margen pedido
    for iva in (0, 19):
        for sobre_base in (False, True):
            p = precio_minimo(costo=42000, margen_objetivo_pct=25, comision_pct=14.5,
                              cargo_fijo=1500, envio=8000, iva_pct=iva, otros=900,
                              comision_sobre_base_sin_iva=sobre_base)
            v = VentaML(precio=p, costo=42000, comision_pct=14.5, cargo_fijo=1500,
                        envio=8000, iva_pct=iva, otros=900,
                        comision_sobre_base_sin_iva=sobre_base)
            check(f"ida y vuelta (IVA {iva}%, comisión sobre "
                  f"{'base' if sobre_base else 'precio'})", v.margen_pct, 25)

    # 5. Margen negativo detectado
    v = VentaML(precio=10000, costo=9000, comision_pct=16, cargo_fijo=1000, envio=8000)
    if v.utilidad >= 0:
        fallos.append("  FALLA no detectó la venta a pérdida")
    else:
        print("  ok  detecta venta a pérdida")

    # 6. Comisión + margen imposibles debe lanzar error, no devolver un absurdo
    try:
        precio_minimo(costo=1000, margen_objetivo_pct=90, comision_pct=20)
        fallos.append("  FALLA aceptó un margen imposible")
    except ValueError:
        print("  ok  rechaza margen imposible")

    print()
    if fallos:
        print("\n".join(fallos))
        print(f"\n{len(fallos)} prueba(s) fallaron.")
        return 1
    print("Todas las pruebas pasaron.")
    return 0


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    p = argparse.ArgumentParser(
        description="Margen real y precio mínimo viable en Mercado Libre.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="La comisión la traes tú del simulador oficial. Este script no la adivina.",
    )
    sub = p.add_subparsers(dest="modo", required=True)

    def comunes(sp):
        sp.add_argument("--costo", type=float, required=True,
                        help="Costo del producto puesto en tu bodega")
        sp.add_argument("--comision", type=float, required=True,
                        help="Comisión %% de TU categoría (del simulador oficial)")
        sp.add_argument("--cargo-fijo", type=float, default=0,
                        help="Cargo fijo por venta de bajo valor, si aplica")
        sp.add_argument("--envio", type=float, default=0,
                        help="Costo de envío que asumes tú, neto de subsidio")
        sp.add_argument("--iva", type=float, default=0,
                        help="IVA %% incluido en el precio publicado (0 si no eres responsable)")
        sp.add_argument("--otros", type=float, default=0,
                        help="Empaque, etiqueta, mano de obra por unidad")
        sp.add_argument("--comision-sin-iva", action="store_true",
                        help="Calcular la comisión sobre la base sin IVA en vez del precio total")

    m = sub.add_parser("margen", help="¿Cuánto me queda si vendo a este precio?")
    m.add_argument("--precio", type=float, required=True, help="Precio publicado, con IVA")
    comunes(m)

    n = sub.add_parser("minimo", help="¿A cuánto vender para ganar X%%?")
    n.add_argument("--margen-objetivo", type=float, required=True,
                   help="Margen %% que quieres sobre la base sin IVA")
    comunes(n)

    sub.add_parser("test", help="Verificar la aritmética del script")

    a = p.parse_args()

    if a.modo == "test":
        return _test()

    if a.modo == "margen":
        v = VentaML(precio=a.precio, costo=a.costo, comision_pct=a.comision,
                    cargo_fijo=a.cargo_fijo, envio=a.envio, iva_pct=a.iva,
                    otros=a.otros, comision_sobre_base_sin_iva=a.comision_sin_iva)
        print(v.informe())
        return 0 if v.utilidad > 0 else 2

    if a.modo == "minimo":
        try:
            precio = precio_minimo(
                costo=a.costo, margen_objetivo_pct=a.margen_objetivo,
                comision_pct=a.comision, cargo_fijo=a.cargo_fijo, envio=a.envio,
                iva_pct=a.iva, otros=a.otros,
                comision_sobre_base_sin_iva=a.comision_sin_iva,
            )
        except ValueError as e:
            print(f"\n  {e}\n", file=sys.stderr)
            return 2

        print()
        print("=" * 62)
        print("  PRECIO MÍNIMO VIABLE")
        print("=" * 62)
        print()
        print(f"  Para ganar {pct(d(a.margen_objetivo))}% sobre un costo de {moneda(d(a.costo))},")
        print(f"  tienes que publicar a:      {moneda(precio):>22}")
        print()
        print("  Por debajo de ese precio no alcanzas el margen que pediste.")
        print()
        v = VentaML(precio=precio, costo=a.costo, comision_pct=a.comision,
                    cargo_fijo=a.cargo_fijo, envio=a.envio, iva_pct=a.iva,
                    otros=a.otros, comision_sobre_base_sin_iva=a.comision_sin_iva)
        print(v.informe())
        print("  Siguiente paso: compara ese precio con el del líder de tu")
        print("  categoría (ver 70). Si te deja muy por encima, el problema no")
        print("  es el precio — es el costo o el producto (ver 84).")
        print()
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
