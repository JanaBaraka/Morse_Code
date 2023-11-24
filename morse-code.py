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

