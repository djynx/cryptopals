#!/usr/bin/env python3
from base64 import b64decode,b64encode
from Crypto.Cipher import AES

def AES_ECB_Encrypt(plain,key):
    obj = AES.new(key)
    cipher = obj.encrypt(plain)
    return cipher

def AES_ECB_Decrypt(cipher,key):
    obj = AES.new(key)
    plain = obj.decrypt(cipher)
    return plain

def main():
    cipher = b64decode(open('chall7.txt','r').read())
    key = b'YELLOW SUBMARINE'
    print(AES_ECB_Decrypt(cipher,key).decode())

if __name__ == "__main__":
    main()
