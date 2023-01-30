#!/usr/bin/python3
"""The Rectangle Module"""


class Rectangle:
    """Class Rectangle containg methods and attributes"""

    # public class attributes
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Init method
        initial method created when a new object is created

        Args:
            width: the width of the rectangle, 0 is default
            height: the height of the rectangle, 0 is default

        Returns:
            Nothing
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __str__(self):
        """Especial method __str__
        Returns the rectangle string representation
        """
        rect = ""
        if self.__width == 0 and self.__height == 0:
            return ""

        for hei in range(self.__height):
            for wid in range(self.__width):
                rect += str(self.print_symbol)
            if hei != self.__height - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        if type(self).number_of_instances != 0:
            type(self).number_of_instances -= 1

    @property
    def width(self):
        """Getter method for private instance width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the private att width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Calculates the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two Rectangles based on their area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
