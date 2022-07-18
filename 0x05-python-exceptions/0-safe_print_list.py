#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    '''A function that prints x elements of a list.'''

    n = 0
    try:
        for a in range(0, x):
            if my_list is not None:
                print("{}".format(my_list[a]), end="")
                n = n + 1
        print()
    except:
        print()

    return n
