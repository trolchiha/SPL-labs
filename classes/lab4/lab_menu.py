"""
Art Generator Module (Lab 4)

This module provides a simple ASCII art generator program. It includes an interactive menu
functionality that allows users to set art text, change settings, view generated art, save
art to a file, view saved art, and exit the program. The program uses the ArtGenerator class
to manage the generation and display of ASCII art based on user input and settings.

Classes:
    - ArtGenerator: A class that generates ASCII art based on user input and settings.

Functions:
    - lab_menu: Creates and runs a menu for the Art Generator program, allowing users to
                perform various actions related to ASCII art generation and management.

Usage:
    Import this module and call the 'lab_menu' function to start the Art Generator program.
    The program will display a menu with options for interacting with the ASCII art generator.
"""

from UI.menu import Menu
from UI.menu_item import Item
from classes.lab4.art_generator.art_generator import ArtGenerator

def lab_menu():
    """
    This function creates and runs a menu for the Art Generator program.
    It initializes an instance of the ArtGenerator class and adds menu items
    for various actions such as setting art text, changing settings, viewing art,
    saving art to a file, viewing saved art, and exiting the program.
    """
    art_generator = ArtGenerator()
    art_menu = Menu("\nArt Menu (Lab 4)")
    art_menu.add_item(Item('1', 'Set Art Text', art_generator.set_text))
    art_menu.add_item(Item('2', 'Change Settings', art_generator.change_settings))
    art_menu.add_item(Item('3', 'View Art', art_generator.view_art))
    art_menu.add_item(Item('4', 'Save Art to File', art_generator.save_art_to_file))
    art_menu.add_item(Item('5', 'View Saved Art', art_generator.view_saved_art))
    art_menu.add_item(Item('0', 'Exit'))

    art_menu.run()
