#!/usr/bin/python3
"""a script that adds all arguments to a python list
and saves them to a file"""
from sys import argv as arg


if __name__ == '__main__':
    load = __import__('6-load_from_json_file').load_from_json_file
    save = __import__('5-save_to_json_file').save_to_json_file

    try:
        item = load("add_item.json")
    except FileNotFoundError:
        item = []

    item = item + arg[1:]
    save(item, "add_item.json")
