#!/usr/bin/python3

def max_integer(my_list=[]):
    '''A function that returns the biggest integer in a list'''

    if my_list is None:
        return None

    j = 0
    n = len(my_list) - 1
    while j < len(my_list) - 1:
        if my_list[j] > my_list[j+1]:
            temp = my_list[j]
            my_list[j] = my_list[j+1]
            my_list[j+1] = temp
        j += 1

    return my_list[n]
