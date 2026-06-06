# Función recursiva para sumar los dígitos

def suma_digitos(numero):

    # Caso base
    if numero < 10:
        return numero

    # Caso recursivo
    return (numero % 10) + suma_digitos(numero // 10)


# Ingreso de datos por consola
numero = int(input("Ingrese un número: "))

resultado = suma_digitos(numero)

print("La suma de los dígitos es:", resultado)