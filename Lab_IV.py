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

def actualizar_visibilidad_celdas(*args):
    size = matriz_size.get() + 2
    for i in range(4):
        for j in range (4):
           estado =  'normal' if (i < size and j < size) else 'disabled'
           mat_a[i][j].delete(0, tk.END)

        estado_vec= 'normal' if i< size else 'disabled'
        mat_b[i][0].config(state=estado_vec)
        mat_x[i][0].config(state=estado_vec)
        if estado_vec == 'disabled'
            mat_b[i][0].delete(0, tk.END)
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

    mat_b = [[nome for _ in range(4)]]
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

    raiz.mainloop()

if __name__ == "__main__":
    creaVentana()