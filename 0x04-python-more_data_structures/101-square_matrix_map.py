#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda seq: list(map(lambda x: x ** 2, seq)), matrix))
