#!/usr/bin/python3


def complex_delete(a_dictionary, value):

    if not a_dictionary:
        return a_dictionary

    c_dictionary = a_dictionary.copy()

    for key in list(c_dictionary.keys()):
        if c_dictionary[key] == value:
            del c_dictionary[key]

    if not c_dictionary:
        return c_dictionary
    else:
        return c_dictionary
