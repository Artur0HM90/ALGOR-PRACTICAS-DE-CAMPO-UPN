# CASO 09: BUCLES ANIDADOS (O(n²))
# Complejidad: O(n²) - n * n iteraciones
def generar_pares(lista):
    pares = []
    for i in range(len(lista)):          # Bucle externo: n veces
        for j in range(len(lista)):      # Bucle interno: n veces por cada i
            if i != j:                   # Condicional O(1)
                pares.append((lista[i], lista[j]))
    return pares


print(" CASO 09: Bucles Anidados - O(n²)")
print(" Lista de entrada: [1, 2, 3]")
print(" Bucle externo: 3 vueltas (i = 0, 1, 2)")
print(" Bucle interno: 3 vueltas por cada i")
print(" Total iteraciones: 3 × 3 = 9")
print(" Generando todos los pares donde i ≠ j...")
resultado = generar_pares([1, 2, 3])
print(f" Resultado: {resultado}")
print()
