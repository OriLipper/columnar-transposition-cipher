
# Columnar Transposition Cipher Project

## Overview

This project implements a **Columnar Transposition Cipher**, a classical encryption technique used in cryptography. The project includes functions to:
- Encrypt plaintext using a columnar transposition method.
- Decrypt ciphertext using the corresponding key.
- Break the cipher by analyzing character frequency to deduce the correct key.

The project demonstrates basic cryptographic principles and offers an introduction to frequency analysis for breaking simple ciphers.

## How It Works

### Columnar Transposition Cipher
The **Columnar Transposition Cipher** is a type of transposition cipher where the plaintext is written into columns. The columns are then rearranged according to a key, and the ciphertext is formed by reading the columns in sequence.

#### Example
Consider the message `HELLO WORLD` and a key of `4`. The message, without spaces, is written in columns as:

```
H E L L
O W O R
L D
```

The ciphertext is formed by reading the columns sequentially: `H O L E W D L O R L`.

### Cipher Breaking
To break the cipher, we use **frequency analysis**, a technique that evaluates how frequently character pairs appear in the decrypted text. By comparing the frequency of letter pairs in the decrypted text with common English frequencies, we can infer the correct key length and thus retrieve the plaintext.

## Features

1. **Encryption**: Encrypts plaintext using a key that specifies how many columns the text is divided into.
2. **Decryption**: Decrypts the ciphertext by reversing the columnar transposition based on the given key.
3. **Cipher Breaking**: Attempts to break the cipher by guessing the key length using frequency analysis.

## Usage

This project is intended for educational purposes and demonstrates basic cryptographic techniques in Python. It can be run via the command line or integrated into other Python applications.

## Dependencies

- Python 3.x
- `math` library (comes with Python standard libraries)

## Folder Structure

```
project-root/
│
├── src/                 # Contains source code for encryption, decryption, and cipher-breaking
│   └── main.py          # Main script that runs the cipher operations
│
├── docs/                # Documentation for the project
│   └── index.md         # Project overview (this file)
│
├── tests/               # Unit tests for the encryption and decryption functions
│
├── README.md            # General information and quick start guide
└── LICENSE              # License for the project
```

## Example

### Encryption
```python
plaintext = "HELLO WORLD"
key = 4
encrypted_message = encrypt(plaintext, key)
print(encrypted_message)
```

Output:
```
"HOLEWDLORL"
```

### Decryption
```python
ciphertext = "HOLEWDLORL"
key = 4
decrypted_message = decrypt(ciphertext, key)
print(decrypted_message)
```

Output:
```
"HELLOWORLD"
```

### Breaking the Cipher
```python
ciphertext = "HOLEWDLORL"
broken_message = break_cipher(ciphertext)
print(broken_message)
```

Output (depends on accuracy of frequency analysis):
```
"HELLOWORLD"
```

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.
