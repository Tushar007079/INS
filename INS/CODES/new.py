def caesar_cipher_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                ciphertext += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                ciphertext += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            ciphertext += char
    return ciphertext

def caesar_cipher_decrypt(ciphertext, shift):
    return caesar_cipher_encrypt(ciphertext, -shift)

def generate_caesar_cipher_pairs(plaintext):
    pairs = []
    for shift in range(26):
        ciphertext = caesar_cipher_encrypt(plaintext, shift)
        pairs.append((ciphertext, caesar_cipher_decrypt(ciphertext, shift)))
    return pairs

def monoalphabetic_cipher_encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                ciphertext += key[ord(char) - 65].upper()
            else:
                ciphertext += key[ord(char) - 97]
        else:
            ciphertext += char
    return ciphertext

def monoalphabetic_cipher_decrypt(ciphertext, key):
    reversed_key = {char: orig_char for orig_char, char in zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", key.upper())}
    reversed_key.update({char.lower(): orig_char.lower() for orig_char, char in zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", key.upper())})
    
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            plaintext += reversed_key.get(char, char)
        else:
            plaintext += char
    return plaintext

# Rest of your code remains unchanged





def validate_monoalphabetic_key(key):
    if len(set(key)) != 26 or not key.isalpha():
        raise ValueError("Mono-alphabetic Cipher key must be a permutation of the alphabet with 26 distinct characters.")
    
# Task 1: Caesar Cipher Encryption and Decryption
plaintext = input("Enter the confidential information to be sent: ")
shift = int(input("Enter the Caesar Cipher shift value: "))

caesar_ciphertext = caesar_cipher_encrypt(plaintext, shift)
print(f"\nCaesar Cipher Encrypted Message: {caesar_ciphertext}")

caesar_decrypted_message = caesar_cipher_decrypt(caesar_ciphertext, shift)
print(f"Caesar Cipher Decrypted Message: {caesar_decrypted_message}\n")

# Task 2: Find all possible Cipher Text & Plaintext pairs for Caesar Cipher
caesar_pairs = generate_caesar_cipher_pairs(plaintext)
print("All Possible Caesar Cipher Pairs:")
for pair in caesar_pairs:
    print(pair)

# Task 3: Mono-alphabetic Cipher Encryption and Decryption
monoalphabetic_key = input("\nEnter the Mono-alphabetic Cipher key: ")

try:
    validate_monoalphabetic_key(monoalphabetic_key)
    monoalphabetic_ciphertext = monoalphabetic_cipher_encrypt(plaintext, monoalphabetic_key)
    print(f"\nMono-alphabetic Cipher Encrypted Message: {monoalphabetic_ciphertext}")

    monoalphabetic_decrypted_message = monoalphabetic_cipher_decrypt(monoalphabetic_ciphertext, monoalphabetic_key)
    print(f"Mono-alphabetic Cipher Decrypted Message: {monoalphabetic_decrypted_message}")

except ValueError as e:
    print(f"Error: {e}")
