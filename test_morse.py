import unittest

"""
instead of importing the encyrpt and decrypt functions from my
morse code file, I wrote the functions in this file for effiency reasons and have the 
unittests run seemlesly

"""

morse_code_dict = {
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
    encrypted = []
    for char in text.upper():
        if char in morse_code_dict:
            encrypted.append(morse_code_dict[char])
    return ' '.join(encrypted)

def decrypt(code):
    decrypted = []
    words = code.split(' ')
    for word in words:
        chars = word.split()
        for char in chars:
            for letter, morse_code in morse_code_dict.items():
                if morse_code == char:
                    decrypted.append(letter)
                    break
    return ''.join(decrypted)


class MorseCodeTestCase(unittest.TestCase): 

    def test_encrypt(self): #tests the encrypt method
        text = "Hello TKH"
        expected_result = ".... . .-.. .-.. --- / - -.- ...."
        self.assertEqual(encrypt(text), expected_result)


    def test_decrypt(self): #tests the decrypt method
        code = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
        expected_result = "HELLO WORLD"
        self.assertEqual(decrypt(code), expected_result)



unittest.main()


