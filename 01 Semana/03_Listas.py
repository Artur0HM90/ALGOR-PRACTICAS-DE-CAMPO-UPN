print("==================")
print("Listas en Python") 
print("==================")

numeros = []

for i in range(8):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

print(f"Los números ingresados son: {numeros}")
print(f"El número mayor es: {max(numeros)}")
print(f"El numero menor es: {min(numeros)}")
print(f"La suma de los números es: {sum(numeros)}")