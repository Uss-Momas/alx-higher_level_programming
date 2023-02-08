#!/usr/bin/python3
""" Square Module
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Square class that inheritate the Rectangle class
    """
    def __init__(self, size):
        super().__init__(size, size)
