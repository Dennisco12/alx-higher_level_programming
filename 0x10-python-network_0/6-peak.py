#!/usr/bin/python3
"""This finds the peak of a list"""

def find_peak(list_of_integers):
    """This returns the found peak"""
    if list_of_integers is not None:
        return sorted(list_of_integers)[-1]
    else:
        return None
