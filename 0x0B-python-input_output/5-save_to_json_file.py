#!/usr/bin/python3

"""a function that writes an Object to a text file, using a JSON
representation"""

import json


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to a text file, using
    a JSON representation

    Args:
        my_obj: to be converted to json and the writen to a file
        filename: to be writen inside
    """

    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
