#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print x elememts which are integers of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

        Returns:
            The number of elements printed.
    """

    ret = 0

    for i in range(x):
        if not isinstance(my_list[i], int):
            continue
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break

    print()
    return (ret)
