import math


def main():
    """
    Main function that demonstrates the encryption, decryption, and cipher-breaking functionality
    with two sample messages.
    """
    msg1 = "at eleven surveillance on front lines"
    print("Original message:", msg1)
    encrypted_msg1 = encrypt(msg1, 6)
    print("Encrypted message:", encrypted_msg1)
    decrypted_msg1 = decrypt(encrypted_msg1, 6)
    print("Decrypted message:", decrypted_msg1)
    broken_msg1 = break_cipher(encrypted_msg1)
    print("Broken cipher message:", broken_msg1)

    msg2 = "This is a secret message"
    print("\nOriginal message:", msg2)
    encrypted_msg2 = encrypt(msg2, 6)
    print("Encrypted message:", encrypted_msg2)
    decrypted_msg2 = decrypt(encrypted_msg2, 6)
    print("Decrypted message:", decrypted_msg2)
    broken_msg2 = break_cipher(encrypted_msg2)
    print("Broken cipher message:", broken_msg2)


def encrypt(plaintext, key):
    """
    Encrypts a given plaintext using a columnar transposition cipher.

    Args:
        plaintext (str): The text to be encrypted.
        key (int): The number of columns used in the transposition.

    Returns:
        str: The encrypted ciphertext.
    """
    ciphertext = [''] * key  # Create an empty list for each column
    no_space = plaintext.replace(" ", "")  # Remove spaces from plaintext

    # Populate each column in the ciphertext
    for column in range(key):
        current_index = column
        while current_index < len(no_space):
            ciphertext[column] += no_space[current_index]
            current_index += key

    return ''.join(ciphertext)  # Concatenate all columns to form the final ciphertext


def decrypt(ciphertext, key):
    """
    Decrypts a given ciphertext encrypted using a columnar transposition cipher.

    Args:
        ciphertext (str): The encrypted text.
        key (int): The number of columns used in the transposition.

    Returns:
        str: The decrypted plaintext.
    """
    ciphertext = ciphertext.replace(" ", "")
    rows = math.ceil(len(ciphertext) / key)  # Number of rows in the grid
    plaintext = [''] * rows  # Prepare rows for the plaintext output

    # Calculate any excess characters in the last column
    excess = round((len(ciphertext) / key - len(ciphertext) // key) * key)

    current_index = 0
    counter = 0
    for column in range(key):
        for row in range(rows):
            if current_index == len(ciphertext) or (row == rows - 1 and counter == excess and excess != 0):
                break
            plaintext[row] += ciphertext[current_index]
            current_index += 1
        if row == rows - 1:
            counter += 1

    return ''.join(plaintext)


def frequency_score(text):
    """
    Scores the text based on the frequency of character pairs in the English language.

    Args:
        text (str): The text to score.

    Returns:
        int: The score based on English character pair frequencies.
    """
    # Frequency matrix of English character pairs (from a-z)
    FrequencyOfCharacterPairsInEnglishLanguageText = [
        [1, 20, 33, 52, 0, 12, 18, 5, 39, 1, 12, 57, 26, 181, 1, 20, 1, 75, 95, 104, 9, 20, 13, 1, 26, 1],
        [11, 1, 0, 0, 47, 0, 0, 0, 6, 1, 0, 17, 0, 0, 19, 0, 0, 11, 2, 1, 21, 0, 0, 0, 11, 0],
        [31, 0, 4, 0, 38, 0, 0, 38, 10, 0, 18, 9, 0, 0, 45, 0, 1, 11, 1, 15, 7, 0, 0, 0, 1, 0],
        [48, 20, 9, 13, 57, 11, 7, 25, 50, 3, 1, 11, 14, 16, 41, 6, 0, 14, 35, 56, 10, 2, 19, 0, 10, 0],
        [110, 23, 45, 126, 48, 30, 15, 33, 41, 3, 5, 55, 47, 111, 33, 28, 2, 169, 115, 83, 6, 24, 50, 9, 26, 0],
        [25, 2, 3, 2, 20, 11, 1, 8, 23, 1, 0, 8, 5, 1, 40, 2, 0, 16, 5, 37, 8, 0, 3, 0, 2, 0],
        [24, 3, 2, 2, 28, 3, 4, 35, 18, 1, 0, 7, 3, 4, 23, 1, 0, 12, 9, 16, 7, 0, 5, 0, 1, 0],
        [114, 2, 2, 1, 302, 2, 1, 6, 97, 0, 0, 2, 3, 1, 49, 1, 0, 8, 5, 32, 8, 0, 4, 0, 4, 0],
        [10, 5, 32, 33, 23, 17, 25, 6, 1, 1, 8, 37, 37, 179, 24, 6, 0, 27, 86, 93, 1, 14, 7, 2, 0, 2],
        [2, 0, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0],
        [6, 1, 1, 1, 29, 1, 0, 2, 14, 0, 0, 2, 1, 9, 4, 0, 0, 0, 5, 4, 1, 0, 2, 0, 2, 0],
        [40, 3, 2, 36, 64, 10, 1, 4, 47, 0, 3, 56, 4, 2, 41, 3, 0, 2, 11, 15, 8, 3, 5, 0, 31, 0],
        [44, 7, 1, 1, 68, 2, 1, 3, 25, 0, 0, 1, 5, 2, 29, 11, 0, 3, 10, 9, 8, 0, 4, 0, 18, 0],
        [40, 7, 25, 146, 66, 8, 92, 16, 33, 2, 8, 9, 7, 8, 60, 4, 1, 3, 33, 106, 6, 2, 12, 0, 11, 0],
        [16, 12, 13, 18, 5, 80, 7, 11, 12, 1, 13, 26, 48, 106, 36, 15, 0, 84, 28, 57, 115, 12, 46, 0, 5, 1],
        [23, 1, 0, 0, 30, 1, 0, 3, 12, 0, 0, 15, 1, 0, 21, 10, 0, 18, 5, 11, 6, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0],
        [50, 7, 10, 20, 133, 8, 10, 12, 50, 1, 8, 10, 14, 16, 55, 6, 0, 14, 37, 42, 12, 4, 11, 0, 21, 0],
        [67, 11, 17, 7, 74, 11, 4, 50, 49, 2, 6, 13, 12, 10, 57, 20, 2, 4, 43, 109, 20, 2, 24, 0, 4, 0],
        [59, 10, 11, 7, 75, 9, 3, 330, 76, 1, 2, 17, 11, 7, 115, 4, 0, 28, 34, 56, 17, 1, 31, 0, 16, 0],
        [7, 5, 12, 7, 7, 2, 14, 2, 8, 0, 1, 34, 8, 36, 1, 16, 0, 44, 35, 48, 0, 0, 2, 0, 1, 0],
        [5, 0, 0, 0, 65, 0, 0, 0, 11, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [66, 1, 1, 2, 39, 1, 0, 44, 39, 0, 0, 2, 1, 12, 29, 0, 0, 3, 4, 4, 1, 0, 2, 0, 1, 0],
        [1, 0, 2, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0],
        [18, 7, 6, 6, 14, 7, 3, 10, 11, 1, 1, 4, 6, 3, 36, 4, 0, 3, 19, 20, 1, 1, 12, 0, 2, 0],
        [1, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    score = 0
    text = text.lower()

    # Calculate score based on the frequency of character pairs
    for i in range(1, len(text)):
        left = ord(text[i - 1]) - 97  # Convert character to index (0 for 'a', 1 for 'b', etc.)
        right = ord(text[i]) - 97
        score += FrequencyOfCharacterPairsInEnglishLanguageText[left][right]

    return score


def break_cipher(ciphertext):
    """
    Attempts to break the cipher by testing different key lengths and evaluating the frequency score.

    Args:
        ciphertext (str): The encrypted text.

    Returns:
        str: The most likely decrypted message based on frequency analysis.
    """
    plaintext_variations = [''] * len(ciphertext)  # Store plaintext guesses for each key length
    frequency_scores = [0] * len(ciphertext)  # Store frequency scores for each key length

    # Try decrypting with different key lengths and score them
    for key in range(1, len(ciphertext)):
        plaintext_variations[key] = decrypt(ciphertext, key)
        frequency_scores[key] = frequency_score(plaintext_variations[key])

    # Find the key that gives the highest frequency score
    max_value = 0
    max_index = 0
    for i in range(1, len(frequency_scores)):
        if frequency_scores[i] > max_value:
            max_value = frequency_scores[i]
            max_index = i

    return plaintext_variations[max_index]  # Return the best guess for the plaintext


if __name__ == '__main__':
    main()
