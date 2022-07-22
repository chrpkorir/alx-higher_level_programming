#!/usr/bin/python3
"""A function that print a square with the character #."""


def print_square(size):
    """A function that prints a square with the character #."""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
