import tkinter as tk
from tkinter import messagebox

# Variables globales
movimientos = []
indice_movimiento = 0
torres = {}

ANCHO_CANVAS = 600
ALTO_CANVAS = 300
BASE_Y = 250
ALTURA_DISCO = 20


def generar_movimientos(n, origen, auxiliar, destino):
    """Genera la lista de movimientos usando recursividad."""
    if n == 1:
        movimientos.append((origen, destino))
    else:
        generar_movimientos(n - 1, origen, destino, auxiliar)
        movimientos.append((origen, destino))
        generar_movimientos(n - 1, auxiliar, origen, destino)


def dibujar():
    """Dibuja las torres y los discos."""
    canvas.delete("all")

    posiciones = {
        "A": 150,
        "B": 300,
        "C": 450
    }

    # Base
    canvas.create_line(
        50,
        BASE_Y + 20,
        550,
        BASE_Y + 20,
        width=3
    )

    # Torres
    for nombre, x in posiciones.items():
        canvas.create_line(
            x,
            BASE_Y,
            x,
            80,
            width=4
        )

        canvas.create_text(
            x,
            BASE_Y + 40,
            text=nombre,
            font=("Arial", 12, "bold")
        )

    # Discos
    for torre, discos in torres.items():

        x = posiciones[torre]

        for nivel, disco in enumerate(reversed(discos)):

            y = BASE_Y - (nivel + 1) * ALTURA_DISCO

            ancho = disco * 25

            canvas.create_rectangle(
                x - ancho,
                y,
                x + ancho,
                y + ALTURA_DISCO,
                fill="skyblue",
                outline="black"
            )

            canvas.create_text(
                x,
                y + ALTURA_DISCO / 2,
                text=str(disco)
            )


def ejecutar_movimiento():
    """Ejecuta los movimientos uno a uno."""

    global indice_movimiento

    if indice_movimiento >= len(movimientos):

        lbl_accion.config(text="Completado")

        messagebox.showinfo(
            "Finalizado",
            f"¡Torres de Hanoi completado!\n\n"
            f"Movimientos realizados: {len(movimientos)}\n"
            f"Movimientos esperados: {len(movimientos)}"
        )

        return

    origen, destino = movimientos[indice_movimiento]

    lbl_accion.config(
        text=f"Moviendo disco: {origen} → {destino}"
    )

    disco = torres[origen].pop()
    torres[destino].append(disco)

    dibujar()

    indice_movimiento += 1

    lbl_estado.config(
        text=f"Movimientos: {indice_movimiento} de {len(movimientos)}"
    )

    ventana.after(700, ejecutar_movimiento)


def iniciar():

    global movimientos
    global indice_movimiento
    global torres

    try:
        n = int(entry.get())

        if n <= 0:
            raise ValueError

        if n > 6:
            messagebox.showwarning(
                "Advertencia",
                "Se recomienda usar máximo 6 discos."
            )
            return

        movimientos = []
        indice_movimiento = 0

        generar_movimientos(
            n,
            "A",
            "B",
            "C"
        )

        torres = {
            "A": list(range(n, 0, -1)),
            "B": [],
            "C": []
        }

        lbl_estado.config(
            text=f"Movimientos: 0 de {len(movimientos)}"
        )

        lbl_accion.config(
            text="Iniciando..."
        )

        dibujar()

        ventana.after(
            700,
            ejecutar_movimiento
        )

    except:
        messagebox.showerror(
            "Error",
            "Ingrese un número válido."
        )


# -------------------------
# INTERFAZ
# -------------------------

ventana = tk.Tk()
ventana.title("Torres de Hanoi Animado")

tk.Label(
    ventana,
    text="Número de discos:"
).pack(pady=5)

entry = tk.Entry(
    ventana,
    width=10
)

entry.pack()

entry.insert(0, "3")

tk.Button(
    ventana,
    text="Iniciar",
    command=iniciar
).pack(pady=5)

# Estado de movimientos
lbl_estado = tk.Label(
    ventana,
    text="Movimientos: 0"
)

lbl_estado.pack()

# Acción actual
lbl_accion = tk.Label(
    ventana,
    text=""
)

lbl_accion.pack()

# Canvas para dibujar
canvas = tk.Canvas(
    ventana,
    width=ANCHO_CANVAS,
    height=ALTO_CANVAS,
    bg="white"
)

canvas.pack(
    padx=10,
    pady=10
)

ventana.mainloop()
