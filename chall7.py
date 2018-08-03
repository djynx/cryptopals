#!/usr/bin/env python3
from base64 import b64decode,b64encode
from Crypto.Cipher import AES
from chall9 import pkcsPadding,pkcsUnpadding

def AES_ECB_Encrypt(plain,key):
    obj = AES.new(key)
    return obj.encrypt(pkcsPadding(plain, len(key)))

def AES_ECB_Decrypt(cipher,key):
    obj = AES.new(key)
    return pkcsUnpadding(obj.decrypt(cipher))

def main():
    cipher = b64decode(open('chall7.txt','r').read())
    key = b'YELLOW SUBMARINE'
    print(AES_ECB_Decrypt(cipher,key)[0].decode())

if __name__ == "__main__":
    main()
