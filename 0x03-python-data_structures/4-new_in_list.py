#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    '''
    A function that replaces an element at a
    specific position without modifying the original list
    '''

    if (idx < 0 or idx > len(my_list) - 1):
        return my_list
    else:
        new_list = []
        for m in my_list:
            new_list.append(m)

        new_list.pop(idx)
        new_list.insert(idx, element)
        return new_list
