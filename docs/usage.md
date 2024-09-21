
# Usage Instructions

This document explains how to install, run, and use the Columnar Transposition Cipher project.

## Installation

To run this project, you need to have Python 3.x installed on your system.

### Steps:
1. Clone the repository or download the source files:
   ```bash
   git clone https://github.com/yourusername/columnar-transposition-cipher.git
   ```
2. Navigate to the project directory:
   ```bash
   cd columnar-transposition-cipher
   ```
3. Ensure Python 3.x is installed on your system. You can check by running:
   ```bash
   python --version
   ```

## Running the Project

You can run the `main.py` script, which includes sample demonstrations of the encryption, decryption, and cipher-breaking functionality.

### Running Encryption

To encrypt a message, you can modify the `main()` function in `main.py` or use the encrypt function directly:

```python
plaintext = "HELLO WORLD"
key = 4
encrypted_message = encrypt(plaintext, key)
print(encrypted_message)
```

Output:
```
HOLEWDLORL
```

### Running Decryption

To decrypt a message, use the decrypt function with the ciphertext and the same key:

```python
ciphertext = "HOLEWDLORL"
key = 4
decrypted_message = decrypt(ciphertext, key)
print(decrypted_message)
```

Output:
```
HELLOWORLD
```

### Breaking the Cipher

If the key is unknown, you can use the `break_cipher()` function to attempt to deduce it using frequency analysis:

```python
ciphertext = "HOLEWDLORL"
broken_message = break_cipher(ciphertext)
print(broken_message)
```

Output (depends on accuracy of frequency analysis):
```
HELLOWORLD
```

## Common Errors and Troubleshooting

- **Incorrect key for decryption**: Make sure that the same key used for encryption is provided for decryption.
- **Cipher-breaking fails**: The frequency analysis used for breaking the cipher is more accurate with longer texts, so it may not work well with very short ciphertexts.

