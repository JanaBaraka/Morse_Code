morse_code_dict = { #alpahbet mapping dictionary
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}

def encrypt(text):
    encrypted = [] # an empty list used to store each character mapped from the dict
    for char in text.upper():
        if char in morse_code_dict:
            encrypted.append(morse_code_dict[char]) 
    return ' '.join(encrypted) #joins the chars to the list with a space between them

def decrypt(code):
    decrypted = []
    words = code.split(' ') #splits the code into words
    for word in words:
        chars = word.split()  
        for char in chars: #goes through each char in the word
            for letter, morse_code in morse_code_dict.items():
                if morse_code == char: #checks if char is in the dictionary
                    decrypted.append(letter)
                    break
    return ''.join(decrypted) #formats the string properly

while True: #a while loop to create a menu-based user interface
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        text = input("Enter the text to encrypt: ")
        encrypted_text = encrypt(text)
        print("Encrypted Morse code: ", encrypted_text)
    elif choice == '2':
        code = input("Enter the Morse code to decrypt (use '.' for dots and '-' for dashes): ")
        decrypted_text = decrypt(code)
        print("Decrypted text: ", decrypted_text)
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.\n")

