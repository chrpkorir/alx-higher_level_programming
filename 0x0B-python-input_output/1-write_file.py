#!/usr/bin/python3
"""
This module contains a function number_of_lines
"""


def number_of_lines(filename=""):
    """
    counts the number of lines in a file
    """
    num_lines = 0
    with open(filename, encoding="utf-8") as myFile:
        return myFile.read().count('\n')
