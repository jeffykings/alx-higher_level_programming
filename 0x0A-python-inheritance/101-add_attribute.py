#!/usr/bin/python3

""" a function that adds a new attribute to an object if it’s possible"""


def add_attribute(mc, attribute_name, value):
    """add attribute to an object"""

    if not hasattr(mc, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(mc, attribute_name, value)
