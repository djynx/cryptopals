#!/usr/bin/env python3

def xor(lhs,rhs): #byte tipinde iki veriyi 1. verinin boyutu kadarlik kisimlarinda xorlar
    res = b''
    for i in range(len(lhs)):
        res += bytes([lhs[i] ^ rhs[i]])
    return res

def main():
    first = input("1? ")
    second = input("2? ")
    print("sonuc: ",xor(bytes.fromhex(first), bytes.fromhex(second)).hex())

if __name__ == "__main__":
    main()
