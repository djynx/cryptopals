#!/usr/bin/env python3
from chall2 import xor

def main():
    plain="Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = "ICE"
    extendedKey=""
    for i in range(0,len(plain)):
         extendedKey+=key[i%len(key)]
    print((xor(bytearray(plain.encode()),bytearray(extendedKey.encode()))).hex())

if __name__ == "__main__":
    main()
