#!/usr/bin/python3
"""A rectangle class that inherits from Base_geometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class definition"""
    def __init__(self, width, height):
        """class initialisation"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """This calculates the area of the rectangle"""
        self.area = self.__width * self.__height
        return self.area

    def __str__(self):
        """This is activated by the print command"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
