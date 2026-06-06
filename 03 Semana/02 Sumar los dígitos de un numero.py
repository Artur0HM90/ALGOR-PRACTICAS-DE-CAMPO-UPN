# Función recursiva para sumar los dígitos de un número

def suma_digitos(numero):

    # Caso base: si el número tiene un solo dígito
    if numero < 10:
        return numero

    # Caso recursivo:
    # Se suma el último dígito con la suma de los demás dígitos
    return (numero % 10) + suma_digitos(numero // 10)


# Ejemplo de uso
numero = 1234

resultado = suma_digitos(numero)

print("Número:", numero)
print("Suma de dígitos:", resultado)
