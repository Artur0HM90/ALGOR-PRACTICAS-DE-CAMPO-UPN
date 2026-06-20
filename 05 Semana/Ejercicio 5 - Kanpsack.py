def knapsack(objetos, capacidad_max):
    n = len(objetos)

    # Tabla dp de (n+1) filas x (capacidad_max+1) columnas, inicializada en 0
    dp = [[0] * (capacidad_max + 1) for _ in range(n + 1)]

    # Construcción de la tabla dp fila por fila (objeto por objeto)
    for i in range(1, n + 1):
        nombre, peso, valor = objetos[i - 1]
        for w in range(capacidad_max + 1):
            if peso <= w:
                # Se elige el máximo entre no llevar el objeto o sí llevarlo
                dp[i][w] = max(dp[i - 1][w], valor + dp[i - 1][w - peso])
            else:
                # El objeto no entra con esta capacidad, se hereda el valor anterior
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacidad_max], dp


def reconstruir_objetos_elegidos(objetos, dp, capacidad_max):
    """
    Función auxiliar que recorre la tabla dp desde la última fila/columna
    hacia atrás para determinar qué objetos fueron seleccionados.
    """
    n = len(objetos)
    w = capacidad_max
    elegidos = []

    for i in range(n, 0, -1):
        # Si el valor cambió respecto a la fila anterior, el objeto fue elegido
        if dp[i][w] != dp[i - 1][w]:
            nombre, peso, valor = objetos[i - 1]
            elegidos.append((nombre, peso, valor))
            w -= peso  # se reduce la capacidad restante

    elegidos.reverse()
    return elegidos


# ---------------- PROGRAMA PRINCIPAL ----------------
if __name__ == "__main__":
    # Cada objeto: (nombre, peso, valor)
    objetos = [
        ("A", 2, 20),
        ("B", 3, 30),
        ("C", 5, 45),
        ("D", 7, 50),
    ]
    capacidad_mochila = 10

    print("=" * 50)
    print("EJERCICIO 5: Problema de la Mochila (Knapsack)")
    print("=" * 50)
    print("Objetos disponibles (nombre, peso, valor):")
    for obj in objetos:
        print(f"   {obj}")
    print(f"Capacidad máxima de la mochila: {capacidad_mochila} kg")

    valor_maximo, tabla_dp = knapsack(objetos, capacidad_mochila)
    seleccionados = reconstruir_objetos_elegidos(objetos, tabla_dp, capacidad_mochila)

    peso_total = sum(p for _, p, _ in seleccionados)

    print("\nTabla dp (filas=objetos acumulados, columnas=capacidad 0..10):")
    for fila in tabla_dp:
        print(fila)

    print(f"\nObjetos seleccionados: {seleccionados}")
    print(f"Peso total utilizado : {peso_total} kg de {capacidad_mochila} kg")
    print(f"Valor máximo transportable: {valor_maximo}")