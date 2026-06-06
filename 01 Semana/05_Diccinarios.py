print("=======================")
print("Diccionarios en Python") 
print("=======================")

trabajador = {
    "nombre": "Arturo Miguel",
    "edad": 35,
    "area": "estadistica",
    "sueldo": 2500,
}
print("Información del trabajador:", trabajador)



trabajador["sueldo"] = 3000 # modificar el sueldo del trabajador
print("Información del trabajador:", trabajador)


trabajador["correo"] = "arturo.miguel@empresa.com" # agregar correo

print("Información del trabajador:", trabajador)
