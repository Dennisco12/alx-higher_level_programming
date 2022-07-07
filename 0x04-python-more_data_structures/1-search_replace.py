#!/usr/bin/python3

def search_replace(my_list, search, replace):
    '''A function that replace all occurence of an element in a list'''

    new_list = []
    for i in my_list:
        if i is search:
            new_list.append(replace)
        else:
            new_list.append(i)

    return new_list
