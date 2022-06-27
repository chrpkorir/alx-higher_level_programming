#!/usr/bin/python3
"""
This module contains the rectangle class
"""


class Rectangle:
    """
    this is an empty class
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ __intit__
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        """delete and instance
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

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
        if not isinstance(value,int):
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
        return "Rectangle({}, {}) ".format(self.__width, self.__height)

    def my_print(self):
        """ returns a string of a rectangle
        """
        if self.perimeter == 0:
            return ""

        print_sym = str(self.print_symbol)
        width = self.width
        height = self.height
        rect_str = []
        for column in range(height):
            rect_str.append("".join([print_sym for row in range(width)]))
        return "\n".join(rect_str)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ static method that compares 2 rect and returns the bigger rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ create a new Rectangle instance with width == height == size
        """
        return cls(size, size)
