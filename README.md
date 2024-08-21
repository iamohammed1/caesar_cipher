# caesar_cipher







try:
    import pyperclip
except ImportError:
    pass

# every possible symbol that can be encrypted/decrypted
# you can add numbers
# symbols as well.
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Caesar Cipher, by Mohammed Almokhtar Mohammed.a.mokhtar01@gmail.com')
print('The Caesar cipher encrypts letters by shifting them over by a')
print('key number. For example, a key of 2 means the letter A is')
print('encrypted into C, the letter B encrypted into D, and so on.')
print()

# let the user enter if they are encrypting ot decrypting:
while True: # ;eep;asling until the user enters e or d.
    print('Do you want to (e)ncrypt or  (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('please enter the letter e or d.')

# let user enter the key to use:
while True:
    maxKey = len(SYMBOLS) - 1
    print(f'Please enter the key (0 to {maxKey} to use)')
    response = input('> ').upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

# let the user enter the message to encrypt/decrypt:
print(f'Enter the message to {mode}')
message = input('> ')

# Caesar cipher only works on uppercase letters:
message = message.upper()

# stores the encrypted/decrypted form of the message:
translated = ''

# encrypted/decrypted  each symbol in the message:
for symbol in message:
    if symbol in SYMBOLS:
        # Get the encrypted (or decrypted) number for this symbol.
        num = SYMBOLS.find(symbol) # get the number of the symbol
        if mode == 'encrypt':
            num += key
        elif mode == 'decrypt':
            num -= key

        # Handle the wrap-around if num is larger than the length of
        # # SYMBOLS or less than 0:
        if num >= len(SYMBOLS):
            num -= len(SYMBOLS)
        elif num < 0:
            num += len(SYMBOLS)

        # add encrypted/ decrypted number's symbol to traslated:
        translated += SYMBOLS[num]
    else:
        # just add the symbol without encrypting/decrypting:
        translated += symbol

# display the encrypted/decrypted string to the screen:
print(translated)

try:
    pyperclip.copy(translated)
    print(f'Full {mode}ed text coped to clipboard.')
except:
    pass
