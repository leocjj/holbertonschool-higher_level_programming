#!/usr/bin/python3
"""class BaseGeometry

class BaseGeometry

Public instance method: def area(self): that raises an Exception with the
    message area() is not implemented
Public instance method: def integer_validator(self, name, value): that
    validates value: you can assume name is always a string
if value is not an integer: raise a TypeError exception, with the message
    <name> must be an integer
if value is less or equal to 0: raise a ValueError exception with the message
    <name> must be greater than 0
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


"""class Rectangle

class Rectangle that inherits from BaseGeometry (7-base_geometry.py).

Instantiation with width and height: def __init__(self, width, height):
    width and height must be private. No getter or setter
    width and height must be positive integers, validated by integer_validator
"""


class Rectangle(BaseGeometry):
    """class BaseGeometry.

    class BaseGeometry.
    """
    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width__ = width
        self.__height__ = height

    def area(self):
        """area method implementation

        Args:
            self: the object itself.

        Returns:
            int: area of the rectangle
        """
        return self.__width__ * self.__height__

    def __str__(self):
        """str method implementation

        Args:
            self: the object itself.

        Returns:
            str: message to return or print.
        """
        return "[Rectangle] {}/{}".format(self.__width__, self.__height__)
