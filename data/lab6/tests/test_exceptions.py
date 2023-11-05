import unittest

from data.lab1.math_operations import count_quotient, count_square_root, count_remainder


class ExceptionsTestCase(unittest.TestCase):
    
    def test_count_quotient_exception(self):
        with self.assertRaises(ZeroDivisionError):
            count_quotient(1, 0)
    
    def test_count_square_root_exception(self):
        with self.assertRaises(ValueError):
            count_square_root(1, -1)

    def test_count_remainder_exception(self):
        with self.assertRaises(ZeroDivisionError):
            count_remainder(20, 0)