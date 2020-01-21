#!/usr/bin/python3
"""Module with function that appends a string at the end of a text file.

    Prototype: def append_write(filename="", text=""):
    If the file doesn’t exist, it should be created
    You must use the with statement
    You don’t need to manage file permission or file doesn't exist exceptions.
    You are not allowed to import any module
"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file (UTF8)
        and returns the number of characters added:

    Args:
        filename: the file name to open.
        text: text to write to a file.

    Returns:
        int: number of lines of a text file
    """
    num_chars_added = 0
    with open(filename, 'a') as f:
        num_chars_added = f.write(str(text))
    return num_chars_added
