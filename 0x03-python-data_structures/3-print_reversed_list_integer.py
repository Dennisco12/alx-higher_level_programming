#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    '''A function that prints all integers of a list in reverse'''

    if my_list:
        for m in range(len(my_list)):
            a = my_list.pop()
            print("{:d}".format(a))
