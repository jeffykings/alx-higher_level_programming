#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    newmatrix = []
    for i in matrix:
        newlist = list(map(lambda x: x**2, i))
        newmatrix.append(newlist)
    return (newmatrix)
