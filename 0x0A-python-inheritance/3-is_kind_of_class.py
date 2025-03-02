#!/usr/bin/python3

"""a function that checks for type of an object"""


def is_kind_of_class(obj, a_class):
    """a function that checks if an object is an instance of a class

    Args:
        obj: the object
        a_class: the class to check for

    Return: True if object otherwise False.
    """
    return isinstance(obj, a_class)
