"""
Module: test_math_operations

This module contains test cases for the count_difference function in the math_operations module.
"""
import unittest

from classes.lab1.math_operations.math_operations import count_difference

class SubtractionTestCase(unittest.TestCase):
    """
    Test case for the count_difference function in the math_operations module.
    """

    def test_subtraction_positive_numbers(self):
        """
        Test subtraction of two positive numbers.
        """
        result = count_difference(20, 5)
        self.assertEqual(result, 15, "Expected 20 - 5 to equal 15")

    def test_subtraction_negative_numbers(self):
        """
        Test subtraction of two negative numbers.
        """
        result = count_difference(-5, -20)
        self.assertEqual(result, 15, "Expected -5 - (-20) to equal 15")

    def test_subtraction_mixed_numbers(self):
        """
        Test subtraction of a positive and a negative number.
        """
        result = count_difference(12, -3)
        self.assertEqual(result, 15, "Expected 12 - (-3) to equal 15")

    def test_subtraction_int_and_zero(self):
        """
        Test subtraction of an integer and zero.
        """
        result = count_difference(15, 0)
        self.assertEqual(result, 15, "Expected 15 - 0 to equal 15")

    def test_subtraction_positive_floats(self):
        """
        Test subtraction of two positive floats.
        """
        result = count_difference(5.0, 2.5)
        self.assertAlmostEqual(result, 2.5, places=2, msg="Expected 5.0 - 2.5 to be approximately 2.5")

    def test_subtraction_negative_floats(self):
        """
        Test subtraction of two negative floats.
        """
        result = count_difference(-8.5, -3.5)
        self.assertAlmostEqual(result, -5.0, places=2, msg="Expected -8.5 - (-3.5) to be approximately -5.0")

    def test_subtraction_mixed_floats(self):
        """
        Test subtraction of a positive float and a negative float.
        """
        result = count_difference(15.6, -7.2)
        self.assertAlmostEqual(result, 22.8, places=2, msg="Expected 15.6 - (-7.2) to be approximately 22.8")

    def test_subtraction_float_and_zero(self):
        """
        Test subtraction of a float and zero.
        """
        result = count_difference(-15, 0)
        self.assertEqual(result, -15, "Expected -15 - 0 to equal -15")

    def test_subtraction_int_and_float(self):
        """
        Test subtraction of an integer and a float.
        """
        result = count_difference(6, -0.7)
        self.assertAlmostEqual(result, 6.7, places=1, msg="Expected 6 - (-0.7) to be approximately 6.7")

    def test_subtraction_float_and_int(self):
        """
        Test subtraction of a float and an integer.
        """
        result = count_difference(8.53, 5)
        self.assertAlmostEqual(result, 3.53, places=2, msg="Expected 8.53 - 5 to be approximately 3.53")
