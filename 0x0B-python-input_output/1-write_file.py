#!/usr/bin/python3
"""A function that writes a string to a text file and
returns the number of characters written"""


def write_file(filename="", text=""):
    """Function definition"""
    with open(filename, 'w', encoding='utf-8') as Dennis:
        bytes_written = Dennis.write(text)
        return bytes_written
