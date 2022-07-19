#!/usr/bin/python3

'''A class that defines a square'''


class Square:
    '''This defines the class'''

    def __init__(self, size=0, position=(0, 0)):
        '''This initializes the class'''
        self.__size = size
        self.__position = position

    @property
    def size(self):
        '''This helps to retrieve the size attribute'''
        return self.__size

    @size.setter
    def size(self, value):
        '''This sets the value of the attribute
        Args:
            value: the value to be set to.'''

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        '''This serves as a getter for the postion attribute'''
        return self.__position

    @position.setter
    def postion(self, value):
        '''This sets the value of the postion attribute
        Args:
            value: the new value to be set to'''
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''This returns the area of the size'''
        return (self.__size ** 2)
    
    def my_print(self):
        '''This prints the area to stdout with #'''
        if self.__size == 0:
            print("")
        else:
            [print("") for num in range(self.__position[1])]
            for i in range(self.__size):
                for m in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
            print("")

    def __str__(self):
        '''This defines the print() representation of the class'''

        if self.__size != 0:
            for i in range(0, self.__position[1]):
                print("", end="")
        else:
            print("")
        for i in range(0, self.__size):
            [print(" ", end="") for k in range(0, self.__position[0])]
            [print("#", end="") for p in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return("")
