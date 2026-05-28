# Encontrar el número mayor
numeros = [15, 9, 30, 22, 18]
mayor = numeros[0]

for numero in numeros:
    if numero > mayor:
        mayor = numero

print("Número mayor:", mayor)