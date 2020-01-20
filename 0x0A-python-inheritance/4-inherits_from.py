#!/usr/bin/python3
"""Function that returns True if the object is an instance of

Function that returns True if the object is an instance of a class that
inherited (directly or indirectly) from the specified class; otherwise False.
"""


def inherits_from(obj, a_class):
    """returns True if the object is inherited from

    Args:
        obj: the object to evaluate.
        a_class: the class to evaluate.

    Returns:
        bool: True if obj is an inherited from a_class
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
