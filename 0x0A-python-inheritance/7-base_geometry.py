#!/usr/bin/python3
"""This is an geometry class"""


class BaseGeometry:
    """Class definition"""
    def area(self):
        """This raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This validates 'value' """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
