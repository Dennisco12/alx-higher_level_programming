#!/usr/bin/python3
"""The base class"""


class Base:
    """This is the class definition"""
    __nb_objects = 0
    def __init__(self, id=None):
        """This is the class initialiser"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
