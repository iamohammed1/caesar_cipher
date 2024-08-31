# Caesar Cipher

This is a simple Caesar Cipher program created by Mohammed Almokhtar. The Caesar Cipher is a type of substitution cipher where each letter in the plaintext is shifted by a certain number of places down or up the alphabet.

## How It Works

The Caesar Cipher shifts letters in the message by a specified key. For example, with a key of 2:
- A becomes C
- B becomes D
- Z wraps around to B

The user can choose to either encrypt or decrypt a message.

## Usage

### Encrypting a Message

1. Run the program and choose the option to encrypt by entering `e`.
2. Enter the key, a number between 0 and 25, to shift the letters.
3. Enter the message you want to encrypt.
4. The program will display the encrypted message.

### Decrypting a Message

1. Run the program and choose the option to decrypt by entering `d`.
2. Enter the key that was used to encrypt the message.
3. Enter the encrypted message.
4. The program will display the decrypted message.

### Example

Encrypting with a key of 3:
- Plaintext: `HELLO`
- Ciphertext: `KHOOR`

Decrypting with the same key of 3:
- Ciphertext: `KHOOR`
- Plaintext: `HELLO`

## Installation

Ensure you have Python installed on your system. The program also uses the `pyperclip` module to copy the result to the clipboard. You can install it via pip:

```bash
pip install pyperclip
To run the program, use the following command:
python caesar_cipher.py
Contact
Created by Mohammed Almokhtar
Email: mohammed.a.mokhtar01@gmail.com

Acknowledgments
This program is a classic example often used to demonstrate basic cryptography concepts.

