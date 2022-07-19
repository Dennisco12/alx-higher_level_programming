#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        '''This instatiate the class with a private arguement'''

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        '''A method that retrieve the value of size'''

        return self.__size

    @size.setter
    def size(self, size):
        '''A ethod that sets the value of size'''

        self.__size = size

    def area(self):
        '''A function that return the current square area'''

        return self.__size ** 2
