#!/usr/bin/python3
"""
This module contains the read_file function

read_file reads text file UTF8
"""


def read_file(filename=""):
    """
    read text file UTF8 and prints to stdout
    """
    with open(filename, encoding="utf-8") as myFile:
        print("{}".format(myFile.read()), end="")
