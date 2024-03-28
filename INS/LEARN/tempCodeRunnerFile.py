import numpy as np
import string

def adjoint(A):
    det = np.linalg.det(A)
    if det != 0:
        cofact = np.linalg.inv(A).T * det
        return cofact.getT() % 26

def display_matrix(matrix):
    print("Matrix:")
    print(matrix)

def display_pairs(pairs):
    print("Plain Text Pairs:")
    for pair in pairs:
        print(pair)

def encrypt(key_int, plain_text_int):
    cipher_text = ""
    for i in range(0, len(plain_text_int), 2):
        temp = np.matrix([plain_text_int[i], plain_text_int[i + 1]]).reshape(2, 1)
        c = np.matmul(key_int, temp)
        c %= 26
        c = c.tolist()
        for x in c:
            for y in x:
                cipher_text += alpha[y - 1]
    return cipher_text

def decrypt(key_int, cipher_text_int):
    det = round(np.linalg.det(key_int) % 26)
    adj = adjoint(key_int)
    mul_inv = mmi.get(det)
    key_inv = np.round(((mul_inv * adj) % 26)).astype(int)
    message = ""
    for i in range(0, len(cipher_text_int), 2):
        temp = np.matrix([cipher_text_int[i], cipher_text_int[i + 1]]).reshape(2, 1)
        c = np.matmul(key_inv, temp)
        c %= 26
        c = c.tolist()
        for x in c:
            for y in x:
                message += alpha[y - 1]
    return message

# List of all alphabets
alpha = list(string.ascii_lowercase)

# Modular Multiplicative Inverse Table
mmi = {1: 1, 3: 9, 5: 21, 7: 15, 9: 3, 11: 19, 15: 7, 17: 23, 19: 11, 21: 5, 23: 17, 25: 25}

def main():
    while True:
        print("\nHill Cipher Encryption and Decryption")
        print("-------------------------------------")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            key = list(input('Enter key: ').lower().replace(' ', ''))
            plain_text = list(input('Enter plaintext: ').lower().replace(' ', ''))
            
            # If message length is odd, add filler character
            if len(plain_text) % 2 != 0:
                plain_text.append('x')

            # Preparing key matrix
            key_int = np.matrix([(ord(c) % 96) for c in key]).reshape(2, 2)
            
            # Preparing plain text
            plain_text_int = [(ord(c) % 96) for c in plain_text]

            display_matrix(key_int)
            display_pairs([(plain_text[i], plain_text[i + 1]) for i in range(0, len(plain_text), 2)])
            
            cipher_text = encrypt(key_int, plain_text_int)
            print('Encrypted Text:', cipher_text)
        elif choice == '2':
            key = list(input('Enter key: ').lower().replace(' ', ''))
            cipher_text = list(input("Enter the ciphertext: ").lower().replace(' ', ''))
            key_int = np.matrix([(ord(c) % 96) for c in key]).reshape(2, 2)
            cipher_text_int = [(ord(c) % 96) for c in cipher_text]
            
            display_matrix(key_int)
            display_pairs([(cipher_text[i], cipher_text[i + 1]) for i in range(0, len(cipher_text), 2)])
            
            message = decrypt(key_int, cipher_text_int)
            print('Decrypted Message:', message)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
