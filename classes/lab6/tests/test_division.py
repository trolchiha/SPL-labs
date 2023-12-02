import unittest

from classes.lab1.math_operations import count_quotient

class DivisionTestCase(unittest.TestCase):
    def test_division_positive_numbers(self):
        result = count_quotient(40, 2)
        self.assertEqual(result, 20, "Expected 40 / 2 to equal 20")

    def test_division_negative_numbers(self):
        result = count_quotient(-100, -5)
        self.assertEqual(result, 20, "Expected -100 / -5 to equal 20")

    def test_division_mixed_numbers(self):
        result = count_quotient(60, -3)
        self.assertEqual(result, -20, "Expected 60 / -3 to equal -20")

    def test_division_int_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            count_quotient(20, 0)


    def test_division_positive_floats(self):
        result = count_quotient(10.0, 3.0)
        self.assertAlmostEqual(result, 3.3333333, places=5, msg="Expected 10.0 / 3.0 to be approximately 3.3333333")

    def test_division_negative_floats(self):
        result = count_quotient(-8.5, -2.5)
        self.assertAlmostEqual(result, 3.4, places=1, msg="Expected -8.5 / -2.5 to be approximately 3.4")

    def test_division_mixed_floats(self):
        result = count_quotient(15.6, -3.2)
        self.assertAlmostEqual(result, -4.875, places=3, msg="Expected 15.6 / -3.2 to be approximately -4.875")

    def test_division_float_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            count_quotient(20.0, 0)


    def test_division_int_and_float(self):
        result = count_quotient(3, 0.5)
        self.assertAlmostEqual(result, 6.0, places=1, msg="Expected 3 / 0.5 to be approximately 6.0")
    
    def test_division_float_and_int(self):
        result = count_quotient(2.5, 5)
        self.assertAlmostEqual(result, 0.5, places=1, msg="Expected 2.5 / 5 to be approximately 2.5")
