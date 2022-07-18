#!/usr/bin/python3

def safe_print_division(a, b):
    '''A function that divides two integer and prints the result'''

    try:
        c = a / b
    except ZeroDivisionError:
        c = None
    finally:
        print("Inside result: {}".format(c))

    return c
