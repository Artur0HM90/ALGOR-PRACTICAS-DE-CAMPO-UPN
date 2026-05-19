print("==================")
print("Listas en Python") 
print("==================")

numeros = []

for i in range(8):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

print(f"Los números ingresados son: {numeros}")
print(f"El primer número es: {numeros[0]}")
print(f"El último número es: {numeros[-1]}")
print(f"El número de elementos en la lista es: {len(numeros)}")