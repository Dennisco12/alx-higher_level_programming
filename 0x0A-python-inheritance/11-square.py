#!/usr/bin/python3
"""This is a square class that inherits from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class definition"""
    def __init__(self, size):
        """method definition"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """This returns a string"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
