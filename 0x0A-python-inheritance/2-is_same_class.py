#!/usr/bin/python3
"""A function that returns true if the obj is an instance type
of the type or false if otherwise"""

def is_same_class(obj, a_class):
    """function definition"""
    if type(obj) == a_class:
        return True
    else:
        return False
