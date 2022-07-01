#!/usr/bin/python3
for m in range(0, 100):
    if m == 99:
        print("{0:d}".format(m))
        continue
    print("{0:02}".format(m), end=", ")
