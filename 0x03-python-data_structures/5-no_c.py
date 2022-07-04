#!/usr/bin/python3

def no_c(my_string):
    '''A function that removes all characters c and C from a string'''

    new_string = []
    for m in my_string:
        new_string.append(m)

    idx = 0
    for n in new_string:
        idx += 1
        if (n == 'c' or n == 'C'):
            new_string.pop(idx - 1)

    return "".join(new_string)
