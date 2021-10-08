# Substitution Cipher (BSD Licensed)

import sys

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt_files(key):

    input_name = ''
    output_name = ''

    for i in range(1, 8):

        input_name = 'plain_input' + str(i) + '.txt'
        output_name = 'encr_output' + str(i) + '.txt'

        f = open(input_name, 'r')
        plain_text = f.read()

        translated = encryptMessage(key, plain_text)

        g = open(output_name, 'w')
        g.write(translated)
        
def main():
           #'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    myKey = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    #myKey = 'DIOPYBFQJZUHVCRGESKNATMWLX'

    checkValidKey(myKey)

    encrypt_files(myKey)

def checkValidKey(key):
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()
    if keyList != lettersList:
        sys.exit('This is not a valid monoalphabetic substitution cipher key!')

def encryptMessage(key, message):
    translated = ''
    charsA = LETTERS
    charsB = key

    for symbol in message:
        if symbol.upper() in charsA:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            # symbol is not in LETTERS, just add it
            translated += symbol

    return translated

if __name__ == "__main__":
    main()

