#!/usr/bin/python3
"""
A class Student"""


class Student:
    """class definition"""
    def __init__(self, first_name, last_name, age):
        """Class initialisation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves the dict representation of a Student instance"""
        return self.__dict__
