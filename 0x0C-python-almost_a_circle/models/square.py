#!/usr/bin/python3
"""Square class.

Class Square inherits from Rectangle
Class constructor: def __init__(self, size, x=0, y=0, id=None)::
    Call the super class with id, x, y, width and height - this super call
    will use the logic of the __init__ of the Rectangle class. The width and
     height must be assigned to the value of size
    You must not create new attributes for this class, use all attributes of
    Rectangle - As reminder: a Square is a Rectangle with the same width and
    height
    All width, height, x and y validation must inherit from Rectangle - same
    behavior in case of wrong data

The overloading __str__ method should return [Square] (<id>) <x>/<y> - <size>
 - in our case, width or height
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Init Rectangle instance."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Print rectangle string"""
        return ('[Square] (' + str(self.id) + ') ' + str(self.x) + '/' +
                str(self.y) + ' - ' + str(self.width))

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.validator('width', value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update parameters"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
