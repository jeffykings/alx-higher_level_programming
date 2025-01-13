#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """a function that prints an integer.

    Args:
        value: the value to be checked

        Returns:
            True if integer else False.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError) as e:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
