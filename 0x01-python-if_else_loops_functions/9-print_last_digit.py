#!/usr/bin/python3
def print_last_digit(number):
    """A FUNCTION THE LAST DIGIT OF A NUMBER AND RETURN ITS VALUE"""
    last = abs(number) % 10
    print("{}".format(last), end='')
    return last
