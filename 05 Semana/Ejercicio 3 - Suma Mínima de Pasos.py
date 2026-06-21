# Ejercicio 3: Suma Mínima de Pasos
# Programación Dinámica
# dp[i] almacena el mínimo número de movimientos para llegar a la posición i.
# En cada movimiento el robot puede avanzar 1, 2 o 3 pasos.

# Solicitar el valor de n
n = int(input("Ingrese la posición final (n): "))

# Crear arreglo DP
dp = [0] * (n + 1)

# Inicializar con infinito
for i in range(1, n + 1):
    dp[i] = float('inf')

# Caso base
dp[0] = 0

# Construcción de la solución
for i in range(1, n + 1):

    if i - 1 >= 0:
        dp[i] = min(dp[i], dp[i - 1] + 1)

    if i - 2 >= 0:
        dp[i] = min(dp[i], dp[i - 2] + 1)

    if i - 3 >= 0:
        dp[i] = min(dp[i], dp[i - 3] + 1)

# Resultado
print(f"Cantidad mínima de movimientos para llegar a {n}: {dp[n]}")