#!/usr/bin/python3
"""This module creates a rectangle."""
import json
from models.base import Base


class Rectangle(Base):
    """This is the class Rectangle
    It inherits from base.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing class Rectangle."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width getter."""
        return(self.__width)

    @width.setter
    def width(self, value):
        """Width setter."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Height getter."""
        return(self.__height)

    @height.setter
    def height(self, value):
        """Height setter."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter."""
        return (self.__x)

    @x.setter
    def x(self, value):
        """ x setter."""
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter."""
        return (self.__y)

    @y.setter
    def y(self, value):
        """ y setter."""
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """This function returns the area of a rectangle."""
        w = self.width
        h = self.height
        return ( w * h)

    def display(self):
        """This function prints a Rectangle."""
        w = self.width
        h = self.height
        horri = self.x
        vert = self.y
        i = 0
        j = 0
        l = 0
        for l in range(vert):
            print()
        for i in range(h):
            for j in range(w + horri):
                if j < horri:
                    print("{}".format(" "), end="")
                else:
                    print("{}".format('#'), end="")
            print()

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return ("[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__, 
                                           self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """ Updates all the info """
        lista = ["id", "width", "height", "x", "y"]
        if args and args != "":
            i = 0
            for i in range(len(args)):
                if i < 5:
                    setattr(self, lista[i], args[i])
        else:
            if kwargs and kwargs != "":
                lista = ["id", "width", "height", "x", "y"]
                for key, value in kwargs.items():
                    for i in range(len(lista)):
                        if key == lista[i]:
                            setattr(self, lista[i], value)

    def to_dictionary(self):
        """ Returns the dictionary representation of rectangle"""
        return {'x': self.x, 'y': self.y, 'id': self.id, 'height': self.height,
                'width': self.width}
