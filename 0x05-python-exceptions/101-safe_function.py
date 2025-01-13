#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """executes a function safely.

    Args:
        fct: the function to be executed
        *args: list of rguements to be placed in the function

    Returns:
            result of the function on success or None on Failure

    """
    try:
        value = fct(*args)
        return (value)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return (None)
