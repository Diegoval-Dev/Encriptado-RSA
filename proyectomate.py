import tkinter as tk

def encode_message(message):
    encoding = {'A': '00', 'B': '01', 'C': '02', 'D': '03', 'E': '04', 'F': '05', 'G': '06', 'H': '07',
                'I': '08', 'J': '09', 'K': '10', 'L': '11', 'M': '12', 'N': '13', 'O': '14', 'P': '15',
                'Q': '16', 'R': '17', 'S': '18', 'T': '19', 'U': '20', 'V': '21', 'W': '22', 'X': '23',
                'Y': '24', 'Z': '25'}
    
    encoded_message = ''
    for char in message:
        if char.isalpha():
            encoded_message += encoding[char.upper()]
    
    return encoded_message

def encrypt_rsa_blocks(encoded_blocks, public_key):
    e, n = public_key
    encrypted_blocks = []

    for block in encoded_blocks:
        num_block = int(block)
        encrypted_block = pow(num_block, e, n)
        encrypted_blocks.append(str(encrypted_block).zfill(4))

    return encrypted_blocks

def decrypt_rsa_blocks(encrypted_blocks, public_key):
    d, n = public_key
    decrypted_blocks = []

    for block in encrypted_blocks:
        num_block = int(block)
        decrypted_block = pow(num_block, d, n)
        decrypted_blocks.append(chr(decrypted_block))

    return decrypted_blocks

def encrypt_message():
    message_to_encrypt = entry_message.get()
    public_key = (13, 2537)

    # Codificar el mensaje según la codificación dada
    encoded_message = encode_message(message_to_encrypt)

    # Agrupar las letras en bloques de 2
    block_size = 2
    encoded_blocks = [encoded_message[i:i+block_size] for i in range(0, len(encoded_message), block_size)]

    # Encriptar los bloques usando RSA
    encrypted_blocks = encrypt_rsa_blocks(encoded_blocks, public_key)

    # Actualizar la etiqueta de salida
    output_label.config(text=f"Bloques encriptados: {' '.join(encrypted_blocks)}")

def decrypt_message():
    encrypted_blocks_str = entry_ciphertext.get()
    encrypted_blocks = encrypted_blocks_str.split()
    public_key = (937, 43*59)  # Usando la clave privada generada anteriormente

    # Desencriptar los bloques usando RSA
    decrypted_blocks = decrypt_rsa_blocks(encrypted_blocks, public_key)

    # Actualizar la etiqueta de salida
    output_label_decrypt.config(text=f"Bloques desencriptados: {''.join(decrypted_blocks)}")

# Crear la ventana principal
window = tk.Tk()
window.title("RSA Encryption and Decryption")

# Crear y posicionar widgets para la encriptación
label_message = tk.Label(window, text="Mensaje:")
label_message.grid(row=0, column=0, padx=5, pady=5)

entry_message = tk.Entry(window)
entry_message.grid(row=0, column=1, padx=5, pady=5)

encrypt_button = tk.Button(window, text="Encriptar", command=encrypt_message)
encrypt_button.grid(row=0, column=2, padx=5, pady=5)

output_label = tk.Label(window, text="Bloques encriptados:")
output_label.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

# Crear y posicionar widgets para la desencriptación
label_ciphertext = tk.Label(window, text="Mensaje cifrado:")
label_ciphertext.grid(row=2, column=0, padx=5, pady=5)

entry_ciphertext = tk.Entry(window)
entry_ciphertext.grid(row=2, column=1, padx=5, pady=5)

decrypt_button = tk.Button(window, text="Desencriptar", command=decrypt_message)
decrypt_button.grid(row=2, column=2, padx=5, pady=5)

output_label_decrypt = tk.Label(window, text="Bloques desencriptados:")
output_label_decrypt.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

# Iniciar el bucle de eventos
window.mainloop()