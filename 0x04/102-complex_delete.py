#!/usr/bin/python3

def complex_delete(a_dictionary, value):

    key2del = [key for key, vlue in a_dictionary.items() if vlue == value]
    for key in key2del:
        del a_dictionary[key]

    return (a_dictionary)
