#!/usr/bin/python3
""" Square module """


class Square:
    """ Declares a square class """

    def __init__(self, size=0):
        """init function documentation

        Args:
            size (int): the size of the square

        Returns:
            None
        """
        self.size = size

    @property
    def size(self):
        """ getter function to retrive the size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter functions to set the size value
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Calculates the area of the square
        args:
            no arguments
        Return:
            current area
        """
        return self.__size ** 2

    def my_print(self):
        """ function that prints in stdout the square
        """
        if self.size == 0:
            print()
        else:
            for i in range(0, self.size):
                for j in range(0, self.size):
                    print("#", end="")
                print()
