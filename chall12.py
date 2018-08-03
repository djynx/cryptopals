#!/usr/bin/env python3

import os
from base64 import b64decode
from random import randint
from chall7 import AES_ECB_Encrypt
from chall8 import countDuplicateBlocks
from chall9 import pkcsPadding
from chall11 import oracle

class oracle:

    def __init__(self, padding):
        self._unknownKey = os.urandom(16)
        self._unknownPadding = padding

    def encrypt(self, data):
        return AES_ECB_Encrypt(data + self._unknownPadding, self._unknownKey)

def findBlockSize(oracleObj):
    paddingData = b''
    cipher = oracleObj.encrypt(paddingData)
    firstLen = len(cipher)
    newLen = firstLen
    while newLen == firstLen:
        paddingData += b'A'
        cipher = oracleObj.encrypt(paddingData)
        newLen = len(cipher)
    return newLen - firstLen

def findNextBlock(oracle, current, blockSize, blockNumber):


def Byte_At_A_Time_ECB_Decryption_S(oracleObj):
    blockSize = findBlockSize(oracleObj)
    if countDuplicateBlocks(oracleObj.encrypt(b'A'*32)) > 0:
        mode = "ECB"
    else:
        print("Mod CBC, islem gecersiz.")
        os._exit(1)
    plain = b''
    for i in range( ):
        plain += findNextBlock(oracleObj, plain, blockSize, i)
    return plain


def main():
    given = b64decode("Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg"
                      "aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq"
                      "dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg"
                      "YnkK")
    ecbOracle = oracle(given)
    print(Byte_At_A_Time_ECB_Decryption_S(ecbOracle))


if __name__ == "__main__":
    main()
