#!/usr/bin/env python3

def pkcsPadding(inputBytes, blockSize):
    if len(inputBytes) == blockSize:
        return inputBytes
    pad = blockSize - len(inputBytes) % blockSize
    return inputBytes  + bytes([pad]*pad)

def pkcsUnpadding(inputBytes):
    for byte in inputBytes[-inputBytes[-1]:]:
        if byte != inputBytes[-1]:
            return inputBytes
    return inputBytes[:-inputBytes[len(inputBytes)-1]]

def main():
    given = input("mesaj? ")
    block = input("blok boyutu? ")
    print("mesaj: ", given)
    padded = pkcsPadding(given.encode(), int(block))
    print("sabitlenmis boyutlu mesaj: ", padded)
    unpadded = pkcsUnpadding(padded)
    print("geri dondurulmus mesaj: ", unpadded)

if __name__ == "__main__":
    main()