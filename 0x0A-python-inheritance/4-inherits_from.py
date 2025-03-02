#!/usr/bin/python3

"""a function that checks for subclass of an object"""


def inherits_from(obj, a_class):
    """a function that checks if an object is an instance of a class
    that inherited  (directly or indirectly) from the specified class

    Args:
        obj: the object
        a_class: the class to check for

    Return: True if its a subclass otherwise False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
