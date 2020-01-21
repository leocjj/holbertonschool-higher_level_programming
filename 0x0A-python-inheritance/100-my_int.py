#!/usr/bin/python3
"""class MyInt that inherits from int:

    MyInt is a rebel. MyInt has == and != operators inverted
"""


class MyInt(int):
    """class MyInt.

    MyInt has == and != operators inverted
    """
    def __eq__(self, other):
        """OVERRIDED METHOD FOR x==y calls x.__eq__(y)

        Args:
            self: the object itself.
            other: the other object to compare.

        Returns:
            bool: True if x is different from y
        """
        if int(self) == int(other):
            return False
        else:
            return True

    def __ne__(self, other):
        """OVERRIDED METHOD FOR x!=y calls x.__ne__(y)

        Args:
            self: the object itself.
            other: the other object to compare.

        Returns:
            bool: True if x is different from y
        """
        if int(self) != int(other):
            return False
        else:
            return True
