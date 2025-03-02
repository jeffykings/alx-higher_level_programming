#!/usr/bin/python3

""" a function that returns the list of available attributes and
    methods of an object"""


def lookup(obj):
    """ checks for the attribute and methods of an obj
    Args:
        obj: the object of a class

    Returns:
        lists of attribute and methods
        """
    return (dir(obj))
