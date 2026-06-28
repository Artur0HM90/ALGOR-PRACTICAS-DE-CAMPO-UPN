import tkinter as tk
from tkinter import ttk, messagebox
import random
import math
import threading

class MonteCarloPi:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador Monte Carlo – Estimación de π")
        self.root.configure(bg="#1e1e2e")
        self.root.resizable(False, False)

        self._build_ui()

    # Construcción de la interfaz
   
    def _build_ui(self):
        FONDO      = "#1e1e2e"
        PANEL      = "#2a2a3e"
        ACENTO     = "#7c3aed"
        ACENTO2    = "#a78bfa"
        TEXTO      = "#e2e8f0"
        VERDE      = "#4ade80"
        ROJO       = "#f87171"
        GRIS       = "#64748b"

        self.COLOR_DENTRO  = "#4ade80"   # puntos dentro del círculo
        self.COLOR_FUERA   = "#f87171"   # puntos fuera
        self.COLOR_CIRCULO = "#a78bfa"
        self.COLOR_CUADRO  = "#334155"

        # ── Título ──────────────────────────────────────────
        tk.Label(self.root, text="Simulador Monte Carlo  –  Estimación de π",
                 bg=FONDO, fg=ACENTO2,
                 font=("Consolas", 16, "bold")).pack(pady=(18, 4))

        tk.Label(self.root,
                 text="Genera puntos aleatorios y estima π con probabilidad",
                 bg=FONDO, fg=GRIS,
                 font=("Consolas", 9)).pack(pady=(0, 14))

        # ── Contenedor principal ─────────────────────────────
        main = tk.Frame(self.root, bg=FONDO)
        main.pack(padx=20, pady=0)

        # ── Panel izquierdo (controles + stats) ─────────────
        left = tk.Frame(main, bg=PANEL, bd=0, relief="flat",
                        padx=18, pady=18)
        left.grid(row=0, column=0, sticky="ns", padx=(0, 16))

        tk.Label(left, text="⚙  Configuración", bg=PANEL, fg=ACENTO2,
                 font=("Consolas", 11, "bold")).grid(row=0, column=0,
                 columnspan=2, sticky="w", pady=(0, 12))

        # Número de simulaciones
        tk.Label(left, text="Número de simulaciones:", bg=PANEL, fg=TEXTO,
                 font=("Consolas", 10)).grid(row=1, column=0, sticky="w")

        self.entry_n = tk.Entry(left, width=14, bg="#0f172a", fg=ACENTO2,
                                insertbackground=ACENTO2,
                                font=("Consolas", 11), bd=0,
                                highlightthickness=1,
                                highlightcolor=ACENTO,
                                highlightbackground=GRIS)
        self.entry_n.insert(0, "5000")
        self.entry_n.grid(row=2, column=0, columnspan=2, sticky="ew",
                          pady=(4, 16))

        # Velocidad de animación
        tk.Label(left, text="Velocidad (puntos/frame):", bg=PANEL, fg=TEXTO,
                 font=("Consolas", 10)).grid(row=3, column=0, sticky="w")

        self.speed_var = tk.IntVar(value=50)
        speed_scale = tk.Scale(left, from_=1, to=200,
                               variable=self.speed_var,
                               orient="horizontal", bg=PANEL,
                               fg=TEXTO, troughcolor="#0f172a",
                               highlightthickness=0,
                               activebackground=ACENTO,
                               font=("Consolas", 9), length=180)
        speed_scale.grid(row=4, column=0, columnspan=2,
                         sticky="ew", pady=(4, 20))

        # Botón ejecutar
        self.btn_run = tk.Button(left, text="▶  Ejecutar Simulación",
                                 bg=ACENTO, fg="white",
                                 font=("Consolas", 11, "bold"),
                                 bd=0, padx=10, pady=8, cursor="hand2",
                                 activebackground="#6d28d9",
                                 activeforeground="white",
                                 command=self._start_simulation)
        self.btn_run.grid(row=5, column=0, columnspan=2,
                          sticky="ew", pady=(0, 6))

        # Botón limpiar
        tk.Button(left, text="✕  Limpiar",
                  bg="#334155", fg=TEXTO,
                  font=("Consolas", 10), bd=0, padx=10, pady=6,
                  cursor="hand2",
                  activebackground="#475569",
                  command=self._clear).grid(row=6, column=0,
                  columnspan=2, sticky="ew", pady=(0, 20))

        # ── Separador ────────────────────────────────────────
        tk.Frame(left, bg=GRIS, height=1).grid(row=7, column=0,
                 columnspan=2, sticky="ew", pady=(0, 16))

        # ── Estadísticas ─────────────────────────────────────
        tk.Label(left, text="📊  Resultados", bg=PANEL, fg=ACENTO2,
                 font=("Consolas", 11, "bold")).grid(row=8, column=0,
                 columnspan=2, sticky="w", pady=(0, 10))

        stats = [
            ("Puntos totales:",    "lbl_total"),
            ("Puntos dentro:",     "lbl_dentro"),
            ("Puntos fuera:",      "lbl_fuera"),
            ("π estimado:",        "lbl_pi_est"),
            ("π real:",            "lbl_pi_real"),
            ("Error porcentual:",  "lbl_error"),
        ]

        for i, (label, attr) in enumerate(stats):
            tk.Label(left, text=label, bg=PANEL, fg=GRIS,
                     font=("Consolas", 9),
                     anchor="w", width=18).grid(row=9+i, column=0,
                     sticky="w", pady=2)
            lbl = tk.Label(left, text="–", bg=PANEL, fg=VERDE,
                           font=("Consolas", 10, "bold"),
                           anchor="e", width=14)
            lbl.grid(row=9+i, column=1, sticky="e", pady=2)
            setattr(self, attr, lbl)

        # Color especial para error
        self.lbl_pi_real.config(fg=TEXTO)
        self.lbl_pi_real.config(text=f"{math.pi:.8f}")
        self.lbl_error.config(fg=ROJO)

        # Barra de progreso
        tk.Label(left, text="Progreso:", bg=PANEL, fg=GRIS,
                 font=("Consolas", 9)).grid(row=16, column=0,
                 sticky="w", pady=(14, 2))

        self.progress = ttk.Progressbar(left, length=200,
                                        mode="determinate")
        self.progress.grid(row=17, column=0, columnspan=2,
                           sticky="ew", pady=(0, 4))

        self.lbl_prog = tk.Label(left, text="0 %", bg=PANEL,
                                 fg=GRIS, font=("Consolas", 8))
        self.lbl_prog.grid(row=18, column=0, columnspan=2)

        # ── Canvas (área gráfica) ─────────────────────────────
        self.canvas_size = 480
        self.canvas = tk.Canvas(main,
                                width=self.canvas_size,
                                height=self.canvas_size,
                                bg="#0f172a", bd=0,
                                highlightthickness=2,
                                highlightbackground=ACENTO)
        self.canvas.grid(row=0, column=1)

        # Estado
        self.running    = False
        self.sim_thread = None

        self._draw_base()

    # Dibujar cuadrado y círculo vacíos
   
    def _draw_base(self):
        cs = self.canvas_size
        m  = 30          # margen
        self.margin = m
        self.plot_size = cs - 2 * m

        self.canvas.delete("all")

        # Cuadrado
        self.canvas.create_rectangle(
            m, m, cs - m, cs - m,
            outline=self.COLOR_CUADRO, width=2)

        # Círculo inscrito
        self.canvas.create_oval(
            m, m, cs - m, cs - m,
            outline=self.COLOR_CIRCULO, width=2, dash=(6, 3))

        # Ejes
        mid = cs // 2
        self.canvas.create_line(mid, m, mid, cs-m,
                                fill="#1e3a5f", width=1, dash=(4,4))
        self.canvas.create_line(m, mid, cs-m, mid,
                                fill="#1e3a5f", width=1, dash=(4,4))

        # Etiquetas esquinas
        for txt, x, y in [("-1", m-2, cs-m+4),
                           (" 1", cs-m-8, cs-m+4),
                           ("-1", m-18, m-4),
                           (" 1", cs-m-10, m-4)]:
            self.canvas.create_text(x, y, text=txt,
                                    fill="#475569",
                                    font=("Consolas", 8))

    # Coordenada de pantalla → canvas

    def _to_canvas(self, x, y):
        """Convierte (x,y) en [-1,1]×[-1,1] a píxeles del canvas."""
        m  = self.margin
        ps = self.plot_size
        cx = m + (x + 1) / 2 * ps
        cy = m + (1 - y) / 2 * ps   # eje Y invertido
        return cx, cy

        # Iniciar simulación en hilo separado
  
    def _start_simulation(self):
        if self.running:
            return

        try:
            n = int(self.entry_n.get())
            if n < 10 or n > 2_000_000:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error",
                "Ingrese un número entero entre 10 y 2,000,000")
            return

        self._clear()
        self.running = True
        self.btn_run.config(state="disabled", bg="#4c1d95")

        self.sim_thread = threading.Thread(
            target=self._run_simulation, args=(n,), daemon=True)
        self.sim_thread.start()

       # Lógica de simulación (corre en hilo secundario)
    
    def _run_simulation(self, n):
        dentro       = 0
        speed        = self.speed_var.get()
        puntos_batch = []   # lote de puntos para dibujar

        for i in range(1, n + 1):
            # Generar punto aleatorio en [-1, 1] × [-1, 1]
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)

            # Comprobar si cae dentro del círculo unitario
            en_circulo = (x**2 + y**2) <= 1.0
            if en_circulo:
                dentro += 1

            puntos_batch.append((x, y, en_circulo))

            # Enviar lote al hilo principal cada `speed` puntos
            if i % speed == 0 or i == n:
                pi_est = 4 * dentro / i
                error  = abs(pi_est - math.pi) / math.pi * 100
                prog   = i / n * 100

                # Capturar lote y stats para pasar al hilo GUI
                lote_copy = puntos_batch.copy()
                puntos_batch.clear()

                self.root.after(0, self._update_ui,
                                lote_copy, i, dentro,
                                pi_est, error, prog)

        self.root.after(0, self._finish)

   
    # Actualizar canvas y etiquetas (hilo principal)
    
    def _update_ui(self, lote, total, dentro, pi_est, error, prog):
        # Dibujar puntos
        for x, y, en_circulo in lote:
            cx, cy = self._to_canvas(x, y)
            color  = self.COLOR_DENTRO if en_circulo else self.COLOR_FUERA
            # Punto de 2 px
            self.canvas.create_oval(cx-1.5, cy-1.5, cx+1.5, cy+1.5,
                                    fill=color, outline="")

        fuera = total - dentro

        # Actualizar etiquetas
        self.lbl_total.config(text=f"{total:,}")
        self.lbl_dentro.config(text=f"{dentro:,}")
        self.lbl_fuera.config(text=f"{fuera:,}")
        self.lbl_pi_est.config(text=f"{pi_est:.8f}")
        self.lbl_error.config(text=f"{error:.4f} %")

        # Barra de progreso
        self.progress["value"] = prog
        self.lbl_prog.config(text=f"{prog:.1f} %")

       # Finalizar simulación
   
    def _finish(self):
        self.running = False
        self.btn_run.config(state="normal", bg="#7c3aed")

        # Dibujar círculo y cuadrado encima para que no queden tapados
        cs = self.canvas_size
        m  = self.margin
        self.canvas.create_rectangle(m, m, cs-m, cs-m,
                                     outline=self.COLOR_CUADRO, width=2)
        self.canvas.create_oval(m, m, cs-m, cs-m,
                                outline=self.COLOR_CIRCULO,
                                width=2, dash=(6, 3))

        self.lbl_prog.config(text="✔  Completado")

   
    # Limpiar todo
    
    def _clear(self):
        self._draw_base()
        self.lbl_total.config(text="–")
        self.lbl_dentro.config(text="–")
        self.lbl_fuera.config(text="–")
        self.lbl_pi_est.config(text="–")
        self.lbl_error.config(text="–")
        self.progress["value"] = 0
        self.lbl_prog.config(text="0 %")



# Punto de entrada

if __name__ == "__main__":
    root = tk.Tk()
    app  = MonteCarloPi(root)
    root.mainloop()