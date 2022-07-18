#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    '''A function that divides elements by elements 2 lists'''

    new_list = []
    for n in range(0, list_length):
        try:
            if (my_list_1[n] is not None and my_list_2[n] is not None):
                c = my_list_1[n] / my_list_2[n]
        except IndexError:
            print("out of range")
            c = 0
        except ZeroDivisionError:
            print("division by 0")
            c = 0
        except TypeError:
            print("wrong type")
            c = 0

        new_list.append(c)
    return new_list
