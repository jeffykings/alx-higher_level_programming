#!/usr/bin/python3

def safe_print_division(a, b):
    """divides 2 integers and prints the result.

        Args:
            a: The numerator
            b: denominator

        Returns:
            on success returns the result else None
    """

    try:
        value = a / b
    except ZeroDivisionError:
        value = None
    finally:
        print("Inside result: {}".format(value))
        return (value)
