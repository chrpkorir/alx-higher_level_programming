#!/usr/bin/python3
"""
This is the is_same_class module
This contains the is_same_class function
"""


def is_same_class(obj, a_class):
    """
    Will reutrn True if a object excatly an instance of the specific class
    """
    return type(obj) == a_class
