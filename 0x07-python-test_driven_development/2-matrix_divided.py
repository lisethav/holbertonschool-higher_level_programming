#!/usr/bin/python3
"""
This is the matrix_divided module
This module returns the result of the division
of all items in a matrix by `div`.
It accepts a multi-dimensional matrix composed of
only ints and floats, otherwise a TypeError is raised.
"""


def matrix_divided(matrix, div):
    """
    Args:
        matrix (list of a list): the list to be divided.
        div (int or float):The divisor for the matrix.
    Returns:
        a new matrix with its values divided by the div
    if a value of matrix is different than a int or float raise an TypeError
    if div is not a int or float raise an TypeError
    if div has a value of 0 raise ZeroDivisionError
    """

    if (not any(isinstance(x, list) for x in matrix) or len(matrix[0]) == 0):
        raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")

    for row in matrix:
        if (len(matrix[0])) != (len(row)):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_list = [[round((x / div), 2)for x in rows] for rows in matrix]
    return new_list
