#!/usr/bin/python3
"""This module has a function that reads a text file (UTF8) and prints it.

    Prototype: def read_file(filename=""):
    You must use the with statement
    You don’t need to manage file permission or file doesn't exist exceptions.
"""


def read_file(filename=""):
    """Function that reads a text file (UTF8) and prints it to stdout.

    Args:
        filename: the file name to open.

    Returns:
        None: nothing
    """
    with open(filename) as f:
        print(f.read(), end='')
