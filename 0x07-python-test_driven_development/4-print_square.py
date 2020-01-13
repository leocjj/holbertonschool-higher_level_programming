#!/usr/bin/python3
"""This module prints a square with the character #.

    size is the size length of the square

    size must be an integer
    otherwise raise TypeError('size must be an integer')

    if size is less than 0
    raise ValueError('size must be >= 0')

    if size is a float and is less than 0
    raise TypeError('size must be an integer')

    You are not allowed to import any module

    Returns nothing

    This module supplies one function, print_square().  For example,

    >>> print_square(3)
    Leonardo Calderon
"""


def print_square(size):
    """prints a square with the character #.

    Args:
        size: the first name.

    Returns:
        None: returns nothing.

    >>> print_square(3)
    ###
    ###
    ###

    """

    if (type(size) is not int):
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    if size is 0:
        return

    for i in range(size):
        print('#' * size)
