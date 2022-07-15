#!/usr/bin/python3
"""This is a Base module for Almost class project.
"""

import json
import csv
import os


class Base:
    """The base superclass.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """This function returns the JSON representation of ans object.
        """
        if list_dictionarie is None or not list_dictionaries:
            return "[]"
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """This function saves a json string to a file """
        json_file = cls.__name__ + ".json"
        json_list = []
        if list_objs:
            for argu in list_objs:
                json_list.append(argu.to_dictionary())
        with open(json_file, 'w') as f:
            changed_file = cls.to_json_string(json_list)
            f.write(changed_file)

    @staticmethod
    def from_json_string(json_string):
        json_list = []
        if json_string:
            json_list = json.loads(json_string)
        return json_list

    @classmethod
    def create(cls, **dictionary):
        """This method creates an instance"""
        name = cls.__name__
        if name == "Square":
            res = cls(10)
        if name == "Rectangle":
            res = cls(10, 42)
        res.update(**dictionary)
        return res

    @classmethod
    def load_from_file(cls):
        """ Load info from file"""
        name = cls.__name__ + ".json"
        listica = []
        if os.path.exists(name):
            with open(name, 'r') as myFile:
                reader = csv.reader(f, delimiter=',')
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                for x, row in enumerate(reader):
                    if x > 0:
                        i = cls(1, 1)
                        for j, e in enumerate(row):
                            if e:
                                setattr(i, fields[j], int(e))
                        new_load.append(i)
        return listica

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saving to csv """
        json_file = cls.__name__ + ".csv"
        with open(json_file, 'w') as file:
            for j in list_objs:
                cont = json.dumps(j)
            json_file.write(cont)

    @classmethod
    def load_from_file_csv(cls):
        """Loading file"""
        json_file = cls.__name__ + ".csv"
        with open(name, 'r') as fl:
            return json.loads(json_file.read())
