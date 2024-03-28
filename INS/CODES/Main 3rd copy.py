from colorama import Fore, Style, init
from tabulate import tabulate

init()

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
        pairs.append((shift, ciphertext, caesar_cipher_decrypt(ciphertext, shift)))
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
    reversed_key = {v: k for k, v in enumerate(key)}
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                plaintext += chr(reversed_key[char.upper()] + 65)
            else:
                plaintext += chr(reversed_key[char] + 97)
        else:
            plaintext += char
    return plaintext

def validate_monoalphabetic_key(key):
    if len(set(key)) != 26 or not key.isalpha():
        raise ValueError("Mono-alphabetic Cipher key must be a permutation of the alphabet with 26 distinct characters.")

def display_banner(message):
    banner = f"{Fore.CYAN}{Style.BRIGHT}=== {message} ==={Style.RESET_ALL}"
    print(banner)

def display_result(message, color=Fore.GREEN):
    print(f"{color}{Style.BRIGHT}{message}{Style.RESET_ALL}")

# Main program
display_banner("Confidential Information Encryption and Decryption")

# Task 1: Caesar Cipher Encryption and Decryption
plaintext = input("Enter the confidential information to be sent: ")
shift = int(input("Enter the Caesar Cipher shift value: "))

caesar_ciphertext = caesar_cipher_encrypt(plaintext, shift)
display_result(f"Caesar Cipher Encrypted Message: {caesar_ciphertext}")
caesar_decrypted_message = caesar_cipher_decrypt(caesar_ciphertext, shift)
display_result(f"Caesar Cipher Decrypted Message: {caesar_decrypted_message}", Fore.BLUE)

# Task 2: Find all possible Cipher Text & Plaintext pairs for Caesar Cipher
display_banner("All Possible Caesar Cipher Pairs")
caesar_pairs = generate_caesar_cipher_pairs(plaintext)

# Display Caesar Cipher Pairs in a table
table_headers = ["Shift", "Cipher Text", "Decrypted Text"]
table_data = [(pair[0], pair[1], pair[1]) for pair in caesar_pairs]
table = tabulate(table_data, headers=table_headers, tablefmt="fancy_grid", numalign="center", stralign="center")
print(table)

def validate_monoalphabetic_key(key):
    if len(set(key.lower())) != 26 or not key.isalpha():
        raise ValueError("Mono-alphabetic Cipher key must be a permutation of the alphabet with 26 distinct characters.")

# Task 3: Mono-alphabetic Cipher Encryption and Decryption
monoalphabetic_key = input("\nEnter the Mono-alphabetic Cipher key: ")

try:
    validate_monoalphabetic_key(monoalphabetic_key)

    # Ensure that the key maintains the case of the original alphabet
    monoalphabetic_key = monoalphabetic_key.lower() + monoalphabetic_key.upper()

    monoalphabetic_ciphertext = monoalphabetic_cipher_encrypt(plaintext, monoalphabetic_key)
    display_result(f"Mono-alphabetic Cipher Encrypted Message: {monoalphabetic_ciphertext}")
    monoalphabetic_decrypted_message = monoalphabetic_cipher_decrypt(monoalphabetic_ciphertext, monoalphabetic_key)
    display_result(f"Mono-alphabetic Cipher Decrypted Message: {monoalphabetic_decrypted_message}", Fore.BLUE)

except ValueError as e:
    display_result(f"Error: {e}", Fore.RED)
