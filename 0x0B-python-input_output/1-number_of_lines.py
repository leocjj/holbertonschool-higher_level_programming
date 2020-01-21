#!/usr/bin/python3
"""This module has a function that returns the number of lines of a text file

    Prototype: def number_of_lines(filename=""):
    You must use the with statement
    You don’t need to manage file permission or file doesn't exist exceptions.
    You are not allowed to import any module
"""


def number_of_lines(filename=""):
    """function that returns the number of lines of a text file:

    Args:
        filename: the file name to open.

    Returns:
        int: number of lines of a text file
    """
    num_lines = 0
    with open(filename) as f:
        num_lines = len(f.readlines())
    return num_lines
