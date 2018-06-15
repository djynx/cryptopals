#!/usr/bin/env python3

def x0r(lhs,rhs):
    return ((hex(int(lhs, 16) ^ int(rhs, 16))).lstrip("0x"))

first = input("1? ")
second = input("2? ")
print(x0r(first, second))
