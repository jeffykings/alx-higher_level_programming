#!/usr/bin/python3

def safe_print_integer(value):
    """checks if  a value is an integer and prints an int

    Args:
        value: The value to check

    Returns: True if int else false
    """

    try:
        int(value)
    except (TypeError, ValueError):
        return (False)

    print("{:d}".format(value))
    return (True)
