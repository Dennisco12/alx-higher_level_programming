#!/usr/bin/python3
"""A function that creates an object from a json file"""
import json


def load_from_json_file(filename):
    """class definition"""
    with open(filename) as Dennis:
        return json.load(Dennis)
