def generate_playfair_matrix(key):
    matrix = []
    for char in key.upper():
        if char not in matrix and char != 'J':
            matrix.append(char)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)

    playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
    return playfair_matrix

def find_char_positions(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return -1, -1

def playfair_encrypt(plaintext, key):
    matrix = generate_playfair_matrix(key)

    # Prepare plaintext pairs
    plaintext_pairs = []
    i = 0
    while i < len(plaintext):
        if i == len(plaintext) - 1 or plaintext[i] == plaintext[i + 1]:
            plaintext_pairs.append(plaintext[i] + 'X')
            i += 1
        else:
            plaintext_pairs.append(plaintext[i] + plaintext[i + 1])
            i += 2

    encrypted_text = ""
    for pair in plaintext_pairs:
        char1, char2 = pair[0], pair[1]
        row1, col1 = find_char_positions(matrix, char1)
        row2, col2 = find_char_positions(matrix, char2)

        if row1 == row2:
            encrypted_text += matrix[row1][(col1 + 1) % 5]
            encrypted_text += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted_text += matrix[(row1 + 1) % 5][col1]
            encrypted_text += matrix[(row2 + 1) % 5][col2]
        else:
            encrypted_text += matrix[row1][col2]
            encrypted_text += matrix[row2][col1]

    return encrypted_text

# Get input from the user after running the code
plaintext = input("Enter the text to encrypt: ")
key = input("Enter the key: ")

encrypted_text = playfair_encrypt(plaintext, key)
print("Original Text:",plaintext)
print("Encrypted Text:",encrypted_text)