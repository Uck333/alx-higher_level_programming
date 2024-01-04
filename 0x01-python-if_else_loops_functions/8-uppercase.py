#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if not ord('a') <= ord(i) <= ord('z'):
            print(i, end="")
        else:
            print(chr(ord(i) - 32), end="")
