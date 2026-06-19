# ============================================================
# PARTE 1: Tipos Estructurados, Registros y Cadenas 
# ============================================================
# ACTIVIDAD 1
# Diseñe una estructura de datos que permita registrar como mínimo 15 pedidos. 

pedidos = [
    {"codigo": "P001", "cliente": "Carlos Mendoza",  "ciudad": "Lima",     "peso": 2.5, "prioridad": "Alta",  "costo": 150.00},
    {"codigo": "P002", "cliente": "Ana Torres",       "ciudad": "Arequipa", "peso": 5.0, "prioridad": "Media", "costo": 220.00},
    {"codigo": "P003", "cliente": "Luis Quispe",      "ciudad": "Cusco",    "peso": 1.2, "prioridad": "Baja",  "costo": 180.00},
    {"codigo": "P004", "cliente": "Maria Flores",     "ciudad": "Trujillo", "peso": 3.8, "prioridad": "Alta",  "costo": 130.00},
    {"codigo": "P005", "cliente": "Jorge Ramirez",    "ciudad": "Piura",    "peso": 7.0, "prioridad": "Media", "costo": 310.00},
    {"codigo": "P006", "cliente": "Rosa Huanca",      "ciudad": "Chiclayo", "peso": 4.5, "prioridad": "Alta",  "costo": 275.00},
    {"codigo": "P007", "cliente": "Pedro Salas",      "ciudad": "Lima",     "peso": 0.8, "prioridad": "Baja",  "costo": 90.00},
    {"codigo": "P008", "cliente": "Elena Vargas",     "ciudad": "Arequipa", "peso": 6.2, "prioridad": "Alta",  "costo": 340.00},
    {"codigo": "P009", "cliente": "Carlos Vega",      "ciudad": "Trujillo", "peso": 2.0, "prioridad": "Baja",  "costo": 115.00},
    {"codigo": "P010", "cliente": "Lucia Paredes",    "ciudad": "Lima",     "peso": 9.5, "prioridad": "Media", "costo": 420.00},
    {"codigo": "P011", "cliente": "Manuel Chavez",    "ciudad": "Cusco",    "peso": 3.3, "prioridad": "Alta",  "costo": 195.00},
    {"codigo": "P012", "cliente": "Sandra Torres",    "ciudad": "Piura",    "peso": 1.7, "prioridad": "Baja",  "costo": 105.00},
    {"codigo": "P013", "cliente": "Roberto Quispe",   "ciudad": "Chiclayo", "peso": 8.1, "prioridad": "Media", "costo": 380.00},
    {"codigo": "P014", "cliente": "Patricia Mendoza", "ciudad": "Lima",     "peso": 4.0, "prioridad": "Alta",  "costo": 260.00},
    {"codigo": "P015", "cliente": "Andres Flores",    "ciudad": "Arequipa", "peso": 5.5, "prioridad": "Media", "costo": 290.00},
]


# Función para mostrar los pedidos de forma ordenada
def mostrar_pedidos(lista):
    print(f"{'Codigo':<8} {'Cliente':<20} {'Ciudad':<12} {'Peso':>6} {'Prioridad':<10} {'Costo':>10}")
    print("-" * 70)
    for p in lista:
        print(f"{p['codigo']:<8} {p['cliente']:<20} {p['ciudad']:<12} "
              f"{p['peso']:>6} {p['prioridad']:<10} S/.{p['costo']:>8.2f}")


if __name__ == "__main__":
    mostrar_pedidos(pedidos)

#============================================================
#c) Implemente una función que permita buscar todos los pedidos cuyo
#nombre de cliente contenga una cadena ingresada por el usuario.
#============================================================
def buscar_por_cliente(pedidos, cadena):
    """Busca todos los pedidos cuyo cliente contenga la cadena dada."""
    cadena = cadena.lower()
    resultados = []
    for pedido in pedidos:
        if cadena in pedido["cliente"].lower():
            resultados.append(pedido)
    return resultados

# Ejemplo de uso
resultados = buscar_por_cliente(pedidos, "torres")
for r in resultados:
    print(r["codigo"], "-", r["cliente"])