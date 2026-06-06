# Función recursiva para contar ocurrencias

def contar_ocurrencias(lista, elemento):

    # Caso base: lista vacía
    if len(lista) == 0:
        return 0

    # Si el primer elemento coincide
    if lista[0] == elemento:
        return 1 + contar_ocurrencias(lista[1:], elemento)

    # Si no coincide
    return contar_ocurrencias(lista[1:], elemento)


# Datos de entrada
lista = [1, 2, 3, 2, 2, 4]
x = 2

resultado = contar_ocurrencias(lista, x)

print("Lista:", lista)
print("Elemento buscado:", x)
print("Cantidad de ocurrencias:", resultado)