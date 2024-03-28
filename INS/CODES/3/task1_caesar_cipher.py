def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) + shift - offset) % 26 + offset)
        else:
            result += char
    return result

plaintext = input("Enter the plaintext: ")
shift = int(input("Enter the shift value: "))
ciphertext = caesar_cipher(plaintext, shift)

print("\nCaesar Cipher:")
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
