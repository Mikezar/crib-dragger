import binascii

def XOR(cipher1, cipher2):
    if type(cipher1) is str:
        cipher1 = cipher1.encode()

    if type(cipher2) is str:
        cipher2 = cipher2.encode()

    if len(cipher1) > len(cipher2):
        return "".join([chr(x ^ y) for (x, y) in zip(cipher1[:len(cipher2)], cipher2)])
    else:
        return "".join([chr(x ^ y) for (x, y) in zip(cipher1, cipher2[:len(cipher1)])])

def decode(cts):
    cypherTextsDecoded = []

    for ct in cts:
        cypherTextsDecoded.append(binascii.unhexlify(ct))

    return cypherTextsDecoded

def crib(xOredText, crib):
    lnth = len(xOredText)

    result = []
    for i in range(lnth):
        substrXoredText = xOredText[i:]
        cribDraggedText = XOR(substrXoredText, crib)

        result.append((i, cribDraggedText))
    return result
