#!/usr/bin/env python3

def score(inputBytes):
    englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09,
                         'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23,
                         'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15,
                         'Q': 0.10, 'Z': 0.07, ' ': 23.00}
    score = 0
    for byte in inputBytes:
            score += englishLetterFreq.get(chr(byte).upper(),0)
    return score

def singleCharXor(inputBytes, k):
    solvedBytes = b''
    for byte in inputBytes:
        solvedBytes += bytes([byte ^ k])
    return solvedBytes

def singleCharXorBruteforce(inputBytes):
    res = b''
    key = 0
    scoreHold = 0
    for i in range (256):
        sb = singleCharXor(inputBytes,i)
        if score(sb) > scoreHold:
            scoreHold = score(sb)
            key = i
            res = sb
    return res,key,scoreHold

def main():
    xord = input("? ")
    plain, key, score = singleCharXorBruteforce(bytes.fromhex(xord))
    print("Metin: ", plain.decode() ,"\nAnahtar: ", chr(key),"\nSkor: ", score)

if __name__ == "__main__":
    main()
