#!/usr/bin/env python3
from base64 import b64encode

def main():
    hexString = bytes.fromhex(input("? "))
    base64String = b64encode(hexString).decode()
    print(base64String)

if __name__=="__main__":
    main()
