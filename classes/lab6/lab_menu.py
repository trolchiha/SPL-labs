"""
Testing Module (Lab 6)

This module provides a testing framework for the project. It includes a menu function 'lab_menu'
that displays options to run tests or exit. The 'run_tests' function runs unit tests for the project
by discovering and executing test files in the specified directory.

Functions:
    - lab_menu: Displays a menu for Lab 6 and allows the user to select options.
                Options:
                    1. Run Tests
                    0. Exit
    - run_tests: Run the unit tests for the project. Prints the test results: 
    "All tests passed." or "Some tests failed."

Usage:
    Import this module and call the 'lab_menu' function to start the testing framework. 
    The menu will display options to run tests or exit.
"""
import unittest
from UI.menu import Menu
from UI.menu_item import Item
from shared.settings import get_lab_settings

settings = get_lab_settings("lab6")
TEST_DIR = settings["test_dir"]

def lab_menu():
    """
    Displays a menu for Lab 6 and allows the user to select options.
    """
    menu = Menu("\nMenu (Lab 6)")
    menu.add_item(Item("1", "Run Tests", run_tests))
    menu.add_item(Item("0", "Exit"))
    menu.run()

def run_tests():
    """
    Run the unit tests for the project.

    Returns:
        None
    """
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=TEST_DIR, pattern="test_*.py")
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    if result.wasSuccessful():
        print("All tests passed.")
    else:
        print("Some tests failed.")
