#!/usr/bin/python3

""" class base """
import json


class Base:
    """class base"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionarie"""
        if list_dictionaries is None:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        lst = []

        if list_objs is not None:
            for i in list_objs:
                dictionary = i.to_dictionary()
                lst.append(dictionary)

        json_dictionary = cls.to_json_string(lst)
        name = cls.__name__

        with open(f"{name}.json", "w", encoding="utf-8") as file:
            file.write(json_dictionary)
