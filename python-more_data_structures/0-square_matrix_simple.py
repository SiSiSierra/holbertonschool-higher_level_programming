#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in matrix:
        new.append(list(i[j] * i[j] for j in range(len(i))))
    return (new)
