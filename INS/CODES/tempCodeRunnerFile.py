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