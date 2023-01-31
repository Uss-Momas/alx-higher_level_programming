#!/usr/bin/python3
""" Lazy Matrix Module
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Lazy matrix function
    calculates the multiplicatio of 2 matrices

    Args:
        m_a: matrix a
        m_b: matrix b
    """
    a = np.array(m_a)
    b = np.array(m_b)
    c = np.matmul(a, b)
    return c
