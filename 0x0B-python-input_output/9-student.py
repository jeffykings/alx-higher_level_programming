#!/usr/bin/python3

"""student class"""


class Student:
    """A student class that has students properties like nme and age"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance """
        return self.__dict__
