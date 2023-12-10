"""
lab_menu Module

This module provides a lab menu for Lab 1.

The main function, `lab_menu`, creates and runs a menu for Lab 1.
The menu allows the user to perform calculations, change decimal places,
view history, clear history, and exit the program.

It utilizes functions from the `calculator` module.

"""
from UI.menu import Menu
from UI.menu_item import Item
from classes.lab1.console_calculator.calculator import make_calculation, change_decimal_places, view_history, clear_history, crate_history_file

def lab_menu():
    """
    This function creates and runs a menu for Lab 1.
    The menu allows the user to perform calculations, change decimal places,
    view history, clear history, and exit the program.
    """
    main_menu = Menu("\nMenu (Lab 1)")
    main_menu.add_item(Item('1', 'Make Calculations', make_calculation))
    main_menu.add_item(Item('2', 'Change Decimal Places (default 2)', change_decimal_places))
    main_menu.add_item(Item('3', 'View History', view_history))
    main_menu.add_item(Item('4', 'Clear History', clear_history))
    main_menu.add_item(Item('0', 'Exit'))
    crate_history_file()
    
    main_menu.run()
