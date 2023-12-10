"""
Module: test_math_operations

This module contains test cases for the count_quotient function in the math_operations module.

Classes:
    DivisionTestCase:
        Test case for the count_quotient function in the math_operations module.

Methods:
    - test_division_positive_numbers(self): Test division of two positive numbers.
    - test_division_negative_numbers(self): Test division of two negative numbers.
    - test_division_mixed_numbers(self): Test division of a positive number and a negative number.
    - test_division_int_by_zero(self): Test division of an integer by zero.
    - test_division_positive_floats(self): Test division of two positive floats.
    - test_division_negative_floats(self): Test division of two negative floats.
    - test_division_mixed_floats(self): Test division of a positive float and a negative float.
    - test_division_float_by_zero(self): Test division of a float by zero.
    - test_division_int_and_float(self): Test division of an integer and a float.
    - test_division_float_and_int(self): Test division of a float and an integer.
"""
import unittest

from classes.lab1.math_operations.math_operations import count_quotient

class DivisionTestCase(unittest.TestCase):
    """
    Test case for the count_quotient function in the math_operations module.
    """

    def test_division_positive_numbers(self):
        """
        Test division of two positive numbers.
        """
        result = count_quotient(40, 2)
        self.assertEqual(result, 20, "Expected 40 / 2 to equal 20")

    def test_division_negative_numbers(self):
        """
        Test division of two negative numbers.
        """
        result = count_quotient(-100, -5)
        self.assertEqual(result, 20, "Expected -100 / -5 to equal 20")

    def test_division_mixed_numbers(self):
        """
        Test division of a positive number and a negative number.
        """
        result = count_quotient(60, -3)
        self.assertEqual(result, -20, "Expected 60 / -3 to equal -20")

    def test_division_int_by_zero(self):
        """
        Test division of an integer by zero.
        """
        with self.assertRaises(ZeroDivisionError):
            count_quotient(20, 0)

    def test_division_positive_floats(self):
        """
        Test division of two positive floats.
        """
        result = count_quotient(10.0, 3.0)
        self.assertAlmostEqual(result, 3.3333333, places=5, msg="Expected 10.0 / 3.0 to be approximately 3.3333333")

    def test_division_negative_floats(self):
        """
        Test division of two negative floats.
        """
        result = count_quotient(-8.5, -2.5)
        self.assertAlmostEqual(result, 3.4, places=1, msg="Expected -8.5 / -2.5 to be approximately 3.4")

    def test_division_mixed_floats(self):
        """
        Test division of a positive float and a negative float.
        """
        result = count_quotient(15.6, -3.2)
        self.assertAlmostEqual(result, -4.875, places=3, msg="Expected 15.6 / -3.2 to be approximately -4.875")

    def test_division_float_by_zero(self):
        """
        Test division of a float by zero.
        """
        with self.assertRaises(ZeroDivisionError):
            count_quotient(20.0, 0)

    def test_division_int_and_float(self):
        """
        Test division of an integer and a float.
        """
        result = count_quotient(3, 0.5)
        self.assertAlmostEqual(result, 6.0, places=1, msg="Expected 3 / 0.5 to be approximately 6.0")

    def test_division_float_and_int(self):
        """
        Test division of a float and an integer.
        """
        result = count_quotient(2.5, 5)
        self.assertAlmostEqual(result, 0.5, places=1, msg="Expected 2.5 / 5 to be approximately 2.5")
