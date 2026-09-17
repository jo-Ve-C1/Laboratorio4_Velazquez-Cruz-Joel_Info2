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



#----------------------------------
#  GRAFICO
#----------------------------------
def creaVentana():
    global raiz
    raiz = tk.Tk()
    raiz.geometry('820x420+200+200')
    raiz.configure(bg='black')
    raiz.title('Resolución de Sistemas de Ecuaciones Lineales - Regla de Cramer')
    global mat_a, mat_b, mat_x

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