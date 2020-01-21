#!/usr/bin/python3
"""Module with function that returns the JSON representation of an object:

    Prototype: def to_json_string(my_obj):
    You don’t need to manage exceptions if the object can’t be serialized.
"""
import json


def to_json_string(my_obj):
    """function that returns the JSON representation of an object (string):

    Args:
        my_obj: the file name to open.

    Returns:
        int: number of lines of a text file
    """
    return json.dumps(my_obj)
