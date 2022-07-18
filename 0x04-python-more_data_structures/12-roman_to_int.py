#!/usr/bin/python3

def roman_to_int(roman_string):
    '''A function that convert a roman_string to int'''

    conv = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    ans = 0
    if roman_string is None:
        return 0

    StoreString = []
    idx = 1
    StoreString.append(1000)
    for strn in roman_string:
        if strn in conv:
            value = conv[strn]
            StoreString.append(value)
            if StoreString[idx - 1] < StoreString[idx]:
                ans += StoreString[idx] - (2 * StoreString[idx - 1])
            else:
                ans += value
            idx += 1
        else:
            return 0

    return ans
