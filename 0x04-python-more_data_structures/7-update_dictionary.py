#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    '''replaces or adds key/value in a dictionary'''

    new_dict = a_dictionary
    for k, v in new_dict.items():
        if k is key:
            v = value
        else:
            continue
    new_dict[key] = value
    return new_dict
