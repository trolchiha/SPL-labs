"""
Calculator Module (Lab 2)

This module provides a simple calculator program with a user interface. 
It includes a menu function 'lab_menu' that allows users to perform various operations such as calculations, 
changing decimal places, viewing history, clearing history, and exiting the program.

Classes:
    - Calculator: A class that implements the calculator functionality.

Functions:
    - lab_menu: Displays a menu for a calculator program and allows the user to perform various operations.

Usage:
    Import this module and call the 'lab_menu' function to start the calculator program. The program will display 
    a menu with options for interacting with the calculator.
"""
from UI.menu import Menu
from UI.menu_item import Item
from classes.lab2.console_calculator.calculator import Calculator

def lab_menu():
    """
    This function displays a menu for a calculator program and allows the user to perform various operations.
    """
    calculator = Calculator()
    terminal_menu = Menu("\nMenu (Lab 2)")
    terminal_menu.add_item(Item("1", "Perform calculations", calculator.perform_calculations))
    terminal_menu.add_item(Item("2", "Change decimal places (default 2)", calculator.change_decimal_places))
    terminal_menu.add_item(Item("3", "View history", calculator.view_history))
    terminal_menu.add_item(Item("4", "Clear history", calculator.clear_history))
    terminal_menu.add_item(Item("0", "Exit"))
    terminal_menu.run()
