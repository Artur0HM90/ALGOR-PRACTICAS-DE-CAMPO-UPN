def encontrar_mayor(lista):
    if not lista:
        return "La lista está vacía"
    
    # 1. Asumimos que el primer elemento es el mayor inicialmente
    mayor = lista[0]
    print(f"Iniciamos asumiendo que el mayor es: {mayor}")
    
    # 2. Iteramos a través de la lista comparando
    for i in range(1, len(lista)):
        numero_actual = lista[i]
        
        # 3. Comparación manual
        if numero_actual > mayor:
            print(f"Comparando {numero_actual} > {mayor}: Sí, actualizamos el mayor a {numero_actual}")
            mayor = numero_actual
        else:
            print(f"Comparando {numero_actual} > {mayor}: No, mantenemos {mayor}")
            
    return mayor

# Ejemplo de uso:
mi_lista = [3, 7, 2, 9, 5]
resultado = encontrar_mayor(mi_lista)
print(f"\nEl número mayor de la lista es: {resultado}")