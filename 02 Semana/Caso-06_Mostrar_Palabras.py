# Mostrar solo palabras con más de 4 letras

opcion = input("¿Quieres ingresar las palabras tú mismo? (s/n): ")

palabras = []

print("Palabras con más de 4 letras seran elegidas:")

if opcion == "s":
    print("Ingresa 6 palabras:")
    for i in range(6):
        palabra = input("Ingresa una palabra: ")
        palabras.append(palabra)
else:
    print("Usando palabras predefinidas")
    palabras = ["sol", "estrella", "mar", "montaña", "volcán", "río"]

for palabra in palabras:
    if len(palabra) > 4:
        print(palabra)