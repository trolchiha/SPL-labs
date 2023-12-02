import unittest

from classes.lab1.math_operations import count_product

class MultiplicationTestCase(unittest.TestCase):
    def test_multiplication_positive_numbers(self):
        result = count_product(5, 2)
        self.assertEqual(result, 10, "Expected 5 * 2 to equal 10")

    def test_multiplication_negative_numbers(self):
        result = count_product(-5, -2)
        self.assertEqual(result, 10, "Expected -5 * (-2) to equal 10")

    def test_multiplication_mixed_numbers(self):
        result = count_product(5, -2)
        self.assertEqual(result, -10, "Expected 5 * (-2) to equal -10")

    def test_multiplication_int_and_zero(self):
        result = count_product(10, 0)
        self.assertEqual(result, 0, "Expected 10 * 0 to equal 0")

    
    def test_multiplication_positive_floats(self):
        result = count_product(2.5, 3.5)
        self.assertAlmostEqual(result, 8.75, places=2, msg="Expected 2.5 * 3.5 to be approximately 8.75")

    def test_multiplication_negative_floats(self):
        result = count_product(-2.0, -1.5)
        self.assertAlmostEqual(result, 3.0, places=1, msg="Expected -2.0 * -1.5 to be approximately 3.0")

    def test_multiplication_mixed_floats(self):
        result = count_product(3.0, -2.5)
        self.assertAlmostEqual(result, -7.5, places=1, msg="Expected 3.0 * -2.5 to be approximately -7.5")
    
    def test_multiplication_float_and_zero(self):
        result = count_product(10.0, 0)
        self.assertEqual(result, 0, "Expected 10.0 * 0 to equal 0")


    def test_multiplication_int_and_float(self):
        result = count_product(-9, -0.2)
        self.assertAlmostEqual(result, 1.8, places=1, msg="Expected -9 * (-0.2) to be approximately 1.8")
    
    def test_multiplication_float_and_int(self):
        result = count_product(-1.25, 4)
        self.assertAlmostEqual(result, -5.0, places=1, msg="Expected -1.25 * 4 to be approximately 5.0")
