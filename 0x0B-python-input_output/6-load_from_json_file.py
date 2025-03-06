#!/usr/bin/python3

"""function that creates an Object from a 'JSON file'"""

import json


def load_from_json_file(filename):
    """ function that creates an Object from a 'JSON file'

    Args:
        filrname: the json file to be converted to obj
    """

    with open(filename, encoding="utf-8") as file:
        return json.loads(file.read())
