# Buscar un número dentro de una lista

numeros = [4, 8, 15, 20, 35, 50]
buscar = 20

encontrado = False

for numero in numeros:
    if numero == buscar:
        encontrado = True
        break

if encontrado:
    print("Número encontrado")
else:
    print("Número no encontrado")
