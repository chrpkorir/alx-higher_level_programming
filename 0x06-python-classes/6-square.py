#!/usr/bin/python3
"""
This is the Square module.

The Square module contains the Square class
"""


class Square:
    """ This is the Square class
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Initialize a new square
        Args:
        size (int): The size of the new square
        position (int, int): The position of new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Size getter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Size setter
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Returns the current square area
        """
        return(self.__size * self.__size)

    def my_print(self):
        """
        Prints in stdout square with character #
        """
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[i])]
        for i in range(position[1]):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in ramge(0, self.__size)]
            print("")
