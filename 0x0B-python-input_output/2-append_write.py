#!/usr/bin/python3
"""A function that appends a text to the content of a file"""


def append_write(filename="", text=""):
    """Function definition"""
    with open(filename, mode='a', encoding='utf-8') as Dennis:
        bytes_added = Dennis.write(text)
        return bytes_added
