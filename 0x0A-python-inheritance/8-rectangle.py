#!/usr/bin/python3
"""
This is the base_geometry class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    this is the Rectangle the class
    """
    def __init__(self, width, height):
        """
        the init of the class
        """
        BaseGeometry.integer_validator(self, "height", height)
        BaseGeometry.integer_validator(self, "width", width)
        self.__height = height
        self.__width = width
