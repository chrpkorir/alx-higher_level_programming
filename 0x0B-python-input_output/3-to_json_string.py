#!/usr/bin/python3
"""
This module contains funcion
to_json_string
"""


def to_json_string(my_obj):
    """
    returns the JSON representation of a object (string)
    """
    import json

    return json.dumps(my_obj)
