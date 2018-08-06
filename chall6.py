#!/usr/bin/env python3
from base64 import b64decode
from chall2 import xor
from chall3 import singleCharXorBruteforce, score
from chall5 import xorExtendedKey
import timeit

def hammingDistance(lhs, rhs):
	dist = 0
	for byte in xor(lhs, rhs):
		dist += bin(byte).count("1")
	return dist

def findKeySize(inputData):
	normalizedDistances = []
	for KEYSIZE in range(2, 41):
		inputData1 = inputData[:KEYSIZE]
		inputData2 = inputData[KEYSIZE:KEYSIZE*2]
		inputData3 = inputData[KEYSIZE*2:KEYSIZE*3]
		inputData4 = inputData[KEYSIZE*3:KEYSIZE*4]
		normalizedDistance = float(
			hammingDistance(inputData1, inputData2)+
			hammingDistance(inputData2, inputData3)+
			hammingDistance(inputData3, inputData4)
		)/(KEYSIZE*3)
		normalizedDistances.append((KEYSIZE, normalizedDistance))
	return sorted(normalizedDistances, key=lambda y: y[1])

def crackRepeatingXor(inputData, inputDistances):
	plainCandidates = []
	for data in inputDistances:
		key = b''
		for i in range(data[0]):
			block = b''
			for j in range(i, len(inputData), data[0]):
				block += bytes([inputData[j]])
			key += bytes([singleCharXorBruteforce(block)[1]])
		plainCandidates.append((xorExtendedKey(inputData, key), key))
	return max(plainCandidates, key=lambda k: score(k[0]) )

def main():
	start = timeit.default_timer()
	with open("chall6.txt", "r") as f:
		data = b64decode(f.read())
	plain, key = crackRepeatingXor(data, findKeySize(data)[:5])
	print("\x1b[6;30;42mCozulen metin:\x1b[0m\n"+plain.decode()+"\n\x1b[6;30;42mAnahtar:\x1b[0m\n"+key.decode())
	stop = timeit.default_timer()

if __name__ == "__main__":
	main()