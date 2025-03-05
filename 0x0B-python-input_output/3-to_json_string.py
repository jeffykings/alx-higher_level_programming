#!/usr/bin/python3

"""a function that returns the JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """
    Args: my_obj: creat a json string from this my_obj

    Return: the JSON representation of an object (string)
    """

    return json.dumps(my_obj)
