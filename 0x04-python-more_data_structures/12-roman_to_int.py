#!/usr/bin/python3

def roman_to_int(roman_string):
    '''A function that convert a roman_string to int'''

    conv = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    ans = 0
    if roman_string is None:
        return 0

    m = []
    j = 1
    m.append(1000)
    for i in roman_string:
        if i in conv:
            co = conv[i]
            m.append(co)
            if m[j - 1] < m[j]:
                ans += abs(m[j] - (2 * m[j - 1]))
            else:
                ans += conv[i]
            j += 1:
        else:
            return 0

    return ans
