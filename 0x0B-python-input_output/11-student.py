#!/usr/bin/python3

"""student class"""


class Student:
    """A student class that has students properties like nme and age"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance """
        if attrs is not [] and attrs is not None:
            tempdic = dict()

            for key in attrs:
                if key in self.__dict__:
                    tempdic[key] = self.__dict__[key]

            return tempdic
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """ that replaces all attributes of the Student instance
        Args:
            json will always be a dictionary
        """
        for key in json.keys():
            setattr(self, key, json[key])
