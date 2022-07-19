#!/usr/bin/python3

'''Using a class'''


class Square:
    '''This is a class definetiin'''

    def __init__(self, size=0):
        '''A function that defines a square by a private
        instance attribute: size'''

        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
