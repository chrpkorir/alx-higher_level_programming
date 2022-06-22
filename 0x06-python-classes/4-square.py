#!/usr/bin/python
"""
This is a Square module

The Square module contains the Square class
"""


class Square:
    """
    This is the Square class
    """
    def __init__(self, size=0):
        """
        The __init__ method
        """
        self.size = size

    @property
    def size(self):
        """
        size getter
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        size setter
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        returns te current square area
        """
        return (self.__size * self.__size)
