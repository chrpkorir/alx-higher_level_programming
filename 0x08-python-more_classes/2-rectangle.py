#!/usr/bin/python3
"""
Define Rectangle module
"""


class Rectangle:
    """
    Rectangle class
    """
    def __init__(self, width=0, height=0):
        """ __intit__
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """__width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """__width setter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
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

    def area(self):
        """finds the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """finds the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
