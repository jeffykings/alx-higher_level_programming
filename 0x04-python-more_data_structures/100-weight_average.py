#!/usr/bin/python3

def weight_average(my_list=[]):

    score_weight = sum_of_weight = 0
    if my_list == []:
        return (0)
    for tuples in my_list:
        score, weight = tuples

        score_weight += (score * weight)
        sum_of_weight += weight

    return (score_weight / sum_of_weight)
