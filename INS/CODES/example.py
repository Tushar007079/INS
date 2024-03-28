def generate_monoalphabetic_key(name):
    name = name.upper()
    unique_letters = ''.join(sorted(set(name), key=lambda x: name.index(x)))
    remaining_alphabet = ''.join(sorted(set('ABCDEFGHIJKLMNOPQRSTUVWXYZ') - set(unique_letters)))
    monoalphabetic_key = unique_letters + remaining_alphabet
    return monoalphabetic_key

# Example usage with the name 'TUSHAR'
name = 'TUSHAR'
monoalphabetic_key = generate_monoalphabetic_key(name)

print(f'Mono-alphabetic Cipher Key for {name}: {monoalphabetic_key}')
