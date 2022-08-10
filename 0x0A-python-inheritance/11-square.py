#!/usr/bin/python3
"""
This is the base_geometry class
"""


class BaseGeometry:
    """
    This class doesn't do anything
    """
    def area(self):
        """
        returns the area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates the value
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    this is the Rectangle the class
    """
    def __init__(self, width, height):
        """
        the init of the class
        """
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        returns the str when called
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    def area(self):
        """
        return the area of a rectangle
        """
        return self.__width * self.__height


class Square(Rectangle):
    """
    This is the square class and inherts from Rectangle
    """
    def __init__(self, size):
        """
        init of the square class
        """
        BaseGeometry.integer_validator(self, "size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def __str__(self):
        """
        returns the str when called
        """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
