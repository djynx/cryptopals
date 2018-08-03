#!/usr/bin/env python3
from chall2 import xor

def xorExtendedKey(plain, key):
	ciphertext = b''
	for i in range(0,len(plain)):
		ciphertext += bytes([plain[i] ^ key[i%len(key)]])
	return ciphertext

def main():
    plain= b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = b'ICE'
    print(xorExtendedKey(plain, key).hex())

if __name__ == "__main__":
    main()
