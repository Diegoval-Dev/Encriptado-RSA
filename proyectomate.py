import tkinter as tk
from tkinter import ttk, messagebox

class SistemaRSA:
    def __init__(self, root):
        self.root = root
        root.title("Sistema RSA")

        self.titulos()
        self.buttonCategory()

    def titulos(self):
        ttk.Label(self.root, text="Proyecto - El sistema RSA", font=("Times new roman", 16)).grid(row=0, column=0, columnspan=2, pady=(10, 5))
        ttk.Label(self.root, text="Ruth de León - Diego Valenzuela", font=("Times new roman", 10)).grid(row=0, column=0, columnspan=2, pady=(10, 50))

    def buttonCategory(self):
        ttk.Button(self.root, text="Encriptar", command=self.ventana_ex).grid(row=2, column=0, padx=30, pady=15)
        ttk.Button(self.root, text="Desencriptar", command=self.ventana_dx).grid(row=2, column=1, padx=30, pady=15)

    def ventana_ex(self):
        windows_encriptar = self.crear_ventana("Encriptador RSA")

        ttk.Label(windows_encriptar, text="Mensaje:").grid(row=0, column=0, sticky="w")
        message = ttk.Entry(windows_encriptar, width=50)
        message.grid(row=0, column=1)

        self.new_clave(windows_encriptar, fila_inicio=1)

        ttk.Button(windows_encriptar, text="Encriptar", command=lambda: self.ex_mssage(message)).grid(row=4, column=0, columnspan=2)

    def ventana_dx(self):
        windows_desencriptar = self.crear_ventana("Desencriptador RSA")

        ttk.Label(windows_desencriptar, text="Mensaje Cifrado:").grid(row=0, column=0, sticky="w")
        entrada_cifrado = ttk.Entry(windows_desencriptar, width=50)
        entrada_cifrado.grid(row=0, column=1)

        self.new_clave(windows_desencriptar, fila_inicio=1)

        ttk.Button(windows_desencriptar, text="Desencriptar", command=lambda: self.ex_message(entrada_cifrado)).grid(row=4, column=0, columnspan=2)

    def new_clave(self, ventana, fila_inicio):
        etiquetas = ["p (primo):", "q (primo):", "e (entero > 1 y coprimo con φ):"]
        entradas = [ttk.Entry(ventana, width=20) for _ in range(len(etiquetas))]

        for i, etiqueta in enumerate(etiquetas):
            ttk.Label(ventana, text=etiqueta).grid(row=fila_inicio + i, column=0, sticky="w")
            entradas[i].grid(row=fila_inicio + i, column=1)

    def crear_ventana(self, titulo):
        ventana = tk.Toplevel(self.root)
        ventana.title(titulo)
        return ventana

    def ex_mssage(self, message):
        pass

    def x_message(self, entrada_cifrado):
        pass

raiz = tk.Tk()
aplicacion = SistemaRSA(raiz)

raiz.mainloop()