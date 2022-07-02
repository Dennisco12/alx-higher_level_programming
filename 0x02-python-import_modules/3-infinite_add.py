#!/usr/bin/python3
if __name__ == "__main__":
    """A function that sums all the command line argument added to it"""
    import sys
    
    argc = len(sys.argv)
    sum = 0
    for m in range(1, argc):
        sum = sum + int(sys.argv[m])
    print("{:d}".format(sum))
