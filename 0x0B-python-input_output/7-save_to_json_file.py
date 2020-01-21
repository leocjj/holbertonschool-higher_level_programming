#!/usr/bin/python3
"""Module with function that writes an Object to a text file, using a JSON

    Prototype: def save_to_json_file(my_obj, filename):
    You don’t need to manage exceptions if the object can’t be serialized.
"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file, using a JSON
        representation:

    Args:
        my_obj: the file name to open.
        filename: file to store json representation of my_obj

    Returns:
        None: nothing
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
