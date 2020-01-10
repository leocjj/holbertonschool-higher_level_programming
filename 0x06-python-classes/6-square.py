#!/usr/bin/python3
""""Module to define Square class"""


class Square:
    """"Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """init method"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """getter method for __size"""
        return self.__size

    @size.setter
    def size(self, size):
        """setter method for __size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """getter method for __position"""
        return self.__position

    @position.setter
    def position(self, position=(0, 0)):
        """setter method for __position"""
        if type(position) == tuple and len(position) == 2 and \
           type(position[0]) == int and type(position[1]) == int:
            if position[0] >= 0 and position[1] >= 0:
                self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """area method"""
        return self.size ** 2

    def my_print(self):
        """print a square method"""
        if self.size == 0:
            print()
        else:
            print('\n' * self.position[1], end='')
            for i in range(self.size):
                print(' ' * self.position[0], end='')
                print('#' * self.size)
