#!/usr/bin/python3
"""
This module contains the function
read_lines
"""


def read_lines(filename="", nb_lines=0):
    """
    Open and print nb_lines to std out
    Read entire file if nb_lines <= 0 or nb_lines >= total lines
    """
    line = 1
    with open(filename, encoding="utf-8", mode='r') as myFile:
        line_count = myFile.read().count('\n')
        myFile.seek(0)
        if nb_lines <= 0 or nb_lines >= line_count:
            print("{:s}".format(myFile.read()), end="")
        else:
            while line <= nb_lines:
                print("{:s}".format(myFile.readline()), end="")
                line += 1
