#!/usr/bin/python3
"""Module for function that adds a new attribute to an object if it’s possible

Raise a TypeError exception, with the message can't add new attribute if the
object can’t have new attribute
"""


def add_attribute(obj, attribute, value):
    """Function that adds a new attribute to an object if it’s possible:

    Args:
        obj: the object add a new attribute.
        attribute: attribute to add.
        value: value to set the attribute.

    Returns:
        None: nothing
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, attribute, value)
        return
    raise TypeError("can't add new attribute")
