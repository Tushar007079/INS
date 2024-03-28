import random

def generate_monoalphabetic_key():
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    shuffled_alphabet = list(alphabet)
    random.shuffle(shuffled_alphabet)
    
    lowercase_alphabet = list("abcdefghijklmnopqrstuvwxyz")
    shuffled_lowercase_alphabet = list(lowercase_alphabet)
    random.shuffle(shuffled_lowercase_alphabet)

    key = dict(zip(alphabet + lowercase_alphabet, shuffled_alphabet + shuffled_lowercase_alphabet))
    return key

def monoalphabetic_cipher(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            case = str.upper if char.isupper() else str.lower
            try:
                result += case(key[char])
            except KeyError:
                print(f"Error: Key not found for character '{char}'")
                return None
        else:
            result += char
    return result

plaintext = input("Enter the plaintext: ")
key = generate_monoalphabetic_key()

if key is not None:
    ciphertext = monoalphabetic_cipher(plaintext, key)
    if ciphertext is not None:
        print("\nMono-alphabetic Cipher:", key)
        print("Plaintext:", plaintext)
        print("Ciphertext:", ciphertext)
