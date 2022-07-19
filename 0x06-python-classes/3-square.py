#!/usr/bin/python3

class Square:
    def __init__(self, size):
        '''This instantiate with size which must be an
        integer and greater than zero'''

        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        '''This returns the current square area'''

        return self.__size ** 2
