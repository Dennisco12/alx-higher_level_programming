#!/usr/bin/python3
"""This tokenise text and seperate lines"""


def text_indentation(text):
    """The method to be used"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for n in range(len(text)):
        if (text[n] in (".", "?", ":")):
            print("{}".format(text[n]))
            print()
            continue
        if text[n - 1] in (".", "?", ":") and n != 0:
            continue
        else:
            print("{}".format(text[n]), end="")
