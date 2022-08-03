#!/usr/bin/python3
"""A function that returns a json representation of an object"""

import json


def to_json_string(my_obj):
    """Function definition"""
    rep = json.dumps(my_obj)
    return rep
