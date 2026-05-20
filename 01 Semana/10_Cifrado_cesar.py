def descifrar_cesar(mensaje_cifrado):
    # Iteramos a través de las 26 claves posibles (0 a 25)
    for clave in range(26):
        mensaje_decodificado = ""
        
        for caracter in mensaje_cifrado:
            if caracter.isalpha():
                # Determinamos si es mayúscula o minúscula para mantener el formato
                inicio = ord('A') if caracter.isupper() else ord('a')
                
                # Aplicamos el desplazamiento inverso: (posicion_actual - clave) % 26
                # Usamos el módulo para que el alfabeto sea circular
                nuevo_caracter = chr((ord(caracter) - inicio - clave) % 26 + inicio)
                mensaje_decodificado += nuevo_caracter
            else:
                # Si no es una letra (espacios, números), se mantiene igual
                mensaje_decodificado += caracter
        
        print(f"Clave {clave:02d}: {mensaje_decodificado}")

# Ejemplo de uso:
mensaje = input("Ingrese el mensaje cifrado: ")
print("\n--- Resultados de Fuerza Bruta ---")
descifrar_cesar(mensaje)