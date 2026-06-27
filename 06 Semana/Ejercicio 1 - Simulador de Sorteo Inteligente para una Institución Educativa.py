import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import random

# ==========================================
# 1. VARIABLES GLOBALES (Listas para los datos)
# ==========================================
lista_estudiantes = []
lista_ganadores = []

# ==========================================
# 2. FUNCIONES LÓGICAS (Acciones de los botones)
# ==========================================

def registrar_estudiante():
    # Obtenemos el texto de la caja de entrada
    nombre = txt_registro.get().strip()
    
    if not nombre:
        messagebox.showwarning("Atención", "Por favor, escribe un nombre válido.")
        return
        
    if nombre in lista_estudiantes:
        messagebox.showwarning("Duplicado", "Este estudiante ya se encuentra registrado.")
        return
        
    # Guardamos en la lista
    lista_estudiantes.append(nombre)
    
    # Mostramos en la tabla visual (usamos el tamaño de la lista como número de ID)
    num_id = len(lista_estudiantes)
    tabla.insert("", "end", values=(num_id, nombre))
    
    # Limpiamos la caja de texto para el próximo ingreso
    txt_registro.delete(0, tk.END)


def realizar_sorteo():
    global lista_ganadores
    # Limpiamos los resultados anteriores en la caja de texto
    txt_resultados.delete("1.0", tk.END)
    
    # Validamos la cantidad de becas ingresada
    try:
        cant_becas = int(txt_becas.get())
    except ValueError:
        messagebox.showerror("Error de Dato", "La cantidad de becas debe ser un número entero.")
        return
        
    if cant_becas <= 0:
        messagebox.showerror("Error", "La cantidad de becas debe ser mayor a 0.")
        return
        
    if cant_becas > len(lista_estudiantes):
        messagebox.showerror("Error", f"No alcanzan los participantes. Solo hay {len(lista_estudiantes)} registrados.")
        return
        
    # --- ALGORITMO PROBABILISTA ---
    # random.sample selecciona elementos al azar de la lista SIN REPETIR (Muestreo sin reposición)
    lista_ganadores = random.sample(lista_estudiantes, cant_becas)
    
    # Cálculo estadístico simple requerido por la práctica
    probabilidad_individual = round((cant_becas / len(lista_estudiantes)) * 100, 2)
    
    # Imprimimos los resultados directamente en el cuadro de texto de la interfaz
    txt_resultados.insert(tk.END, "====== ESTADÍSTICAS DEL SORTEO ======\n")
    txt_resultados.insert(tk.END, f"Total de inscritos: {len(lista_estudiantes)}\n")
    txt_resultados.insert(tk.END, f"Probabilidad de éxito por alumno: {probabilidad_individual}%\n")
    txt_resultados.insert(tk.END, "=====================================\n\n")
    txt_resultados.insert(tk.END, "LISTA DE GANADORES:\n")
    
    for i, ganador in enumerate(lista_ganadores, 1):
        txt_resultados.insert(tk.END, f"Beca N°{i}: {ganador}\n")


def generar_reporte():
    if not lista_ganadores:
        messagebox.showwarning("Sin datos", "Primero debes realizar el sorteo para generar un reporte.")
        return
        
    # Abre la ventana interactiva de Windows para que elijas dónde guardar el archivo
    ruta_guardar = filedialog.asksaveasfilename(
        initialfile="reporte_becas_semana6.txt",
        defaultextension=".txt",
        filetypes=[("Archivos de Texto", "*.txt"), ("Todos los archivos", "*.*")],
        title="Selecciona dónde guardar el reporte"
    )
    
    # Si el usuario cierra la ventana de Windows o presiona "Cancelar", no hace nada
    if not ruta_guardar:
        return
        
    # Guardamos el archivo de texto en la ruta que elegiste (ej: tu Escritorio)
    with open(ruta_guardar, "w", encoding="utf-8") as archivo:
        archivo.write("=========================================\n")
        archivo.write("   INSTITUCIÓN EDUCATIVA - REPORTE DE BECAS\n")
        archivo.write("=========================================\n")
        for i, ganador in enumerate(lista_ganadores, 1):
            archivo.write(f"Ganador de Beca {i}: {ganador}\n")
        archivo.write("=========================================\n")
        
    messagebox.showinfo("Reporte Guardado", "El reporte se ha guardado exitosamente en la ubicación elegida.")


# ==========================================
# 3. CREACIÓN DE LA INTERFAZ GRÁFICA
# ==========================================

# Creamos la ventana principal
ventana = tk.Tk()
ventana.title("Simulador de Sorteo Inteligente")
ventana.geometry("550x550")

# --- COMPONENTE 1: Registro ---
label_titulo1 = tk.Label(ventana, text="Nombre del Estudiante:", font=("Arial", 10, "bold"))
label_titulo1.pack(pady=5)

txt_registro = tk.Entry(ventana, width=35, font=("Arial", 10))
txt_registro.pack(pady=5)

btn_registrar = tk.Button(ventana, text="Registrar Estudiante", bg="#4CAF50", fg="white", command=registrar_estudiante)
btn_registrar.pack(pady=5)

# --- COMPONENTE 2: Tabla ---
label_titulo2 = tk.Label(ventana, text="Estudiantes Inscritos:", font=("Arial", 10, "bold"))
label_titulo2.pack(pady=5)

tabla = ttk.Treeview(ventana, columns=("ID", "Nombre"), show="headings", height=6)
tabla.heading("ID", text="N°")
tabla.heading("Nombre", text="Nombre Completo")
tabla.column("ID", width=50, anchor="center")
tabla.column("Nombre", width=250)
tabla.pack(pady=5)

# --- COMPONENTE 3: Configuración del Sorteo ---
label_titulo3 = tk.Label(ventana, text="Cantidad de Becas a Sortear:", font=("Arial", 10, "bold"))
label_titulo3.pack(pady=5)

txt_becas = tk.Entry(ventana, width=10, font=("Arial", 10), justify="center")
txt_becas.pack(pady=5)
txt_becas.insert(0, "1") # Valor inicial por defecto

btn_sortear = tk.Button(ventana, text="¡Realizar Sorteo!", bg="#008CBA", fg="white", font=("Arial", 10, "bold"), command=realizar_sorteo)
btn_sortear.pack(pady=10)

# --- COMPONENTE 4: Resultados ---
label_titulo4 = tk.Label(ventana, text="Resultados y Estadísticas:", font=("Arial", 10, "bold"))
label_titulo4.pack(pady=5)

txt_resultados = tk.Text(ventana, height=6, width=55, font=("Arial", 10))
txt_resultados.pack(pady=5)

# --- COMPONENTE 5: Botón de Reporte ---
btn_reporte = tk.Button(ventana, text="Generar Reporte (.txt)", bg="#f44336", fg="white", command=generar_reporte)
btn_reporte.pack(pady=10)

# Iniciamos el bucle de la ventana gráfica
ventana.mainloop()