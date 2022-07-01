#!/usr/bin/python3
def uppercase(str):
    """A function that print a string in uppercase"""
    for b in str:
        if (ord(b) > 96 and ord(b) < 123):
            b = chr(ord(b) - 32)
        print("{}".format(b), end='')
    print()
