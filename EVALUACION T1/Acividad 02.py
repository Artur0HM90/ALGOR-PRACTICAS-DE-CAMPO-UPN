
# ============================================================
# ACTIVIDAD 2: ALGORITMOS DE BÚSQUEDA
# ============================================================

# ============================================================
# 1. DATOS DE EJEMPLO (15 PEDIDOS)
# ============================================================

pedidos = [
    {"codigo": "P001", "cliente": "Luis Perez", "ciudad": "Lima", "peso": 2.5, "prioridad": "Alta", "costo": 150.00},
    {"codigo": "P002", "cliente": "Maria Gomez", "ciudad": "Arequipa", "peso": 1.8, "prioridad": "Media", "costo": 120.00},
    {"codigo": "P003", "cliente": "Carlos Ruiz", "ciudad": "Cusco", "peso": 3.2, "prioridad": "Baja", "costo": 200.00},
    {"codigo": "P004", "cliente": "Ana Torres", "ciudad": "Trujillo", "peso": 4.0, "prioridad": "Alta", "costo": 250.00},
    {"codigo": "P005", "cliente": "Pedro Diaz", "ciudad": "Piura", "peso": 1.5, "prioridad": "Media", "costo": 90.00},
    {"codigo": "P006", "cliente": "Laura Sanchez", "ciudad": "Chiclayo", "peso": 2.0, "prioridad": "Alta", "costo": 180.00},
    {"codigo": "P007", "cliente": "Jorge Castro", "ciudad": "Lima", "peso": 3.8, "prioridad": "Baja", "costo": 220.00},
    {"codigo": "P008", "cliente": "Sofia Mendoza", "ciudad": "Arequipa", "peso": 2.2, "prioridad": "Media", "costo": 130.00},
    {"codigo": "P009", "cliente": "Diego Flores", "ciudad": "Cusco", "peso": 5.0, "prioridad": "Alta", "costo": 300.00},
    {"codigo": "P010", "cliente": "Valentina Rios", "ciudad": "Trujillo", "peso": 1.2, "prioridad": "Media", "costo": 75.00},
    {"codigo": "P011", "cliente": "Andres Vega", "ciudad": "Piura", "peso": 2.8, "prioridad": "Baja", "costo": 160.00},
    {"codigo": "P012", "cliente": "Camila Soto", "ciudad": "Chiclayo", "peso": 3.0, "prioridad": "Alta", "costo": 210.00},
    {"codigo": "P013", "cliente": "Roberto Nunez", "ciudad": "Lima", "peso": 1.7, "prioridad": "Media", "costo": 110.00},
    {"codigo": "P014", "cliente": "Daniela Paredes", "ciudad": "Arequipa", "peso": 4.5, "prioridad": "Alta", "costo": 280.00},
    {"codigo": "P015", "cliente": "Fernando Cruz", "ciudad": "Cusco", "peso": 2.3, "prioridad": "Baja", "costo": 140.00}
]

# ============================================================
# 2. ALGORITMO 1: BÚSQUEDA LINEAL
# ============================================================

def busqueda_lineal(lista, codigo):
    comparaciones = 0
    for pedido in lista:
        comparaciones += 1
        if pedido["codigo"] == codigo:
            return pedido, comparaciones
    return None, comparaciones

# ============================================================
# 3. ALGORITMO 2: BÚSQUEDA LINEAL ACOTADA
# ============================================================

def busqueda_lineal_acotada(lista, codigo):
    comparaciones = 0
    lista_temp = lista.copy()
    centinela = {"codigo": codigo}
    lista_temp.append(centinela)

    i = 0
    while lista_temp[i]["codigo"] != codigo:
        comparaciones += 1
        i += 1

    comparaciones += 1  # Contamos la comparación con el centinela

    if i == len(lista_temp) - 1:
        return None, comparaciones
    return lista_temp[i], comparaciones

# ============================================================
# 4. FUNCIÓN PARA ORDENAR (NECESARIA PARA BÚSQUEDA BINARIA)
# ============================================================

def ordenar_por_codigo(lista):
    return sorted(lista, key=lambda x: x["codigo"])

# ============================================================
# 5. ALGORITMO 3: BÚSQUEDA BINARIA ITERATIVA
# ============================================================

def busqueda_binaria_iterativa(lista, codigo):
    comparaciones = 0
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        comparaciones += 1
        medio = (izquierda + derecha) // 2

        if lista[medio]["codigo"] == codigo:
            return lista[medio], comparaciones
        elif lista[medio]["codigo"] < codigo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return None, comparaciones

# ============================================================
# 6. ALGORITMO 4: BÚSQUEDA BINARIA RECURSIVA
# ============================================================

def busqueda_binaria_recursiva(lista, codigo, izquierda=0, derecha=None):
    if derecha is None:
        derecha = len(lista) - 1

    def recursiva(izq, der, contador):
        if izq > der:
            return None, contador

        contador += 1
        medio = (izq + der) // 2

        if lista[medio]["codigo"] == codigo:
            return lista[medio], contador
        elif lista[medio]["codigo"] > codigo:
            return recursiva(izq, medio - 1, contador)
        else:
            return recursiva(medio + 1, der, contador)

    return recursiva(izquierda, derecha, 0)

# ============================================================
# 7. FUNCIÓN PARA PROBAR Y COMPARAR
# ============================================================

def comparar_algoritmos():
    print("=" * 70)
    print("          COMPARACIÓN DE ALGORITMOS DE BÚSQUEDA")
    print("=" * 70)
    print(f"Total de pedidos: {len(pedidos)}")
    print("=" * 70)

    pedidos_ordenados = ordenar_por_codigo(pedidos)
    codigos_prueba = ["P005", "P015", "P999"]

    for codigo in codigos_prueba:
        print(f"\n Buscando código: {codigo}")
        print("-" * 50)

        # Búsqueda Lineal
        resultado, comps = busqueda_lineal(pedidos, codigo)
        if resultado:
            print(f"- Lineal simple:     {resultado['cliente']} (comparaciones: {comps})")
        else:
            print(f"- Lineal simple:     No encontrado (comparaciones: {comps})")

        # Búsqueda Lineal Acotada
        resultado, comps = busqueda_lineal_acotada(pedidos, codigo)
        if resultado:
            print(f"- Lineal acotada:    {resultado['cliente']} (comparaciones: {comps})")
        else:
            print(f"- Lineal acotada:    No encontrado (comparaciones: {comps})")

        # Búsqueda Binaria Iterativa
        resultado, comps = busqueda_binaria_iterativa(pedidos_ordenados, codigo)
        if resultado:
            print(f"- Binaria iterativa: {resultado['cliente']} (comparaciones: {comps})")
        else:
            print(f"- Binaria iterativa: No encontrado (comparaciones: {comps})")

        # Búsqueda Binaria Recursiva
        resultado, comps = busqueda_binaria_recursiva(pedidos_ordenados, codigo)
        if resultado:
            print(f"- Binaria recursiva: {resultado['cliente']} (comparaciones: {comps})")
        else:
            print(f"- Binaria recursiva: No encontrado (comparaciones: {comps})")

# ============================================================
# 8. ANÁLISIS DE EFICIENCIA
# ============================================================

def analizar_eficiencia():
    print("\n" + "=" * 70)
    print("          ANÁLISIS DE EFICIENCIA")
    print("=" * 70)

    pedidos_ordenados = ordenar_por_codigo(pedidos)
    codigo = "P999"  # Código que no existe (peor caso)

    print(f"\n Buscando código: {codigo} (NO EXISTE)")
    print("-" * 50)

    # 1. Búsqueda Lineal
    _, comps_lineal = busqueda_lineal(pedidos, codigo)
    print(f"1. Búsqueda Lineal:        {comps_lineal} comparaciones")

    # 2. Búsqueda Lineal Acotada
    _, comps_acotada = busqueda_lineal_acotada(pedidos, codigo)
    print(f"2. Búsqueda Lineal Acotada: {comps_acotada} comparaciones")

    # 3. Búsqueda Binaria Iterativa
    _, comps_binaria = busqueda_binaria_iterativa(pedidos_ordenados, codigo)
    print(f"3. Búsqueda Binaria Iterativa: {comps_binaria} comparaciones")

    # 4. Búsqueda Binaria Recursiva
    _, comps_recursiva = busqueda_binaria_recursiva(pedidos_ordenados, codigo)
    print(f"4. Búsqueda Binaria Recursiva: {comps_recursiva} comparaciones")

    print("\n" + "=" * 70)
    print("          RESUMEN DE COMPARACIONES")
    print("=" * 70)
    print("\nAlgoritmo                 | Comparaciones | Complejidad")
    print("-" * 60)
    print(f"Lineal Simple           | {comps_lineal:>12} | O(n)")
    print(f"Lineal Acotada          | {comps_acotada:>12} | O(n)")
    print(f"Binaria Iterativa       | {comps_binaria:>12} | O(log n)")
    print(f"Binaria Recursiva       | {comps_recursiva:>12} | O(log n)")
    print("=" * 70)

    factor = comps_lineal / comps_binaria
    print(f"\n La búsqueda binaria es {factor:.1f} veces más rápida que la lineal")

# ============================================================
# 9. COMPLEJIDAD TEMPORAL
# ============================================================

def mostrar_complejidad():
    print("\n" + "=" * 70)
  
    print("\n ¿Qué significa O(log n)?")
    print("-" * 60)
    print("Cada vez que duplicas los datos, el tiempo solo aumenta en 1 paso.")
    print("\nEjemplo con 10,000 pedidos:")
    print("• Búsqueda Lineal:  10,000 comparaciones")
    print("• Búsqueda Binaria: ~14 comparaciones")
    print("\n La binaria es 714 veces más rápida")

# ============================================================
# 10. EJECUCIÓN PRINCIPAL
# ============================================================

if __name__ == "__main__":
    comparar_algoritmos()
    analizar_eficiencia()
    mostrar_complejidad()