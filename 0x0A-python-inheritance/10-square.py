#!/usr/bin/python3
"""class Square

class Square that inherits from Rectangle (9-rectangle.py):
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square.

    class Square.
    """
    def __init__(self, size):
        super().__init__(size, size)
