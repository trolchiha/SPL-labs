"""
Module: run_api_menu

Module provides a simple script to run the API Menu for Lab 7.
"""
from classes.lab7.api_menu.api_menu import APIMenu

def run():
    """
    Initializes and runs the API Menu.
    """
    api_menu = APIMenu()
    api_menu.menu()
