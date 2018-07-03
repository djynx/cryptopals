#!/usr/bin/env python3

def xor(lhs,rhs): #bytearray tipinde iki veriyi 1. verinin boyutu kadarlik kisimlarinda xorlar
    for i in range(len(lhs)):
        lhs[i] ^= rhs[i]
    return lhs

def main():
    first = input("1? ")
    second = input("2? ")
    print("sonuc: ",xor(bytearray.fromhex(first), bytearray.fromhex(second)).hex())

if __name__ == "__main__":
    main()
