#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary == {} or a_dictionary is None:
        return (None)
    dict_values = list(a_dictionary.values())
    tempvalue = dict_values[0]

    for key in a_dictionary.keys():

        if a_dictionary[key] >= tempvalue:
            tenpvalue = a_dictionary[key]
            highest_key = key

    return (highest_key)
