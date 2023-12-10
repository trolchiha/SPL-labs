"""
Module: test_math_operations

This module contains test cases for handling exceptions in math operations.

Classes:
    ExceptionsTestCase:
        Test case for handling exceptions in math operations.

Methods:
    - test_count_quotient_exception(self): Test for ZeroDivisionError exception in count_quotient function.
    - test_count_square_root_exception(self): Test for ValueError exception in count_square_root function.
    - test_count_remainder_exception(self): Test for ZeroDivisionError exception in count_remainder function.
"""
import unittest

from classes.lab1.math_operations.math_operations import count_quotient, count_square_root, count_remainder


class ExceptionsTestCase(unittest.TestCase):
    """
    Test case for handling exceptions in math operations.
    """

    def test_count_quotient_exception(self):
        """
        Test for ZeroDivisionError exception in count_quotient function.
        """
        with self.assertRaises(ZeroDivisionError):
            count_quotient(1, 0)
    
    def test_count_square_root_exception(self):
        """
        Test for ValueError exception in count_square_root function.
        """
        with self.assertRaises(ValueError):
            count_square_root(1, -1)

    def test_count_remainder_exception(self):
        """
        Test for ZeroDivisionError exception in count_remainder function.
        """
        with self.assertRaises(ZeroDivisionError):
            count_remainder(20, 0)
