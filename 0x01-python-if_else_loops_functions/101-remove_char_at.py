#!/usr/bin/python3
def remove_char_at(str, n):
    """A function that removes a char at the position n"""
    if n < 0:
        return str
    return (str[0:n] + str[n+1:])
