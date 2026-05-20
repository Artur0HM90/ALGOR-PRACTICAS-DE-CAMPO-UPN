contrasena_objetivo = input("Ingrese la contraseña numérica de 3 dígitos (ej. 123): ")

intentos = 0
encontrada = False

# Iteramos desde 000 hasta 999
# Usamos f-string con :03d para asegurar que el número tenga siempre 3 dígitos
for i in range(1000):
    intento_actual = f"{i:03d}"
    intentos += 1
    
    print(f"Probando: {intento_actual}")
    
    if intento_actual == contrasena_objetivo:
        print(f"\n¡Contraseña encontrada! Es: {intento_actual}")
        encontrada = True
        break

print(f"Total de intentos realizados: {intentos}")