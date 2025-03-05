#!/usr/bin/python3

import json

"""a function that returns the JSON representation of an object (string)"""


def to_json_string(my_obj):
    """
    Args: my_obj: creat a json string from this my_obj

    Return: the JSON representation of an object (string)
    """

    return json.dumps(my_obj)
