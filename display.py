import tkinter as tk


morse_code_dict = { 
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/',
    'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..', 'Е': '.', 'Ё': '.', 'Ж': '...-', 'З': '--..', 'И': '..',
    'Й': '.---', 'К': '-.-', 'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---', 'П': '.--.', 'Р': '.-.', 'С': '...', 'Т': '-',
    'У': '..-', 'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 'Ч': '---.', 'Ш': '----', 'Щ': '--.-', 'Ъ': '--.--', 'Ы': '-.--',
    'Ь': '-..-', 'Э': '..-..', 'Ю': '..--', 'Я': '.-.-'
}

def encrypt():
    text = input_text.get()
    encrypted_text = ""
    for char in text.upper():
        if char in morse_code_dict:
            encrypted_text += morse_code_dict[char] + " "
    output_label.config(text="Encrypted Morse code: " + encrypted_text)

def decrypt():
    code = input_text.get()
    decrypted_text = ""
    words = code.split(" ")
    for word in words:
        chars = word.split()
        for char in chars:
            for letter, morse_code in morse_code_dict.items():
                if morse_code == char:
                    decrypted_text += letter
                    break
    output_label.config(text="Decrypted text: " + decrypted_text)

root = tk.Tk()
root.title("Morse Code Encryption/Decryption")
root.geometry("600x400")

input_label = tk.Label(root, text="Enter text or Morse code:", font=("Georgia", 20))
input_label.pack()

input_text = tk.Entry(root, font=("Georgia", 14))
input_text.pack()

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt, font=("Georgia", 14))
encrypt_button.pack()

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt, font=("Georgia", 14))
decrypt_button.pack()

output_label = tk.Label(root, text="", font=("Georgia", 20))
output_label.pack()

exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Georgia", 14))
exit_button.pack()

root.mainloop()