# Actividad 03 

import copy

# ----------------------------------------------------------
# Se genero una base de datos de 15 pedidos
# ----------------------------------------------------------
pedidos = [
    {"codigo": "P001", "cliente": "Tech Solutions SAC",    "ciudad": "Lima",      "peso": 5.0,  "prioridad": "Alta",  "costo": 250.00},
    {"codigo": "P002", "cliente": "Inversiones Norte",     "ciudad": "Trujillo",  "peso": 8.5,  "prioridad": "Media", "costo": 380.00},
    {"codigo": "P003", "cliente": "Distribuidora Sur",     "ciudad": "Arequipa",  "peso": 12.0, "prioridad": "Alta",  "costo": 520.00},
    {"codigo": "P004", "cliente": "Moda Express",          "ciudad": "Cusco",     "peso": 3.2,  "prioridad": "Baja",  "costo": 175.00},
    {"codigo": "P005", "cliente": "Importaciones Lima",    "ciudad": "Lima",      "peso": 20.0, "prioridad": "Alta",  "costo": 890.00},
    {"codigo": "P006", "cliente": "Comercial Piura",       "ciudad": "Piura",     "peso": 6.8,  "prioridad": "Media", "costo": 310.00},
    {"codigo": "P007", "cliente": "Grupo Chiclayo",        "ciudad": "Chiclayo",  "peso": 9.1,  "prioridad": "Alta",  "costo": 430.00},
    {"codigo": "P008", "cliente": "Almacenes Centro",      "ciudad": "Lima",      "peso": 4.5,  "prioridad": "Baja",  "costo": 120.00},
    {"codigo": "P009", "cliente": "Ferreterias del Norte", "ciudad": "Trujillo",  "peso": 15.0, "prioridad": "Media", "costo": 670.00},
    {"codigo": "P010", "cliente": "Textiles Arequipa",     "ciudad": "Arequipa",  "peso": 7.3,  "prioridad": "Alta",  "costo": 340.00},
    {"codigo": "P011", "cliente": "Electronica Cusco",     "ciudad": "Cusco",     "peso": 2.8,  "prioridad": "Baja",  "costo": 95.00},
    {"codigo": "P012", "cliente": "Supermercados SA",      "ciudad": "Lima",      "peso": 30.0, "prioridad": "Alta",  "costo": 1200.00},
    {"codigo": "P013", "cliente": "Distribuidora Piura",   "ciudad": "Piura",     "peso": 11.2, "prioridad": "Media", "costo": 480.00},
    {"codigo": "P014", "cliente": "Logistics Chiclayo",    "ciudad": "Chiclayo",  "peso": 5.9,  "prioridad": "Baja",  "costo": 210.00},
    {"codigo": "P015", "cliente": "Minera del Sur",        "ciudad": "Arequipa",  "peso": 18.4, "prioridad": "Alta",  "costo": 760.00},
]

# ----------------------------------------------------------
# Utilidades
# ----------------------------------------------------------
def mostrar_pedidos(lista, titulo=""):
    if titulo:
        print(f"\n{'='*60}")
        print(f"  {titulo}")
        print(f"{'='*60}")
    print(f"{'Código':<8} {'Cliente':<25} {'Ciudad':<12} {'Costo':>10}")
    print("-" * 60)
    for p in lista:
        print(f"{p['codigo']:<8} {p['cliente']:<25} {p['ciudad']:<12} S/. {p['costo']:>8.2f}")

# ----------------------------------------------------------
# 1. ORDENAMIENTO BURBUJA
# ----------------------------------------------------------
def burbuja(lista):
    datos = copy.deepcopy(lista)
    n = len(datos)
    comparaciones = 0
    intercambios = 0

    for i in range(n - 1):
        for j in range(n - 1 - i):
            comparaciones += 1
            if datos[j]["costo"] > datos[j + 1]["costo"]:
                datos[j], datos[j + 1] = datos[j + 1], datos[j]
                intercambios += 1

    return datos, comparaciones, intercambios

# ----------------------------------------------------------
# 2. ORDENAMIENTO POR SELECCIÓN
# ----------------------------------------------------------
def seleccion(lista):
    datos = copy.deepcopy(lista)
    n = len(datos)
    comparaciones = 0
    intercambios = 0

    for i in range(n - 1):
        idx_min = i
        for j in range(i + 1, n):
            comparaciones += 1
            if datos[j]["costo"] < datos[idx_min]["costo"]:
                idx_min = j
        if idx_min != i:
            datos[i], datos[idx_min] = datos[idx_min], datos[i]
            intercambios += 1

    return datos, comparaciones, intercambios

# ----------------------------------------------------------
# 3. ORDENAMIENTO POR INSERCIÓN
# ----------------------------------------------------------
def insercion(lista):
    datos = copy.deepcopy(lista)
    n = len(datos)
    comparaciones = 0
    intercambios = 0

    for i in range(1, n):
        clave = datos[i]
        j = i - 1
        while j >= 0 and datos[j]["costo"] > clave["costo"]:
            comparaciones += 1
            datos[j + 1] = datos[j]
            intercambios += 1
            j -= 1
        comparaciones += 1  # comparación que falló o llegó a 0
        datos[j + 1] = clave

    return datos, comparaciones, intercambios

# ----------------------------------------------------------
# EJECUCIÓN Y COMPARACIÓN
# ----------------------------------------------------------
print("\n" + "="*60)
print("  UPN CARGO S.A.C. - ALGORITMOS DE ORDENAMIENTO")
print("  Criterio: Costo del envío (de menor a mayor)")
print("="*60)

mostrar_pedidos(pedidos, "PEDIDOS ORIGINALES (sin ordenar)")

# Burbuja
res_b, comp_b, inter_b = burbuja(pedidos)
mostrar_pedidos(res_b, "ORDENAMIENTO BURBUJA")
print(f"\n  >> Comparaciones: {comp_b}  |  Intercambios: {inter_b}")

# Selección
res_s, comp_s, inter_s = seleccion(pedidos)
mostrar_pedidos(res_s, "ORDENAMIENTO POR SELECCIÓN")
print(f"\n  >> Comparaciones: {comp_s}  |  Intercambios: {inter_s}")

# Inserción
res_i, comp_i, inter_i = insercion(pedidos)
mostrar_pedidos(res_i, "ORDENAMIENTO POR INSERCIÓN")
print(f"\n  >> Comparaciones: {comp_i}  |  Intercambios: {inter_i}")

# ----------------------------------------------------------
# TABLA COMPARATIVA
# ----------------------------------------------------------
print("\n" + "="*60)
print("  TABLA COMPARATIVA DE RENDIMIENTO (n=15 pedidos)")
print("="*60)
print(f"{'Algoritmo':<25} {'Comparaciones':>15} {'Intercambios':>14}")
print("-" * 55)
print(f"{'Burbuja':<25} {comp_b:>15} {inter_b:>14}")
print(f"{'Selección':<25} {comp_s:>15} {inter_s:>14}")
print(f"{'Inserción':<25} {comp_i:>15} {inter_i:>14}")
print("="*60)