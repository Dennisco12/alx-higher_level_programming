#!/usr/bin/python3
"""This adds two integers"""


def add_integer(a, b=98):
    """
    >>> add_integer(2, 3)
    5

    >>> add_integer(-2, 7)
    5

    >>> add_integer(2.0, 5.0)
    7

    >>> add_integer(2.5, "size")
    Traceback (most recent call last):
    TypeError: b must be an integer

    >>> add_integer("size", 6.2)
    Traceback (most recent call last):
    TypeError: a must be an integer
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
