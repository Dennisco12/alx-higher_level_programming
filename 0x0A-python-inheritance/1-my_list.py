#!/usr/bin/python3
"""This inherits from a list"""


class MyList(list):
    """clas definition"""
    def print_sorted(self):
        """This prints the sorted list"""
        print(sorted(self))
