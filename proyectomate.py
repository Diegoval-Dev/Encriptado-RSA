import tkinter as tk

def message_code(message):
    alphab = {'A': '00', 'B': '01', 'C': '02', 'D': '03', 'E': '04', 'F': '05', 'G': '06', 'H': '07',
                'I': '08', 'J': '09', 'K': '10', 'L': '11', 'M': '12', 'N': '13', 'O': '14', 'P': '15',
                'Q': '16', 'R': '17', 'S': '18', 'T': '19', 'U': '20', 'V': '21', 'W': '22', 'X': '23',
                'Y': '24', 'Z': '25'}
    
    message_encode = ''
    for char in message:
        if char.isalpha():
            message_encode += alphab[char.upper()]
    
    return message_encode

def block_RSA(block_code, public_key):
    e, n = public_key
    encrypted_blocks = []

    for block in block_code:
        num_block = int(block)
        encrypted_block = pow(num_block, e, n)
        encrypted_blocks.append(str(encrypted_block).zfill(4))

    return encrypted_blocks

def encrypt_message():
    message_to_encrypt = entry_message.get()
    public_key = (13, 2537)

    # Codificar el mensaje según la codificación dada
    message_encode = message_code(message_to_encrypt)

    # Agrupar las letras en bloques de 2
    block_size = 2
    block_code = [message_encode[i:i+block_size] for i in range(0, len(message_encode), block_size)]

    # Encriptar los bloques usando RSA
    encrypted_blocks = block_RSA(block_code, public_key)

    # Actualizar la etiqueta de salida
    output_label.config(text=f"Bloques encriptados: {encrypted_blocks}")

# Crear la ventana principal
window = tk.Tk()
window.title("RSA Encryption")

# Crear y posicionar widgets
label_message = tk.Label(window, text="Mensaje:")
label_message.grid(row=0, column=0, padx=5, pady=5)

entry_message = tk.Entry(window)
entry_message.grid(row=0, column=1, padx=5, pady=5)

encrypt_button = tk.Button(window, text="Encriptar", command=encrypt_message)
encrypt_button.grid(row=0, column=2, padx=5, pady=5)

output_label = tk.Label(window, text="Bloques encriptados:")
output_label.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

# Iniciar el bucle de eventos
window.mainloop()