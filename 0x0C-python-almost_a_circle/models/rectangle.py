#!/usr/bin/python3
"""Rectangle class.

Class Rectangle inherits from Base
Private instance attributes, each with its own public getter and setter:

    __width -> width
    __height -> height
    __x -> x
    __y -> y

Class constructor: def __init__(self, width, height, x=0, y=0, id=None):

    Call the super class with id - this super call with use the logic of
    the __init__ of the Base class
    Assign each argument width, height, x and y to the right attribute
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Init Rectangle instance."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        self.validator('width', value)
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        self.validator('height', value)
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        self.validator('x', value)
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        self.validator('y', value)
        self.__y = value

    def validator(self, var, value):
        """Validator method"""
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(var))

        if (var == 'width' or var == 'height') and (value <= 0):
            raise ValueError('{} must be > 0'.format(var))

        if (var == 'x' or var == 'y') and (value < 0):
            raise ValueError('{} must be >= 0'.format(var))

    def area(self):
        """Return area of rectangle"""
        return self.__width * self.__height
