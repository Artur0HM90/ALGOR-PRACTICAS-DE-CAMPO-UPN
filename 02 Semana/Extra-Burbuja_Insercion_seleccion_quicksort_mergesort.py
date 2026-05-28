# Lista base (mismo conjunto de datos)
datos_originales = [64, 25, 12, 22, 11]

# -------------------------------
# MÉTODOS DE ORDENACIÓN
# -------------------------------

def burbuja(lista):
    datos = lista.copy()
    n = len(datos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if datos[j] > datos[j + 1]:
                datos[j], datos[j + 1] = datos[j + 1], datos[j]
    return datos


def insercion(lista):
    datos = lista.copy()
    for i in range(1, len(datos)):
        clave = datos[i]
        j = i - 1
        while j >= 0 and datos[j] > clave:
            datos[j + 1] = datos[j]
            j -= 1
        datos[j + 1] = clave
    return datos


def seleccion(lista):
    datos = lista.copy()
    n = len(datos)
    for i in range(n):
        minimo = i
        for j in range(i + 1, n):
            if datos[j] < datos[minimo]:
                minimo = j
        datos[i], datos[minimo] = datos[minimo], datos[i]
    return datos


def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    menores = [x for x in lista[1:] if x <= pivote]
    mayores = [x for x in lista[1:] if x > pivote]
    return quicksort(menores) + [pivote] + quicksort(mayores)


def mergesort(lista):
    if len(lista) <= 1:
        return lista

    medio = len(lista) // 2
    izquierda = mergesort(lista[:medio])
    derecha = mergesort(lista[medio:])

    return merge(izquierda, derecha)


def merge(izq, der):
    resultado = []
    i = j = 0

    while i < len(izq) and j < len(der):
        if izq[i] < der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1

    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado


# -------------------------------
# MENÚ
# -------------------------------

while True:
    print("\n--- MENÚ DE ORDENACIÓN ---")
    print("Datos originales:", datos_originales)
    print("1. Burbuja")
    print("2. Inserción")
    print("3. Selección")
    print("4. Quicksort")
    print("5. Mergesort")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("Resultado:", burbuja(datos_originales))
    elif opcion == "2":
        print("Resultado:", insercion(datos_originales))
    elif opcion == "3":
        print("Resultado:", seleccion(datos_originales))
    elif opcion == "4":
        print("Resultado:", quicksort(datos_originales))
    elif opcion == "5":
        print("Resultado:", mergesort(datos_originales))
    elif opcion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida")