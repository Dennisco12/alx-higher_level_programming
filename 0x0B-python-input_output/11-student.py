#!/usr/bin/python3
"""A class"""


class Student:
    """class definition"""
    def __init__(self, first_name, last_name, age):
        """initialise the class"""
        self.firt_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dict representation of a Student
        instance"""
        if (type(attrs) == list and
                all(type(item) == str for item in attrs)):
            return {d: getattr(self, d) for d in attrs if hasattr(self, d)}
        return self.__dict__

    def reload_from_json(self, json):
        """This replaces all attributes of the Student instance"""
