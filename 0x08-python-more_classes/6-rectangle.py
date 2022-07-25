#!/usr/bin/python3
"""This creates a class"""


class Rectangle:
    """This defines the class"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """This initialises the class"""
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """This retrieves the vlaue of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """This sets the value of the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This return the value of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """This sets the value of the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """This computes the area of the rectangle"""
        self.area = self.__width * self.__height
        return self.area

    def perimeter(self):
        self.perimeter = 2 * (self.__width + self.height)
        return self.perimeter

    def __str__(self):
        """This prints a string representation of the rectangle
        using '#' """
        if self.width == 0 or self.height == 0:
            return ("")
        matrix = []
        for i in range(self.__height):
            for j in range(self.__width):
                matrix.append("#")
            if i != self.__height - 1:
                matrix.append("\n")
        return ("".join(matrix))

    def __repr__(self):
        """This prints the string representation of the rectangle
        to be able to recreate a new instance by using eval()"""
        matrix = "Rectangle(" + str(self.__width) + "," + str(self.width)
        matrix += ")"
        return (matrix)

    def __del__(self):
        """This activates when an instance is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
