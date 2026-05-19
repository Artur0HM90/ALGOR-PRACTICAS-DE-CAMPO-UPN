print("===========================")
print("Calcular promedio de notas") 
print("===========================")


nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))   
nota4 = float(input("Ingrese la cuarta nota: "))   

promedio = (nota1 + nota2 + nota3 + nota4) / 4


if promedio >= 11:
    print(f"¡Felicidades! Has aprobado con un promedio de {promedio}.")
else:
    print(f"No has aprobado. Tu promedio es de {promedio}.")
