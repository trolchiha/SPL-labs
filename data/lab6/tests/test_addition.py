import unittest

from data.lab1.math_operations import count_sum


class AdditionTestCase(unittest.TestCase):
    def test_addition_positive_numbers(self):
        result = count_sum(5, 7)
        self.assertEqual(result, 12, "Expected 5 + 7 to equal 12")

    def test_addition_negative_numbers(self):
        result = count_sum(-7, -5)
        self.assertEqual(result, -12, "Expected -7 + (-5) to equal -12")

    def test_addition_mixed_numbers(self):
        result = count_sum(22, -10)
        self.assertEqual(result, 12, "Expected 22 + (-10) to equal 12")

    def test_addition_int_and_zero(self):
        result = count_sum(1, 0)
        self.assertEqual(result, 1, "Expected 1 + 0 to equal 1")


    def test_addition_positive_floats(self):
        result = count_sum(3.2, 2.8)
        self.assertAlmostEqual(result, 6.0, places=1, msg="Expected 3.2 + 2.8 to be approximately 6.0")

    def test_addition_negative_floats(self):
        result = count_sum(-1.5, -2.5)
        self.assertAlmostEqual(result, -4.0, places=1, msg="Expected -1.5 + (-2.5) to be approximately -4.0")

    def test_addition_mixed_floats(self):
        result = count_sum(4.3, -1.7)
        self.assertAlmostEqual(result, 2.6, places=1, msg="Expected 4.3 + (-1.7) to be approximately 2.6")

    def test_addition_float_and_zero(self):
        result = count_sum(0.1, 0)
        self.assertEqual(result, 0.1, "Expected 0.1 + 0 to equal 0.1")


    def test_addition_int_and_float(self):
        result = count_sum(3, 0.3)
        self.assertAlmostEqual(result, 3.3, places=1, msg="Expected 3 + 0.3 to be approximately 3.3")

    def test_addition_float_and_int(self):
        result = count_sum(0.4, 4)
        self.assertAlmostEqual(result, 4.4, places=1, msg="Expected 0.4 + 4 to be approximately 4.4")

