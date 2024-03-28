import numpy as np
def arrayGenerate(kw):
    array = np.empty((5, 5), dtype='str')
    alpha = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    
    used_letters = set()
    row, col = 0, 0
    
    for letter in kw:
        if letter not in used_letters:
            array[row, col] = letter
            used_letters.add(letter)
            col += 1
            
            if col == 5:
                col = 0
                row += 1
                if row == 5: 
                    break
            
    for letter in alpha:
        if letter not in used_letters and letter != 'J':
            array[row, col] = letter
            used_letters.add(letter)
            col += 1
            
            if col == 5:
                col = 0
                row += 1
                if row == 5:  
                    break
                
    return array
    
def print_matrix(matrix):
        for row in matrix:
            print(" ".join(row))
        
def find_letter(matrix, letter):
        for row in range(5):
            for col in range(5):
                if matrix[row, col] == letter:
                    return row, col
        return None, None
    
def playfair_encrypt(plain_text, matrix):
        encrypted_text = ""
        plain_text = plain_text.upper().replace("J", "I").replace(" ", "")
        
        for i in range(0, len(plain_text), 2):
            letter1 = plain_text[i]
            letter2 = plain_text[i + 1] if i + 1 < len(plain_text) else 'X'
            
            row1, col1 = find_letter(matrix, letter1)
            row2, col2 = find_letter(matrix, letter2)
        
            if row1 == row2:
                encrypted_text += matrix[row1, (col1 + 1) % 5] + matrix[row2, (col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5, col1] + matrix[(row2 + 1) % 5, col2]
            else:
                encrypted_text += matrix[row1, col2] + matrix[row2, col1]
                
        return encrypted_text
        
def main():
    keyword = input("Enter keyword: ").upper()
    matrix = arrayGenerate(keyword)
    
    print("Generated Playfair Matrix:")
    print_matrix(matrix)
    
    plain_text = input("Enter plain text : ")
    encrypted_text = playfair_encrypt(plain_text, matrix)
    
    print("Encrypted text:", encrypted_text)
    
main()
        
        