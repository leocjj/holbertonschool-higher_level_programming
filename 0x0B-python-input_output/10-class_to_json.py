#!/usr/bin/python3
"""Module with function that returns the dictionary description

    with simple data structure (list, dictionary, string, integer
    and boolean) for JSON serialization of an object:
"""


def class_to_json(o):
    """Return the dict description for JSON serialization of an object."""
    return o.__dict__
