#!/usr/bin/python3
"""A class that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """"class definition"""
    def __init__(self, size, x=0, y=0, id=None):
        """This initialises the class"""
        super().__init__(size, size, x, y, id)
        self.__size = self.width

    @property
    def size(self):
        """This retrieves the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """This sets the value of size"""
        self.width = value
        self.height = value

    def __str__(self):
        """This returns the print function"""
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.width))
