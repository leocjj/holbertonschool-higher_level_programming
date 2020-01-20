#!/usr/bin/python3
"""Functions to evaluate if an object is instance of a class.

function that returns True if the object is exactly an instance of
the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """evaluate if an object is instance of a class

    Args:
        obj: the object to evaluate.
        a_class: the class to evaluate.

    Returns:
        bool: if obj is exactly an instance of a_class
    """
    return type(obj) == a_class
