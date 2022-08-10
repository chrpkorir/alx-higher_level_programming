#!/usr/bin/python3
"""
This is the base_geometry class
"""
Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('9-rectangle').BaseGeometry


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
