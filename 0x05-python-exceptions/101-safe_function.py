#!/usr/bin/python3

from __future__ import print_function
import sys


def safe_function(fct, *args):
    '''A function that executes a function safely
    Args:
        fct: a pointer to the function to be executed
        args: the arguments to the function'''

    try:
        res = fct(*args)

    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    else:
        return res
