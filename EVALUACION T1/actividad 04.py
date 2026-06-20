"""
Actividad 4 - Algoritmo Voraz (Greedy)
Caso: UPN Cargo S.A.C. - Entrega de viáticos a conductores

Denominaciones disponibles: S/. 200, 100, 50, 20, 10
"""

def calcular_cambio_voraz(monto, billetes=(200, 100, 50, 20, 10)):
    """
    Determina la menor cantidad de billetes necesarios para entregar 'monto'
    aplicando una estrategia voraz (greedy).

    Estrategia: en cada paso se elige el billete de mayor valor posible
    que no exceda el monto restante (elección localmente óptima),
    y se repite hasta agotar el monto.
    """
    billetes_ordenados = sorted(billetes, reverse=True)
    detalle = {}
    restante = monto

    for billete in billetes_ordenados:
        if restante <= 0:
            break
        cantidad = restante // billete
        if cantidad > 0:
            detalle[billete] = cantidad
            restante -= cantidad * billete

    total_billetes = sum(detalle.values())
    return detalle, total_billetes, restante


def mostrar_resultado(monto):
    detalle, total, restante = calcular_cambio_voraz(monto)
    print(f"\nMonto a entregar: S/. {monto}")
    print("-" * 38)
    for billete in sorted(detalle.keys(), reverse=True):
        print(f"  Billete S/. {billete:>3}  x {detalle[billete]}")
    print("-" * 38)
    print(f"Total de billetes utilizados: {total}")
    if restante > 0:
        print(f"Monto no cubierto exactamente: S/. {restante}")


if __name__ == "__main__":
    montos_a_entregar = [380, 670, 920]

    print("=" * 38)
    print(" SISTEMA DE VIÁTICOS - UPN CARGO S.A.C.")
    print("=" * 38)

    for monto in montos_a_entregar:
        mostrar_resultado(monto)
