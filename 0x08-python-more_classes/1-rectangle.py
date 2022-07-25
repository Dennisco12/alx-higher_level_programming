#!/usr/bin/python3

"""A class that defines a rectangle by some attributes"""


class Rectangle:
    """class definition"""
    def __init__(self, width=0, height=0):
        """This initialize the class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """This is used to retrieve the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """This is used to set the value of the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This is used to retrieve the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """This is used to set the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
