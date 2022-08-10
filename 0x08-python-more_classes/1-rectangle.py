#!/usr/bin/python3
"""
Define class Rectangle
"""


class Rectangle:
    """
    Square class
    """
    def __init__(self, width=0, height=0):
        """
        Initialize a new square
        Args:
        height (int): Height of the rectangle
        width (int): Width of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        __width geter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        __width setter
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """__height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """__height setter
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
