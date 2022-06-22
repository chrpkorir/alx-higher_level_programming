#!/usr/bin/python3
"""
This is the Square module.

The Square module contains the Square class
"""


class Square:
    """ This is the Square class
    """

    def __init__(self, size):
        """ The __init__ method
        """
        self.size = size

    @property
    def size(self):
        """ size getter
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ size setter
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ returns the current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """
        prints in stdout square with the # character.""" 
        if self.__size == 0:
            print("")
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
