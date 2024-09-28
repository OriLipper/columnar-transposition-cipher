
# Columnar Transposition Cipher

## Overview

This project implements a **Columnar Transposition Cipher**, a classical encryption technique used in cryptography. It includes functions to:
- Encrypt plaintext using a columnar transposition method.
- Decrypt ciphertext using the corresponding key.
- Break the cipher using frequency analysis to deduce the correct key.

The project is built in Python and can be run via the command line or integrated into other Python applications. This is a great example of classical cryptography in action.

## Features

1. **Encryption**: Encrypt plaintext using a specified key.
2. **Decryption**: Decrypt ciphertext using the correct key.
3. **Cipher Breaking**: Break the cipher using frequency analysis.

## Installation

### Prerequisites

- Python 3.x must be installed on your system.
- Ensure you have the required dependencies listed in `requirements.txt`.

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/OriLipper/columnar-transposition-cipher.git
   ```

2. Navigate into the project directory:
   ```bash
   cd columnar-transposition-cipher
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Encryption Example
To encrypt a message, use the `encrypt()` function:

```python
from main import encrypt
plaintext = "HELLO WORLD"
key = 4
encrypted_message = encrypt(plaintext, key)
print(encrypted_message)
```

### Decryption Example
To decrypt a message, use the `decrypt()` function:

```python
from main import decrypt
ciphertext = "HOLEWDLORL"
key = 4
decrypted_message = decrypt(ciphertext, key)
print(decrypted_message)
```

### Breaking the Cipher
To attempt to break the cipher without knowing the key, use the `break_cipher()` function:

```python
from main import break_cipher
ciphertext = "HOLEWDLORL"
broken_message = break_cipher(ciphertext)
print(broken_message)
```

## Running Tests

Tests are included in the `tests/` directory. You can run the tests using the following command:

```bash
python -m unittest discover -s tests
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
