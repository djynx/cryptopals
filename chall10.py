#!/usr/bin/env python3
import os
from base64 import b64decode
from chall2 import xor
from chall7 import AES_ECB_Decrypt,AES_ECB_Encrypt
from chall9 import pkcsPadding,pkcsUnpadding

def AES_CBC_Encrypt(plain, bs, key, iv=None):
    cipher = b''
    plain = pkcsPadding(plain, bs)
    if iv == None:
        iv = os.urandom(bs)
    for i in range(int(len(plain)/bs)):
        block = plain[(i*bs):(i+1)*bs]
        if i == 0:
            block = xor(block, iv)
        else:
            block = xor(block, cipher[(i-1)*bs:i*bs])
        block = AES_ECB_Encrypt(block,key)
        cipher += block
    return cipher, iv

def AES_CBC_Decrypt(cipher,bs,key,iv):
    plain = b''
    for i in range(int(len(cipher)/bs)):
        block = cipher[(i*bs):(i+1)*bs]
        block = AES_ECB_Decrypt(block, key)
        if i == 0:
            plain += xor(block, iv)
        else:
            plain += xor(block, cipher[(i-1)*bs:i*bs])
    print(plain)
    return pkcsUnpadding(plain), iv

def main():
    given = b64decode(open('chall10.txt', 'r').read())
    key = b'YELLOW SUBMARINE'
    iv=bytes([0]*len(key))
    plain, iv = AES_CBC_Decrypt(given, len(key), key, iv)
    print(plain.decode())

if __name__ == "__main__":
    main()
