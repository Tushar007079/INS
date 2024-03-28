import string

def prepare_key(key):
    key = key.upper().replace('J', 'I')
    key_set = sorted(set(key), key=key.find)
    alphabet = list(string.ascii_uppercase.replace('J', ''))  # Convert alphabet to list

    # Fill the remaining matrix with unique letters from the alphabet (excluding 'J')
    matrix = key_set + [letter for letter in alphabet if letter not in key_set]

    # Create a 5x5 matrix
    playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
    return playfair_matrix

def find_position(char, matrix):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return -1, -1

def encrypt(plaintext, matrix):
    ciphertext = ""
    plaintext = plaintext.upper().replace('J', 'I')
    pairs = []

    for i in range(0, len(plaintext), 2):
        char1 = plaintext[i]
        char2 = plaintext[i+1] if i+1 < len(plaintext) else 'X'
        pairs.append((char1, char2))

        row1, col1 = find_position(char1, matrix)
        if row1 == -1:
            row1, col1 = find_position('X', matrix)

        row2, col2 = find_position(char2, matrix)
        if row2 == -1:
            row2, col2 = find_position('X', matrix)

        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2] + matrix[row2][col1]

    return ciphertext, pairs

def decrypt(ciphertext, matrix):
    plaintext = ""
    pairs = []

    for i in range(0, len(ciphertext), 2):
        char1 = ciphertext[i]
        char2 = ciphertext[i+1]
        pairs.append((char1, char2))

        row1, col1 = find_position(char1, matrix)
        if row1 == -1:
            row1, col1 = find_position('X', matrix)

        row2, col2 = find_position(char2, matrix)
        if row2 == -1:
            row2, col2 = find_position('X', matrix)

        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2] + matrix[row2][col1]

    return plaintext, pairs

# Taking input from the user for encryption
key = input("Enter the key: ")
plaintext = input("Enter the plaintext: ")

# Encrypting the plaintext
matrix = prepare_key(key)
encrypted_text, encryption_pairs = encrypt(plaintext, matrix)

# Displaying encryption output
print("\nEncryption Output:")
print(f"Plaintext Pairs: {encryption_pairs}")
print(f"Encrypted Text: {encrypted_text}")

# Displaying encryption output and key matrix
print("\nEncryption Output:")
print(f"Plaintext Pairs: {encryption_pairs}")
print(f"Encrypted Text: {encrypted_text}")
print("\nKey Matrix:")
for row in matrix:
    print(row)

# Taking input from the user for decryption
encrypted_text_input = input("\nEnter the encrypted text for decryption: ")

# Decrypting the encrypted text
decrypted_text, decryption_pairs = decrypt(encrypted_text_input, matrix)

# Displaying decryption output and key matrix
print("\nDecryption Output:")
print(f"Encrypted Text: {encrypted_text_input}")
print(f"Plaintext: {plaintext}")
print("\nKey Matrix:")
for row in matrix:
    print(row)
print(f"Decryption Pairs: {decryption_pairs}")