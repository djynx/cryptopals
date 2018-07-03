#!/usr/bin/env python3

def countDuplicateBlocks(inputBytes):
    blocks = [inputBytes[i:i + 16] for i in range(0, len(inputBytes), 16)]
    duplicates = len(blocks) - len(set(blocks))
    return duplicates


def detectECB(inputList):
    maxScore = 0
    line = -1
    for i in range(len(inputList)):
        score = countDuplicateBlocks(inputList[i])
        if score > maxScore:
            maxScore = score
            line = i
    return line, maxScore


def main():
    candidates = [bytes.fromhex(line.strip()) for line in open("chall8.txt")]
    line, score = detectECB(candidates)
    print("ECB kullanilarak sifrelenmis veri", line, "nolu satirda ve", score, "adet tekrarlayan bloga sahip.")


if __name__ == "__main__":
    main()
