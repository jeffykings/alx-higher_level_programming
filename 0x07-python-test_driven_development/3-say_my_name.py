#!/usr/bin/python3
"""function that prints My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """prints a name
    Args:
    first_name: must be a string
    last_name: must be a string

    Returns:
         My name is <first name> <last name>
    Raises:
        TypeError: first_name must be a string or
        last_name must be a string if any is not string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
