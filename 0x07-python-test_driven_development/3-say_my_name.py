#!/usr/bin/python3
"""This module prints My name is <first name> <last name>

    first_name and last_name must be strings
    otherwise, raise a TypeError exception
        with the message    'first_name must be a string' or
                            'last_name must be a string'

    You are not allowed to import any module

    Returns nothing

    This module supplies one function, say_my_name().  For example,

    >>> say_my_name('Leonardo', 'Calderon')
    Leonardo Calderon
"""


def say_my_name(first_name, last_name=""):
    """Prints first_name last_name.

    Args:
        param1 (first_name): the first name.
        param2 (last_name): the second name. By default is "".

    Returns:
        None: returns nothing.

    >>> say_my_name('leocjj', '')
    leocjj

    """

    if (type(first_name) is not str):
        raise TypeError('first_name must be a string')

    if (type(last_name) is not str):
        raise TypeError('last_name must be a string')

    print('My name is {} {}'.format(first_name, last_name))
