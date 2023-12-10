"""
Figlet Art Generator Module (Lab 3)

This module provides a program that allows users to generate ASCII art using the Figlet font. 
It includes a menu function 'lab_menu', which creates and runs a menu allowing users to perform 
various actions such as generating art, changing settings, previewing art, saving art, viewing saved art, 
and exiting the program.

Classes:
    - FigletGenerator: A class that generates ASCII art using the Figlet font.

Functions:
    - lab_menu: Creates and runs a menu for the Lab 3 program. The menu allows the user to generate art, 
    change settings, preview art, save art, view saved art, and exit the program.

Usage:
    Import this module and call the 'lab_menu' function to start the Figlet Art Generator program. 
    The program will display a menu with options to interact with Figlet-generated ASCII art.
"""

from UI.menu import Menu
from UI.menu_item import Item
from classes.lab3.figlet.figlet_generator import FigletGenerator

def lab_menu():
    """
    This function creates and runs a menu for the Lab 3 program.
    The menu allows the user to generate art, change settings, preview art,
    save art, view saved art, and exit the program.
    """
    figlet_generator = FigletGenerator()
    main_menu = Menu("\nMenu (Lab 3)")
    main_menu.set_color('grey')
    main_menu.add_item(Item('1', 'Generate art', figlet_generator.generate_art))
    main_menu.add_item(Item('2', 'Change settings', figlet_generator.change_settings))
    main_menu.add_item(Item('3', 'Preview', figlet_generator.view_art ))
    main_menu.add_item(Item('4', 'Save art', figlet_generator.save_art))
    main_menu.add_item(Item('5', 'View saved art', figlet_generator.view_saved_art))
    main_menu.add_item(Item('0', 'Exit'))
        
    main_menu.run()
