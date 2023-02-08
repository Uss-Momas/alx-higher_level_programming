#!/usr/bin/python3
""" Base geometry Module
"""


class BaseGeometry(object):
    """Base Geometry class
    """
    def area(self):
        """ function that computes the area of a base geometry object
        """
        raise Exception("area() is not implemented")
