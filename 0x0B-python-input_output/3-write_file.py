#!/usr/bin/python3
"""Module with function that writes a string to a text file (UTF8)

    Prototype: def write_file(filename="", text=""):
    You don’t need to manage file permission exceptions.
    Your function should create the file if doesn’t exist.
    Your function should overwrite the content of the file if already exists.
    You are not allowed to import any module
"""


def write_file(filename="", text=""):
    """Function that writes a string to a text file (UTF8) and
        returns the number of characters written:

    Args:
        filename: the file name to open.
        text: text to write to a file.

    Returns:
        int: number of lines of a text file
    """
    num_chars_written = 0
    with open(filename, 'w') as f:
        num_chars_written = f.write(str(text))
    return num_chars_written
