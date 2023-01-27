#!/usr/bin/python3
""" Matrix Divided Module """


def matrix_divided(matrix, div):
    """matrix_divided function
    Divides all elements of a matrix given as parameter

    Args:
        matrix: it's a list of integers/floats
        div: it's the divisor of every number of the matrix

    Returns:
        a new Matrix
    """
    # Matrix can be: [[1, 2, 3], [4, 5, 6]]
    # the rows are: [1, 2, 3], [4, 5, 6]
    # the elements of the rows are: 1, 2, 3 | 4, 5, 6
    msg1 = "matrix must be a matrix (list of lists) of integers/float"
    for row in matrix:
        # get the length of the first row of the matrix
        length = len(matrix[0])
        # compare the length with every other row of the matrix
        if (length != len(row)):
            raise TypeError("Each row of the matrix must have the same size")

        for element in row:
            if (type(element) is not int) and (type(element) is not float):
                raise TypeError(msg1)

    if (type(div) is not int) and (type(div) is not float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        new_matrix.append([round(i / div, 2) for i in row])

    return new_matrix
