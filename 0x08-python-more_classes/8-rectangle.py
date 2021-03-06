#!/usr/bin/python3
""""Module to define a rectangle class"""


class Rectangle:
    """"Rectangle class"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """Informal string, return rectangle representation with char #"""
        result = ''
        if self.height == 0 or self.width == 0:
            return result
        for i in range(self.height):
            result += str(self.print_symbol) * self.width + '\n'
        return result[:-1]

    def __repr__(self):
        """Return oficial representation of rectangle."""
        return 'Rectangle(' + str(self.width) + ', ' + str(self.height) + ')'

    def __del__(self):
        """Method called when the program finish"""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
