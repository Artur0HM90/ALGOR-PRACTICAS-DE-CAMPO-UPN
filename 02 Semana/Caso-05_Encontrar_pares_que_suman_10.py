# Encontrar pares que suman 10
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in numeros:
    for j in numeros:
        if i + j == 10:
            print(i, "+", j, "= 10")