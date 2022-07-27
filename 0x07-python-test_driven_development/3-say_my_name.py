#!/usr/bin/python3
"""This prints the first and last name if the user"""


def say_my_name(first_name, last_name=""):
    """The prints the names of the user"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
