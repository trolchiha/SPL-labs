"""
Module: test_runner

This module contains the main function for running unit tests using the unittest module.
"""
import unittest

TEST_DIR = "classes/lab7/tests"

def __main__():
    """
    Run the test suite and print the test results.

    Returns:
        None
    """
    test_loader = unittest.TestLoader()
    suite = test_loader.discover(start_dir=TEST_DIR, pattern="test_*.py")
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_result = test_runner.run(suite)

    if test_result.wasSuccessful():
        print("All tests passed.")
    else:
        print("Some tests failed.")
