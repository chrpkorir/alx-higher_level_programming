#!/usr/bin/python3
"""This module contains the Square class."""
from .rectangle import Rectangle


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
