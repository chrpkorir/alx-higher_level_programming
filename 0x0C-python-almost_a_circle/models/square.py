#!/usr/bin/python3
"""This module contains the Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Initialize square class."""

    def __init__(self, size, x=0, y=0, id):
        """ Class constructor."""
        Rectangle.__init__(self, size, size, x, y, id)

    @property
    def size(self):
        """Size getter."""
        return (self.width)

    @size.setter
    def size(self, size):
        """ Size setter"""
        self.width = size
        self.height = size

     def __str__(self):
        """ This function returns a string representation of the polygone"""
        return("[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
               self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """ This function updates values in the instance attributes"""
        if args and args != "":
            lista = ["id", "size", "x", "y"]
            for i in range(len(args)):
                if i < 5:
                    setattr(self, lista[i], args[i])
        else:
            if kwargs and kwargs != "":
                lista = ["id", "size", "x", "y"]
                for key, value in kwargs.items():
                    for i in range(len(lista)):
                        if key == lista[i]:
                            setattr(self, lista[i], value)

    def to_dictionary(self):
        """This function returns a dictionary representation of the square"""
        return {'id': self.id, 'x': self.x, 'y': self.y, 'size': self.size}
