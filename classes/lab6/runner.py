"""
Module: run_tests_menu

Module provides a simple script to run the Tests Menu for Lab 6.
"""
from classes.lab6.tests.test_menu import TestMenu

def run():
    """
    Initializes and runs the Tests Menu.
    """

    tests_menu = TestMenu()
    tests_menu.menu()
