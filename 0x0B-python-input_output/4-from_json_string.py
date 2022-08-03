#!/usr/bin/python3
"""A function that returns an object from a json representation"""

import json

def from_json_string(my_str):
    """Function definition"""
    rep = json.loads(my_str)
    return rep
