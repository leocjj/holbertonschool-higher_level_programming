#!/usr/bin/python3
"""This module adds to integer numbers.

This module adds two integer. a and b must be integers or floats otherwise
raise a TypeError exception with the message a must be an integer, if a is not
an integer, b must be an integer, if b is not an integer.

a and b must be first casted to integers if they are float

Returns an integer: the addition of a and b

You are not allowed to import any module

This module supplies one function, add_integer().  For example,

>>> add_integer(1, 2)
3
"""

def add_integer(a, b=98):
    """Return the add of two integers.

    Args:
        param1 (a): The first number to add.
        param2 (b): The second number to add. By default is 98.

    Returns:
        integer: The return value. The add of two integers.

    >>> add_integer(1)
    99

    """

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    if (type(a) is not int):
        raise TypeError("a must be an integer")
    if (type(b) is not int):
        raise TypeError("b must be an integer")

    return (a + b)
