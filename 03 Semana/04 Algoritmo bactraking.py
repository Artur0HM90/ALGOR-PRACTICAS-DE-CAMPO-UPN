def generar_strings(letras, longitud_objetivo, cadena_actual=""):
    # Caso base: si la cadena tiene la longitud deseada, la imprimimos
    if len(cadena_actual) == longitud_objetivo:
        print(cadena_actual)
        return

    # Paso recursivo: probamos añadir cada letra posible
    for letra in letras:
        # Llamada recursiva añadiendo la letra actual
        generar_strings(letras, longitud_objetivo, cadena_actual + letra)

# Configuración del problema
letras = ['a', 'b', 'c']
longitud = 3

print(f"Combinaciones de longitud {longitud} con las letras {letras}:")
generar_strings(letras, longitud)