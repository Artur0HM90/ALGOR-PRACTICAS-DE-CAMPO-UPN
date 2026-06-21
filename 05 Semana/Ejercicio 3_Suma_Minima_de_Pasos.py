# Ejercicio 3: Suma Mínima de Pasos - SEMANA 5


def minimos_movimientos(n):
  
  # esta funcion recibe un numero n y nos dice
  # cuantos movimientos minimos necesita el robot para llegar ahi
  # el robot puede avanzar 1, 2 o 3 pasos cada vez
    
    # Caso base: ya estamos en la posición destino
    if n <= 0:
        return 0
    
    # Creamos la tabla DP de tamaño (n+1)
    # dp[i] = mínimo de movimientos para llegar a la posición i
    dp = [float('inf')] * (n + 1)
    
    # Casos base iniciales
    dp[0] = 0  # posición 0: 0 movimientos (punto de partida antes del paso 1)
    
    # Llenamos la tabla de forma iterativa (bottom-up)
    for i in range(1, n + 1):
        # Venimos desde i-1 (avanzamos 1 paso)
        if i - 1 >= 0:
            dp[i] = min(dp[i], dp[i - 1] + 1)
        # Venimos desde i-2 (avanzamos 2 pasos)
        if i - 2 >= 0:
            dp[i] = min(dp[i], dp[i - 2] + 1)
        # Venimos desde i-3 (avanzamos 3 pasos)
        if i - 3 >= 0:
            dp[i] = min(dp[i], dp[i - 3] + 1)
    
    return dp[n]


def mostrar_tabla_dp(n):
    """
    Muestra la tabla DP completa para visualizar el proceso.
    """
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        if i - 1 >= 0:
            dp[i] = min(dp[i], dp[i - 1] + 1)
        if i - 2 >= 0:
            dp[i] = min(dp[i], dp[i - 2] + 1)
        if i - 3 >= 0:
            dp[i] = min(dp[i], dp[i - 3] + 1)

    print("\n  Tabla DP:")
    print("  " + "-" * (n * 6 + 5))
    encabezado = "  | " + " | ".join(f"i={i:2}" for i in range(n + 1)) + " |"
    print(encabezado)
    print("  " + "-" * (n * 6 + 5))
    valores = "  | " + " | ".join(f"dp={v:1}" for v in dp) + " |"
    print(valores)
    print("  " + "-" * (n * 6 + 5))
    return dp


# PROGRAMA PRINCIPAL

print("=" * 55)
print("   EJERCICIO 3: SUMA MÍNIMA DE PASOS")
print("   Programación Dinámica - Análisis de Algoritmos")
print("=" * 55)

# Solicitar entrada al usuario
try:
    n = int(input("\n  Ingrese la posición destino n: "))
    if n <= 0:
        print("  ⚠ Por favor ingrese un número entero positivo.")
    else:
        resultado = minimos_movimientos(n)
        print(f"\n  ✔ Mínimo de movimientos para llegar a la posición {n}: {resultado}")
        
        # Mostrar tabla DP si n es manejable visualmente
        if n <= 15:
            mostrar_tabla_dp(n)
        
        # Análisis de complejidad
        print("\n  Análisis de Complejidad:")
        print(f"  - Complejidad Temporal: O(n) → un solo recorrido de 1 a {n}")
        print(f"  - Complejidad Espacial: O(n) → tabla dp de tamaño {n + 1}")

except ValueError:
    print("  ⚠ Entrada inválida. Debe ingresar un número entero.")

print("\n" + "=" * 55)