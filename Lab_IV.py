#---------------------------------------------------
# Laboratorio N°4 
# Integrantes: Bañares, Pablo
#              Velazquez Cruz, Joel
# Repo GitHub: https://github.com/jo-Ve-C1/Laboratorio4_Velazquez-Cruz-Joel_Info2.git
#---------------------------------------------------

import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
#----------------------------------
#  FUNCIONES
#----------------------------------
def rta_x(A, b):
    n = len(b)
    D = np.linalg.det(A)
    x = np.zeros(n)
    for k in range(n):
        Ak = A.copy()
        Ak[:, k] = b
        Dk = np.linalg.det(Ak)
        x[k] = Dk / D 
    return x

def obtener_datos():
    size = matriz_size.get() + 2
    matriz_A = []
    for i in range(size):
        fila = []
        for j in range(size):
            val = mat_a[i][j].get().strip()
            if not val:
                raise ValueError(f"Falta ingresar el valor en A[{i+1}][{j+1}]")
            fila.append(float(val))
        matriz_A.append(fila)

    vector_B = []
    for i in range(size):
        val = mat_b[i][0].get().strip()
        if not val:
            raise ValueError(f"Falta ingresar el valor en b[{i+1}]")
        vector_B.append(float(val))

    return np.array(matriz_A), np.array(vector_B), size

def cramer():
    try:
        matriz_A, vector_B, size = obtener_datos()
        detA = np.linalg.det(matriz_A)

        if abs(detA) < 1e-9:
            message.config(text="¡Atención! El determinante es 0.\nEl sistema no tiene solución única.")
            tx_det.delete(0, tk.END)
            tx_det.insert(0, "0")
            return

        x_rta = rta_x(matriz_A, vector_B)
        limpiar_resultados()

        for i in range(size):
            mat_x[i][0].config(state='normal')
            mat_x[i][0].delete(0, tk.END)
            mat_x[i][0].insert(0, str(round(x_rta[i], 4)))

        tx_det.delete(0, tk.END)
        tx_det.insert(0, str(round(detA, 4)))
        message.config(text="Sistema resuelto exitosamente.")

    except ValueError as ve:
        messagebox.showwarning("Campos incompletos", str(ve))
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error inesperado:\n{e}")

def calcularDeterminante():
    try:
        matriz_A, _, _ = obtener_datos()
        det = np.linalg.det(matriz_A)
        tx_det.delete(0, tk.END)
        tx_det.insert(0, str(round(det, 4)))
        message.config(text="Determinante calculado correctamente.")
    except ValueError as ve:
        messagebox.showwarning("Campos incompletos", str(ve))

def actualizar_visibilidad_celdas(*args):
    """Habilita u deshabilita celdas según el tamaño seleccionado (2x2, 3x3, 4x4)"""
    size = matriz_size.get() + 2
    for i in range(4):
        for j in range(4):
            estado = 'normal' if (i < size and j < size) else 'disabled'
            mat_a[i][j].config(state=estado)
            if estado == 'disabled':
                mat_a[i][j].delete(0, tk.END)

        estado_vec = 'normal' if i < size else 'disabled'
        mat_b[i][0].config(state=estado_vec)
        mat_x[i][0].config(state=estado_vec)
        if estado_vec == 'disabled':
            mat_b[i][0].delete(0, tk.END)
            mat_x[i][0].delete(0, tk.END)

def limpiar_resultados():
    tx_det.delete(0, tk.END)
    for i in range(4):
        mat_x[i][0].delete(0, tk.END)

def borrarTodo():
    tx_det.delete(0, tk.END)
    for i in range(4):
        for j in range(4):
            mat_a[i][j].delete(0, tk.END)
        mat_b[i][0].delete(0, tk.END)
        mat_x[i][0].delete(0, tk.END)
    message.config(text="Todos los campos han sido limpiados.")




#----------------------------------
#  GRAFICO
#----------------------------------
def creaVentana():
    global raiz, matriz_size, tx_det, message, mat_a, mat_b, mat_x
    raiz = tk.Tk()
    raiz.geometry('820x420+200+200')
    raiz.configure(bg='black')
    raiz.title('Resolución de Sistemas de Ecuaciones Lineales - Regla de Cramer')


# Selector de tamaño
    matriz_size = tk.IntVar(raiz, value=0)
    matriz_size.trace_add("write", actualizar_visibilidad_celdas)

    rb_frame = tk.LabelFrame(raiz, text="Dimensión", fg="white", bg="black", padx=5, pady=5)
    rb_frame.place(x=30, y=60, width=100, height=130)

    opciones = [("2x2", 0), ("3x3", 1), ("4x4", 2)]
    for text, val in opciones:
        tk.Radiobutton(rb_frame, text=text, variable=matriz_size, value=val, 
                       bg="black", fg="white", selectcolor="#333333",
                       activebackground="black", activeforeground="white").pack(anchor=tk.W, pady=2)


    #matrizA
    ventana_mat_a = tk.LabelFrame(raiz, text='matriz A', fg="white", bg="black", padx=10, pady=10)
    ventana_mat_a.place(x=150, y=50)

    mat_a = [[None for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            mat_a[i][j] = tk.Entry(ventana_mat_a, width=6, justify='center')
            mat_a[i][j].grid(row=i, column=j, padx=4, pady=4)

    #matriz B
    ventana_mat_b = tk.LabelFrame(raiz, text='matriz B', fg="black", padx=10, pady=10)
    ventana_mat_b.place(x=430, y=50)

    mat_b = [[None] for _ in range(4)]
    for i in range(4):
        mat_b[i][0] = tk.Entry(ventana_mat_b, width=6, justify='center')
        mat_b[i][0].grid(row=i, column=0, padx=4, pady=4)

    # Vector X (Resultado)
    ventana_mat_x = tk.LabelFrame(raiz, text='Vector x', fg="white", bg="black", padx=10, pady=10)
    ventana_mat_x.place(x=540, y=50)
    
    mat_x = [[None] for _ in range(4)]
    for i in range(4):
        mat_x[i][0] = tk.Entry(ventana_mat_x, width=8, justify='center')
        mat_x[i][0].grid(row=i, column=0, padx=4, pady=4)

# Controles y Botones
    b_calcular = tk.Button(raiz, text='Calcular Cramer', command=cramer, width=15, bg='#1f1f1f', fg='white', relief=tk.RAISED)
    b_calcular.place(x=660, y=70)

    b_det = tk.Button(raiz, text='Calcular Det(A)', command=calcularDeterminante, width=15, bg='#1f1f1f', fg='white')
    b_det.place(x=660, y=110)

    b_borrar = tk.Button(raiz, text='Borrar Todo', command=borrarTodo, width=15, bg='#1f1f1f', fg='white')
    b_borrar.place(x=660, y=150)

    # Determinante y Panel de Estado
    tk.Label(raiz, text="Determinante:", bg='black', fg='white').place(x=430, y=260)
    tx_det = tk.Entry(raiz, width=12, justify='center')
    tx_det.place(x=530, y=260)

    tk.Label(raiz, text="Estado / Ayuda:", fg="white", bg="black", font=('Helvetica', 9, 'bold')).place(x=30, y=290)
    message = tk.Label(raiz, text="Cargue los coeficientes en A y b, luego presione 'Calcular Cramer'.", 
                       fg="#4CAF50", bg="black", anchor="w", justify=tk.LEFT)
    message.place(x=30, y=320)

    actualizar_visibilidad_celdas()
    raiz.mainloop()

if __name__ == "__main__":
    creaVentana()