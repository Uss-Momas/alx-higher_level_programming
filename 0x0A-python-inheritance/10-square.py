#!/usr/bin/python3
""" Square Module
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Square class that inheritate the Rectangle class
    """
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
