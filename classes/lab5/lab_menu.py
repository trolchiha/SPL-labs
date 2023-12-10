"""
Art Menu Module (Lab 5)

This module provides a menu function 'lab_menu' that creates and runs an Art Menu (Lab 5).
The Art Menu allows users to choose a shape and provides an option to exit the menu.

Classes:
    - ArtMenu: A class that implements the Art Menu functionality.

Functions:
    - lab_menu: Creates and runs a menu for the Art Menu (Lab 5). It adds menu items for 
    choosing a shape and exiting the menu.

Usage:
    Import this module and call the 'lab_menu' function to start the Art Menu. The program 
    will display a menu with options for choosing a shape or exiting.
"""
from UI.menu import Menu
from UI.menu_item import Item
from classes.lab5.art.art_menu import ArtMenu

def lab_menu():
    """
    This function creates and runs a menu for the Art Menu (Lab 5).
    It adds menu items for choosing a shape and exiting the menu.
    """
    art = ArtMenu()
    art_menu = Menu("\nArt Menu (Lab 5)")
    art_menu.add_item(Item('1', 'Choose shape', art.set_shape))
    art_menu.add_item(Item('0', 'Exit'))

    art_menu.run()
