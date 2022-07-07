#!/usr/bin/python3

def common_elements(set_1, set_2):
    '''A function that returns a set of cmmon elements in two sets'''

    new_list = []
    for i in set_1:
        for j in set_2:
            if i is j:
                new_list.append(i)

    return new_list
