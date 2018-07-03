#!/usr/bin/env python3
import codecs,sys
from chall3 import singleCharXorBruteforce

def detectBest(inputData): #her satir icin once ayri ayri skor hesaplayip en yuksek skorlu olanlari bulur,
    res = b''              #sonra da satirlarin skorlarindan en yuksek olani, anahtarini, skorunu. satirini dondurur.
    resKey = 0
    scoreHold = 0
    lineT = 0
    for string in inputData:
        lineT +=1
        plain, key, score = singleCharXorBruteforce(string)
        if score > scoreHold:
            scoreHold = score
            res = plain
            resKey = key
            line = lineT
    return res, resKey, scoreHold, line

def main():
    candidates = [bytes.fromhex(line.strip()) for line in open("chall4.txt")]
    plain, key, score, line = detectBest(candidates)
    print("\nSatir ",line,"\nPlain: ",plain.decode(),"\bAnahtar: ",key,"\nSkor: ",score)

if __name__ == "__main__":
    main()

