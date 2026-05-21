print("=======================")
print("Busqueda Lineal") 
print("=======================")

import random

def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

# Generar lista de 10 números aleatorios
lista = random.sample(range(1, 100), 10)
print("Lista:", lista)

buscar = int(input("Ingresa el número a buscar: "))

resultado = busqueda_lineal(lista, buscar)

if resultado != -1:
    print("Número encontrado en la posición:", resultado)
else:
    print("El número", buscar, "no existe en la lista")