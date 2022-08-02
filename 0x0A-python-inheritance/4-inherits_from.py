#!/usr/bin/python3
""" A function that returns True if the object is an instance of a class
that inherited from the specified class, otherwise false"""

def inherits_from(obj, a_class):
    """method definition"""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
