#!/usr/bin/python3

"""This defines the class"""


class Rectangle:
    """Class definition"""

    def __init__(self, width=0, height=0):
        """This initialises the instance"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """This returns the value of width"""
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
        """This returns the value of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """This sets the value of the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("heigth must be >= 0")
        self.__height = value

    def area(self):
        """This computes the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """This computes the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__height + self.__width))

    def __str__(self):
        """This prints the rectangle with '#' """
        if self.__width == 0 or self.__height == 0:
            return ("")

        matrix = []
        for n in range(self.__height):
            [matrix.append("#") for m in range(self.__width)]
            if n != self.__height - 1:
                matrix.append("\n")
        return ("".join(matrix))
