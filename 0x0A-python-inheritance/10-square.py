#!/usr/bin/python3
"""class Rectangle

class Rectangle that inherits from BaseGeometry (7-base_geometry.py).

Instantiation with width and height: def __init__(self, width, height):
    width and height must be private. No getter or setter
    width and height must be positive integers, validated by integer_validator
"""
Rectangle = __import__('9-rectangle').Rectangle


"""class Square

class Square that inherits from Rectangle (9-rectangle.py):
"""


class Square(Rectangle):
    """class Square.

    class Square.
    """
    def __init__(self, size):
        super().__init__(size, size)
