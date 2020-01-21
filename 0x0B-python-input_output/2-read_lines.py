#!/usr/bin/python3
"""Module with function that reads n lines of a text file and prints it:

    Prototype: def read_lines(filename="", nb_lines=0):
    Read the entire file if nb_lines is lower or equal to 0 OR
        greater or equal to the total number of lines of the file
    You must use the with statement
    You don’t need to manage file permission or file doesn't exist exceptions.
    You are not allowed to import any module
"""


def read_lines(filename="", nb_lines=0):
    """Reads n lines of a text file (UTF8) and prints it to stdout

    Args:
        filename: the file name to open.
        nb_lines: number of lines to print

    Returns:
        None: nothing
    """
    if nb_lines <= 0:
        with open(filename) as f:
            print(f.read(), end='')
            return

    num_lines = 0
    with open(filename) as f:
        for a_line in f:
            num_lines += 1
            if num_lines <= nb_lines:
                print(a_line, end='')
            else:
                return
    return
