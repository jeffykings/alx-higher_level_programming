#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    newdict = {}

    for key, value in a_dictionary.items():
        newdict[key] = 2 * value

    return (newdict)
