#!/usr/bin/python3
"""class Student that defines a student by:

    Public instance attributes:
        first_name
        last_name
        age
    Instantiation with first_name, last_name and age:
    def __init__(self, first_name, last_name, age):

    Public method def to_json(self, attrs=None):
    that retrieves a dictionary representation of a Student instance
    (same as 10-class_to_json.py):
    If attrs is a list of strings, only attribute names contained in this
    list must be retrieved.
    Otherwise, all attributes must be retrieved
"""


class Student:
    """class Student.

    class Student.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance"""
        a = {}
        if type(attrs) == list:
            for key, value in self.__dict__.items():
                if key in attrs:
                    a[key] = value
        else:
            return self.__dict__
        return a
