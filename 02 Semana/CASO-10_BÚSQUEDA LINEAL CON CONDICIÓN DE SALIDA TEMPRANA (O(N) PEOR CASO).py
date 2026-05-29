# CASO 10: BÚSQUEDA LINEAL CON CONDICIÓN DE SALIDA TEMPRANA (O(N) PEOR CASO)
# Complejidad: O(n) peor caso, Ω(1) mejor caso
def buscar_elemento(lista, objetivo):
    for i, elemento in enumerate(lista):
        print(f"  Revisando índice {i}: valor {elemento}")
        if elemento == objetivo:
            print(f"  ¡Encontrado {objetivo} en índice {i}!")
            return i
    print(f"  {objetivo} no encontrado")
    return -1

print("\n CASO 10: Búsqueda Lineal con salida temprana")
print("  Lista: [5, 8, 12, 20, 25]")
print("  Buscando: 20")
print("  Proceso:")
resultado = buscar_elemento([5, 8, 12, 20, 25], 20)
print(f"\n   Resultado final: índice {resultado}")