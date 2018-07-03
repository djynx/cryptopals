#!/usr/bin/env python3
from base64 import b64decode
from Crypto.Cipher import AES

def main():
    cipher = b64decode(open('chall7.txt','r').read())
    obj = AES.new(b'YELLOW SUBMARINE')
    plain = obj.decrypt(cipher)
    print(plain)

if __name__ == "__main__":
    main()
