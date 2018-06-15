#!/usr/bin/env python3
import codecs

def xor(lhs,rhs):
    xord = ""
    for i in range(0, len(lhs)):
        xord += hex(ord(lhs[i]) ^ (ord(rhs[i]))).lstrip("0x")
    return xord

def main():
    plain="Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = "ICE"
    extendedKey=""
    for i in range(0,len(plain)):
         extendedKey+=key[i%len(key)]
    print(xor(plain,extendedKey))

if __name__ == "__main__":
    main()
