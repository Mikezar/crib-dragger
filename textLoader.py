import os

def loadCiphers():
    pathToFile = input('Enter path to the .txt file with ciphertexts split per line:')

    if pathToFile == "":
        loadCiphers()

    if os.path.exists(pathToFile) == False:
        print('File wasn\'t found')
        loadCiphers()

    with open(pathToFile, 'rb') as file:
        texts = [line.rstrip() for line in file]

    return texts