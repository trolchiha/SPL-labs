"""
Module: run_console_calculator

Module provides a simple script to run the console calculator for Lab 2.

"""
from classes.lab2.console_calculator.calculator import Calculator

def run():
    """
    Initializes and runs the console calculator.
    """
    console_calculator = Calculator()
    console_calculator.menu()
