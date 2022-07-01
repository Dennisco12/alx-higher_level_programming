#!/usr/bin/python3
for d in range(0, 10):
    for e in range(d + 1, 10):
        if (d == 8 and e == 9):
            print("{0:d}{1:d}".format(d, e))
            continue
        print("{0:d}{1:d}".format(d, e), end=", ")
