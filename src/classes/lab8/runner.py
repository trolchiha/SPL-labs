"""
Module: run_csv_menu

Module provides a simple script to run the CSV Menu for diagrams for Lab 8.
"""
from classes.lab8.diagrams_menu.csv_menu import CSVMenu

def run():
    """
    Initializes and runs the CSV Menu for diagrams.
    """
    csv_menu = CSVMenu()
    csv_menu.main_menu()
