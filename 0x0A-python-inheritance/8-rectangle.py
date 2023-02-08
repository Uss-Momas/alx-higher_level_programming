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

    def integer_validator(self, name, value):
        """Validades the value attribute
        Args:
            name: a string
            value: the value to be validated
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
        return value


class Rectangle(BaseGeometry):
    """ Inherits from BaseGeomtry class
    """
    def __init__(self, width, height):
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)
