#!/usr/bin/python3
""" Test Module for 6-max_integer Module
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Class responsible for having all the test cases
    for the max_integer Module
    """

    def test_positive(self):
        """ checking the max positive number of the list
        """
        self.assertEqual(max_integer([2, 10, 3, 5]), 10)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 1000, 4]), 1000)
        self.assertEqual(max_integer([0]), 0)

    def test_negative(self):
        """ Test the max negative numbers
        """
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([0, -2, -3, -4]), 0)
        self.assertEqual(max_integer([-10, -2, -50, -30]), -2)
        self.assertEqual(max_integer([-100000, -20000, 1, -1213312]), 1)

    def test_floatNumbers(self):
        """Testing float values
        """
        self.assertEqual(max_integer([1.0, -0.5, 15.145, 15.15, 10.67]), 15.15)
        self.assertEqual(max_integer([-0.75, -0.25, -0.10, -0.1]), -0.10)

    def test_EmptyList(self):
        """ Testing when a list is empty
        """
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([]), None)

    def test_None_as_argument(self):
        """ Testin the function when None is provided
        """
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_wrong_type(self):
        """ Testing when a list as a wrong type in it
        """
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, "whatever", "You", 6])

    def test_strings(self):
        """ Testing what happens when you introduce strings
        """
        self.assertEqual(max_integer(["ad", 'asds']), "asds")
