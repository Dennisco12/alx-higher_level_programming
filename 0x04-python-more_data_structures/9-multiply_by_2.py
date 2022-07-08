#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    '''A functions thst multiples the values in  adict by 2'''

    new_dict = {}
    for k, v in a_dictionary.items():
        new_dict[k] = v * 2
    return new_dict
