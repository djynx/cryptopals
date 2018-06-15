#!/usr/bin/env python3
import codecs,sys
from third import singleXor, score

def main():
    scoreHold = 0
    lineNumberHold = 0
    for line in open("fourth.txt", "r"):
        lineNumberHold += 1
        line = line.rstrip()
        for i in range(1, 256):
            c = singleXor(codecs.decode(line,"hex").decode("latin-1"), chr(i))
            if score(c) > scoreHold:
                scoreHold = score(c)
                key = i
                best = c
                lineNumber = lineNumberHold
    print("Line: ", lineNumber,"\nPlain: ",best.lstrip().rstrip(), "\nKey: ", chr(i))

if __name__ == "__main__":
    main()
