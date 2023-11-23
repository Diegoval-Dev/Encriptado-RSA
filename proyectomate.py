import tkinter as tk
from tkinter import ttk, messagebox

class SistemRSA:
    def __init__(self, root):
        self.root = root
        root.title("Sistema RSA")

        self.create_labels()
        self.create_buttons()
        
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        x_position = (screen_width - root.winfo_reqwidth()) // 2
        y_position = (screen_height - root.winfo_reqheight()) // 2

        root.geometry(f"+{x_position}+{y_position}")

    def create_labels(self):
        ttk.Label(self.root, text="Bienvenido al Sistema RSA", font=("Times new roman", 16)).grid(row=0, column=0, columnspan=2, pady=(10, 5))

    def create_buttons(self):
        ttk.Button(self.root, text="Encriptar", command=self.open_encrypt_window).grid(row=2, column=0, padx=10, pady=10)
        ttk.Button(self.root, text="Desencriptar", command=self.open_decrypt_window).grid(row=2, column=1, padx=10, pady=10)

    def open_encrypt_window(self):
        encrypt_window = self.create_window("Encriptador RSA")

        ttk.Label(encrypt_window, text="Mensaje:").grid(row=0, column=0, sticky="w")
        message_entry = ttk.Entry(encrypt_window, width=50)
        message_entry.grid(row=0, column=1)

        self.create_key_entries(encrypt_window, row_start=1)

        ttk.Button(encrypt_window, text="Encriptar", command=lambda: self.encrypt_message(message_entry)).grid(row=4, column=0, columnspan=2)

    def open_decrypt_window(self):
        decrypt_window = self.create_window("Desencriptador RSA")

        ttk.Label(decrypt_window, text="Mensaje Cifrado:").grid(row=0, column=0, sticky="w")
        cipher_entry = ttk.Entry(decrypt_window, width=50)
        cipher_entry.grid(row=0, column=1)

        self.create_key_entries(decrypt_window, row_start=1)

        ttk.Button(decrypt_window, text="Desencriptar", command=lambda: self.decrypt_message(cipher_entry)).grid(row=4, column=0, columnspan=2)

    def create_key_entries(self, window, row_start):
        labels = ["p (primo):", "q (primo):", "e (entero > 1 y coprimo con φ):"]
        entries = [ttk.Entry(window, width=20) for _ in range(len(labels))]

        for i, label in enumerate(labels):
            ttk.Label(window, text=label).grid(row=row_start + i, column=0, sticky="w")
            entries[i].grid(row=row_start + i, column=1)

    def create_window(self, title):
        window = tk.Toplevel(self.root)
        window.title(title)
        
        window.withdraw()
        window.update_idletasks()
        window_width = window.winfo_reqwidth()
        window_height = window.winfo_reqheight()
        x_position = (window.winfo_screenwidth() - window_width) // 2
        y_position = (window.winfo_screenheight() - window_height) // 2
        window.geometry(f"+{x_position}+{y_position}")
        window.deiconify()
        
        return window

    def encrypt_message(self, message_entry):
        # Implementa la lógica de encriptación
        pass

    def decrypt_message(self, cipher_entry):
        # Implementa la lógica de desencriptación
        pass

# Crear la ventana principal
root = tk.Tk()
app = SistemRSA(root)

# Ejecutar la aplicación
root.mainloop()