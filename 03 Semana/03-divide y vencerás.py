def encontrar_max_min_dyv(lista, inicio, fin, contador):

    # --- CASO BASE 1: un solo elemento ---
    # No hay comparaciones, el elemento es a la vez máximo y mínimo.
    if inicio == fin:
        return lista[inicio], lista[inicio]

    # --- CASO BASE 2: dos elementos ---
    # Basta una sola comparación para saber cuál es mayor.
    if fin - inicio == 1:
        contador[0] += 1
        if lista[inicio] < lista[fin]:
            return lista[fin], lista[inicio]   # (max, min)
        else:
            return lista[inicio], lista[fin]

    # --- DIVIDIR ---
    medio = (inicio + fin) // 2

    # --- VENCER (recursión sobre cada mitad) ---
    max_izq, min_izq = encontrar_max_min_dyv(lista, inicio, medio, contador)
    max_der, min_der = encontrar_max_min_dyv(lista, medio + 1, fin, contador)

    # --- COMBINAR ---
    # Solo 2 comparaciones para unir los resultados de ambas mitades.
    contador[0] += 2
    maximo = max_izq if max_izq > max_der else max_der
    minimo = min_izq if min_izq < min_der else min_der

    return maximo, minimo


def encontrar_max_min_iterativo(lista):

    contador = 0
    maximo = lista[0]
    minimo = lista[0]

    for i in range(1, len(lista)):
        contador += 1
        if lista[i] > maximo:
            maximo = lista[i]
        else:
            contador += 1
            if lista[i] < minimo:
                minimo = lista[i]

    return maximo, minimo, contador


# =============================================================
# PROGRAMA PRINCIPAL
# =============================================================
if __name__ == "__main__":
    lista = [3, 5, 1, 2, 8, 9, 4]
    n = len(lista)

    print("=" * 55)
    print(f"ENTRADA: {lista}")
    print("=" * 55)

    # ---------- Divide y Vencerás ----------
    contador_dyv = [0]   # lista de un elemento para pasar por referencia
    maximo, minimo = encontrar_max_min_dyv(lista, 0, n - 1, contador_dyv)

    print("\n>>> ENFOQUE DIVIDE Y VENCERÁS")
    print(f"   Máximo: {maximo}")
    print(f"   Mínimo: {minimo}")
    print(f"   Comparaciones realizadas: {contador_dyv[0]}")

    # ---------- Iterativo ----------
    max_it, min_it, comp_it = encontrar_max_min_iterativo(lista)

    print("\n>>> ENFOQUE ITERATIVO (referencia)")
    print(f"   Máximo: {max_it}")
    print(f"   Mínimo: {min_it}")
    print(f"   Comparaciones realizadas: {comp_it}")

    # ---------- Análisis de complejidad ----------
    print("\n" + "=" * 55)
    print("ANÁLISIS DE COMPLEJIDAD")
    print("=" * 55)
    print(f"Tamaño de la lista (n) = {n}")
    print(f"Iterativo  -> peor caso 2(n-1) = {2 * (n - 1)} comparaciones")
    print(f"D y V      -> aprox. 3n/2 - 2 = {(3 * n) // 2 - 2} comparaciones")
    print("\nRelación de recurrencia:")
    print("   T(n) = 2·T(n/2) + 2,   T(2) = 1,   T(1) = 0")
    print("Complejidad temporal: O(n)")
    print("Complejidad espacial: O(log n)  (pila de recursión)")