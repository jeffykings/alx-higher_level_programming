#!/usr/bin/python3

"""a function that returns the dictionary description with simple data
structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object"""


def class_to_json(obj):
    """
    Args:
        obj: is an instance of a Class

    Returns: list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    """

    return (obj.__dict__)
