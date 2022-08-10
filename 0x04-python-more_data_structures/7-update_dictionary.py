#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary.setdefault(key, value) != value:
        a_dictionary[key] = value
    return a_dictionary
