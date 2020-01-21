#!/usr/bin/python3
"""Module with function that returns an object  represented by a JSON string:

    Prototype: def from_json_string(my_str):
    You don’t need to manage exceptions if the object can’t be serialized.
"""
import json


def from_json_string(my_str):
    """function that returns an object (Python data structure)
        represented by a JSON string:

    Args:
        my_str: the file name to open.

    Returns:
        int: number of lines of a text file
    """
    return json.loads(my_str)
