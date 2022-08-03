#!/usr/bin/python3
"""A function that returns the dictionary description with simple
data structure for json serialisation ob an object"""


def class_to_json(obj):
    """Function definition"""
    return obj.__dict__
