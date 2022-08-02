#!/usr/bin/python3
"""A function that adds a new attribute to an object if possible"""


def add_attribute(obj, att, value):
    """This adds att to obj and sets its value to value"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
