#!/usr/bin/env python3

import os
from random import randint
from chall7 import AES_ECB_Encrypt
from chall8 import countDuplicateBlocks
from chall10 import AES_CBC_Encrypt

def encrypt(inputData, inputKey):
    if randint(0, 1) == 0:
        return AES_ECB_Encrypt(inputData,inputKey), "ECB"
    else:
        return AES_CBC_Encrypt(inputData,len(inputKey),inputKey), "CBC"

def randomPadding(inputData):
    return os.urandom(randint(5,10))+inputData+os.urandom(randint(5,10))

def oracle(inputData):
    if  countDuplicateBlocks(inputData) > 0:
        return "ECB"
    else:
        return "CBC"

def main():
    randomData = bytes([randint(0,10)]*80)
    key = os.urandom(16)
    inputData = randomPadding(randomData)
    cipher, mode = encrypt(inputData,key)
    if mode == "CBC":
        cipher = cipher[0]
    oracleMode = oracle(cipher)
    print("Mod:",mode)
    print("Tahmin edilen mod:",oracleMode)
    if mode == oracleMode:
        print("Basarili!")
    else:
        print("Basarisiz!")

if __name__ == "__main__":
    main()
