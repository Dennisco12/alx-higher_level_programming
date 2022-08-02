#!/usr/bin/python3
"""A class that inherits from an int"""


class MyInt(int):
    """This class has the == and != operators inverted"""
    def __eq__(self, value):
        """Uses this for the == operator"""
        return self.real != value

    def __ne__(self, value):
        """uses this for the != operator"""
        return self.real == value
