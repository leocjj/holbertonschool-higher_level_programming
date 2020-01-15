#!/usr/bin/python3
""""Module to define a rectangle class"""


class Rectangle:
    """"Rectangle class"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """"getter for Rectangle width"""
        return self.__width

    @width.setter
    def width(self, width):
        """"setter for Rectangle width"""
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    @property
    def height(self):
        """"getter for Rectangle height"""
        return self.__height

    @height.setter
    def height(self, height):
        """"setter for Rectangle height"""
        if type(height) is not int:
            raise TypeError('width must be an integer')
        if height < 0:
            raise ValueError('width must be >= 0')
        self.__height = height

    def area(self):
        """Returns area of the rectangle"""
        return self.height * self.width

    def perimeter(self):
        """Returns rectangle perimeter. Zero if height or width are zero."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
