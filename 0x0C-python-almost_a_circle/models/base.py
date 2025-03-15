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

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string

        Args:
            json_string: is a string representing a list of dictionaries

        Return:
            json_string is None or empty, return an empty list
            Otherwise, return the list represented by json_string
        """

        if json_string is None or json_string == "[]":
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if dictionary is None or dictionary == {}:
            return None

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
        else:
            dummy = cls(1)

        dummy.update(**dictionary)

        return dummy
