# Contar cuántos números negativos hay en una lista
import random

print("=== MENÚ ===")
print("1. Ingresar los números manualmente")
print("2. Usar números aleatorios")

opcion = input("Elige una opción (1/2): ")

numeros = []

if opcion == "1":
    print("Ingresa 8 números:")
    for i in range(8):
        numero = int(input("Ingresa un número: "))
        numeros.append(numero)
elif opcion == "2":
    print("Generando 8 números aleatorios")
    for i in range(8):
        numero = random.randint(-20, 20)
        numeros.append(numero)
    print("Números generados:", numeros)

contador = 0

for numero in numeros:
    if numero < 0:
        contador = contador + 1

print("Cantidad de negativos:", contador)