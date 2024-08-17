#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    This function divides all the elements of a matrix

    Arguments:
		matrix: matrix to divide its arguments
		div: integer to divide  with the matrix

	Raises:
		TypeError: when the matrix is not a list of integers
					or floats or when div is not an integer
		ZeroDivisionError: when div is equal to zero.

	Returns:
		int: a new matrix
    """
