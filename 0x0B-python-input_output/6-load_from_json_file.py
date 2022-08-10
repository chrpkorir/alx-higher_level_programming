#!/usr/bin/python3
"""
This module contains the function
load_from_json_file
"""


def load_from_json_file(filename):
    """
    creates an object from a JSON File
    """
    import os
    import json
    with open(filename, mode='r', encoding='utf-8') as myFile:
        return json.loads(myFile.read())
