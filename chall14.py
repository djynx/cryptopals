#!/usr/bin/env python3
import os
from base64 import b64decode
from random import randint
from chall7 import AES_ECB_Encrypt
from chall9 import pkcsUnpadding
from chall8 import countDuplicateBlocks
from chall12 import findBlockSize

class oracle():
	def __init__(self, padding):
		self._unknownKey = os.urandom(16)
		self._unknownPadding = padding
		self._randomPrefix = os.urandom(randint(0, 128))
	def encrypt(self, data):
		return AES_ECB_Encrypt(self._randomPrefix + data + self._unknownPadding, self._unknownKey)

def findPrefixLength(oracleObj,blockSize):
	noChar = oracleObj.encrypt(b'')
	oneChar = oracleObj.encrypt(b' ')
	whichBlock=0
	for i in range(0,len(oneChar),blockSize):
		if noChar[i:i+blockSize] != oneChar[i:i+blockSize]:
			whichBlock = int(i/blockSize)
			break
	for i in range(blockSize):
		data = b'\x00'*(2*blockSize+i)
		cipher = oracleObj.encrypt(data)
		check = False
		for j in range(0, len(cipher) - 1, blockSize):
			if cipher[j:j+blockSize] == cipher[j+blockSize:j+2*blockSize]:
				check = True
		if check==True:
			return ((whichBlock+1)*blockSize)-i if i != 0 else whichBlock*blockSize

def findNextH(oracleObj, blockSize, prefixLength, current):
    roundLen = (blockSize - prefixLength - (1 + len(current))) % blockSize
    crafted = b' ' * roundLen
    crackLen = prefixLength + roundLen + len(current) + 1
    result = oracleObj.encrypt(crafted)
    for i in range(256):
        fakeCipher = oracleObj.encrypt(crafted + current + bytes([i]))
        if result[:crackLen] == fakeCipher[:crackLen]:
            return bytes([i])
    return b''

def Byte_At_A_Time_ECB_Decryption_H(oracleObj):
    blockSize = findBlockSize(oracleObj)
    if countDuplicateBlocks(oracleObj.encrypt(b'A'*64)) > 0:
        mode = "ECB"
    else:
        print("Mod CBC, islem gecersiz.")
        os._exit(1)
    prefixLength = findPrefixLength(oracleObj,blockSize)
    targetLength = len(oracleObj.encrypt(b'')) - prefixLength
    result = b''
    for i in range(targetLength):
    	result += findNextH(oracleObj, blockSize, prefixLength, result)
    return result

def main():
	givenData = b64decode("Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGF"
                          "pciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IH"
					      "RvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK")
	ecbOracle = oracle(givenData)
	print(Byte_At_A_Time_ECB_Decryption_H(ecbOracle).decode())
	

if __name__ == "__main__":
	main()