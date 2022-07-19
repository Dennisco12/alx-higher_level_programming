#!/usr/bin/python3

class Square:
    def __init__(self, size=0, position=(0, 0)):
        '''This is used to instantiate the class'''
        self.__size = size
        self.__position = position

    @property
    def size(self):
        '''Used to retrieve the attribute size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Used to set the value of size'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        '''This is used to retrieve the attribute position'''
        return self.__position

    @position.setter
    def position(self, value):
        '''This is used to set the value of position'''
        if (not isinstance(value, tuple) or len(value) != 2
                or not all(isinstance(n, int) for n in value)
                or not all(m >= 0 for m in value)):
            raise TypeError("position must be a tuple of two positive integers")
        self.__position = value

    def area(self):
        '''Computes the square of size'''
        return self.__size ** 2

    def my_print(self):
        '''Prints the area using # to stdout'''
        if self.__size == 0:
            print()
        else:
            [print() for n in range(self.__position[1])]
            for m in range(self.__size):
                [print(" ", end="") for k in range(self.__position[0])]
                [print("#", end="") for p in range(self.__size)]
                print()
