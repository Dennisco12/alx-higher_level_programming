#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    '''A function that deletes the item at a specific position'''

    if (idx < 0 or idx > len(my_list) - 1):
        return my_list

    n = 0
    new_list = []
    for m in my_list:
        n += 1
        if idx + 1 == n:
            continue
        else:
            new_list.append(m)

    del my_list[:]
    for j in new_list:
        my_list.append(j)
    return new_list
