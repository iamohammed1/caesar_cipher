
# Caesar Cipher

![image](https://github.com/user-attachments/assets/9aae5c1f-3306-451b-a6c1-93aa1d947fa0)

# Caesar Cipher Web Application

A Django-based web application that implements the Caesar cipher encryption and decryption algorithm.

## Features

- Encrypt and decrypt messages using the Caesar cipher
- Responsive web interface with Bootstrap styling
- Copy to clipboard functionality for results
- Green-themed UI that matches Django's aesthetic

## How It Works

The Caesar cipher is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

### Encryption Process
1. The user selects the "Encrypt" mode
2. Enter a message to encrypt
3. Specify a key (0-25)
4. Each letter in the message is shifted forward through the alphabet by the key value

### Decryption Process
1. The user selects the "Decrypt" mode
2. Enter an encrypted message
3. Specify the key that was used for encryption
4. Each letter in the message is shifted backward through the alphabet by the key value

## Installation

1. Clone the repository:
