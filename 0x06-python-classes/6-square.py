#!/usr/bin/python3
""" Square module """


class Square:
    """ Declares a square class """

    def __init__(self, size=0, position=(0, 0)):
        """init function documentation

        Args:
            size (int): the size of the square
            position (tuple): the position of the square

        Returns:
            None
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter for the position attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the position attribute"""
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2 or (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
            pos1, pos2 = self.position

            for n_line in range(pos2):
                print()
            for i in range(0, self.size):
                for k in range(pos1):
                    print(" ", end="")
                for j in range(0, self.size):
                    print("#", end="")
                print()
