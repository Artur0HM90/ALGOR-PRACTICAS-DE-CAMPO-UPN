import tkinter as tk
from tkinter import ttk, messagebox
import time

# Movimientos del caballo
mov_x = [1, 2, 2, 1, -1, -2, -2, -1]
mov_y = [2, 1, -1, -2, -2, -1, 1, 2]

N = 5
tablero = []
botones = []


def es_valido(x, y):
    return (
        0 <= x < N and
        0 <= y < N and
        tablero[x][y] == -1
    )


# Backtracking
def resolver_caballo(x, y, paso):

    if paso == N * N:
        return True

    for i in range(8):

        nx = x + mov_x[i]
        ny = y + mov_y[i]

        if es_valido(nx, ny):

            tablero[nx][ny] = paso

            if resolver_caballo(nx, ny, paso + 1):
                return True

            # Retroceder
            tablero[nx][ny] = -1

    return False


def actualizar_tablero():

    for i in range(N):
        for j in range(N):

            valor = tablero[i][j]

            if valor == -1:
                botones[i][j].config(text="")
            else:
                botones[i][j].config(text=str(valor))


def resolver():

    global tablero

    tablero = [[-1 for _ in range(N)] for _ in range(N)]

    tablero[0][0] = 0

    ventana.config(cursor="watch")
    ventana.update()

    inicio = time.time()

    encontrado = resolver_caballo(0, 0, 1)

    fin = time.time()

    ventana.config(cursor="")

    if encontrado:

        actualizar_tablero()

        tiempo = fin - inicio

        lbl_tiempo.config(
            text=f"Tiempo: {tiempo:.2f} segundos"
        )

        messagebox.showinfo(
            "Resultado",
            "¡Se encontró una solución!"
        )

    else:

        messagebox.showwarning(
            "Resultado",
            "No se encontró solución."
        )


def crear_tablero():

    global N, botones, tablero

    N = int(combo.get())

    for widget in frame.winfo_children():
        widget.destroy()

    botones = []

    tablero = [[-1 for _ in range(N)] for _ in range(N)]

    for i in range(N):

        fila = []

        for j in range(N):

            color = "white" if (i + j) % 2 == 0 else "lightgray"

            btn = tk.Button(
                frame,
                width=4,
                height=2,
                bg=color,
                text=""
            )

            btn.grid(row=i, column=j)

            fila.append(btn)

        botones.append(fila)

    lbl_tiempo.config(text="")


# ------------------------
# INTERFAZ
# ------------------------

ventana = tk.Tk()
ventana.title("Salto del Caballo - Backtracking")

top = tk.Frame(ventana)
top.pack(pady=10)

tk.Label(
    top,
    text="Tamaño del tablero:"
).pack(side=tk.LEFT)

combo = ttk.Combobox(
    top,
    values=[5, 6, 7, 8],
    width=5,
    state="readonly"
)

combo.set(5)
combo.pack(side=tk.LEFT, padx=5)

tk.Button(
    top,
    text="Crear tablero",
    command=crear_tablero
).pack(side=tk.LEFT)

tk.Button(
    top,
    text="Resolver",
    command=resolver
).pack(side=tk.LEFT, padx=5)

frame = tk.Frame(ventana)
frame.pack(pady=10)

lbl_tiempo = tk.Label(
    ventana,
    text=""
)

lbl_tiempo.pack()

crear_tablero()

ventana.mainloop()
