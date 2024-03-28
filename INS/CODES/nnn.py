import random
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) + shift - offset) % 26 + offset)
        else:
            result += char
    return result

def all_possible_pairs(text):
    pairs = []
    for shift in range(26):
        ciphertext = caesar_cipher(text, shift)
        pairs.append((ciphertext, shift))
    return pairs

def generate_monoalphabetic_key():
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    shuffled_alphabet = list(alphabet)
    random.shuffle(shuffled_alphabet)
    key = dict(zip(alphabet, shuffled_alphabet))
    return key

def monoalphabetic_cipher(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            case = str.upper if char.isupper() else str.lower
            # Use get method with a default value to handle KeyError
            result += case(key.get(char, char))
        else:
            result += char
    return result

# Take user input for Caesar Cipher
plaintext_caesar = input("Enter the plaintext for Caesar Cipher: ")
shift_caesar = int(input("Enter the shift for Caesar Cipher (an integer between 0 and 25): "))
ciphertext_caesar = caesar_cipher(plaintext_caesar, shift_caesar)
print("Caesar Cipher - Input:")
print("Plaintext:", plaintext_caesar)
print("Shift:", shift_caesar)
print("\nCaesar Cipher - Output:")
print("Ciphertext:", ciphertext_caesar)

# Take user input for Mono-alphabetic Cipher
plaintext_mono = input("Enter the plaintext for Mono-alphabetic Cipher: ")
key_mono = generate_monoalphabetic_key()
print("Generated Mono-alphabetic Key:", key_mono)
ciphertext_mono = monoalphabetic_cipher(plaintext_mono, key_mono)
print("\nMono-alphabetic Cipher - Input:")
print("Plaintext:", plaintext_mono)
print("Key:", key_mono)
print("\nMono-alphabetic Cipher - Output:")
print("Ciphertext:", ciphertext_mono)
