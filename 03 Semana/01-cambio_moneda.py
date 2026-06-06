def cambio_moneda(monto, monedas):
    monedas.sort(reverse=True)
    resultado = []

    for moneda in monedas:
        while monto >= moneda:
            monto -= moneda
            resultado.append(moneda)

    return resultado

# Ejemplo de uso
monedas = [1, 2, 5, 10, 20, 50]
monto = 87

cambio = cambio_moneda(monto, monedas)

print("Monedas utilizadas:", cambio)
print("Cantidad de monedas:", len(cambio))
