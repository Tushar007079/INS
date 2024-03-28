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
    reversed_key = {char: orig_char for orig_char, char in zip(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ", key.upper())}
    reversed_key.update({char.lower(): orig_char.lower() for orig_char, char in zip(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ", key.upper())})

    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            plaintext += reversed_key.get(char, char)
        else:
            plaintext += char
    return plaintext


def validate_monoalphabetic_key(key):
    if len(set(key)) != 26 or not key.isalpha():
        raise ValueError(
            "Mono-alphabetic Cipher key must be a permutation of the alphabet with 26 distinct characters.")

# Task 1: Caesar Cipher Encryption and Decryption
print("\033[95;1mTask 1: Caesar Cipher Encryption and Decryption\033[0m")
plaintext = input(
    "\033[93mEnter the confidential information to be sent: \033[0m")
shift = int(input("\033[93mEnter the Caesar Cipher shift value: \033[0m"))

caesar_ciphertext = caesar_cipher_encrypt(plaintext, shift)
print("\033[92;1mCaesar Cipher Encrypted Message: {}\033[0m".format(
    caesar_ciphertext))

caesar_decrypted_message = caesar_cipher_decrypt(caesar_ciphertext, shift)
print("\033[94;1mCaesar Cipher Decrypted Message: {}\033[0m\n".format(
    caesar_decrypted_message))

# Task 2: Find all possible Cipher Text & Plaintext pairs for Caesar Cipher
print("\033[93mTask 2: Find all possible Cipher Text & Plaintext pairs for Caesar Cipher\033[0m")
caesar_pairs = generate_caesar_cipher_pairs(plaintext)
for idx, pair in enumerate(caesar_pairs, 1):
    print("\033[96;1m{}) Cipher Text: {}, Plaintext: {}\033[0m".format(
        idx, pair[0], pair[1]))

# Task 3: Mono-alphabetic Cipher Encryption and Decryption
print("\033[95;1mTask 3: Mono-alphabetic Cipher Encryption and Decryption\033[0m")
monoalphabetic_key = input(
    "\033[93mEnter the Mono-alphabetic Cipher key: \033[0m")

try:
    validate_monoalphabetic_key(monoalphabetic_key)
    monoalphabetic_ciphertext = monoalphabetic_cipher_encrypt(
        plaintext, monoalphabetic_key)
    print("\033[92;1mMono-alphabetic Cipher Encrypted Message: {}\033[0m".format(monoalphabetic_ciphertext))

    monoalphabetic_decrypted_message = monoalphabetic_cipher_decrypt(
        monoalphabetic_ciphertext, monoalphabetic_key)
    print("\033[94;1mMono-alphabetic Cipher Decrypted Message: {}\033[0m".format(
        monoalphabetic_decrypted_message))

except ValueError as e:
    print("\033[91;1mError: {}\033[0m".format(e))