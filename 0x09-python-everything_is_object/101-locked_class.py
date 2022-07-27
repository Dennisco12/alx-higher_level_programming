#!/usr/bin/python3
"""Creates a locked class"""


class LockedClass:
    """Prevent the usr fron creating any instance except
    if its name is 'first_name'"""
    __slots__ = ["first_name"]
