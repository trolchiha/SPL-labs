"""
CSV Menu Module (Lab 8)

This module provides a menu function 'lab_menu' for Lab 8, focusing on CSV operations. 
The menu allows users to choose options such as analyzing extreme values, generating diagrams, 
and exiting the program.

Classes:
    - CSVMenu: A class that implements CSV menu functionality.

Usage:
    Import this module and call the 'lab_menu' function to start the Lab 8 CSV menu. 
    The program will display a menu with options for interacting with CSV data.
"""
from UI.menu import Menu
from UI.menu_item import Item
from classes.lab8.diagrams_menu.csv_menu import CSVMenu

def lab_menu():
    """
    This function displays a menu for the Lab 8 and allows the user to select different options.
    It initializes a CSVMenu object and a main menu object, adds items to the main menu, and runs the menu.
    """
    csv_menu = CSVMenu()
    main_menu = Menu("\nMenu (Lab 8)")
    main_menu.set_color("red")
    main_menu.add_item(Item("1", "Extreme values", csv_menu.values_menu))
    main_menu.add_item(Item("2", "Diagrams", csv_menu.diagram_menu))
    main_menu.add_item(Item("0", "Exit"))
    main_menu.run()
