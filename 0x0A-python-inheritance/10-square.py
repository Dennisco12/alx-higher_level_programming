#!/usr/bin/python3
""" A square class that inherits from Rectangle """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class definition"""
    def __init__(self, size):
        """class initialisation"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
