#!/usr/bin/env python3

def isPkcsPadded(inputData):
	padding = inputData[-inputData[-1]:]
	return all(padding[b] == len(padding) for b in range(0, len(padding)))

def main():
	print(isPkcsPadded(b"ICE ICE BABY\x04\x04\x04\x04"))
	print(isPkcsPadded(b"ICE ICE BABY\x05\x05\x05\x05"))
	print(isPkcsPadded(b"ICE ICE BABY\x01\x02\x03\x04"))

if __name__ == "__main__":
	main()