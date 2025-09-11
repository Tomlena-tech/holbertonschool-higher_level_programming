#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists of int/float): The matrix to be divided.
        div (int/float): The divisor.

    Returns:
        list of lists of float: A new matrix with the divided values.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats,
                   or if the rows are not of the same size.
