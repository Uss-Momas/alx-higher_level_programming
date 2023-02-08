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
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

        self.value = value
