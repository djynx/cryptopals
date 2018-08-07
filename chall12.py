#!/usr/bin/env python3

import os
from base64 import b64decode
from random import randint
from chall7 import AES_ECB_Encrypt
from chall8 import countDuplicateBlocks
from chall9 import pkcsUnpadding
from chall11 import oracle

class oracle:
    def __init__(self, padding):
        self._unknownKey = os.urandom(16)
        self._unknownPadding = padding
    def encrypt(self, data):
        return AES_ECB_Encrypt(data + self._unknownPadding, self._unknownKey)

def findBlockSize(oracleObj):
    paddingData = b""
    cipher = oracleObj.encrypt(paddingData)
    firstLen = len(cipher)
    newLen = firstLen
    while newLen == firstLen:
        paddingData += b'A'
        cipher = oracleObj.encrypt(paddingData)
        newLen = len(cipher)
    return newLen - firstLen

def findNext(oracleObj, current, blockSize):
    size = (blockSize - (1 + len(current))) % blockSize
    prefix = b'A' * size
    crackingSize = size + len(current) + 1
    cipher = oracleObj.encrypt(prefix)
    for i in range(256):
        fakeCipher = oracleObj.encrypt(prefix + current + bytes([i]))
        if fakeCipher[:crackingSize] == cipher[:crackingSize]:
           	return bytes([i])
    return b''

def Byte_At_A_Time_ECB_Decryption_S(oracleObj):
    blockSize = findBlockSize(oracleObj)
    if countDuplicateBlocks(oracleObj.encrypt(b'A'*64)) > 0:
        mode = "ECB"
    else:
        print("Mod CBC, islem gecersiz.")
        os._exit(1)
    plain = b''
    for i in range(len(oracleObj.encrypt(b''))):
        plain += findNext(oracleObj, plain, blockSize)
    return plain, blockSize


def main():
    givenSuffix = b64decode("Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGF"
                            "pciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IH"
							"RvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK")
    ecbOracle = oracle(givenSuffix)
    plain, bs = Byte_At_A_Time_ECB_Decryption_S(ecbOracle)
    print(pkcsUnpadding(plain).decode())


if __name__ == "__main__":
    main()
