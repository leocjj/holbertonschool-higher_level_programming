#!/usr/bin/python3
"""This module adds to integer numbers.

Function that returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """Return the add of two integers.

    Args:
        obj: The first number to add.

    Returns:
        list: available attributes and methods of an object
    """

    return dir(obj)
