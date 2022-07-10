#!/usr/bin/python3

def best_score(a_dictionary):
    '''A function that returns the key with the highest value'''

    highest = 0
    if len(a_dictionary) not None:
        for k, v in a_dictionary.items():
            if v > highest:
                highest = v
                key = k
        return key
    else:
        return None
