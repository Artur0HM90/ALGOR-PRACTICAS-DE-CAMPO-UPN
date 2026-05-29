# Contar cuántos estudiantes aprobaron (nota >= 11)
import random

print("=== MENÚ ===")
print("1. Ingresar las notas manualmente")
print("2. Usar notas aleatorias")

opcion = input("Elige una opción (1/2): ")

estudiantes = ["Ana", "Luis", "María", "Carlos", "Rosa", "Pedro", "Jorge"]
notas = []

if opcion == "1":
    print("Ingresa la nota de cada estudiante (0 al 20):")
    for estudiante in estudiantes:
        while True:
            nota = int(input("Nota de " + estudiante + ": "))
            if 0 <= nota <= 20:
                notas.append(nota)
                break
            else:
                print("Nota inválida. Debe estar entre 0 y 20.")
elif opcion == "2":
    print("Generando notas aleatorias...")
    for estudiante in estudiantes:
        nota = random.randint(0, 20)
        notas.append(nota)
        print(estudiante + ":", nota)

aprobados = 0

for i in range(len(estudiantes)):
    if notas[i] >= 11:
        aprobados = aprobados + 1
        print(estudiantes[i], "- Aprobado con", notas[i])
    else:
        print(estudiantes[i], "- Reprobado con", notas[i])

print("Cantidad de aprobados:", aprobados)
print("Cantidad de reprobados:", len(estudiantes) - aprobados)