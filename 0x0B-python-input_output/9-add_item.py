#!/usr/bin/python3
"""Module with script that adds all arguments to a Python list, and then save

    Prototype: def save_to_json_file(my_obj, filename):
    You don’t need to manage exceptions if the object can’t be serialized.
"""
import json
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


filename = "add_item.json"
try:
    arguments = load_from_json_file(filename)
except FileNotFoundError:
    arguments = []

for i in range(1, len(argv)):
    arguments.append(argv[i])

save_to_json_file(arguments, filename)
