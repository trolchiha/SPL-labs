"""
Module: test_math_operations

This module contains test cases for the count_product function in the math_operations module.
"""
import unittest

from classes.lab1.math_operations.math_operations import count_product

class MultiplicationTestCase(unittest.TestCase):
    """
    Test case for the count_product function in the math_operations module.
    """

    def test_multiplication_positive_numbers(self):
        """
        Test multiplication of two positive numbers.
        """
        result = count_product(5, 2)
        self.assertEqual(result, 10, "Expected 5 * 2 to equal 10")

    def test_multiplication_negative_numbers(self):
        """
        Test multiplication of two negative numbers.
        """
        result = count_product(-5, -2)
        self.assertEqual(result, 10, "Expected -5 * (-2) to equal 10")

    def test_multiplication_mixed_numbers(self):
        """
        Test multiplication of a positive and a negative number.
        """
        result = count_product(5, -2)
        self.assertEqual(result, -10, "Expected 5 * (-2) to equal -10")

    def test_multiplication_int_and_zero(self):
        """
        Test multiplication of an integer and zero.
        """
        result = count_product(10, 0)
        self.assertEqual(result, 0, "Expected 10 * 0 to equal 0")

    def test_multiplication_positive_floats(self):
        """
        Test multiplication of two positive floats.
        """
        result = count_product(2.5, 3.5)
        self.assertAlmostEqual(result, 8.75, places=2, msg="Expected 2.5 * 3.5 to be approximately 8.75")

    def test_multiplication_negative_floats(self):
        """
        Test multiplication of two negative floats.
        """
        result = count_product(-2.0, -1.5)
        self.assertAlmostEqual(result, 3.0, places=1, msg="Expected -2.0 * -1.5 to be approximately 3.0")

    def test_multiplication_mixed_floats(self):
        """
        Test multiplication of a positive float and a negative float.
        """
        result = count_product(3.0, -2.5)
        self.assertAlmostEqual(result, -7.5, places=1, msg="Expected 3.0 * -2.5 to be approximately -7.5")

    def test_multiplication_float_and_zero(self):
        """
        Test multiplication of a float and zero.
        """
        result = count_product(10.0, 0)
        self.assertEqual(result, 0, "Expected 10.0 * 0 to equal 0")

    def test_multiplication_int_and_float(self):
        """
        Test multiplication of an integer and a float.
        """
        result = count_product(-9, -0.2)
        self.assertAlmostEqual(result, 1.8, places=1, msg="Expected -9 * (-0.2) to be approximately 1.8")

    def test_multiplication_float_and_int(self):
        """
        Test multiplication of a float and an integer.
        """
        result = count_product(-1.25, 4)
        self.assertAlmostEqual(result, -5.0, places=1, msg="Expected -1.25 * 4 to be approximately 5.0")
