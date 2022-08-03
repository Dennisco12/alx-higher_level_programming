#!/usr/bin/python3
"""A function that reads a text file and prints it to stdout"""


def read_file(filename=""):
    """Function declaration"""

    with open(filename, encoding='utf-8') as txtfile:
        content = txtfile.read()

    print(content, end='')
