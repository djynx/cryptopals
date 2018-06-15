#!/usr/bin/env python3
import codecs

def score(tex):
    charmap = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.'\n"
    score = 0
    for c in tex:
        if (c in charmap or c == ' ' or c == '\''):
            score+=1
    return score

def singleXor(lhs, rhs):
    string = ""
    for i in range(0, len(lhs)):
        string += chr(ord(lhs[i]) ^ ord(rhs[i%len(rhs)]))
    return string

def main():
    scoreHold = 0
    xord = input("? ")
    for i in range(1,256):
        c = singleXor(codecs.decode(xord,"hex").decode("utf-8"), chr(i))
        if score(c) > scoreHold:
            scoreHold = score(c)
            key = i
            best = c
    print("Plain: ", best,"\nKey: ", chr(i))

if __name__ == "__main__":
    main()
