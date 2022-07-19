#!/usr/bin/python3

'''Using a new class'''

class Square:
    def __init__(self, size=0):
        '''This instantiate the class'''

        self.__size = size

    @property
    def size(self):
        '''This is used to retrieve the value of size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''This is used to set te value of size'''
    
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        '''This returns the current square area'''
        return self.__size ** 2

    def my_print(self):
        '''This print to stdout the square with the character #'''

        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
