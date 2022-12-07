#!/usr/bin/python3
"""Compute the square value of all integers of a matrix."""

def square_matrix_simple(matrix=[]):
    if not matrix:
        print()
    return [[item**2 for item in row] for row in matrix]
