#!/usr/bin/python3
"""Base class.

Class Base:

    private class attribute __nb_objects = 0
    class constructor: def __init__(self, id=None)::
        if id is not None, assign the public instance attribute id with this
        argument value - you can assume id is an integer and you don’t need
        to test the type of it
        otherwise, increment __nb_objects and assign the new value to the
        public instance attribute id
"""
import json


class Base:
    """Define a Base class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Init Base instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return '[]'

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + '.json'
        dictionaries = []
        if list_objs:
            for obj in list_objs:
                dictionaries += [obj.to_dictionary()]
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation"""
        if json_string:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            new_base = cls(1, 1)
        else:
            new_base = cls(1)
        new_base.update(**dictionary)
        return new_base
