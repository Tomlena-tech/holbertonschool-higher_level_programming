#!/usr/bin/python
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
    map(lambda x: new_matrix.append(x * x), row)
    square_matrix_simple.append(new_matrix)
        new_matrix = []
return square_matrix_simple
