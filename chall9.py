#!/usr/bin/env python3
from chall15 import isPkcsPadded

def pkcsPadding(inputBytes, blockSize):
    if len(inputBytes) == blockSize:
        return inputBytes
    pad = blockSize - len(inputBytes) % blockSize
    return inputBytes  + bytes([pad]*pad)

def pkcsUnpadding(inputBytes):
    if len(inputBytes) == 0:
        raise Exception("Girdi bos olamaz")
    if not isPkcsPadded(inputBytes):
        return inputBytes
    padding = inputBytes[len(inputBytes) - 1]
    return inputBytes[:-padding]

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