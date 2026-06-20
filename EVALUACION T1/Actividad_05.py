
# Actividad 05: RUTA DE ENTREGA Y ÁRBOL DE RECUBRIMIENTO MÍNIMO

import heapq


# GRAFO


grafo = {
    "Lima":     [("Trujillo", 580), ("Chiclayo", 770), ("Arequipa", 1050)],
    "Trujillo": [("Lima", 580), ("Chiclayo", 190), ("Piura", 360)],
    "Chiclayo": [("Lima", 770), ("Trujillo", 190), ("Piura", 230)],
    "Piura":    [("Chiclayo", 230), ("Trujillo", 360)],
    "Arequipa": [("Lima", 1050), ("Cusco", 520)],
    "Cusco":    [("Arequipa", 520), ("Lima", 1180)],
}

ciudades = list(grafo.keys())


# UTILIDADES

def mostrar_grafo():
    print("\n" + "="*60)
    print("  GRAFO DE CONEXIONES - UPN CARGO S.A.C.")
    print("  (Costos en soles por ruta de distribución)")
    print("="*60)
    for ciudad, vecinos in grafo.items():
        for destino, costo in vecinos:
            if ciudad < destino:  # evitar duplicados
                print(f"  {ciudad:<12} ──── S/. {costo:>5} ────  {destino}")
    print("="*60)


# PARTE A: DIJKSTRA - Ruta más corta entre dos ciudades

def dijkstra(origen, destino):
    """Encuentra la ruta de menor costo usando el algoritmo de Dijkstra."""
    distancias = {c: float('inf') for c in grafo}
    distancias[origen] = 0
    previo = {c: None for c in grafo}
    visitados = set()

    # Cola de prioridad: (costo_acumulado, ciudad)
    cola = [(0, origen)]

    while cola:
        costo_actual, ciudad_actual = heapq.heappop(cola)

        if ciudad_actual in visitados:
            continue
        visitados.add(ciudad_actual)

        if ciudad_actual == destino:
            break

        for vecino, peso in grafo[ciudad_actual]:
            nuevo_costo = costo_actual + peso
            if nuevo_costo < distancias[vecino]:
                distancias[vecino] = nuevo_costo
                previo[vecino] = ciudad_actual
                heapq.heappush(cola, (nuevo_costo, vecino))

    # Reconstruir ruta
    ruta = []
    actual = destino
    while actual is not None:
        ruta.append(actual)
        actual = previo[actual]
    ruta.reverse()

    return ruta, distancias[destino]


# PARTE B: PRIM - Árbol de Recubrimiento Mínimo

def prim():
    """Obtiene el Árbol de Recubrimiento Mínimo con el algoritmo de Prim."""
    inicio = "Lima"
    visitados = {inicio}
    aristas_arm = []
    costo_total = 0

    # Cola de prioridad: (peso, ciudad_origen, ciudad_destino)
    cola = []
    for vecino, peso in grafo[inicio]:
        heapq.heappush(cola, (peso, inicio, vecino))

    print("\n" + "="*60)
    print("  ÁRBOL DE RECUBRIMIENTO MÍNIMO - Algoritmo de Prim")
    print(f"  Nodo inicial: {inicio}")
    print("="*60)
    print(f"  {'Paso':<6} {'Arista':<30} {'Costo':>10}")
    print("-"*50)

    paso = 1
    while cola and len(visitados) < len(grafo):
        peso, origen, destino = heapq.heappop(cola)

        if destino in visitados:
            continue

        visitados.add(destino)
        aristas_arm.append((origen, destino, peso))
        costo_total += peso

        print(f"  {paso:<6} {origen:<12} → {destino:<15}  S/. {peso:>6}")
        paso += 1

        for vecino, w in grafo[destino]:
            if vecino not in visitados:
                heapq.heappush(cola, (w, destino, vecino))

    print("-"*50)
    print(f"  {'COSTO TOTAL DEL ARM:':<36}  S/. {costo_total:>6}")
    print("="*60)

    return aristas_arm, costo_total


# EJECUCIÓN

mostrar_grafo()

# --- Parte A: Ruta Lima → Cusco ---
origen, destino = "Lima", "Cusco"
ruta, costo = dijkstra(origen, destino)
print(f"\n{'='*60}")
print(f"  PARTE A: RUTA ÓPTIMA ENTRE {origen.upper()} Y {destino.upper()}")
print(f"{'='*60}")
print(f"  Ruta encontrada: {' → '.join(ruta)}")
print(f"  Costo total:     S/. {costo}")
print(f"{'='*60}")

# Mostrar desglose por tramos
print("\n  Desglose por tramos:")
for i in range(len(ruta) - 1):
    c1, c2 = ruta[i], ruta[i+1]
    for vecino, peso in grafo[c1]:
        if vecino == c2:
            print(f"    {c1:<12} → {c2:<12}  S/. {peso}")
            break

# --- Parte B: ARM con Prim ---
arm, costo_arm = prim()

# Comparación: costo de conectar todo vs ARM
costo_todas = sum(p for c, vs in grafo.items() for _, p in vs) // 2
print(f"\n  Ahorro vs conectar todas las rutas: S/. {costo_todas - costo_arm}")
