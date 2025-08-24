from django.shortcuts import render
from .forms import CaesarCipherForm

def caesar_cipher(message, key, mode):
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    message = message.upper()
    translated = ''
    
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)
            if mode == 'encrypt':
                num += key
            elif mode == 'decrypt':
                num -= key

            if num >= len(SYMBOLS):
                num -= len(SYMBOLS)
            elif num < 0:
                num += len(SYMBOLS)

            translated += SYMBOLS[num]
        else:
            translated += symbol
    
    return translated

def index(request):
    result = ''
    if request.method == 'POST':
        form = CaesarCipherForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            key = form.cleaned_data['key']
            mode = form.cleaned_data['mode']
            result = caesar_cipher(message, key, mode)
    else:
        form = CaesarCipherForm()
    
    return render(request, 'cipher_app/index.html', {'form': form, 'result': result})
