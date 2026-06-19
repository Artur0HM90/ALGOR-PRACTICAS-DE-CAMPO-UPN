# ============================================================
# PARTE 6: Problema de Backtracking
# ============================================================
# ACTIVIDAD 6: Backtracking - Generación de Permutaciones de Rutas

almacenes = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8"]
soluciones = []


def backtracking_rutas(ruta_actual, disponibles):
    """
    Genera todas las permutaciones posibles de visita a los
    8 almacenes usando Backtracking.
    """
    # Caso base: ya se asignaron todos los almacenes
    if not disponibles:
        soluciones.append(ruta_actual[:])
        return

    for i in range(len(disponibles)):
        almacen = disponibles[i]

        # Elegir
        ruta_actual.append(almacen)
        nuevos_disponibles = disponibles[:i] + disponibles[i+1:]

        # Explorar
        backtracking_rutas(ruta_actual, nuevos_disponibles)

        # Deshacer (backtrack)
        ruta_actual.pop()


if __name__ == "__main__":
    backtracking_rutas([], almacenes)

    print(f"Total de rutas posibles: {len(soluciones)}")
    print("\nPrimeras 5 rutas generadas:")
    for i, ruta in enumerate(soluciones[:5], 1):
        print(f"  Ruta {i}: {' -> '.join(ruta)}")