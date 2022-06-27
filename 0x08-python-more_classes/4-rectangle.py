#!/usr/bin/python3
"""
Rectangle class module
"""


class Rectangle:
    """
    this is an empty class
    """
    def __init__(self, width=0, height=0):
        """ __init__
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
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """returns the string of the create rectangle
        """
        return self.my_print()

    def __repr__(self):
        """back up to __str__ returns the string of the create rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def my_print(self):
        """ returns a string of a rectangle
        """
        width = self.width
        height = self.height
        if width == 0 or height == 0:
            return ""
        rect_str = []
        for column in range(height):
            rect_str.append("".join(["#" for row in range(width)]))
        return "\n".join(rect_str)i
