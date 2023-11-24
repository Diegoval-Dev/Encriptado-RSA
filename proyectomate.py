import tkinter as tk
from tkinter import ttk, messagebox

class RSA:
    def __init__(self, root):
        self.root = root
        root.title("Proyecto - Sistema RSA")

        ttk.Label(root, text="Creado por: Ruth de León y Diego Valenzuela", font=("Arial", 9)).grid(row=1, column=0, columnspan=2, pady=(0, 5))
        ttk.Label(root, text="Sistema RSA", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=(0, 10))

        ttk.Button(root, text="Encriptar", command=self.window_encriptar).grid(row=2, column=0, padx=10, pady=10)
        ttk.Button(root, text="Desencriptar", command=self.window_desencriptar).grid(row=2, column=1, padx=10, pady=10)

    def encriptar_window(self):
        window_encriptar = tk.Toplevel(self.root)
        window_encriptar.title("Encriptador RSA")

        tk.Label(window_encriptar, text="Texto a Encriptar:").grid(row=0, column=0, sticky="w")
        message_recibido = ttk.Entry(window_encriptar, width=50)
        message_recibido.grid(row=0, column=1)

        tk.Label(window_encriptar, text="p (primo):").grid(row=1, column=0, sticky="w")
        primo_p = ttk.Entry(window_encriptar, width=20)
        primo_p.grid(row=1, column=1)

        tk.Label(window_encriptar, text="q (primo):").grid(row=2, column=0, sticky="w")
        primo_q = ttk.Entry(window_encriptar, width=20)
        primo_q.grid(row=2, column=1)

        tk.Label(window_encriptar, text="e (entero > 1 y coprimo con φ):").grid(row=3, column=0, sticky="w")
        num_e = ttk.Entry(window_encriptar, width=20)
        num_e.grid(row=3, column=1)

        encripB = ttk.Button(window_encriptar, text="Encriptar", command=lambda: self.encriptar_mensaje(message_recibido, primo_p, primo_q, num_e))
        encripB.grid(row=4, column=0, columnspan=2)

    def msg_encriptar(self, message_recibido, primo_p, primo_q, num_e):
        try:
            mensaje = message_recibido.get()
            p = int(primo_p.get())
            q = int(primo_q.get())
            e = int(num_e.get())
            n = p * q
            phi = (p - 1) * (q - 1)

            if e <= 1 or not self.primos(e, phi):
                messagebox.showerror("Error", "e debe ser mayor que 1 y coprimo con φ")
                return

            resulnum = ''.join([format(ord(char.upper()) - ord('A'), '02d') for char in mensaje if char.isalpha()])
            bloques_2 = [int(resulnum[i:i+4]) for i in range(0, len(resulnum), 4)]

            encriptMe = [format(pow(bloque, e, n), '04d') for bloque in bloques_2]

            messagebox.showinfo("Mensaje Encriptado", ' '.join(encriptMe))
        except ValueError:
            messagebox.showerror("Error", "Entrada inválida")

    def primos(self, a, b):
        return self.mcd(a, b) == 1

    def mcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def desencriptar_window(self):
        window_desencriptar = tk.Toplevel(self.root)
        window_desencriptar.title("Desencriptador en RSA")

        tk.Label(window_desencriptar, text="Mensaje Cifrado:").grid(row=0, column=0, sticky="w")
        cifrado_start = ttk.Entry(window_desencriptar, width=50)
        cifrado_start.grid(row=0, column=1)

        tk.Label(window_desencriptar, text="n:").grid(row=1, column=0, sticky="w")
        num_n = ttk.Entry(window_desencriptar, width=20)
        num_n.grid(row=1, column=1)

        tk.Label(window_desencriptar, text="e:").grid(row=2, column=0, sticky="w")
        num_e = ttk.Entry(window_desencriptar, width=20)
        num_e.grid(row=2, column=1)

        desencriptB = ttk.Button(window_desencriptar, text="Desencriptar", command=lambda: self.modo_desencriptar(cifrado_start, num_n, num_e))
        desencriptB.grid(row=3, column=0, columnspan=2)

    def modo_desencriptar(self, cifrado_start, num_n, num_e):
        try:
            cifrado_txt = [int(bloque) for bloque in cifrado_start.get().split()]
            n = int(num_n.get())
            e = int(num_e.get())

            phi = self.phi(n)
            d = self.inverso_modular(e, phi)

            desenBlocks = [pow(c, d, n) for c in cifrado_txt]

            desencriptado_msg = ''.join([chr(bloque // 100 + ord('A')) + chr(bloque % 100 + ord('A')) for bloque in desenBlocks])

            messagebox.showinfo("Resultado de Desencriptación", f"Mensaje Desencriptado: {desencriptado_msg}\nClave Privada d: {d}")
        except ValueError:
            messagebox.showerror("Error", "Entrada inválida")

    def inverso_modular(self, a, m):
        g, x, y = self.egcd(a, m)
        if g != 1:
            raise Exception('No existe inverso modular para %d mod %d' % (a, m))
        else:
            return x % m

    def algorithm(self, a, b):
        if a == 0:
            return b, 0, 1
        else:
            MCD, x, y = self.algorithm(b % a, a)
            return MCD, y - (b // a) * x, x

    def phi(self, n):
        p, q = self.facto(n)
        return (p - 1) * (q - 1)

    def facto(self, n):
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return i, n // i
        return n, 1

root = tk.Tk()
app = RSA(root)

root.mainloop()