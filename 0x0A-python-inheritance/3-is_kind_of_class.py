#!/usr/bin/python3
"""Function that returns True if the object is an instance of

Function that returns True if the object is an instance of, or if the object
is an instance of a class that inherited from, the specified class;
otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of

    Args:
        obj: the object to evaluate.
        a_class: the class to evaluate.

    Returns:
        bool: True if obj is an instance of a_class
    """
    return isinstance(obj, a_class)
