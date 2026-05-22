print("=======================")
print("Busqueda Lineal") 
print("=======================")

def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

# Crear lista ingresada por el usuario
lista = []

n = int(input("¿Cuántos números deseas ingresar?: "))

for i in range(n):
    num = int(input("Ingresa un número: "))
    lista.append(num)

print("Lista:", lista)

buscar = int(input("Ingresa el número a buscar: "))

resultado = busqueda_lineal(lista, buscar)

if resultado != -1:
    print("Número encontrado en la posición:", resultado)
else:
    print("El número", buscar, "no existe en la lista")