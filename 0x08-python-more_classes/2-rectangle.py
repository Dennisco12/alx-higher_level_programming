#!/usr/bin/python3

"""This creates a class called rectangle"""


class Rectangle:
    """class definition"""

    def __init__(self, width=0, height=0):
        """This initialises the instance"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """this returns the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """This sets the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This returns the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """This sets the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """This returns the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """This returs the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (2 * (self.__height + self.__width))
