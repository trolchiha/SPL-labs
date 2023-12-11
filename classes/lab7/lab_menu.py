"""
Spotify API Menu Module (Lab 7)

This module provides a menu function 'lab_menu' for Lab 7, focusing on the Spotify API. 
The menu allows users to perform various actions related to Spotify, such as searching for songs, 
accessing artist information, viewing listening history, running tests, and exiting the program.

Classes:
    - APIMenu: A class that implements the Spotify API menu functionality.

Usage:
    Import this module and call the 'lab_menu' function to start the Spotify API menu. 
    The program will display a menu with options for interacting with the Spotify API.
"""
import classes.lab7.tests.main as tests
from UI.menu import Menu
from UI.menu_item import Item
from .api_menu.api_menu import APIMenu

def lab_menu():
    """
    This function displays a menu of Lab 7 for the Spotify API.
    It allows the user to perform various actions such as searching for songs, accessing artist information,
    viewing listening history, running tests, and exiting the program.
    """
    
    api = APIMenu()
    menu = Menu("\nSpotify API Menu (Lab 7)")
    menu.set_color("green")
    menu.add_item(Item("1", "Search Menu", api.search_menu))
    menu.add_item(Item("2", "Artist Menu", api.player_menu))
    menu.add_item(Item("3", "History Menu", api.history_menu))
    menu.add_item(Item("4", "Tests", tests.__main__))
    menu.add_item(Item("0", "Exit", ))
    menu.run()
    