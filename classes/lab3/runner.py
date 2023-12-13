"""
Module: run_figlet_generator

Module provides a simple script to run the Figlet text generator for Lab 3.

"""

from classes.lab3.figlet.figlet_generator import FigletGenerator

def run():
    """
    Initializes and runs the Figlet text generator.
    """
    figlet_generator = FigletGenerator()
    figlet_generator.menu()
