#!/usr/bin/python3
""""Module to define Square class"""


class Square:
    """"Square class"""

    def __init__(self, size=0):
        """init method"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
