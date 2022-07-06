#!/usr/bin/python3
"""Module 101-add_attribute.py.
Checks if an attribute can be added to an object.
"""

def add_attribute(obj, attr, a_value):
    """Checks if attr of value a_value can be added to obj.


    Args:
        - obj: object to add attribute to
        - attr: attribute name
        - a_value: value of attribute to be added
    """

    if not hasattr(obj, '__slots__') and not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    if hasattr(obj, '__slots__') and not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attr, a_value)
