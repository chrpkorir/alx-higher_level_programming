#!/usr/bin/python3
"""
This module contains a function
from_json_string
"""


def from_json_string(my_str):
    """
    returns an object represented by a JSON string
    """
    import json

    return json.loads(my_str)
