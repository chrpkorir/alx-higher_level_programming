#!/usr/bin/python3
"""
This module contains the write_file
"""


def write_file(filename="", text=""):
    """
    write the text a file
    returns the number of character written
    """
    with open(filename, mode='w', encoding="utf-8") as myFile:
        myFile.write(text)
    count = 0
    return len([char for char in text])
