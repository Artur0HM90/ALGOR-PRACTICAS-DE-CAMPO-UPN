"""
DETECTOR DE FRAUDES BANCARIOS 
"""

import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import datetime
import random

# ==========================================
# 1. VARIABLES GLOBALES
# ==========================================

historial = []
sospechosas = []
contador_id = 1

# ==========================================
# 2. ALGORITMO PROBABILISTA
# ==========================================

def calcular_probabilidad(monto, hora, frecuencia, ubicacion):
    # Factor 1: Monto
    if monto > 10000:
        prob_monto = 0.9
    elif monto > 5000:
        prob_monto = 0.7
    elif monto > 1000:
        prob_monto = 0.4
    else:
        prob_monto = 0.1
    
    # Factor 2: Hora
    if hora >= 0 and hora <= 5:
        prob_hora = 0.8
    elif hora >= 22 and hora <= 23:
        prob_hora = 0.7
    elif hora >= 18 and hora <= 21:
        prob_hora = 0.5
    else:
        prob_hora = 0.2
    
    # Factor 3: Frecuencia
    if frecuencia > 20:
        prob_frecuencia = 0.9
    elif frecuencia > 10:
        prob_frecuencia = 0.6
    elif frecuencia > 5:
        prob_frecuencia = 0.3
    else:
        prob_frecuencia = 0.1
    
    # Factor 4: Ubicacion
    ubicaciones_sospechosas = ["extranjero", "desconocida", "fuera del pais"]
    if ubicacion.lower() in ubicaciones_sospechosas:
        prob_ubicacion = 0.8
    elif "otro" in ubicacion.lower():
        prob_ubicacion = 0.5
    else:
        prob_ubicacion = 0.2
    
    # Naive Bayes simplificado
    p_fraude = (prob_monto * prob_hora * prob_frecuencia * prob_ubicacion)
    p_no_fraude = ((1 - prob_monto) * (1 - prob_hora) * 
                   (1 - prob_frecuencia) * (1 - prob_ubicacion))
    
    if p_fraude + p_no_fraude == 0:
        return 0.0
    
    return round(p_fraude / (p_fraude + p_no_fraude), 4)


def clasificar_riesgo(probabilidad):
    if probabilidad >= 0.7:
        return "Alto"
    elif probabilidad >= 0.4:
        return "Medio"
    else:
        return "Bajo"

# ==========================================
# 3. FUNCIONES DE LA INTERFAZ
# ==========================================

def analizar_transaccion():
    global contador_id
    
    try:
        monto = float(txt_monto.get())
        hora = int(txt_hora.get())
        frecuencia = int(txt_frecuencia.get())
        ubicacion = txt_ubicacion.get().strip()
        descripcion = txt_descripcion.get().strip()
        
        if monto <= 0:
            messagebox.showerror("Error", "El monto debe ser mayor a 0")
            return
        if hora < 0 or hora > 23:
            messagebox.showerror("Error", "La hora debe ser entre 0 y 23")
            return
        if frecuencia < 0:
            messagebox.showerror("Error", "La frecuencia no puede ser negativa")
            return
        if not ubicacion:
            messagebox.showerror("Error", "Ingrese una ubicacion")
            return
        
        probabilidad = calcular_probabilidad(monto, hora, frecuencia, ubicacion)
        riesgo = clasificar_riesgo(probabilidad)
        
        transaccion = {
            "id": contador_id,
            "fecha": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "monto": monto,
            "hora": hora,
            "frecuencia": frecuencia,
            "ubicacion": ubicacion,
            "descripcion": descripcion,
            "probabilidad": probabilidad,
            "riesgo": riesgo
        }
        contador_id += 1
        
        historial.append(transaccion)
        
        if probabilidad >= 0.4:
            sospechosas.append(transaccion)
        
        # Mostrar en la tabla
        tabla.insert("", "end", values=(
            transaccion["id"],
            transaccion["fecha"],
            f"S/. {transaccion['monto']:.2f}",
            f"{transaccion['hora']:02d}:00",
            transaccion["riesgo"],
            f"{transaccion['probabilidad']*100:.1f}%"
        ))
        
        actualizar_indicador(probabilidad, riesgo)
        actualizar_sospechosas()
        
      #  messagebox.showinfo("Análisis Completado", 
        #    f"Transacción analizada:\nRiesgo: {riesgo}\nProbabilidad: {probabilidad*100:.2f}%")
        
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores numéricos válidos")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")


def actualizar_indicador(probabilidad, riesgo):
    label_riesgo.config(text=f"Nivel: {riesgo}")
    label_probabilidad.config(text=f"Probabilidad: {probabilidad*100:.2f}%")
    barra_riesgo['value'] = probabilidad * 100
    
    if riesgo == "Bajo":
        label_riesgo.config(fg="green")
    elif riesgo == "Medio":
        label_riesgo.config(fg="orange")
    else:
        label_riesgo.config(fg="red")


def actualizar_sospechosas():
    txt_sospechosas.delete("1.0", tk.END)
    
    if not sospechosas:
        txt_sospechosas.insert(tk.END, "No hay transacciones sospechosas.")
        return
    
    txt_sospechosas.insert(tk.END, "=== TRANSACCIONES SOSPECHOSAS ===\n")
    txt_sospechosas.insert(tk.END, "=" * 35 + "\n\n")
    
    for t in sospechosas[-5:]:
        txt_sospechosas.insert(tk.END,
            f"ID: {t['id']} | {t['fecha'][5:16]}\n"
            f"  Monto: S/. {t['monto']:.2f} | Ubicación: {t['ubicacion']}\n"
            f"  Riesgo: {t['riesgo']} | Prob: {t['probabilidad']*100:.1f}%\n"
            f"  {'-'*35}\n")


def mostrar_estadisticas():
    if not historial:
        messagebox.showinfo("Estadísticas", "No hay transacciones analizadas.")
        return
    
    # Contar niveles de riesgo
    bajo = medio = alto = 0
    for t in historial:
        if t["riesgo"] == "Bajo":
            bajo += 1
        elif t["riesgo"] == "Medio":
            medio += 1
        else:
            alto += 1
    
    total_prob = sum(t["probabilidad"] for t in historial)
    total_monto = sum(t["monto"] for t in historial)
    prom_prob = total_prob / len(historial)
    
    ventana_est = tk.Toplevel(ventana)
    ventana_est.title("Estadísticas")
    ventana_est.geometry("400x400")
    
    texto = f"""
    ==================================
       ESTADÍSTICAS DEL ANÁLISIS
    ==================================
    
    Total transacciones:    {len(historial)}
    Transacciones sospechosas: {len(sospechosas)}
    
    NIVELES DE RIESGO:
    • Bajo:  {bajo}
    • Medio: {medio}
    • Alto:  {alto}
    
    PROMEDIOS:
    • Probabilidad: {prom_prob*100:.2f}%
    • Monto total:  S/. {total_monto:,.2f}
    """
    
    txt = tk.Text(ventana_est, font=("Courier", 11), padx=20, pady=20)
    txt.insert(tk.END, texto)
    txt.config(state=tk.DISABLED)
    txt.pack(fill=tk.BOTH, expand=True)
    
    # ==========================================
    # GRÁFICO DE BARRAS 
    # ==========================================
    frame_grafico = tk.LabelFrame(ventana_est, text="Gráfico de Barras - Niveles de Riesgo", font=("Arial", 10, "bold"))
    frame_grafico.pack(fill=tk.X, padx=10, pady=10)
    
    # Canvas para dibujar
    canvas = tk.Canvas(frame_grafico, width=350, height=200, bg="white")
    canvas.pack(pady=10)
    
    # Datos para el gráfico
    datos = [bajo, medio, alto]
    colores = ["green", "orange", "red"]
    etiquetas = ["Bajo", "Medio", "Alto"]
    max_valor = max(datos) if max(datos) > 0 else 1
    
    # Dibujar barras
    ancho_barra = 60
    espacio = 30
    inicio_x = 50
    
    for i, (valor, color, etiqueta) in enumerate(zip(datos, colores, etiquetas)):
        x1 = inicio_x + i * (ancho_barra + espacio)
        y1 = 170 - (valor / max_valor) * 140  # Altura proporcional
        x2 = x1 + ancho_barra
        y2 = 170
        
        # Dibujar barra
        canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
        
        # Dibujar valor encima
        canvas.create_text(x1 + ancho_barra/2, y1 - 10, text=str(valor), font=("Arial", 10, "bold"))
        
        # Dibujar etiqueta abajo
        canvas.create_text(x1 + ancho_barra/2, 190, text=etiqueta, font=("Arial", 9))
    
    # Título
    canvas.create_text(175, 15, text="Distribución por Nivel de Riesgo", font=("Arial", 10, "bold"))
    
    tk.Button(ventana_est, text="Cerrar", command=ventana_est.destroy).pack(pady=10)


def mostrar_graficos():
    
    if not historial:
        messagebox.showinfo("Gráficos", "No hay transacciones para graficar.")
        return
    
    # Crear ventana de gráficos
    ventana_graf = tk.Toplevel(ventana)
    ventana_graf.title("Gráficos Estadísticos")
    ventana_graf.geometry("500x400")
    
    # Título
    tk.Label(ventana_graf, text="GRÁFICOS ESTADÍSTICOS", font=("Arial", 14, "bold")).pack(pady=10)
    
 
    
    # ==========================================
    # GRÁFICO 2: PROBABILIDADES INDIVIDUALES
    # ==========================================
    frame2 = tk.LabelFrame(ventana_graf, text="Probabilidad por Transacción", font=("Arial", 11, "bold"))
    frame2.pack(fill=tk.X, padx=10, pady=5)
    
    canvas2 = tk.Canvas(frame2, width=450, height=150, bg="white")
    canvas2.pack(pady=10)
    
    # Mostrar las últimas 10 transacciones
    mostrar = historial[-10:] if len(historial) > 10 else historial
    
    if mostrar:
        ancho_barra = 25
        espacio = 10
        inicio_x = 30
        
        for i, t in enumerate(mostrar):
            prob = t["probabilidad"] * 100
            x1 = inicio_x + i * (ancho_barra + espacio)
            y1 = 130 - prob * 1.2  # Escalar
            x2 = x1 + ancho_barra
            y2 = 130
            
            # Color según riesgo
            if t["riesgo"] == "Bajo":
                color = "#4CAF50"
            elif t["riesgo"] == "Medio":
                color = "#FF9800"
            else:
                color = "#f44336"
            
            canvas2.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
            canvas2.create_text(x1 + ancho_barra/2, y1 - 8, text=f"{prob:.0f}%", font=("Arial", 8))
            canvas2.create_text(x1 + ancho_barra/2, 145, text=str(t["id"]), font=("Arial", 8))
        
        canvas2.create_text(225, 10, text="Probabilidad de Fraude por Transacción", font=("Arial", 9, "bold"))
        canvas2.create_text(225, 160, text="ID de Transacción →", font=("Arial", 8))
    
    # Botón cerrar
    tk.Button(ventana_graf, text="Cerrar", font=("Arial", 10), padx=20, command=ventana_graf.destroy).pack(pady=10)


def generar_reporte():
    if not historial:
        messagebox.showwarning("Sin datos", "No hay transacciones para reportar.")
        return
    
    ruta = filedialog.asksaveasfilename(
        initialfile="reporte_fraudes.txt",
        defaultextension=".txt",
        filetypes=[("Archivos de Texto", "*.txt")],
        title="Guardar Reporte"
    )
    
    if not ruta:
        return
    
    lineas = []
    lineas.append("=" * 50)
    lineas.append("DETECTOR DE FRAUDES BANCARIOS - REPORTE")
    lineas.append("=" * 50)
    lineas.append(f"Fecha: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lineas.append("=" * 50)
    lineas.append("")
    lineas.append("TRANSACCIONES ANALIZADAS:")
    lineas.append("")
    
    for t in historial:
        lineas.append(f"ID: {t['id']}")
        lineas.append(f"  Fecha:        {t['fecha']}")
        lineas.append(f"  Monto:        S/. {t['monto']:.2f}")
        lineas.append(f"  Hora:         {t['hora']:02d}:00")
        lineas.append(f"  Frecuencia:   {t['frecuencia']}")
        lineas.append(f"  Ubicación:    {t['ubicacion']}")
        lineas.append(f"  Descripción:  {t['descripcion'] or 'N/A'}")
        lineas.append(f"  Riesgo:       {t['riesgo']}")
        lineas.append(f"  Probabilidad: {t['probabilidad']*100:.2f}%")
        lineas.append("  " + "-" * 45)
    
    lineas.append("")
    lineas.append("=" * 50)
    lineas.append("FIN DEL REPORTE")
    
    with open(ruta, 'w', encoding='utf-8') as f:
        f.write("\n".join(lineas))
    
    messagebox.showinfo("Éxito", f"Reporte guardado en:\n{ruta}")


def limpiar_historial():
    global historial, sospechosas, contador_id
    if messagebox.askyesno("Confirmar", "¿Limpiar todo el historial?"):
        historial = []
        sospechosas = []
        contador_id = 1
        
        for item in tabla.get_children():
            tabla.delete(item)
        
        txt_sospechosas.delete("1.0", tk.END)
        txt_sospechosas.insert(tk.END, "No hay transacciones sospechosas.")
        
        label_riesgo.config(text="Esperando análisis...", fg="black")
        label_probabilidad.config(text="Probabilidad: --")
        barra_riesgo['value'] = 0
        
        messagebox.showinfo("Historial", "Historial limpiado.")

# ==========================================
# 4. CREACIÓN DE LA INTERFAZ
# ==========================================

ventana = tk.Tk()
ventana.title("Detector de Fraudes Bancarios")
ventana.geometry("950x650")

# PANEL IZQUIERDO
frame_izquierdo = tk.LabelFrame(ventana, text="INGRESAR TRANSACCIÓN", font=("Arial", 12, "bold"))
frame_izquierdo.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

campos = [
    ("Monto (S/.):", "txt_monto", "5000"),
    ("Hora (0-23):", "txt_hora", "23"),
    ("Frecuencia (mov/hora):", "txt_frecuencia", "15"),
    ("Ubicación:", "txt_ubicacion", "Lima"),
    ("Descripción:", "txt_descripcion", "Transferencia")
]

entries = {}
for etiqueta, nombre, valor_defecto in campos:
    tk.Label(frame_izquierdo, text=etiqueta, font=("Arial", 10)).pack(anchor=tk.W, pady=(8, 2))
    entry = tk.Entry(frame_izquierdo, width=35, font=("Arial", 10))
    entry.insert(0, valor_defecto)
    entry.pack(fill=tk.X, pady=(0, 5))
    entries[nombre] = entry

txt_monto = entries["txt_monto"]
txt_hora = entries["txt_hora"]
txt_frecuencia = entries["txt_frecuencia"]
txt_ubicacion = entries["txt_ubicacion"]
txt_descripcion = entries["txt_descripcion"]

btn_analizar = tk.Button(frame_izquierdo, text="INGRESAR Y ANALIZAR RIESGO", 
                         font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",
                         padx=20, pady=8, command=analizar_transaccion)
btn_analizar.pack(pady=15)

frame_indicador = tk.LabelFrame(frame_izquierdo, text="INDICADOR DE RIESGO", font=("Arial", 12, "bold"))
frame_indicador.pack(fill=tk.X, pady=10)

label_riesgo = tk.Label(frame_indicador, text="Esperando análisis...", font=("Arial", 14, "bold"))
label_riesgo.pack(pady=5)

label_probabilidad = tk.Label(frame_indicador, text="Probabilidad: --", font=("Arial", 11))
label_probabilidad.pack()

barra_riesgo = ttk.Progressbar(frame_indicador, length=280, mode='determinate')
barra_riesgo.pack(pady=10)

# PANEL DERECHO
frame_derecho = tk.Frame(ventana)
frame_derecho.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

frame_historial = tk.LabelFrame(frame_derecho, text="HISTORIAL DE TRANSACCIONES", font=("Arial", 12, "bold"))
frame_historial.pack(fill=tk.BOTH, expand=True)

columnas = ("ID", "Fecha", "Monto", "Hora", "Riesgo", "Prob.")
tabla = ttk.Treeview(frame_historial, columns=columnas, show='headings', height=8)

for col in columnas:
    tabla.heading(col, text=col)
    if col == "ID":
        tabla.column(col, width=40)
    elif col == "Fecha":
        tabla.column(col, width=130)
    elif col == "Monto":
        tabla.column(col, width=90)
    elif col == "Hora":
        tabla.column(col, width=50)
    elif col == "Riesgo":
        tabla.column(col, width=70)
    elif col == "Prob.":
        tabla.column(col, width=70)

scrollbar = ttk.Scrollbar(frame_historial, orient=tk.VERTICAL, command=tabla.yview)
tabla.configure(yscrollcommand=scrollbar.set)
tabla.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

frame_botones = tk.Frame(frame_derecho)
frame_botones.pack(fill=tk.X, pady=5)

btn_estadisticas = tk.Button(frame_botones, text="Estadísticas", padx=10, command=mostrar_estadisticas)
btn_estadisticas.pack(side=tk.LEFT, padx=2)

btn_graficos = tk.Button(frame_botones, text="Gráficos", padx=10, command=mostrar_graficos)
btn_graficos.pack(side=tk.LEFT, padx=2)

btn_reporte = tk.Button(frame_botones, text="Reporte", padx=10, command=generar_reporte)
btn_reporte.pack(side=tk.LEFT, padx=2)

btn_limpiar = tk.Button(frame_botones, text="Limpiar", padx=10, command=limpiar_historial)
btn_limpiar.pack(side=tk.LEFT, padx=2)

frame_sospechosas = tk.LabelFrame(frame_derecho, text="TRANSACCIONES SOSPECHOSAS", font=("Arial", 12, "bold"))
frame_sospechosas.pack(fill=tk.BOTH, expand=True, pady=5)

txt_sospechosas = tk.Text(frame_sospechosas, height=4, font=("Arial", 9))
txt_sospechosas.pack(fill=tk.BOTH, expand=True)
txt_sospechosas.insert(tk.END, "No hay transacciones sospechosas.")

# ==========================================
# 5. INICIAR
# ==========================================

ventana.mainloop()