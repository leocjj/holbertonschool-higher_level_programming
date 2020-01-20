#!/usr/bin/python3
"""class BaseGeometry

Write a class BaseGeometry (based on 5-base_geometry.py).

Public instance method: def area(self): that raises an Exception with the
message area() is not implemented
"""


class BaseGeometry:
    """class BaseGeometry.

    empty class BaseGeometry.
    """

    def area(self):
        """raises an Exception with the message area() is not implemented

        Args:
            self: the object itself.

        Returns:
            None: nothing
        """
        raise Exception("area() is not implemented")
