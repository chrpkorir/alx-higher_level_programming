#!/usr/bin/python3
"""
This module contains funcion
save_to_json_file
"""


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text using Json representation.
    """
    import json
    import os
    with open(filename, mode='w', encoding="utf-8") as myFile:
        myFile.write(json.dumps(my_obj))
