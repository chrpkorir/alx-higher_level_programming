#!/usr/bin/python3
"""
This is the Square module.

The Square module contains the Square class
"""


class Square:
    """ This is the Square class
    """
    def __init__(self, size=0):
        """ The __init__ method
        """
        self.size = size

    @property
    def size(self):
        """ size getter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ size setter
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ returns the current square area
        """
        size = self.__size
        return(size ** 2)

    def my_print(self):
        """
        prints in stdout square with character #
        """
        size = self.__size
        if size == 0:
            print()
        else:
            for i in range(position[1]):
                print()
            print_sq = []
            for i in range(size):
                row = []
                for i in range(size + position[0]):
                    if i < position[0]:
                        row.append(" ")
                    else:
                        row.append("#")
                print_sq.append("".join(row))
            print("\n".join(print_sq))
