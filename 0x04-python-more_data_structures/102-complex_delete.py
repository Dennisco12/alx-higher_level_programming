#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    '''A function that deletes keys with specific values'''

    Skey = 'cyclx'
    for k, v in a_dictionary.items():
        if v is value:
            k = Skey

    a_dictionary.pop(Skey)
    return a_dictionary
