#!/usr/bin/python3

def roman_to_int(roman_string):
    '''A function that convert a roman_string to int'''

    conv = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    ans = 0
    for i in roman_string:
        if i in conv:
            ans += conv[i]
    return ans
