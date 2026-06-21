
# Ejercicio 4: Máxima Suma sin Elementos Consecutivos - SEMANA 5


def maxima_suma(arreglo):
    # esta funcion recibe una lista de numeros
    # y nos devuelve la mayor suma posible
    # pero sin agarrar dos numeros que esten uno al lado del otro

    n = len(arreglo)

    # si la lista esta vacia no hay nada que sumar
    if n == 0:
        return 0

    # si solo hay un numero, ese es el maximo
    if n == 1:
        return arreglo[0]

    # creamos una tabla donde guardaremos la mejor suma hasta cada posicion
    dp = [0] * n

    # en la posicion 0 solo podemos elegir el primer numero
    dp[0] = arreglo[0]

    # en la posicion 1 elegimos el mayor entre el primero y el segundo
    dp[1] = max(arreglo[0], arreglo[1])

    # a partir de la posicion 2 comparamos dos opciones:
    # opcion A: no agarramos el numero actual, nos quedamos con lo mejor anterior
    # opcion B: agarramos el numero actual mas lo mejor de dos posiciones atras
    for i in range(2, n):
        opcion_a = dp[i - 1]                    # no tomamos arreglo[i]
        opcion_b = dp[i - 2] + arreglo[i]       # tomamos arreglo[i] + mejor de i-2

        dp[i] = max(opcion_a, opcion_b)

    return dp[n - 1]

# PROGRAMA PRINCIPAL

print("=" * 50)
print("  EJERCICIO 4: MÁXIMA SUMA SIN CONSECUTIVOS")
print("  Programación Dinámica - Análisis de Algoritmos")
print("=" * 50)

# arreglo del enunciado
arreglo = [3, 2, 7, 10]

print(f"\n  Arreglo dado: {arreglo}")
print(f"  Índices:       {list(range(len(arreglo)))}")

# mostramos la tabla dp paso a paso
print("\n  Construyendo tabla DP paso a paso:")
print("  " + "-" * 40)

n = len(arreglo)
dp = [0] * n
dp[0] = arreglo[0]
dp[1] = max(arreglo[0], arreglo[1])

print(f"  dp[0] = {arreglo[0]}  → solo hay un elemento")
print(f"  dp[1] = max({arreglo[0]}, {arreglo[1]}) = {dp[1]}  → elegimos el mayor entre los dos primeros")

for i in range(2, n):
    opcion_a = dp[i - 1]
    opcion_b = dp[i - 2] + arreglo[i]
    dp[i] = max(opcion_a, opcion_b)
    print(f"  dp[{i}] = max({opcion_a}, {dp[i-2]}+{arreglo[i]}) = max({opcion_a}, {opcion_b}) = {dp[i]}")

print("  " + "-" * 40)
print(f"\n  Tabla DP final: {dp}")
print(f"\n  ✔ Máxima suma sin consecutivos: {dp[n - 1]}")
print(f"  ✔ Elementos elegidos: 3 + 10 = 13  (índices 0 y 3)")

print("\n  Análisis de Complejidad:")
print("  - Complejidad Temporal: O(n)")
print("  - Complejidad Espacial: O(n)")
print("=" * 50)