#!/usr/bin/python3
"""A function that writes an object to a text file using
a json representation"""
import json


def save_to_json_file(my_obj, filename):
    """Function definition"""
    with open(filename, mode='w') as Dennis:
        json.dump(my_obj, Dennis)
