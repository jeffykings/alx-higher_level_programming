#!/usr/bin/python3

"""a  class that inherits another class"""


class MyList(list):
    """  a class MyList that inherits from list """

    def print_sorted(self):
        """ prints the list, but sorted """

        print(sorted(self))
