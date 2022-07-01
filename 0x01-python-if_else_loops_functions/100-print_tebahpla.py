#!/usr/bin/python3

for d in range(122, 96, -1):
    if (d % 2 != 0):
        d = d - 32
    print("{}".format(chr(d)), end='')
