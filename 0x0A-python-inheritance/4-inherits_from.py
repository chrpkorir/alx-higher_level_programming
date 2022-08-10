#!/usr/bin/python3
"""
This is the inherits from module
This contains the inherits_from function
"""


def inherits_from(obj, a_class):
    """
    Returns true if only if an object inherits directly, or indirectly
    from the specific class
    """
    return isinstance(obj, a_class) and type(obj) != a_class
