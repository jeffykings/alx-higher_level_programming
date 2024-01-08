#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    newdict = dict(sorted(a_dictionary.items()))

    for key, value in newdict.items():
        print(f"{key}: {value}")
