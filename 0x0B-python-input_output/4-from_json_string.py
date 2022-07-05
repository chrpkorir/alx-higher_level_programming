#!/usr/bin/python3
"""
this module contains the function
append_write
"""


def append_write(filename="", text=""):
    """
    append text to filename
    will create filename if it doesn't exist
    """
    with open(filename, mode='a', encoding="utf-8") as myFile:
        myFile.write(text)
    return len([char for char in text])
