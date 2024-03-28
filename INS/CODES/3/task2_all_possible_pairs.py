from task1_caesar_cipher import caesar_cipher

def all_possible_pairs(text):
    pairs = []
    for shift in range(26):
        ciphertext = caesar_cipher(text, shift)
        pairs.append((ciphertext, shift))
    return pairs

plaintext = input("Enter the plaintext: ")
pairs = all_possible_pairs(plaintext)

print("\nAll Possible Pairs for Caesar Cipher:")
for pair in pairs:
    print(pair)
